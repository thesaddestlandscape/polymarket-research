# Hipótesis automáticas — 2026-10-13 04:03 UTC
_Generado por shadow_postmortem.py sobre 874749 resoluciones (PNL=+111041.85€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.211 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.192 (n=248)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 68.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.255 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.125)

- **PATRÓN** `banda_z` > `9.451` → IC=+0.186 (n=243)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 9.451 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=782)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.125)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.213 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.211 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.6161` → IC=+0.242 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6161 (IC base=+0.130)

- **PATRÓN** `banda_z` > `9.925` → IC=+0.219 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.925 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=684)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.130)

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
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=113)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.004)

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
- **FILTRO** `restante_s_al_confirmar` < `144.22` → IC=-0.205 (n=9249)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.22
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=27749)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.76` → IC=-0.265 (n=1106)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.76
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3320)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.47` → IC=-0.300 (n=1030)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.47
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3091)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.02` → IC=-0.219 (n=2407)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.02
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7221)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.03` → IC=-0.294 (n=1791)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.03
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=5376)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=19529)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=4105)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `9413.2764` → IC=+0.180 (n=1838)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9413.2764 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.133 (n=16489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=19869)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=15198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=6792)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7339.2742` → IC=+0.161 (n=2615)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7339.2742 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=1964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1920)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2411)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `16172.9987` → IC=+0.210 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16172.9987 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=1732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=1935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=2477)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `16068.6951` → IC=+0.199 (n=639)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 16068.6951 (IC base=+0.188)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.169 (n=436)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `6900.0098` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6900.0098 (IC base=+0.086)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=1029)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `5830.4537` → IC=+0.128 (n=240)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 5830.4537 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.365 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.227 (n=1691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=1971)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.258 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=740)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `1512.3969` → IC=+0.146 (n=811)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1512.3969 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4420.281 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.409 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=833)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.232 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.795` → IC=-0.329 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=16342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=13866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=6839)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=3809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3598)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3673)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=1775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.228 (n=1768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.311 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=3740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=3577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=2961)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=3260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.349 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.244)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=3668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1277)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.430 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=631)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `4010.7815` → IC=+0.438 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4010.7815 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.447 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `18155.0675` → IC=+0.438 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18155.0675 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.443 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3430.6036` → IC=+0.440 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3430.6036 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.403 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=21116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=21438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.193 (n=3143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=6724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=9387)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=4410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.228 (n=4296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3095)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=3614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.179 (n=6718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=8963)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=4442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=3364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3044)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=8103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=8022)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=3536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=3681)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=7597)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=7442)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.43` → IC=+0.138 (n=6981)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.43 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3760)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3749)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=4584)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.87` → IC=+0.146 (n=3460)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.87 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=3837)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=4074)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=3518)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=1510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=1489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `4280.52` → IC=+0.301 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4280.52 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.293 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.286 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `5373.0997` → IC=+0.303 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5373.0997 (IC base=+0.284)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=716)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1707.6334` → IC=+0.303 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1707.6334 (IC base=+0.292)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.441 (n=578)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.446 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.441 (n=288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.447 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.464 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.453 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.447 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `2084.3627` → IC=+0.462 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2084.3627 (IC base=+0.446)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.296 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4779` → IC=+0.132 (n=11734)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.4779 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.9838` → IC=+0.243 (n=3912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9838 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.1477` → IC=+0.253 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1477 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.252 (n=2741)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.972` → IC=+0.184 (n=4426)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.972 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `0.6169` → IC=+0.256 (n=3322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6169 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.232 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.3493` → IC=+0.222 (n=3754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3493 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5689` → IC=+0.143 (n=14394)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5689 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.5751` → IC=+0.191 (n=957)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5751 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1973` → IC=+0.183 (n=5434)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.1973 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0551` → IC=+0.182 (n=2464)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0551 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.230 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6874` → IC=+0.212 (n=3097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6874 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.220 (n=9121)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.215 (n=867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.214 (n=864)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.193 (n=2588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=1257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=1731)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.9736` → IC=+0.272 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9736 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.142` → IC=+0.289 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.142 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.237 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.203 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=2701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2100.72` → IC=+0.211 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2100.72 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.236 (n=2129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.242 (n=964)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.264 (n=709)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5078` → IC=+0.255 (n=2127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5078 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.879` → IC=+0.237 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.879 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.236 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.251 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6545` → IC=+0.253 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6545 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1611.1` → IC=+0.246 (n=2127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1611.1 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.231 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.234 (n=928)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.257 (n=920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=2128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9692` → IC=+0.268 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9692 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1304` → IC=+0.228 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1304 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2485` → IC=+0.224 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2485 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.228 (n=2085)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.252 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.7781` → IC=+0.222 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7781 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4452` → IC=+0.248 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4452 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.186 (n=702)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0741` → IC=+0.176 (n=699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0741 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.588` → IC=+0.187 (n=1844)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.588 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.229` → IC=+0.160 (n=339)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.229 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.284` → IC=+0.143 (n=1916)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.284 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.148 (n=2095)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1974 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.166 (n=770)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4638` → IC=+0.147 (n=1979)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4638 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7966` → IC=+0.148 (n=1320)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7966 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.180 (n=842)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 225.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.208 (n=1207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=2796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.319` → IC=+0.262 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.319 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.193 (n=2346)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.210 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.6919` → IC=+0.208 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6919 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=3141)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2007.0492` → IC=+0.201 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.0492 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.227 (n=2070)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1763` → IC=+0.230 (n=1035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1763 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1091)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.0708` → IC=+0.238 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0708 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.541` → IC=+0.258 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.541 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3463` → IC=+0.254 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3463 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7265` → IC=+0.218 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7265 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.7276` → IC=+0.233 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7276 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2079.8232` → IC=+0.229 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2079.8232 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.223 (n=2165)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=138)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3179)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.146 (n=642)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0041 (IC base=+0.049)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.221 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1837` → IC=+0.331 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1837 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.069` → IC=+0.182 (n=1032)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.069 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.331 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8538 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.236` → IC=+0.347 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.236 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.343 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.360 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.323 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.332 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.098` → IC=+0.172 (n=830)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.098 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.4652` → IC=+0.174 (n=262)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.4652 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.150 (n=932)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8504 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.213 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.518` → IC=+0.158 (n=1194)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.518 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.178 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=493)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.187 (n=145)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=436)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.130 (n=3185)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=1578)

- **FILTRO** `sigma_ewma_delta_pct` > `8.665` → IC=-0.228 (n=490)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.665
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4273)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.185 (n=198)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7913 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.9864` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9864 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.257` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.257 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.255 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8709 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.267 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.283 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.256 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.149 (n=1578)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2222 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2597` → IC=+0.278 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2597 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.284 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.305 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.4196` → IC=+0.302 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4196 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6331` → IC=-0.181 (n=836)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6331
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=2509)

- **FILTRO** `ibs_20min` < `0.72` → IC=-0.154 (n=2207)

  - _Acción_: SKIP cuando `ibs_20min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=1138)

- **FILTRO** `ibs_20min` > `0.7628` → IC=-0.202 (n=1241)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7628
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=3726)

- **PATRÓN** `dist_vwap_pct` > `0.724` → IC=+0.318 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.724 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2591` → IC=+0.298 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2591 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` < `1.0052` → IC=+0.291 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0052 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` > `0.6377` → IC=+0.302 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6377 (IC base=-0.074)

- **PATRÓN** `volumen_pendiente_norm` < `0.1097` → IC=+0.296 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1097 (IC base=-0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.0764` → IC=+0.293 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0764 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.6005` → IC=+0.297 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6005 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` > `1.8754` → IC=+0.298 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8754 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.275 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8089 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.0812` → IC=+0.280 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0812 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.283 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `2.1868` → IC=+0.258 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1868 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `1.5493` → IC=+0.261 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5493 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.203 (n=5163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.459` → IC=+0.186 (n=13831)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.459 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.9362` → IC=+0.288 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9362 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.654` → IC=+0.155 (n=6938)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.654 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1764` → IC=+0.252 (n=5689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1764 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6884` → IC=+0.260 (n=5082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6884 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2404` → IC=+0.269 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2404 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.265 (n=3044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.283 (n=8697)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.160 (n=4970)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.009 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5392` → IC=+0.160 (n=13108)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5392 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.876` → IC=+0.255 (n=3077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.876 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.263 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1975 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.313 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5882` → IC=+0.284 (n=2861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5882 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2886` → IC=+0.278 (n=2947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2886 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.288 (n=6402)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3718` → IC=-0.160 (n=1413)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3718
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=2871)

- **FILTRO** `ibs_20min` > `0.7542` → IC=-0.193 (n=882)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7542
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2650)

- **FILTRO** `sigma_ewma_delta_pct` > `4.567` → IC=-0.192 (n=776)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.567
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2756)

- **PATRÓN** `ibs_20min` > `0.9143` → IC=+0.292 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9143 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.156` → IC=+0.205 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.156 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.291 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.221 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.2386` → IC=+0.256 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2386 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.254 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.1593` → IC=+0.155 (n=884)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1593 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.2303` → IC=+0.415 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2303 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.6091` → IC=+0.412 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6091 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5399` → IC=+0.408 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5399 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.421 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8555` → IC=+0.144 (n=1057)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.8555 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1124` → IC=+0.198 (n=790)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1124 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6792` → IC=+0.187 (n=1340)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.6792 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.220 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.197 (n=493)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.192 (n=492)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `193.0` → IC=+0.232 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 193.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1515` → IC=+0.233 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1515 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.236 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.302 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5585` → IC=+0.231 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5585 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1954` → IC=+0.251 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1954 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.290 (n=1534)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.263 (n=2304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.259 (n=1535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.714` → IC=+0.285 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.714 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.269 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.1663` → IC=+0.268 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1663 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.269 (n=2704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1992.3584` → IC=+0.284 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.3584 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.331 (n=885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.308 (n=858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3647` → IC=+0.294 (n=1949)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3647 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.1071` → IC=+0.293 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1071 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.307 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.1954` → IC=+0.289 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1954 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.307 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.5718` → IC=+0.306 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5718 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.298 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2074.627` → IC=+0.311 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2074.627 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.294 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.291)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7519` → IC=-0.182 (n=915)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7519
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=2747)

- **PATRÓN** `ibs_20min` > `0.8918` → IC=+0.169 (n=857)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.8918 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.2109` → IC=+0.226 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2109 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0163` → IC=+0.237 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0163 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.244 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.251 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4714` → IC=+0.228 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4714 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.257 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1826` → IC=+0.226 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1826 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `1.041` → IC=+0.236 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.041 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.103` → IC=+0.240 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.103 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.285 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.8289` → IC=+0.272 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8289 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.478` → IC=+0.250 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.478 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.256 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 130.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7645` → IC=-0.199 (n=1638)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7645
  - _Potencial_: sin este filtro IC_bueno=+0.295 (n=1639)

- **FILTRO** `ibs_20min` > `0.6585` → IC=-0.235 (n=812)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6585
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=2447)

- **FILTRO** `sigma_ewma_delta_pct` > `8.582` → IC=-0.231 (n=370)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.582
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=2889)

- **PATRÓN** `ibs_20min` > `0.7645` → IC=+0.295 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7645 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `1.0275` → IC=+0.340 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0275 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.626` → IC=+0.169 (n=509)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.626 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8499` → IC=+0.321 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8499 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6316` → IC=+0.314 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6316 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.310 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.332 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.336 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.139 (n=2155)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5556 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `0.7045` → IC=+0.259 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7045 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.240 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.247 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.251 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.270 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.029)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.339 (n=1590)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.323 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.315 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.947` → IC=+0.294 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.947 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `0.6244` → IC=+0.304 (n=1779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6244 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.342 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.306 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2482.0514` → IC=+0.307 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2482.0514 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.328 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.328 (n=1258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.295 (n=829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.301 (n=1276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.295)

- **PATRÓN** `ibs_20min` < `0.3679` → IC=+0.321 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3679 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.306 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.036` → IC=+0.296 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.036 (IC base=+0.295)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.325 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.295)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.348 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` < `1.4187` → IC=+0.301 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4187 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` > `2.1452` → IC=+0.298 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1452 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `2448.553` → IC=+0.304 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2448.553 (IC base=+0.295)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.216 (n=3804)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3469` → IC=+0.186 (n=10035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3469 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=11858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.5622` → IC=+0.230 (n=11403)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5622 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1656` → IC=+0.205 (n=4731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1656 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.355` → IC=+0.254 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.355 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1989` → IC=+0.168 (n=7568)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1989 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.162 (n=7569)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6258 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2945` → IC=+0.199 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2945 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6103` → IC=+0.186 (n=3679)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6103 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2021.1172` → IC=+0.183 (n=10187)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2021.1172 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.193 (n=10323)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.189 (n=7305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0067 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.225 (n=3646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=4118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.4953` → IC=+0.236 (n=10937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4953 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.177` → IC=+0.197 (n=1812)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.177 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1833` → IC=+0.168 (n=7816)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1833 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.226 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6319` → IC=+0.187 (n=3404)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6319 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.195 (n=8743)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 68.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.236 (n=638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.229 (n=639)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.3327` → IC=+0.224 (n=1914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3327 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=2015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.9205` → IC=+0.288 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9205 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.154` → IC=+0.333 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.154 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.262 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.5429` → IC=+0.207 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5429 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2101.57` → IC=+0.219 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2101.57 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.245 (n=1306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.243 (n=986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0987` → IC=+0.293 (n=651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0987 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=1334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.2672` → IC=+0.265 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2672 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.126` → IC=+0.246 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.126 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.243 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.276 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.260 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.679` → IC=+0.252 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.679 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1604.32` → IC=+0.257 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.32 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.246 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.217 (n=577)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1628` → IC=+0.183 (n=1146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1628 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=1802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3619` → IC=+0.224 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3619 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1373` → IC=+0.212 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1373 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.226 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.167 (n=755)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6892 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.0736` → IC=+0.156 (n=777)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0736 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2845` → IC=+0.184 (n=273)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2845 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.176 (n=559)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.5153` → IC=+0.157 (n=558)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5153 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `425.0` → IC=+0.160 (n=1636)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 425.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.169 (n=1796)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0057 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2316` → IC=+0.178 (n=1581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2316 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6054` → IC=+0.207 (n=1796)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6054 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.719` → IC=+0.209 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.719 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.168 (n=1796)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.204 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.148 (n=1507)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.154 (n=553)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.155 (n=1678)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.151 (n=1119)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.178 (n=535)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 206.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.234 (n=876)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4024` → IC=+0.220 (n=1692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4024 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=2000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.209 (n=1311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.488` → IC=+0.287 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.488 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.223 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7734` → IC=+0.214 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7734 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7054` → IC=+0.222 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7054 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1994.9584` → IC=+0.224 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.9584 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.247 (n=1446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1424` → IC=+0.269 (n=725)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1424 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.287 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.252 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.616` → IC=+0.271 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.616 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.273 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.724` → IC=+0.247 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.724 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.7291` → IC=+0.241 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7291 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2075.0484` → IC=+0.245 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.0484 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.230 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.182 (n=1617)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0063 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0758` → IC=+0.199 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0758 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3202` → IC=+0.209 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3202 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1379` → IC=+0.193 (n=1147)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1379 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.208 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.162 (n=1226)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.856 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.177 (n=757)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4269` → IC=+0.158 (n=600)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4269 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.169 (n=600)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4835.6925` → IC=+0.201 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4835.6925 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.160 (n=1774)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 145.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.158 (n=1931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.007 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3848` → IC=+0.148 (n=1931)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3848 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6819` → IC=+0.190 (n=1931)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6819 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.889` → IC=+0.155 (n=679)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.889 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.164 (n=1288)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8585 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.194 (n=292)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.136 (n=1200)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4191` → IC=+0.133 (n=1799)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4191 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4468.9287` → IC=+0.173 (n=1287)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4468.9287 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.132 (n=1541)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 122.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.128 (n=696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0058 (IC base=+0.125)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.165 (n=946)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0099 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5631` → IC=+0.127 (n=2087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5631 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4889` → IC=+0.214 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4889 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.1944` → IC=+0.190 (n=1233)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1944 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.686` → IC=+0.265 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.686 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1893` → IC=+0.139 (n=2087)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1893 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.134 (n=2111)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4403` → IC=+0.141 (n=675)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4403 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2878.9982` → IC=+0.211 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2878.9982 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.154 (n=662)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 21.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.138 (n=2117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0104 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1055` → IC=+0.171 (n=706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1055 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.5897` → IC=+0.220 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5897 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.542` → IC=+0.127 (n=429)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 7.542 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.536` → IC=+0.124 (n=1868)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 2.536 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1787` → IC=+0.134 (n=2116)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1787 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.153 (n=275)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4542` → IC=+0.140 (n=653)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4542 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.4425` → IC=+0.128 (n=652)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.4425 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2736.5522` → IC=+0.189 (n=960)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2736.5522 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.131 (n=1929)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.121)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.239 (n=1727)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.283` → IC=+0.222 (n=1290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.283 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2004)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.219 (n=1741)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6533` → IC=+0.253 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6533 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1903` → IC=+0.221 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1903 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2706` → IC=+0.215 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2706 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.577` → IC=+0.246 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.577 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.1814` → IC=+0.218 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1814 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.223 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.266 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.4841` → IC=+0.220 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4841 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.815` → IC=+0.230 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.815 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2662.7024` → IC=+0.227 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2662.7024 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.235 (n=869)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0121 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.229 (n=895)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.255 (n=658)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.4226` → IC=+0.257 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4226 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `1.1573` → IC=+0.235 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1573 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.388` → IC=+0.251 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.388 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6401` → IC=+0.235 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6401 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.285 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.567` → IC=+0.220 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.567 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.228 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2422.6754` → IC=+0.233 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2422.6754 (IC base=+0.226)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.203 (n=1299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3327` → IC=+0.182 (n=2598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3327 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=1465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.4901` → IC=+0.208 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4901 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.7717` → IC=+0.184 (n=450)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7717 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.691` → IC=+0.200 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.691 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.190 (n=1763)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8641 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.176 (n=2362)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6955 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1017` → IC=+0.184 (n=1062)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1017 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.4367` → IC=+0.190 (n=957)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4367 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.5252` → IC=+0.175 (n=956)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.5252 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.175 (n=3358)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `2770.0146` → IC=+0.178 (n=2636)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2770.0146 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.185 (n=2728)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 151.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.141 (n=1020)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0036 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.084` → IC=+0.193 (n=1019)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.084 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `1.436` → IC=+0.133 (n=991)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.436 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `4408.7993` → IC=+0.129 (n=2038)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 4408.7993 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.134 (n=1279)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 29.0 (IC base=+0.104)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.206 (n=372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0995` → IC=+0.217 (n=372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0995 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.193 (n=771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.6458` → IC=+0.220 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6458 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.3035` → IC=+0.185 (n=265)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3035 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.109` → IC=+0.186 (n=361)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.109 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.191 (n=564)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8753 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.173 (n=331)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `2.22` → IC=+0.171 (n=728)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.22 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.4195` → IC=+0.165 (n=828)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4195 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `14790.7557` → IC=+0.173 (n=564)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 14790.7557 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.198 (n=362)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 154.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.191 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.146 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6256` → IC=+0.176 (n=861)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6256 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.715` → IC=+0.140 (n=187)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.715 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.16` → IC=+0.137 (n=888)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.16 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.134 (n=979)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2046 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.0617` → IC=+0.155 (n=444)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.0617 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0702` → IC=+0.174 (n=382)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0702 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1178` → IC=+0.146 (n=851)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.1178 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1269)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `297.0` → IC=+0.154 (n=833)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 297.0 (IC base=+0.133)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.248 (n=612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.2019` → IC=+0.224 (n=613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2019 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.6787` → IC=+0.265 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6787 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.212 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.2053` → IC=+0.211 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2053 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.225 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.212 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.224 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.182 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.237 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.243 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.4439` → IC=+0.224 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4439 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.127 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0038 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.0955` → IC=+0.168 (n=302)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0955 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `3963.1458` → IC=+0.123 (n=809)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3963.1458 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.122 (n=582)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 63.0 (IC base=+0.087)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.150 (n=461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.151 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0092 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.174 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.9447` → IC=+0.210 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9447 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.155` → IC=+0.206 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.155 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.166 (n=608)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.0604 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.7231` → IC=+0.156 (n=617)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7231 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.482` → IC=+0.147 (n=667)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.482 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1991` → IC=+0.158 (n=302)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1991 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=718)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3081.1151` → IC=+0.194 (n=230)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3081.1151 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.4762` → IC=+0.152 (n=599)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.4762 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.135 (n=217)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `2817.1909` → IC=+0.159 (n=309)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2817.1909 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.120 (n=556)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 33.0 (IC base=+0.065)

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

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.158 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0117 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.61 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.009` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.009 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.2382` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2382 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.180 (n=4954)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.219 (n=4952)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=15497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5584` → IC=+0.238 (n=13265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5584 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1616` → IC=+0.191 (n=5393)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1616 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.345` → IC=+0.251 (n=3645)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.345 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2292` → IC=+0.167 (n=9944)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2292 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.203 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.2718` → IC=+0.193 (n=6531)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.2718 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `1839.0284` → IC=+0.185 (n=14848)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1839.0284 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.204 (n=11893)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.194 (n=5895)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.38` → IC=+0.192 (n=11787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.38 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=5019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5773` → IC=+0.243 (n=13395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5773 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.96` → IC=+0.211 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.96 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.67` → IC=+0.190 (n=12925)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.67 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.0605` → IC=+0.162 (n=7963)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0605 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2901` → IC=+0.253 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2901 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6242` → IC=+0.201 (n=4201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6242 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `1776.75` → IC=+0.189 (n=13394)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1776.75 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.214 (n=8249)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.241 (n=814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.243 (n=816)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3497` → IC=+0.218 (n=2441)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3497 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.218 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.666` → IC=+0.350 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.666 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2784` → IC=+0.281 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2784 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.2672` → IC=+0.229 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2672 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=2531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2021.1172` → IC=+0.232 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2021.1172 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.229 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.262 (n=2054)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.259 (n=934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2026` → IC=+0.270 (n=1369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2026 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.275 (n=750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4951` → IC=+0.284 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4951 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.468` → IC=+0.265 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.468 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.1577` → IC=+0.257 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1577 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.282 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.279 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1609.04` → IC=+0.270 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1609.04 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.256 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.199 (n=801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1765` → IC=+0.164 (n=1591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1765 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2671` → IC=+0.208 (n=2386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2671 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.193 (n=1290)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.703` → IC=+0.166 (n=399)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.703 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.156 (n=2176)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.175 (n=797)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6288 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.154 (n=2123)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2724` → IC=+0.172 (n=343)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2724 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1826` → IC=+0.159 (n=2048)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1826 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.533` → IC=+0.154 (n=2080)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.533 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.181 (n=997)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 268.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.193 (n=660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0026 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.161 (n=1979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6969` → IC=+0.199 (n=1979)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6969 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.170 (n=1827)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.346` → IC=+0.163 (n=443)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.346 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.160 (n=1979)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1847 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1548` → IC=+0.193 (n=529)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1548 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.153 (n=1876)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7866` → IC=+0.162 (n=1250)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7866 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `252.0` → IC=+0.150 (n=596)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 252.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.248 (n=822)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.311 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.223 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.6984` → IC=+0.236 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6984 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2902)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2008.5984` → IC=+0.239 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.5984 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.248 (n=2023)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.245 (n=2052)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1786` → IC=+0.260 (n=1010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1786 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.268 (n=869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0222` → IC=+0.303 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0222 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.074` → IC=+0.291 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.074 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3428` → IC=+0.300 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3428 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.241 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1371` → IC=+0.251 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1371 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2075.512` → IC=+0.263 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2075.512 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.266 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.201 (n=1123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4149` → IC=+0.156 (n=2542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4149 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=2646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2622` → IC=+0.193 (n=2541)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2622 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1389` → IC=+0.164 (n=1380)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1389 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.196` → IC=+0.164 (n=1035)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.196 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.873` → IC=+0.165 (n=1695)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.873 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.185 (n=338)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.169 (n=1090)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1776` → IC=+0.159 (n=1124)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1776 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7089.8255` → IC=+0.237 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7089.8255 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.173 (n=1064)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 78.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.194 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0032 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4319` → IC=+0.144 (n=2081)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4319 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.7426` → IC=+0.191 (n=2081)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.7426 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.170 (n=425)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.143 (n=1388)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8747 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.229 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.2436` → IC=+0.136 (n=1758)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2436 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.435` → IC=+0.142 (n=1998)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.435 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `5257.3722` → IC=+0.204 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5257.3722 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.132 (n=2003)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 160.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.142 (n=1712)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0081 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.198 (n=2568)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4483 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0341` → IC=+0.206 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0341 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.919` → IC=+0.263 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.919 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.887` → IC=+0.147 (n=1712)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.887 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.0989` → IC=+0.124 (n=2416)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.0989 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.138 (n=332)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `2.4798` → IC=+0.123 (n=2504)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4798 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.4677` → IC=+0.127 (n=2504)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4677 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=2618)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2549.0292` → IC=+0.238 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2549.0292 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.135 (n=820)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 26.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.143 (n=2441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0109 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.132` → IC=+0.163 (n=814)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.132 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.159 (n=1147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.215 (n=2441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.389` → IC=+0.135 (n=2349)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.389 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `0.7128` → IC=+0.146 (n=1074)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7128 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2237` → IC=+0.172 (n=409)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2237 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.157 (n=757)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2755.5964` → IC=+0.210 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2755.5964 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.140 (n=2004)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 49.0 (IC base=+0.121)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.240 (n=2189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=2557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.229 (n=1765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.6038` → IC=+0.267 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6038 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1997` → IC=+0.238 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1997 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.716` → IC=+0.265 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.716 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2336` → IC=+0.226 (n=2450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2336 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6388` → IC=+0.224 (n=2450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6388 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.252 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.5212` → IC=+0.248 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5212 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2359.8754` → IC=+0.229 (n=2450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2359.8754 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.243 (n=1156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.233 (n=2395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.263 (n=2555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.201` → IC=+0.258 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.201 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.255 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.297 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.229 (n=2355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2435.8884` → IC=+0.229 (n=2277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2435.8884 (IC base=+0.225)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=4464)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.238 (n=1514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.5039` → IC=+0.209 (n=4534)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5039 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=3115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9408` → IC=+0.245 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9408 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.1706` → IC=+0.202 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1706 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2448` → IC=+0.204 (n=2875)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2448 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.192` → IC=+0.216 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.192 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.633` → IC=+0.200 (n=4047)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.633 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.212 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.8899` → IC=+0.205 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8899 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.221 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.208 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6083` → IC=+0.205 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6083 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=3469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2967.5262` → IC=+0.209 (n=4051)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2967.5262 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.231 (n=1124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.199 (n=3360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=1144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=1510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.1776` → IC=+0.199 (n=1479)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1776 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.188 (n=555)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.135` → IC=+0.190 (n=3366)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 6.135 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.1015` → IC=+0.194 (n=2786)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1015 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.188 (n=3059)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.188 (n=1458)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.5356 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.8199` → IC=+0.190 (n=2209)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.8199 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=4464)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.196 (n=2196)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 69.0 (IC base=+0.183)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.256 (n=534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.272 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.236 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.2754` → IC=+0.270 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2754 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.7593` → IC=+0.236 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7593 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` < `0.3418` → IC=+0.248 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3418 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.55` → IC=+0.243 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.55 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.587` → IC=+0.238 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.587 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.245 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2271 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.8658` → IC=+0.254 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8658 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.447` → IC=+0.250 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.447 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `12446.0249` → IC=+0.252 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12446.0249 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.243 (n=507)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3698` → IC=+0.175 (n=1146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3698 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.187 (n=429)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.194 (n=504)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1409 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.6039` → IC=+0.167 (n=520)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.6039 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.6916` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6916 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.180 (n=1128)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.200 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8855 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.185 (n=531)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.5265` → IC=+0.168 (n=1141)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.5265 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8143` → IC=+0.178 (n=761)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.8143 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `11387.9096` → IC=+0.173 (n=1146)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 11387.9096 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.173 (n=1100)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 701.0 (IC base=+0.162)

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
- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.216 (n=1320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4605` → IC=+0.208 (n=1320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4605 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.5142` → IC=+0.218 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5142 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.8779` → IC=+0.206 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8779 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.208 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.882` → IC=+0.203 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.882 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2372` → IC=+0.213 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2372 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.205 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.205 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4166` → IC=+0.223 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4166 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.245 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.204 (n=1064)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.198 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 16.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.7503` → IC=+0.186 (n=1064)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7503 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.0837` → IC=+0.182 (n=1064)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.0837 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.6564` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6564 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.185 (n=1085)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.193 (n=1064)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.2445 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.197 (n=450)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1797` → IC=+0.191 (n=917)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1797 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `7202.6889` → IC=+0.193 (n=1064)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7202.6889 (IC base=+0.180)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.207 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3048` → IC=+0.176 (n=433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3048 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.203 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.255 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.19` → IC=+0.210 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.19 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.216 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.7012` → IC=+0.219 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7012 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.1079` → IC=+0.180 (n=588)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1079 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.199 (n=194)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5067` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5067 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=750)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `3157.365` → IC=+0.199 (n=579)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3157.365 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.191 (n=633)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 54.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.206 (n=417)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.3638` → IC=+0.231 (n=310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3638 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.222 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.7143` → IC=+0.215 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7143 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.7767` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7767 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.2939` → IC=+0.204 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2939 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.982` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.982 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.837` → IC=+0.197 (n=410)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 2.837 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.7551` → IC=+0.209 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7551 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `0.9427` → IC=+0.198 (n=309)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.9427 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.231 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.220 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `3081.4536` → IC=+0.217 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3081.4536 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.231 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.195)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.4165` → IC=+0.147 (n=1365)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4165 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.7246` → IC=+0.165 (n=249)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7246 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.428` → IC=+0.184 (n=305)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.428 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1786` → IC=+0.261 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1786 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `0.089` → IC=+0.136 (n=657)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.089 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.626` → IC=+0.145 (n=108)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.626 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.148` → IC=+0.203 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.148 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.6035` → IC=+0.123 (n=598)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.6035 (IC base=+0.065)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.138 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.139 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 18.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.3752` → IC=+0.170 (n=462)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3752 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.158 (n=241)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.461` → IC=+0.123 (n=263)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 3.461 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.121 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0045 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0409` → IC=+0.287 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0409 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.138 (n=313)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.623` → IC=+0.135 (n=261)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.623 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.124 (n=304)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.1823 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.0743` → IC=+0.161 (n=125)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0743 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.131 (n=280)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.085)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.156 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6606` → IC=+0.207 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6606 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.123` → IC=+0.183 (n=235)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.123 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.652` → IC=+0.246 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.652 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.5851` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.5851 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `1737.9704` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 1737.9704 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0108` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0108 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.031` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.031 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.1373` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1373 (IC base=+0.020)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.158 (n=317)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.75 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.865` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 7.865 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2427` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2427 (IC base=+0.030)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.163 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0092 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.255 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.2042` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2042 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.3579` → IC=+0.174 (n=176)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.3579 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.803` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.803 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `1.0763` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0763 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.2389` → IC=+0.186 (n=119)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.2389 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.083)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.211 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.083)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.328 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=220)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=265)

- **FILTRO** `volumen_regimen` < `0.7615` → IC=-0.333 (n=70)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7615
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=212)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.381 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=179)

- **FILTRO** `drift_60min` |x|> `0.2042` → IC=-0.314 (n=57)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2042
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=173)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=215)

- **FILTRO** `sigma_ewma_delta_pct` > `10.676` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.676
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=212)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=125)

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

- **FILTRO** `sigma_h` < `0.002` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

- **FILTRO** `sigma_ewma_delta_pct` > `2.402` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.402
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=69)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6398` → IC=-0.439 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6398
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=67)

- **FILTRO** `ibs_20min` > `0.7432` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7432
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=59)

- **FILTRO** `dist_vwap_pct` > `0.1189` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1189
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=62)

- **FILTRO** `volumen_spike_ratio` < `1.4507` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4507
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=39)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.9508 (IC base=-0.163)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=77)

- **FILTRO** `volumen_spike_ratio` < `1.5847` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5847
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=67)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.165 (n=210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0057 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.149 (n=459)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6757 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.4858` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4858 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6589` → IC=+0.154 (n=154)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6589 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` < `0.2347` → IC=+0.135 (n=398)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.2347 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.5562` → IC=+0.136 (n=358)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5562 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.168 (n=471)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1622 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.209` → IC=+0.191 (n=163)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.209 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `3082.2157` → IC=+0.160 (n=357)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3082.2157 (IC base=+0.072)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6544` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6544
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=141)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.235 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.171 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 12.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.177 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.205 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1361 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.0931` → IC=+0.164 (n=248)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.0931 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.257` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.257 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.678` → IC=+0.172 (n=193)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 4.678 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.168 (n=242)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6194 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.078` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.078 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.5892` → IC=+0.185 (n=211)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.5892 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.4563` → IC=+0.165 (n=210)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4563 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `5157.3278` → IC=+0.163 (n=161)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5157.3278 (IC base=+0.154)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1371` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1371
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=151)

- **FILTRO** `ibs_20min` > `0.2194` → IC=-0.134 (n=91)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2194
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=178)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.130 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0046 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.7164` → IC=+0.127 (n=164)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.7164 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.033` → IC=+0.134 (n=121)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.033 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` < `0.1371` → IC=+0.128 (n=151)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1371 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.2194` → IC=+0.133 (n=178)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2194 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.042)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=92)

- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=98)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.302 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.270 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.242 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.2516` → IC=+0.296 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2516 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `665.8128` → IC=+0.245 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 665.8128 (IC base=+0.242)

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
- **PATRÓN** `libro_liquidez` > `2869.517` → IC=+0.131 (n=527)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2869.517 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2869.517` → IC=+0.131 (n=527)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2869.517 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=169)

- **FILTRO** `libro_liquidez` < `2696.1504` → IC=-0.229 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 2696.1504
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=139)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=61)

- **FILTRO** `liq_n` < `5.0` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `liq_n` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

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

- **FILTRO** `libro_liquidez` < `2892.3985` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2892.3985
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3134)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=129)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.142 (n=213)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.046)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=1144)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1098)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=392)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=373)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=151)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.017)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=799)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=799)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=674)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=674)

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
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=170)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=194)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=245)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=211)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=321)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=321)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=232)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=171)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=1729)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1872)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.065)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.065)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.135 (n=236)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=128)

- **FILTRO** `profundidad_ratio` < `180.1` → IC=-0.134 (n=91)

  - _Acción_: SKIP cuando `profundidad_ratio` < 180.1
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=273)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.46 (IC base=+0.024)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.214 (n=40)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=191)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.157 (n=106)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=126)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.5 (IC base=+0.039)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.243 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=250)

- **FILTRO** `restante_min` < `12.72` → IC=-0.121 (n=159)

  - _Acción_: SKIP cuando `restante_min` < 12.72
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=159)

- **FILTRO** `lag_apertura_s` > `139.69` → IC=-0.125 (n=158)

  - _Acción_: SKIP cuando `lag_apertura_s` > 139.69
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=160)

- **FILTRO** `profundidad_ratio` < `36.4` → IC=-0.175 (n=78)

  - _Acción_: SKIP cuando `profundidad_ratio` < 36.4
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=240)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.254 (n=55)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=251)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.46 (IC base=-0.029)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.128 (n=253)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=150)

- **FILTRO** `restante_min` < `3.34` → IC=-0.179 (n=132)

  - _Acción_: SKIP cuando `restante_min` < 3.34
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=271)

- **FILTRO** `lag_apertura_s` > `97.61` → IC=-0.191 (n=137)

  - _Acción_: SKIP cuando `lag_apertura_s` > 97.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=266)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=253)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.48` → IC=+0.125 (n=126)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.48 (IC base=-0.018)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.143 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=125)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.183 (n=99)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=357)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=5092)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=16454)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.166 (n=5557)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=16677)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.188 (n=933)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2930)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.157 (n=916)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3061)

- **PATRÓN** `libro_liquidez` > `1446.82` → IC=+0.131 (n=1932)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1446.82 (IC base=+0.037)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.123 (n=1839)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.5 (IC base=+0.015)

- **PATRÓN** `libro_liquidez` > `1577.16` → IC=+0.149 (n=1353)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1577.16 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.174 (n=768)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2423)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.175 (n=947)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2966)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=1003)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=3044)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.123 (n=1332)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.9643 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1864.9284` → IC=+0.131 (n=1331)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1864.9284 (IC base=+0.035)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2255)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2677)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3417)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=414)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.140 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=414)

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

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=327)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=826)

- **FILTRO** `libro_liquidez` < `2042.3274` → IC=-0.163 (n=342)

  - _Acción_: SKIP cuando `libro_liquidez` < 2042.3274
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=697)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=41)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=14910)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=33327)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=11604)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=36633)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=12052)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=36185)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.155 (n=15894)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=32343)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.237 (n=14795)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=46285)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.180 (n=15173)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=45907)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5904)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1990)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=6318)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.247 (n=2741)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=5567)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.174 (n=1934)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=6374)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2601)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=8001)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.208 (n=2646)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=7956)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.125 (n=1971)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=6216)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=1867)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6320)

- **FILTRO** `ibs_7min` < `0.7338` → IC=-0.197 (n=2046)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7338
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6141)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.188 (n=2039)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6148)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=2015)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6318)

- **FILTRO** `ibs_7min` > `0.2677` → IC=-0.196 (n=2081)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2677
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6252)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.185 (n=2074)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6259)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=1946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=5960)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=1891)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=6015)

- **FILTRO** `ibs_7min` < `0.7034` → IC=-0.245 (n=2608)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7034
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5298)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.223 (n=1669)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6237)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.247 (n=2556)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=8718)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.175 (n=2817)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8457)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=1818)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=6081)

- **FILTRO** `ibs_7min` < `0.7339` → IC=-0.186 (n=1974)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7339
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5925)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.191 (n=1960)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5939)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2038)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6121)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.180 (n=2038)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=6121)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=2004)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6155)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=1977)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=6056)

- **FILTRO** `ibs_7min` < `0.2321` → IC=-0.235 (n=2008)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2321
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=6025)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.186 (n=2757)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=8904)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=1946)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5958)

- **FILTRO** `ibs_7min` < `0.2228` → IC=-0.224 (n=1976)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2228
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5928)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1848)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6056)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.209 (n=2687)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=8364)

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

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=817)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=371)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.138 (n=158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=315)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=606)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=353)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.143 (n=1035)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `441.7389` → IC=+0.157 (n=345)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 441.7389 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4250.6823` → IC=+0.131 (n=345)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4250.6823 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.148 (n=356)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 14.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.163 (n=81)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.223 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2614.7862` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2614.7862 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 9.0 (IC base=+0.147)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4389` → IC=+0.134 (n=69)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4389 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.125 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 14.0 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.127 (n=242)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2039.5706` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2039.5706 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 10.0 (IC base=+0.116)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.174 (n=139)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `390.044` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.044 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `8025.1558` → IC=+0.131 (n=139)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8025.1558 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 72.0 (IC base=+0.127)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.186 (n=183)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.174 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 12.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `4950.202` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `total_vol_5m` < 4950.202 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3092.8641` → IC=+0.160 (n=183)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3092.8641 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 28.0 (IC base=+0.150)

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

- **FILTRO** `sigma_h` > `0.0061` → IC=-0.294 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=393)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.169 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0034 (IC base=-0.085)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.348 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=134)

- **FILTRO** `T_h` > `87.9981` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=134)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.308 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.044)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `87.9936` → IC=-0.148 (n=52)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=52)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.224 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=138)

- **FILTRO** `pct_vs_K` |x|> `2.2275` → IC=-0.384 (n=230)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.2275
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=232)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.127 (n=140)

- **FILTRO** `T_h` > `79.6334` → IC=-0.180 (n=123)

  - _Acción_: SKIP cuando `T_h` > 79.6334
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=62)

- **FILTRO** `pct_vs_K` |x|> `2.0268` → IC=-0.395 (n=84)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0268
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=85)

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
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.314 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=39)

- **FILTRO** `T_h` > `135.9806` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `T_h` > 135.9806
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=117)

- **FILTRO** `pct_vs_K` |x|> `2.6864` → IC=-0.403 (n=70)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6864
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=72)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.276 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=97)

- **FILTRO** `T_h` > `113.0501` → IC=-0.199 (n=71)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=73)

- **FILTRO** `pct_vs_K` |x|> `3.8526` → IC=-0.412 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8526
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=63)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.475 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.343)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.365 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.388 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.343)

- **PATRÓN** `T_h` < `0.9178` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9178 (IC base=+0.343)

- **PATRÓN** `T_h` > `1.1834` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1834 (IC base=+0.343)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.096` → IC=+0.446 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.441 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.418)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.430 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.466 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.418)

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

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.433)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.464 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.433)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.433)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.477 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.1968` → IC=+0.477 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1968 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4421` → IC=+0.485 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4421 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=280)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=358)

- **FILTRO** `streak_estiramiento` > `0.7643` → IC=-0.151 (n=107)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.7643
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=210)

- **PATRÓN** `streak_estiramiento` < `0.4187` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4187 (IC base=+0.033)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `volumen_racha` < `982893.6` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_racha` < 982893.6 (IC base=+0.010)

- **PATRÓN** `streak_estiramiento` < `0.293` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.293 (IC base=+0.010)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.077)

- **PATRÓN** `streak_estiramiento` < `0.326` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.326 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 30.0 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `2338.687` → IC=+0.144 (n=116)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2338.687 (IC base=+0.077)

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

- **FILTRO** `hora_utc` < `15.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=690)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `9.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `libro_liquidez` < `2349.4469` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 2349.4469
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=906)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1327)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1040)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1051)

### STRUCT_NO_15M
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3716)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1993)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.202 (n=1022)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.229 (n=1022)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1662` → IC=+0.199 (n=2698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1662 (IC base=+0.191)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2285` → IC=+0.192 (n=1023)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2285 (IC base=+0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3516` → IC=+0.202 (n=2730)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3516 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=2849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=2804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_15` > `0.5859` → IC=+0.268 (n=3065)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5859 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1217` → IC=+0.186 (n=1444)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1217 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.3024` → IC=+0.178 (n=2321)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.3024 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.579` → IC=+0.268 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.579 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `5349.0852` → IC=+0.201 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5349.0852 (IC base=+0.191)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1214)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.238 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.265 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.255` → IC=+0.264 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.255 (IC base=+0.218)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.233 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.281 (n=541)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.242 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.166` → IC=+0.297 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.166 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.249 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.218)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.391` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.391
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=688)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.188 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.156 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.144)

- **PATRÓN** `drift_15min` |x|≤ `0.3985` → IC=+0.144 (n=203)

  - _Acción_: Kelly boost +0.72€ cuando `drift_15min` |x|≤ 0.3985 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1469` → IC=+0.159 (n=405)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1469 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.162 (n=235)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.241 (n=608)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1135` → IC=+0.152 (n=383)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1135 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.2686` → IC=+0.146 (n=569)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2686 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.003` → IC=+0.281 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.003 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3532.4883` → IC=+0.151 (n=543)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3532.4883 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.995` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.995
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=253)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.138 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.114)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.158 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0098 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1421` → IC=+0.154 (n=388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1421 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.121 (n=528)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.190 (n=530)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.5 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.3619` → IC=+0.126 (n=600)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.3619 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=324)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.114)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.283 (n=233)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.230 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1101` → IC=+0.223 (n=467)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1101 (IC base=+0.222)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.327` → IC=+0.248 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.327 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_15` > `0.5745` → IC=+0.303 (n=699)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5745 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1857` → IC=+0.232 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1857 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.272 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2928.9931` → IC=+0.277 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2928.9931 (IC base=+0.222)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.162 (n=722)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1111 (IC base=+0.065)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.367 (n=388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.368 (n=581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.384 (n=387)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2309` → IC=+0.383 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2309 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.374 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.396 (n=582)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.389 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.387 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `3851.736` → IC=+0.371 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3851.736 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.361 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.5086` → IC=+0.361 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5086 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.394 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.393 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.387 (n=308)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.394 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.382 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.360 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `15272.807` → IC=+0.387 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15272.807 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.409 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.362 (n=121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.381 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.359 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0902` → IC=+0.374 (n=244)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0902 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.386 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.388 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.358)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.364 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.406 (n=273)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.361 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.362 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.352` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.352 (IC base=+0.358)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.389 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.360 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.358)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.222 (n=987)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2963)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1531)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2419)

- **FILTRO** `libro_liquidez` < `4133.0032` → IC=-0.145 (n=2607)

  - _Acción_: SKIP cuando `libro_liquidez` < 4133.0032
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=1343)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1422` → IC=+0.187 (n=634)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1422 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.284 (n=951)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1081` → IC=+0.205 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1081 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2619` → IC=+0.201 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2619 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2253` → IC=+0.267 (n=1073)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2253 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.282 (n=3221)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6474` → IC=+0.281 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6474 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.207 (n=554)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1670)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.228 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1668)

- **FILTRO** `sigma_ewma_delta_pct` > `23.806` → IC=-0.268 (n=321)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.806
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1903)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.208 (n=63)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2161)

- **FILTRO** `libro_liquidez` < `16272.4583` → IC=-0.205 (n=1467)

  - _Acción_: SKIP cuando `libro_liquidez` < 16272.4583
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=757)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.173 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0026 (IC base=+0.094)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.301 (n=134)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=+0.094)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.094)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.337 (n=292)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.302 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` < `0.3639` → IC=+0.293 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3639 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.877` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 24.877 (IC base=+0.094)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.236 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.194)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.311 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.194)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.194)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=618)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.161 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.162 (n=477)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0033 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.184 (n=318)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.153)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.159 (n=318)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.199 (n=360)

  - _Acción_: Kelly boost +0.99€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.176 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.256 (n=477)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.4313` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.4313 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2663` → IC=+0.157 (n=447)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2663 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.260 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=618)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10755.3155` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10755.3155 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.252 (n=743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.245 (n=982)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7573` → IC=+0.255 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7573 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2143` → IC=+0.261 (n=505)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2143 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.245 (n=989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3682` → IC=+0.273 (n=1114)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3682 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.7773` → IC=+0.298 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7773 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.409` → IC=+0.259 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.409 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.679` → IC=+0.247 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.679 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1043` → IC=-0.202 (n=451)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1043
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=453)

- **FILTRO** `drift_60min` |x|> `0.1716` → IC=-0.254 (n=307)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1716
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=597)

- **FILTRO** `drift_15min` |x|> `0.8773` → IC=-0.275 (n=225)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8773
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=679)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.181)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.181)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.181)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0646` → IC=+0.243 (n=501)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0646 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.288 (n=504)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.1747` → IC=+0.248 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1747 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.249 (n=548)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=550)

- **FILTRO** `drift_15min` |x|> `1.2333` → IC=-0.261 (n=274)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2333
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=824)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1079)

- **FILTRO** `libro_liquidez` < `2982.5179` → IC=-0.213 (n=823)

  - _Acción_: SKIP cuando `libro_liquidez` < 2982.5179
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1517` → IC=+0.276 (n=351)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1517 (IC base=-0.027)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1114` → IC=+0.302 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1114 (IC base=-0.027)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=778)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7812` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7812 (IC base=-0.027)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.036)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.036)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.295 (n=961)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.320 (n=321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.248` → IC=+0.298 (n=320)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.248 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2243` → IC=+0.306 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2243 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=1005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.838` → IC=+0.322 (n=961)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.838 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.1554` → IC=+0.313 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1554 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.976` → IC=+0.366 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.976 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `12753.6666` → IC=+0.308 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12753.6666 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.309 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.312 (n=174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `0.6308` → IC=+0.286 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6308 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.311 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8267` → IC=+0.312 (n=519)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8267 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.327 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.371` → IC=+0.374 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.371 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16341.0554` → IC=+0.323 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16341.0554 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.305 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.295 (n=442)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.320 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.302 (n=296)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.313 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.295 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8759` → IC=+0.339 (n=395)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8759 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.6029` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6029 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.349 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1212` → IC=-0.151 (n=81)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1212
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=243)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.136 (n=218)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=74)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.172 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=354)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=158)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.3151` → IC=-0.158 (n=36)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3151
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `82.5234` → IC=+0.197 (n=437)

  - _Acción_: Kelly boost +0.99€ cuando `T_h` > 82.5234 (IC base=+0.192)

- **PATRÓN** `ratio` < `0.973` → IC=+0.417 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.192)

- **PATRÓN** `T_h` > `111.9959` → IC=+0.352 (n=1979)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9959 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.367 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `T_h` > 103.3918 (IC base=+0.167)

- **PATRÓN** `ratio` < `0.9702` → IC=+0.375 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9702 (IC base=+0.167)

- **PATRÓN** `T_h` > `108.3228` → IC=+0.303 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 108.3228 (IC base=+0.290)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.393 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.290)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `82.5234` → IC=+0.238 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.228)

- **PATRÓN** `ratio` < `0.985` → IC=+0.428 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.985 (IC base=+0.228)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.350 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.345 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1062` → IC=+0.450 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1062 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5859 sube el IC de +0.191 a +0.268 en UPDOWN_GBM#15min (n=3065). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.218 a +0.281 en UPDOWN_GBM#BTC#15min (n=541). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.144 a +0.241 en UPDOWN_GBM#ETH#15min (n=608). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.114 a +0.190 en UPDOWN_GBM#SOL#15min (n=530). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5745 sube el IC de +0.222 a +0.303 en UPDOWN_GBM#XRP#15min (n=699). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.065 a +0.162 en UPDOWN_GBM#XRP#15min (n=722). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.066 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=951). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.012 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3221). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.094 a +0.337 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=292). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.194 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6307 sube el IC de +0.153 a +0.256 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=477). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3682 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1114). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.181 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.038 a +0.288 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=504). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.202 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.027 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=778). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.838 sube el IC de +0.290 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=961). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8267 sube el IC de +0.287 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=519). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8759 sube el IC de +0.294 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=395). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.361 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=582). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.362 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=308). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.358 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=273). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1733 | +0.086 | +190.01€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1733 | +0.086 | +190.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1359 | +0.089 | +162.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1359 | +0.089 | +162.16€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 271 | +0.068 | +12.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 271 | +0.068 | +12.14€ | 5 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 418 | +0.002 | +69.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 418 | +0.002 | +69.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 301 | +0.002 | +46.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 301 | +0.002 | +46.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 91 | +0.016 | +17.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 91 | +0.016 | +17.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 36998 | -0.083 | -4719.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1967 | +0.009 | -243.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 35031 | -0.088 | -4475.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4426 | -0.116 | -763.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4426 | -0.116 | -763.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1967 | +0.009 | -243.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1967 | +0.009 | -243.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4121 | -0.113 | -845.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4121 | -0.113 | -845.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9689 | -0.002 | -897.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9689 | -0.002 | -897.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9628 | -0.108 | -706.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9628 | -0.108 | -706.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7167 | -0.145 | -1262.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7167 | -0.145 | -1262.60€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 30351 | -0.018 | +3564.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7847 | +0.003 | +1741.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 22504 | -0.025 | +1823.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 30351 | -0.018 | +3564.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7847 | +0.003 | +1741.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 22504 | -0.025 | +1823.48€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 130377 | +0.114 | -5458.54€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17448 | +0.182 | -537.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 564 | -0.032 | -64.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 104425 | +0.105 | -4590.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7940 | +0.103 | -265.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17330 | +0.106 | -1100.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 58 | -0.150 | +11.01€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17257 | +0.107 | -1099.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 25537 | +0.128 | -411.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5051 | +0.192 | -158.30€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17312 | +0.118 | -149.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3132 | +0.086 | -81.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 17381 | +0.097 | -1275.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 69 | -0.106 | -3.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17297 | +0.098 | -1260.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 27706 | +0.124 | -486.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7275 | +0.176 | -126.71€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 17525 | +0.106 | -302.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2894 | +0.101 | -49.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 25075 | +0.114 | -1321.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4933 | +0.192 | -267.86€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 467 | +0.003 | -10.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 17761 | +0.093 | -908.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1914 | +0.135 | -134.65€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17348 | +0.104 | -862.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 62 | -0.062 | +8.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17273 | +0.105 | -870.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 20911 | +0.194 | -1329.88€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 20911 | +0.194 | -1329.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4802 | +0.175 | -437.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4802 | +0.175 | -437.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2465 | +0.201 | -53.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2465 | +0.201 | -53.48€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4742 | +0.179 | -394.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4742 | +0.179 | -394.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4142 | +0.244 | -142.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4142 | +0.244 | -142.23€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4681 | +0.186 | -316.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4681 | +0.186 | -316.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 933 | +0.427 | -31.53€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 933 | +0.427 | -31.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 370 | +0.435 | -5.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 370 | +0.435 | -5.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 360 | +0.431 | -8.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 360 | +0.431 | -8.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 191 | +0.402 | -14.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 191 | +0.402 | -14.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 72783 | +0.201 | -5282.88€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 72783 | +0.201 | -5282.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12512 | +0.185 | -1298.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12512 | +0.185 | -1298.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11729 | +0.225 | -396.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11729 | +0.225 | -396.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12490 | +0.179 | -1354.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12490 | +0.179 | -1354.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11807 | +0.221 | -439.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11807 | +0.221 | -439.49€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 12070 | +0.202 | -804.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 12070 | +0.202 | -804.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12175 | +0.196 | -990.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12175 | +0.196 | -990.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 27812 | +0.117 | +199.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 27812 | +0.117 | +199.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 13822 | +0.120 | +173.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 13822 | +0.120 | +173.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13990 | +0.114 | +26.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13990 | +0.114 | +26.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1897 | +0.293 | -0.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1897 | +0.293 | -0.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 861 | +0.284 | -8.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 861 | +0.284 | -8.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 917 | +0.292 | +3.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 917 | +0.292 | +3.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 874 | +0.442 | +4.98€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 874 | +0.442 | +4.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 423 | +0.439 | -0.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 423 | +0.439 | -0.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 405 | +0.446 | +5.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 405 | +0.446 | +5.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1474 | +0.070 | -64.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 554 | +0.059 | -40.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 920 | +0.076 | -24.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 70 | +0.111 | +3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 70 | +0.111 | +3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1140 | +0.076 | -30.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 220 | +0.077 | -5.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 920 | +0.076 | -24.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 264 | +0.030 | -37.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 264 | +0.030 | -37.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 54161 | +0.100 | -1358.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4385 | +0.093 | +66.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 49776 | +0.101 | -1425.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 29910 | +0.105 | -315.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4385 | +0.093 | +66.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 25525 | +0.107 | -382.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 10956 | +0.109 | -48.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 10956 | +0.109 | -48.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13295 | +0.082 | -995.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13295 | +0.082 | -995.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 883 | +0.197 | -111.73€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 883 | +0.197 | -111.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 883 | +0.197 | -111.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 883 | +0.197 | -111.73€ | 2 | 4 |
| ✅ GBM_LATE_15M | 37454 | +0.091 | +19117.53€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 37454 | +0.091 | +19117.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6285 | +0.208 | +4978.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6285 | +0.208 | +4978.79€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 5573 | +0.180 | +4163.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5573 | +0.180 | +4163.60€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 6680 | +0.203 | +5139.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6680 | +0.203 | +5139.05€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 5260 | +0.039 | +1412.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5260 | +0.039 | +1412.37€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 5344 | -0.030 | +1183.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5344 | -0.030 | +1183.09€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 8312 | -0.035 | +2240.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8312 | -0.035 | +2240.63€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 40503 | +0.086 | +21819.73€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 40503 | +0.086 | +21819.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7816 | +0.006 | +4057.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7816 | +0.006 | +4057.34€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8515 | +0.013 | +1899.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8515 | +0.013 | +1899.64€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5666 | +0.273 | +5971.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5666 | +0.273 | +5971.82€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7087 | +0.014 | +1669.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7087 | +0.014 | +1669.60€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6536 | +0.038 | +2660.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6536 | +0.038 | +2660.60€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4883 | +0.294 | +5560.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4883 | +0.294 | +5560.73€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 29786 | +0.178 | +23756.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 29786 | +0.178 | +23756.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4523 | +0.221 | +3868.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4523 | +0.221 | +3868.69€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4678 | +0.152 | +3462.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4678 | +0.152 | +3462.61€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4753 | +0.220 | +4030.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4753 | +0.220 | +4030.33€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5021 | +0.140 | +3828.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5021 | +0.140 | +3828.92€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5603 | +0.123 | +4103.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5603 | +0.123 | +4103.52€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5208 | +0.221 | +4462.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5208 | +0.221 | +4462.86€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8009 | +0.137 | +3887.52€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8009 | +0.137 | +3887.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 371 | +0.149 | +225.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 371 | +0.149 | +225.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2431 | +0.147 | +1370.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2431 | +0.147 | +1370.36€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 413 | +0.146 | +201.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 413 | +0.146 | +201.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2429 | +0.147 | +1189.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2429 | +0.147 | +1189.10€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1826 | +0.106 | +660.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1826 | +0.106 | +660.65€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 539 | +0.134 | +240.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 539 | +0.134 | +240.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 37655 | +0.183 | +29630.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 37655 | +0.183 | +29630.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5989 | +0.235 | +5417.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5989 | +0.235 | +5417.28€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5819 | +0.149 | +3904.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5819 | +0.149 | +3904.17€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6345 | +0.231 | +5615.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6345 | +0.231 | +5615.83€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6162 | +0.139 | +4401.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6162 | +0.139 | +4401.54€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6676 | +0.122 | +4572.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6676 | +0.122 | +4572.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6664 | +0.223 | +5719.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6664 | +0.223 | +5719.12€ | 0 | 20 |
| ✅ GBM_LATE_5M | 10524 | +0.193 | +7793.57€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 10524 | +0.193 | +7793.57€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2335 | +0.188 | +1837.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2335 | +0.188 | +1837.19€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 3177 | +0.192 | +2233.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3177 | +0.192 | +2233.15€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 1482 | +0.184 | +1088.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1482 | +0.184 | +1088.25€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1609 | +0.195 | +1163.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1609 | +0.195 | +1163.01€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2926 | +0.070 | +1007.63€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 2926 | +0.070 | +1007.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1092 | +0.090 | +402.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1092 | +0.090 | +402.71€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 933 | +0.071 | +362.09€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 933 | +0.071 | +362.09€ | 0 | 10 |
| ✅ GBM_LATE_60M#SOL | 901 | +0.045 | +242.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 901 | +0.045 | +242.83€ | 0 | 13 |
| 🚫 GBM_LATE_60M_FADE | 518 | -0.240 | -16.35€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 518 | -0.240 | -16.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 195 | -0.231 | -7.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 195 | -0.231 | -7.88€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 185 | -0.222 | -1.51€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 185 | -0.222 | -1.51€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 138 | -0.271 | -6.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 138 | -0.271 | -6.96€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1325 | +0.087 | +344.35€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1325 | +0.087 | +344.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 509 | +0.087 | +111.28€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 509 | +0.087 | +111.28€ | 1 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 487 | +0.062 | +82.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 487 | +0.062 | +82.58€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 329 | +0.122 | +150.49€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 329 | +0.122 | +150.49€ | 2 | 13 |
| ✅ LATE_WINDOW_5MIN | 144 | +0.253 | +124.85€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 144 | +0.253 | +124.85€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 144 | +0.253 | +124.85€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 144 | +0.253 | +124.85€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3151 | +0.100 | +784.42€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3151 | +0.100 | +784.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3151 | +0.100 | +784.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3151 | +0.100 | +784.42€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 452 | -0.064 | -29.57€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 452 | -0.064 | -29.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 130 | -0.015 | +1.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 130 | -0.015 | +1.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 73 | -0.087 | -8.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 73 | -0.087 | -8.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3340 | +0.021 | +92.01€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3340 | +0.021 | +92.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 165 | +0.015 | -3.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 165 | +0.015 | -3.72€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 610 | +0.033 | +45.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 610 | +0.033 | +45.36€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1194 | +0.032 | +35.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1194 | +0.032 | +35.64€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 746 | +0.011 | +0.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 746 | +0.011 | +0.72€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 422 | +0.009 | +19.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 422 | +0.009 | +19.09€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1568 | -0.041 | -26.94€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1568 | -0.041 | -26.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 442 | -0.034 | -11.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 442 | -0.034 | -11.40€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 528 | -0.017 | +4.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 528 | -0.017 | +4.57€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 598 | -0.068 | -20.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 598 | -0.068 | -20.11€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 6546 | -0.025 | +6.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3116 | -0.034 | -62.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3430 | -0.016 | +69.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 190 | -0.005 | +9.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 94 | +0.042 | +13.50€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 96 | -0.051 | -4.13€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1642 | -0.015 | +23.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 787 | -0.021 | -3.04€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 855 | -0.009 | +26.09€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 728 | -0.026 | +3.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 370 | -0.046 | -13.44€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 358 | -0.006 | +17.27€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1348 | -0.039 | -51.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 624 | -0.056 | -50.21€ | 5 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 724 | -0.025 | -1.30€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1287 | -0.021 | +15.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 618 | -0.031 | -0.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 669 | -0.013 | +16.46€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1351 | -0.029 | +6.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 623 | -0.038 | -8.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 728 | -0.021 | +14.65€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 43780 | -0.001 | +2140.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 43780 | -0.001 | +2140.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7840 | +0.026 | +1016.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7840 | +0.026 | +1016.42€ | 2 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6416 | -0.034 | -109.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6416 | -0.034 | -109.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7960 | +0.022 | +780.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7960 | +0.022 | +780.63€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6246 | -0.047 | -148.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6246 | -0.047 | -148.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7381 | -0.004 | +251.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7381 | -0.004 | +251.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7937 | +0.015 | +349.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7937 | +0.015 | +349.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6390 | -0.060 | -156.22€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6390 | -0.060 | -156.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1224 | +0.000 | -14.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1224 | +0.000 | -14.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1626 | -0.079 | -40.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1626 | -0.079 | -40.12€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 747 | -0.121 | -32.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 747 | -0.121 | -32.57€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1884 | -0.079 | -40.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1884 | -0.079 | -40.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3362 | +0.004 | -1.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3362 | +0.004 | -1.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 129 | -0.042 | -1.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 129 | -0.042 | -1.78€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1324 | +0.006 | +6.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1324 | +0.006 | +6.33€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 109317 | -0.074 | +1678.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 109317 | -0.074 | +1678.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 18910 | -0.074 | +995.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 18910 | -0.074 | +995.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 16520 | -0.099 | -925.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 16520 | -0.099 | -925.54€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 19180 | -0.066 | +1089.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 19180 | -0.066 | +1089.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 16058 | -0.095 | -484.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 16058 | -0.095 | -484.60€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 19694 | -0.054 | +364.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 19694 | -0.054 | +364.59€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 18955 | -0.066 | +639.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 18955 | -0.066 | +639.90€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8598 | -0.032 | -170.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8598 | -0.032 | -170.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1963 | -0.045 | -22.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1963 | -0.045 | -22.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2568 | -0.026 | -41.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2568 | -0.026 | -41.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1148 | -0.050 | -23.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1148 | -0.050 | -23.12€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 915 | -0.028 | -31.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 915 | -0.028 | -31.37€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1515 | +0.122 | +608.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1379 | +0.129 | +596.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 324 | +0.147 | +175.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 324 | +0.147 | +175.72€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 274 | +0.116 | +91.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 274 | +0.116 | +91.00€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 277 | +0.127 | +123.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 277 | +0.127 | +123.87€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 244 | +0.150 | +132.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 244 | +0.150 | +132.57€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 260 | +0.095 | +72.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 260 | +0.095 | +72.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1186 | -0.022 | -31.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1186 | -0.022 | -31.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 227 | -0.015 | +0.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 227 | -0.015 | +0.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 201 | -0.017 | -0.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 201 | -0.017 | -0.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 303 | -0.038 | -20.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 303 | -0.038 | -20.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 252 | -0.008 | -4.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 252 | -0.008 | -4.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 203 | -0.027 | -5.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 203 | -0.027 | -5.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 835 | -0.071 | -38.83€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 385 | -0.120 | -77.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 296 | -0.154 | -67.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 298 | -0.033 | +25.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 212 | -0.028 | +25.80€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 152 | -0.019 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 630 | -0.087 | -33.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1011 | -0.207 | -54.90€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 410 | -0.206 | -37.86€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 354 | -0.211 | -38.14€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 343 | -0.216 | -29.45€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 297 | -0.226 | -35.14€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 258 | -0.192 | +12.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 239 | -0.189 | +9.26€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 890 | -0.211 | -64.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 417 | +0.397 | +402.51€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 104 | +0.377 | +93.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 104 | +0.377 | +93.44€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 260 | +0.458 | +262.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 260 | +0.458 | +262.94€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 417 | +0.397 | +402.51€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 676 | +0.025 | +22.52€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 676 | +0.025 | +22.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 54 | -0.036 | -6.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 54 | -0.036 | -6.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 70 | -0.014 | -0.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 70 | -0.014 | -0.57€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 256 | +0.050 | +26.44€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 256 | +0.050 | +26.44€ | 0 | 6 |
| ✅ STREAK_FADE_5M | 3369 | -0.021 | -130.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3369 | -0.021 | -130.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 586 | -0.025 | -25.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 586 | -0.025 | -25.10€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 162 | -0.043 | -14.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 162 | -0.043 | -14.36€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1570 | -0.017 | -53.59€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1570 | -0.017 | -53.59€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 94 | -0.052 | -9.37€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 94 | -0.052 | -9.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10284 | +0.018 | +101.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10284 | +0.018 | +101.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2619 | +0.022 | +41.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2619 | +0.022 | +41.87€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2884 | +0.009 | -2.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2884 | +0.009 | -2.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2133 | +0.022 | +34.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2133 | +0.022 | +34.71€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9365 | +0.013 | -48.94€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9365 | +0.013 | -48.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3735 | +0.018 | -6.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3735 | +0.018 | -6.31€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3603 | +0.011 | -28.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3603 | +0.011 | -28.25€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2027 | +0.008 | -14.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2027 | +0.008 | -14.39€ | 1 | 0 |
| ✅ UPDOWN_GBM | 68339 | +0.052 | +5934.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 16997 | +0.085 | +3839.05€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2251 | +0.006 | +15.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 44949 | +0.046 | +2011.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3908 | +0.009 | +69.61€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 13801 | +0.054 | +1156.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2118 | +0.090 | +513.34€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 578 | +0.012 | +7.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9278 | +0.058 | +583.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1742 | +0.006 | +49.71€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 85 | -0.075 | +2.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8043 | +0.066 | +843.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6436 | +0.047 | +237.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 15121 | +0.043 | +929.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3927 | +0.063 | +545.98€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 572 | +0.009 | +9.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9209 | +0.042 | +357.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1335 | +0.012 | +13.80€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 78 | -0.100 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 15018 | +0.029 | +648.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4084 | +0.035 | +347.26€ | 0 | 8 |
| ✅ UPDOWN_GBM#SOL#240min | 558 | -0.004 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9476 | +0.031 | +299.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 831 | +0.008 | +6.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 69 | -0.134 | -4.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9536 | +0.062 | +1285.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3796 | +0.103 | +1130.42€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5352 | +0.036 | +155.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 232 | -0.103 | +0.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 774 | +0.361 | +273.34€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 774 | +0.361 | +273.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 410 | +0.362 | +140.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 410 | +0.362 | +140.33€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 364 | +0.358 | +133.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 364 | +0.358 | +133.00€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18190 | -0.024 | +4401.05€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18190 | -0.024 | +4401.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3116 | -0.112 | +125.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3116 | -0.112 | +125.59€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2120 | +0.216 | +1366.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2120 | +0.216 | +1366.63€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5170 | -0.063 | +704.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5170 | -0.063 | +704.13€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5184 | -0.064 | +936.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5184 | -0.064 | +936.25€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 201 | +0.037 | +7.46€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 201 | +0.037 | +7.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 201 | +0.037 | +7.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 201 | +0.037 | +7.46€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1281 | +0.290 | +1068.17€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1281 | +0.290 | +1068.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 692 | +0.287 | +543.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 692 | +0.287 | +543.26€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 589 | +0.294 | +524.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 589 | +0.294 | +524.91€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 795 | -0.111 | -81.71€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 795 | -0.111 | -81.71€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 239 | -0.085 | -18.46€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 239 | -0.085 | -18.46€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 84 | -0.151 | -7.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 84 | -0.151 | -7.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 89 | -0.181 | -6.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 89 | -0.181 | -6.27€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3287 | +0.303 | +1584.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1194 | +0.256 | +160.29€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1262 | +0.297 | +560.00€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 831 | +0.379 | +864.08€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.014 n=848 — no justifica filtro, seguir monitorizando
  - _Datos_: n=848 IC=+0.014 PNL=+32.68€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 676 celda(s) pasan gate riguroso completo de 2589 evaluadas (n>=40) y 3584 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=4084 IC=+0.035 PNL=+347.26€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1262/15 IC=+0.297 PNL=+560.00€ | BTC: n=1194/15 IC=+0.256 PNL=+160.29€ | SOL: n=831/15 IC=+0.379 PNL=+864.08€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=716/60 | contraria IC=+0.201 n=747 | gap=-0.060 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=417, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1335/40 IC=+0.012 PNL=+13.80€ | BTC#60min: n=1742/40 IC=+0.006 PNL=+49.71€ | SOL#60min: n=831/40 IC=+0.008 PNL=+6.10€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=495769 | tras_1loss IC=+0.092 n=378174 | tras_2loss IC=+0.062 n=154091/40 | gap=-0.013 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.08 con n=622 PNL=+498.63€
  - _Datos_: n=622 IC=+0.216 PNL=+498.63€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.08 con n=715 PNL=+455.24€
  - _Datos_: n=715 IC=+0.186 PNL=+455.24€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2681 PNL=+1495.23€
  - _Datos_: n=2681 IC=+0.332 PNL=+1495.23€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=568 IC=+0.075 PNL=+66.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=568 IC=+0.075 PNL=+66.51€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=74 IC=+0.171 PNL=+45.37€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=74 IC=+0.171 PNL=+45.37€

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
  - _Estado_: n=2640 IC=+0.009 PNL=+8.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2640 IC=+0.009 PNL=+8.38€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1268 IC=+0.008 PNL=+61.23€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1268 IC=+0.008 PNL=+61.23€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=848 IC=+0.014 PNL=+32.68€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=848 IC=+0.014 PNL=+32.68€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.1 con n=4086 PNL=+2734.20€
  - _Datos_: n=4086 IC=+0.191 PNL=+2734.20€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2118 IC=+0.090 PNL=+513.34€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2118 IC=+0.090 PNL=+513.34€

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
  - _Estado_: n=873 IC=+0.041 PNL=+87.65€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=873 IC=+0.041 PNL=+87.65€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=99 IC=+0.035 PNL=+3.55€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=99 IC=+0.035 PNL=+3.55€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.252 n=143) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=143 IC=+0.252 PNL=+122.85€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.02 con n=873 PNL=+374.09€
  - _Datos_: n=873 IC=+0.129 PNL=+374.09€

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
  - _Estado_: n=26269 IC=+0.074 PNL=+3854.20€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=26269 IC=+0.074 PNL=+3854.20€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.134 < -0.1 con n=410 PNL=+56.22€
  - _Datos_: n=410 IC=-0.134 PNL=+56.22€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2864 IC=+0.065 PNL=+347.74€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2864 IC=+0.065 PNL=+347.74€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.1 con n=691 PNL=+182.10€
  - _Datos_: n=691 IC=+0.116 PNL=+182.10€

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
  - _Estado_: n=27814 IC=-0.136 PNL=+2049.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=27814 IC=-0.136 PNL=+2049.23€

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
  - _Estado_: n=2791 IC=+0.138 PNL=+1697.86€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2791 IC=+0.138 PNL=+1697.86€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6993 IC=+0.046 PNL=+531.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6993 IC=+0.046 PNL=+531.74€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=3034 PNL=+1607.17€
  - _Datos_: n=3034 IC=+0.090 PNL=+1607.17€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=2850 PNL=-224.11€
  - _Datos_: n=2850 IC=-0.224 PNL=-224.11€

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
  - _Estado_: n=59 IC=-0.008 PNL=+5.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=59 IC=-0.008 PNL=+5.77€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=1600) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1600 IC=+0.099 PNL=+348.58€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=534) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=534 IC=+0.412 PNL=+766.29€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=12503 IC=+0.185 PNL=-1296.90€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=12503 IC=+0.185 PNL=-1296.90€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.1 con n=208 PNL=+130.38€
  - _Datos_: n=208 IC=+0.209 PNL=+130.38€
