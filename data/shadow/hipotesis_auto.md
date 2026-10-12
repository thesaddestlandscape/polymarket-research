# Hipótesis automáticas — 2026-10-12 01:59 UTC
_Generado por shadow_postmortem.py sobre 859125 resoluciones (PNL=+107919.13€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.237 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.129)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.195 (n=244)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 68.0 (IC base=+0.129)

- **PATRÓN** `banda_hit_calibrado` > `0.6191` → IC=+0.255 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6191 (IC base=+0.129)

- **PATRÓN** `banda_z` > `9.307` → IC=+0.194 (n=240)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 9.307 (IC base=+0.129)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.723` → IC=+0.128 (n=640)

  - _Acción_: Kelly boost +0.64€ cuando `ballenas_wallet_edge_medio` > 0.723 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=769)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.234 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.135)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.211 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.135)

- **PATRÓN** `banda_hit_calibrado` > `0.6158` → IC=+0.244 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6158 (IC base=+0.135)

- **PATRÓN** `banda_z` > `9.75` → IC=+0.219 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.75 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=671)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.135)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=113)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

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
- **FILTRO** `restante_s_al_confirmar` < `143.95` → IC=-0.205 (n=9138)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.95
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=27426)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.91` → IC=-0.265 (n=1105)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.91
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3318)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.47` → IC=-0.300 (n=1030)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.47
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3091)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.13` → IC=-0.221 (n=2371)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.13
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7114)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.61` → IC=-0.297 (n=1773)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.61
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=5321)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=19273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=4073)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `9416.0594` → IC=+0.181 (n=1820)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9416.0594 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=16201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=19492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=14922)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=6728)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7401.6146` → IC=+0.163 (n=2588)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7401.6146 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=1906)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2396)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `16141.6015` → IC=+0.207 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16141.6015 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=1725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=1922)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=2463)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `16052.1822` → IC=+0.203 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16052.1822 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=429)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `6926.0677` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6926.0677 (IC base=+0.088)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.137 (n=1015)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `5815.7893` → IC=+0.127 (n=239)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 5815.7893 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=3762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.365 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=1665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=937)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.260 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=732)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1510.3152` → IC=+0.148 (n=800)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1510.3152 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.409 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=831)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.370 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.227 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.795` → IC=-0.329 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=16120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=13635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=6756)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=3553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.177 (n=3737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3622)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=1731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.228 (n=1717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.312 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=3694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=3520)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3778)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.188 (n=2030)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.350 (n=1043)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=3618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=3087)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1272)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.431 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.428 (n=626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `4019.0364` → IC=+0.438 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4019.0364 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.447 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `18111.1478` → IC=+0.438 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18111.1478 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.443 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3430.6036` → IC=+0.439 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3430.6036 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.410 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.409 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.421 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.406)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=48086)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=21099)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=3092)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=6600)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=9210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=4213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3050)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=8220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=8800)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=4367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.277 (n=3000)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=7981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=7873)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=3631)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=7465)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.124 (n=6850)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.2 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=7265)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=9046)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.44` → IC=+0.139 (n=6840)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.44 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3694)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.127 (n=3397)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3657)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=4481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `2.93` → IC=+0.146 (n=3392)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.93 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=3771)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=3979)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=3443)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=1498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `4262.2927` → IC=+0.303 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4262.2927 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.296 (n=673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `5350.3552` → IC=+0.314 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5350.3552 (IC base=+0.285)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.326 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1705.54` → IC=+0.307 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1705.54 (IC base=+0.293)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.447 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.464 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.447 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `2089.6231` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2089.6231 (IC base=+0.445)

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

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.271 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=585)

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

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.271 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3641` → IC=+0.137 (n=10131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3641 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.9851` → IC=+0.244 (n=3839)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9851 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2117` → IC=+0.254 (n=2660)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2117 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.977` → IC=+0.186 (n=4348)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.977 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6899` → IC=+0.258 (n=2902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6899 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.232 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.5905` → IC=+0.211 (n=3572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5905 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.3412` → IC=+0.221 (n=3679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3412 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5686` → IC=+0.141 (n=14081)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5686 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.5629` → IC=+0.199 (n=964)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.5629 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.182 (n=5280)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1942 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.054` → IC=+0.182 (n=2393)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.054 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.229 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.451` → IC=+0.204 (n=9037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.451 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.218 (n=8857)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=+0.073)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.214 (n=852)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.209 (n=850)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.2784` → IC=+0.190 (n=2239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2784 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=1698)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.154` → IC=+0.289 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.154 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.240 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.2666` → IC=+0.199 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2666 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=2657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.235 (n=2079)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.244 (n=1863)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.267 (n=693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5048` → IC=+0.255 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5048 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.339` → IC=+0.239 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.339 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0942` → IC=+0.236 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0942 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.256 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6484` → IC=+0.256 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6484 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.236 (n=907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1745` → IC=+0.248 (n=1362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1745 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.235 (n=2044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=2084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9712` → IC=+0.266 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9712 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.1887` → IC=+0.225 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1887 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.260 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.2468` → IC=+0.222 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2468 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.225 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.246 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.5138` → IC=+0.223 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5138 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.247 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.189 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0735` → IC=+0.171 (n=679)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0735 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7276` → IC=+0.180 (n=2038)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7276 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.254` → IC=+0.149 (n=329)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.254 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.302` → IC=+0.146 (n=1861)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.302 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1958` → IC=+0.149 (n=2037)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1958 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.165 (n=753)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4604` → IC=+0.150 (n=1921)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4604 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4188` → IC=+0.145 (n=1921)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4188 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.174 (n=813)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 226.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.216 (n=870)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.264 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.194 (n=2297)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.205 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.1616` → IC=+0.202 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1616 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=3087)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.226 (n=1535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.174` → IC=+0.229 (n=1012)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.174 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1069)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.0693` → IC=+0.236 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0693 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.584` → IC=+0.253 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.584 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.257 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.724` → IC=+0.216 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.724 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.719` → IC=+0.229 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.719 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.220 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.216)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=137)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=3103)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.145 (n=635)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.004 (IC base=+0.049)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.222 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.056` → IC=+0.182 (n=1015)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.056 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8538` → IC=+0.334 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8538 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.236` → IC=+0.350 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.236 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.324 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.347 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.363 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.330 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 150.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.1003` → IC=+0.170 (n=811)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1003 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.184 (n=267)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.455 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.146 (n=901)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8497 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.1692` → IC=+0.142 (n=450)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1692 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.203 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.159 (n=1153)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.031)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=486)

- **FILTRO** `ibs_20min` > `0.2245` → IC=-0.130 (n=3131)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2245
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=1543)

- **FILTRO** `sigma_ewma_delta_pct` > `8.673` → IC=-0.226 (n=480)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.673
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=4194)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.362` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.362 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `0.992` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.992 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1539` → IC=+0.266 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1539 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.2245` → IC=+0.145 (n=1543)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.2245 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2587` → IC=+0.278 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2587 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7066` → IC=+0.285 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7066 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.298 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4196` → IC=+0.297 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4196 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6317` → IC=-0.179 (n=817)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6317
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2454)

- **FILTRO** `ibs_20min` < `0.717` → IC=-0.153 (n=2157)

  - _Acción_: SKIP cuando `ibs_20min` < 0.717
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=1114)

- **FILTRO** `ibs_20min` > `0.7619` → IC=-0.205 (n=1217)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=3653)

- **PATRÓN** `dist_vwap_pct` > `0.7126` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7126 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` < `1.0012` → IC=+0.299 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0012 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.309 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.302 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5988` → IC=+0.299 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5988 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.8742` → IC=+0.303 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8742 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7953` → IC=+0.278 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7953 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.279 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.279 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.257 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.5493` → IC=+0.260 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5493 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.204 (n=5056)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.187 (n=13556)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4615 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.9166` → IC=+0.283 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9166 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.156 (n=6822)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.251 (n=5575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1737 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.688` → IC=+0.259 (n=4982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.688 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2402` → IC=+0.267 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2402 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4632` → IC=+0.249 (n=2986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4632 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6398` → IC=+0.263 (n=2986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6398 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.283 (n=8522)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.160 (n=4879)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0089 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5412` → IC=+0.158 (n=12847)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5412 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.8763` → IC=+0.253 (n=2996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8763 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1974` → IC=+0.261 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1974 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.310 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5882` → IC=+0.282 (n=2777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5882 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2861` → IC=+0.275 (n=2861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2861 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.286 (n=6230)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.259` → IC=-0.178 (n=1049)

  - _Acción_: SKIP cuando `ibs_20min` < 0.259
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=3148)

- **FILTRO** `ibs_20min` > `0.758` → IC=-0.194 (n=864)

  - _Acción_: SKIP cuando `ibs_20min` > 0.758
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2594)

- **FILTRO** `sigma_ewma_delta_pct` > `4.579` → IC=-0.188 (n=763)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.579
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2695)

- **PATRÓN** `ibs_20min` > `0.9143` → IC=+0.288 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9143 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.221` → IC=+0.206 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.221 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.292 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.221 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.2347` → IC=+0.254 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2347 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.249 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.1601` → IC=+0.149 (n=865)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1601 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0804` → IC=+0.422 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0804 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.6091` → IC=+0.410 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6091 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.4542` → IC=+0.410 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4542 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.414 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8587` → IC=+0.143 (n=1031)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8587 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.194 (n=782)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1115 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6777` → IC=+0.185 (n=1311)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6777 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.223 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.196 (n=482)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.4707` → IC=+0.196 (n=482)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4707 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.228 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 222.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1452` → IC=+0.229 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1452 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.232 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6194 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0739` → IC=+0.226 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0739 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.297 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5537` → IC=+0.232 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5537 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1954` → IC=+0.248 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1954 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.281 (n=2025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.263 (n=2274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.259 (n=2023)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.267` → IC=+0.290 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.267 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.269 (n=2064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.1663` → IC=+0.266 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1663 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.268 (n=2665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.305 (n=1909)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.1775` → IC=+0.305 (n=840)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1775 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` < `0.3644` → IC=+0.294 (n=1909)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3644 (IC base=+0.289)

- **PATRÓN** `ibs_20min` > `0.1071` → IC=+0.291 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1071 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.303 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` < `0.1942` → IC=+0.287 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1942 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.3385` → IC=+0.301 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3385 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` < `1.57` → IC=+0.304 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.57 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` > `2.1025` → IC=+0.291 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1025 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.291 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.289)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7559` → IC=-0.181 (n=895)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7559
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=2686)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.166 (n=833)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8947 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0124` → IC=+0.236 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0124 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.237 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.257 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.287 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1235` → IC=+0.214 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1235 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0404` → IC=+0.231 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0404 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.235 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.8358` → IC=+0.261 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8358 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.5032` → IC=+0.244 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5032 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.250 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 130.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7647` → IC=-0.197 (n=1605)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7647
  - _Potencial_: sin este filtro IC_bueno=+0.294 (n=1607)

- **FILTRO** `ibs_20min` > `0.6618` → IC=-0.239 (n=798)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6618
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=2398)

- **FILTRO** `sigma_ewma_delta_pct` > `8.616` → IC=-0.230 (n=365)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.616
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2831)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.294 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7647 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0155` → IC=+0.341 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0155 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.646` → IC=+0.168 (n=501)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.646 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8519` → IC=+0.319 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8519 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.314 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6339 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.309 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.345 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.7951` → IC=+0.322 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7951 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.336 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5574` → IC=+0.135 (n=2110)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5574 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.260 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.236 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.245 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.249 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.266 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.025)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.338 (n=1570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.321 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.315 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.926` → IC=+0.294 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.926 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `0.6244` → IC=+0.305 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6244 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.341 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.306 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.329 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.325 (n=1239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1852` → IC=+0.295 (n=818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1852 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.301 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.37` → IC=+0.319 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.37 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.304 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.013` → IC=+0.294 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.013 (IC base=+0.293)

- **PATRÓN** `volumen_regimen` > `1.2282` → IC=+0.325 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2282 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.344 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.4194` → IC=+0.300 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4194 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.1442` → IC=+0.297 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1442 (IC base=+0.293)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.217 (n=3737)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3442` → IC=+0.187 (n=9861)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3442 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=11694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.563` → IC=+0.230 (n=11204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.563 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1636` → IC=+0.202 (n=4687)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1636 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.371` → IC=+0.253 (n=2237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.371 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1981` → IC=+0.169 (n=7429)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1981 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6267` → IC=+0.163 (n=7429)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6267 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.198 (n=1648)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4523` → IC=+0.176 (n=3612)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4523 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6086` → IC=+0.186 (n=3611)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6086 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2527.9944` → IC=+0.180 (n=7469)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2527.9944 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.193 (n=10112)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.187 (n=7133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0066 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0789` → IC=+0.225 (n=3563)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0789 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=4029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.494` → IC=+0.234 (n=10685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.494 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.205` → IC=+0.195 (n=1773)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.205 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1807` → IC=+0.165 (n=7642)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1807 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.222 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6192` → IC=+0.182 (n=3321)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6192 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.192 (n=8497)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 68.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.234 (n=630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.220 (n=630)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.224 (n=1885)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=1263)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.92` → IC=+0.285 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.92 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.19` → IC=+0.333 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.19 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.261 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.5423` → IC=+0.205 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5423 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1984)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.246 (n=1268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=1291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0986` → IC=+0.293 (n=635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0986 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.2662` → IC=+0.264 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2662 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.16` → IC=+0.245 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.16 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.240 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2945` → IC=+0.281 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2945 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4285` → IC=+0.253 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4285 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.251 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.220 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.1598` → IC=+0.188 (n=1120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1598 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=1773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3685` → IC=+0.223 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3685 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1357` → IC=+0.208 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1357 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.229 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6891` → IC=+0.169 (n=739)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6891 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.185 (n=268)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.414` → IC=+0.183 (n=547)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.414 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.5032` → IC=+0.159 (n=547)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5032 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `427.0` → IC=+0.162 (n=1600)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 427.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.165 (n=1755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0056 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2285` → IC=+0.175 (n=1545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2285 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6041` → IC=+0.203 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6041 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.732` → IC=+0.204 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.732 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.165 (n=1755)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2032 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0943` → IC=+0.145 (n=1469)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0943 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.146 (n=541)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.154 (n=1638)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7741` → IC=+0.147 (n=1092)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7741 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.166 (n=687)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 235.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.231 (n=861)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.3997` → IC=+0.220 (n=1664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3997 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.472` → IC=+0.287 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.472 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.216 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7731` → IC=+0.217 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7731 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.218 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.246 (n=1412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.559` → IC=+0.244 (n=1605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.559 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.283 (n=537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.3529` → IC=+0.251 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3529 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.265 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.265 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7192` → IC=+0.243 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7192 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.7169` → IC=+0.234 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7169 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.232 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.231)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.183 (n=1588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0063 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.202 (n=601)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3217` → IC=+0.208 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3217 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1353` → IC=+0.188 (n=1134)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1353 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.208 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.162 (n=1202)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.856 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.177 (n=744)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4265` → IC=+0.160 (n=589)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4265 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.167 (n=589)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `5124.8114` → IC=+0.201 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5124.8114 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.158 (n=1744)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 146.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.158 (n=1665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3804` → IC=+0.146 (n=1887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3804 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.187 (n=1887)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6801 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.868` → IC=+0.152 (n=662)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 6.868 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.161 (n=1258)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8557 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.188 (n=286)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8063` → IC=+0.132 (n=1170)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8063 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4127` → IC=+0.131 (n=1755)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4127 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `4523.6243` → IC=+0.172 (n=1258)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4523.6243 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.126 (n=1702)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 145.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.167 (n=928)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0099 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4347` → IC=+0.128 (n=1803)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4347 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.214 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.191` → IC=+0.186 (n=1223)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.191 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.731` → IC=+0.265 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.731 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.141 (n=2047)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1894 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.128 (n=1829)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.7151 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.137 (n=2072)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4402` → IC=+0.142 (n=662)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4402 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=2123)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2898.7698` → IC=+0.209 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2898.7698 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.159 (n=638)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 21.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.137 (n=2068)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0103 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1027` → IC=+0.172 (n=689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1027 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5893` → IC=+0.217 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5893 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.7373` → IC=+0.129 (n=354)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.7373 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.223` → IC=+0.125 (n=622)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 5.223 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.131 (n=2067)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1753 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.149 (n=269)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4517` → IC=+0.136 (n=636)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4517 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.127 (n=636)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2162.3017` → IC=+0.175 (n=1378)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2162.3017 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.128 (n=1875)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 51.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.238 (n=1700)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.2828` → IC=+0.224 (n=1269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2828 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=1979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6552` → IC=+0.252 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6552 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1892` → IC=+0.219 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1892 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2685` → IC=+0.216 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2685 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.246 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.0264` → IC=+0.216 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0264 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6192` → IC=+0.223 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6192 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2338` → IC=+0.263 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2338 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.4918` → IC=+0.219 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4918 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.8141` → IC=+0.230 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8141 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2994.8954` → IC=+0.225 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.8954 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.232 (n=852)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.228 (n=879)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0887` → IC=+0.253 (n=645)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0887 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=884)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.253 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `1.1412` → IC=+0.235 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1412 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.251 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.233 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.283 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.2093` → IC=+0.217 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2093 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.225 (n=1787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.223)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.209 (n=974)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3303` → IC=+0.181 (n=2566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3303 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=2644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4861` → IC=+0.205 (n=2605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4861 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.5777` → IC=+0.181 (n=574)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.5777 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.197 (n=1247)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.0587` → IC=+0.182 (n=2306)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0587 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.174 (n=2341)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6955 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.181 (n=1047)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.187 (n=945)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.174 (n=945)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=2692)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2783.1673` → IC=+0.176 (n=2605)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2783.1673 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.184 (n=2696)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 151.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.145 (n=998)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0036 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.123 (n=2006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 11.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.0816` → IC=+0.196 (n=995)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0816 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.123 (n=1142)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.4323` → IC=+0.138 (n=967)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4323 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `4538.7388` → IC=+0.134 (n=1989)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 4538.7388 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.133 (n=946)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 20.0 (IC base=+0.108)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.207 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.214 (n=369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.6393` → IC=+0.212 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6393 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.3004` → IC=+0.180 (n=264)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3004 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.088` → IC=+0.183 (n=358)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.088 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.186 (n=558)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8755 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.170 (n=328)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.2301` → IC=+0.165 (n=721)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.2301 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.4195` → IC=+0.161 (n=819)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4195 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `14731.9311` → IC=+0.170 (n=558)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14731.9311 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.198 (n=356)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 152.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.187 (n=321)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.2637` → IC=+0.151 (n=846)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2637 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.3773` → IC=+0.198 (n=641)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3773 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.508` → IC=+0.143 (n=1010)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.508 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2002` → IC=+0.142 (n=961)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2002 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.152 (n=859)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6986 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.180 (n=379)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.156 (n=836)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=1246)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `356.0` → IC=+0.152 (n=929)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 356.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.248 (n=609)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.1988` → IC=+0.225 (n=608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1988 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.6787` → IC=+0.264 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6787 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.210 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.211 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.224 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.836` → IC=+0.211 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.836 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.222 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.182 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.235 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4106` → IC=+0.245 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4106 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.222 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.125 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0037 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.0923` → IC=+0.169 (n=297)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0923 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `3973.2352` → IC=+0.128 (n=796)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3973.2352 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.128 (n=382)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 43.0 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.154 (n=455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0074 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.175 (n=613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.932 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.127` → IC=+0.204 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.127 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.163 (n=600)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0604 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.7239` → IC=+0.156 (n=609)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7239 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1675` → IC=+0.174 (n=191)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1675 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.1991` → IC=+0.157 (n=298)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1991 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=708)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3089.4567` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3089.4567 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.211 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.5717` → IC=+0.132 (n=275)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.5717 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `2878.0687` → IC=+0.154 (n=296)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2878.0687 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.122 (n=533)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 33.0 (IC base=+0.071)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.180 (n=4871)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.219 (n=4856)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=15231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5596` → IC=+0.237 (n=13004)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5596 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1597` → IC=+0.187 (n=5339)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1597 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.252 (n=3583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.878` → IC=+0.175 (n=6497)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.878 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.202 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6096` → IC=+0.195 (n=4706)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6096 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2501.6603` → IC=+0.185 (n=9704)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2501.6603 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.205 (n=11606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.194 (n=5774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1438` → IC=+0.196 (n=5763)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1438 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.241 (n=13097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.01` → IC=+0.207 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.01 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.683` → IC=+0.189 (n=12633)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.683 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.164 (n=3895)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7044 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.251 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6155` → IC=+0.198 (n=4103)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6155 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.212 (n=8011)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.244 (n=802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.244 (n=799)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.220 (n=2401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.217 (n=1608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.666` → IC=+0.350 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.666 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.277 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.5938` → IC=+0.227 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5938 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=2487)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.229 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.262 (n=2007)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=2005)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.202` → IC=+0.272 (n=1337)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.202 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.494` → IC=+0.283 (n=2005)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.494 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.536` → IC=+0.263 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.536 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.286 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6447` → IC=+0.280 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6447 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2215)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.199 (n=781)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0026 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.175` → IC=+0.169 (n=1558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.175 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=2445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.2726` → IC=+0.208 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2726 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.191 (n=1279)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.71` → IC=+0.167 (n=394)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.71 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.2` → IC=+0.157 (n=2127)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.2 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6278` → IC=+0.176 (n=779)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6278 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.180 (n=336)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1754` → IC=+0.160 (n=2003)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1754 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5326` → IC=+0.154 (n=2033)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5326 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `271.0` → IC=+0.183 (n=977)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 271.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.197 (n=648)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0026 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0767` → IC=+0.185 (n=645)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0767 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6944` → IC=+0.198 (n=1930)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6944 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.5` → IC=+0.159 (n=326)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.5 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1838` → IC=+0.161 (n=1930)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1838 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1535` → IC=+0.194 (n=521)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1535 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.155 (n=1828)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7857` → IC=+0.162 (n=1218)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7857 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.247 (n=806)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.406` → IC=+0.313 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.406 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.225 (n=2119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7698` → IC=+0.228 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7698 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2851)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.244 (n=1498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.240 (n=2009)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.178` → IC=+0.259 (n=988)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.178 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0196` → IC=+0.303 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0196 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.1` → IC=+0.289 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.1 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3416` → IC=+0.301 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3416 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.723` → IC=+0.239 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.723 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1315` → IC=+0.248 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1315 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.260 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.239)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.201 (n=1100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.166 (n=1097)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2654` → IC=+0.193 (n=2493)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2654 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.5371` → IC=+0.167 (n=641)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.5371 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.203` → IC=+0.163 (n=1019)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.203 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.165 (n=1662)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8725 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2354` → IC=+0.179 (n=443)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2354 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5213` → IC=+0.172 (n=1069)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5213 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1702` → IC=+0.158 (n=1101)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1702 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7207.809` → IC=+0.238 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7207.809 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.178 (n=808)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 68.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.195 (n=679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0032 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3357` → IC=+0.140 (n=1785)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3357 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7417` → IC=+0.187 (n=2029)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7417 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.168 (n=416)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6997` → IC=+0.145 (n=893)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6997 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.224 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4325` → IC=+0.141 (n=1946)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4325 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5472.4764` → IC=+0.204 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5472.4764 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.145 (n=1678)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.008 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4507` → IC=+0.199 (n=2514)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4507 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0121` → IC=+0.205 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0121 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.948` → IC=+0.264 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.948 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8874` → IC=+0.149 (n=1677)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8874 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1628` → IC=+0.127 (n=2602)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1628 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.134 (n=329)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.4804` → IC=+0.124 (n=2452)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4804 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.4662` → IC=+0.128 (n=2451)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4662 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2559)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2925.9204` → IC=+0.252 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2925.9204 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.138 (n=789)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 26.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.177 (n=800)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0057 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1288` → IC=+0.161 (n=795)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1288 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=1121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.213 (n=2387)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.401` → IC=+0.134 (n=2291)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.401 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.7128` → IC=+0.149 (n=1049)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.7128 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.171 (n=396)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4342` → IC=+0.154 (n=738)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4342 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2801.7024` → IC=+0.208 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2801.7024 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.138 (n=1948)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 49.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.241 (n=2149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.605` → IC=+0.269 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.605 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.236 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.73` → IC=+0.264 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.73 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.2312` → IC=+0.228 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2312 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6382` → IC=+0.225 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6382 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2371` → IC=+0.249 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2371 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.5202` → IC=+0.249 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5202 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=2108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2994.512` → IC=+0.242 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.512 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.225 (n=837)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.239 (n=1136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=2351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.261 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.188` → IC=+0.254 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.188 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.254 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.291 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.5473` → IC=+0.223 (n=2067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5473 (IC base=+0.222)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=4278)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.235 (n=1462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.4948` → IC=+0.205 (n=4375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4948 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=1606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=2999)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.245 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.1667` → IC=+0.200 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1667 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.2359` → IC=+0.198 (n=2698)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2359 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.174` → IC=+0.212 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.174 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.208 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `0.8892` → IC=+0.200 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8892 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.1674` → IC=+0.218 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1674 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.203 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.272` → IC=+0.201 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.272 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=3290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2995.9331` → IC=+0.207 (n=3908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.9331 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.226 (n=1077)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.195 (n=3220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=1106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=1465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.1819` → IC=+0.196 (n=1417)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1819 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.6371` → IC=+0.185 (n=564)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6371 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.169` → IC=+0.182 (n=3223)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.169 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2515` → IC=+0.183 (n=3027)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2515 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.181 (n=2936)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.182 (n=1469)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.183 (n=1397)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8164` → IC=+0.184 (n=2117)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.8164 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=4278)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.187 (n=1398)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 35.0 (IC base=+0.177)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.249 (n=373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.271 (n=186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.229 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.5098` → IC=+0.246 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5098 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.7609` → IC=+0.226 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7609 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.3158` → IC=+0.232 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3158 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.078` → IC=+0.244 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.078 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.566` → IC=+0.223 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.566 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.230 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2271 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.5974` → IC=+0.235 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5974 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.239 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `12554.5188` → IC=+0.246 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12554.5188 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.235 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3655` → IC=+0.170 (n=1099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3655 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.188 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.157` → IC=+0.183 (n=484)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.157 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.161 (n=499)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6091 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.6635` → IC=+0.185 (n=109)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6635 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.1554` → IC=+0.157 (n=1073)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1554 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.114` → IC=+0.167 (n=1203)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 9.114 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.194 (n=733)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8817 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.194 (n=230)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.5375` → IC=+0.162 (n=1096)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5375 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8143` → IC=+0.175 (n=730)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8143 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `11538.1781` → IC=+0.170 (n=1099)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 11538.1781 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.169 (n=1054)

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
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.215 (n=1133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.4565` → IC=+0.209 (n=1286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4565 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.202 (n=595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.5211` → IC=+0.217 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5211 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.208 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8799 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.134` → IC=+0.209 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.134 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.8828` → IC=+0.207 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8828 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `1.2441` → IC=+0.210 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2441 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.204 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.209 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.4204` → IC=+0.220 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4204 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.241 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.202 (n=1030)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.190 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.189 (n=699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 10.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.7588` → IC=+0.180 (n=1030)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7588 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.0884` → IC=+0.178 (n=1030)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.0884 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.6251` → IC=+0.197 (n=196)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6251 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.747` → IC=+0.180 (n=1055)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.747 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.2456` → IC=+0.189 (n=1030)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2456 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `0.721` → IC=+0.176 (n=920)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.721 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.195 (n=434)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `2.183` → IC=+0.189 (n=888)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.183 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.7774` → IC=+0.178 (n=672)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.7774 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `7364.453` → IC=+0.190 (n=1030)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7364.453 (IC base=+0.175)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.206 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.197 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 4.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.244 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.6619` → IC=+0.209 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6619 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.165` → IC=+0.211 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.165 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.7012` → IC=+0.212 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7012 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` < `0.1075` → IC=+0.173 (n=551)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.1075 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.192 (n=186)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.5474` → IC=+0.206 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5474 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=712)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3226.1934` → IC=+0.200 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3226.1934 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.180 (n=592)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 54.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.193 (n=294)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0083 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.220 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.357` → IC=+0.231 (n=292)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.357 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.222 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.2034` → IC=+0.244 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2034 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.762` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.762 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.982` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.982 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.862` → IC=+0.194 (n=384)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.862 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.7551` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7551 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.226 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.194 (n=142)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3191.6314` → IC=+0.215 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3191.6314 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.225 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.190)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.159 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.4161` → IC=+0.148 (n=1343)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4161 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1388` → IC=+0.139 (n=718)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1388 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.184 (n=302)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.167 (n=181)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.1925` → IC=+0.248 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1925 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.0854` → IC=+0.126 (n=615)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.0854 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.1463` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1463 (IC base=+0.055)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.138 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.137 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 18.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.5456` → IC=+0.193 (n=409)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5456 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.126 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0034 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.1051` → IC=+0.130 (n=298)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1051 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.698` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 4.698 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `1.0149` → IC=+0.121 (n=259)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.0149 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.123 (n=271)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.076)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.185 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0029 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.211 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.179 (n=235)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.658` → IC=+0.270 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.658 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.5851` → IC=+0.128 (n=146)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.5851 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.200 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1723.7312` → IC=+0.153 (n=145)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1723.7312 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.106 (IC base=+0.005)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.243` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.243 (IC base=+0.005)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1379` → IC=-0.245 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1379
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=150)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.161 (n=299)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.76 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.874` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 7.874 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.033)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.156 (n=181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.1379` → IC=+0.257 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1379 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1328` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1328 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.3459` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3459 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.803` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.803 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.6637` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6637 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `0.9765` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.9765 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.1886` → IC=+0.178 (n=113)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.1886 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `1.49` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.49 (IC base=+0.074)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.204 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `781.6495` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 781.6495 (IC base=+0.074)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.328 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=215)

- **FILTRO** `dist_vwap_pct` > `0.235` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.235
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=261)

- **FILTRO** `volumen_regimen` < `0.7597` → IC=-0.331 (n=69)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7597
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=208)

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
- **FILTRO** `hora_utc` > `9.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=52)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=76)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=35)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.438 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=63)

- **FILTRO** `volumen_spike_ratio` > `2.7358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.7358
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=51)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=67)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=57)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=35)

- **FILTRO** `volumen_spike_ratio` < `1.4493` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4493
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=36)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.9583 (IC base=-0.153)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=76)

- **FILTRO** `volumen_spike_ratio` < `1.5614` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5614
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=66)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.175 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0057 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.145 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 15.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.6732` → IC=+0.153 (n=450)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6732 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.4854` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4854 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.657` → IC=+0.158 (n=150)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.657 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` < `0.2366` → IC=+0.144 (n=388)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2366 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.5344` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5344 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.1653` → IC=+0.170 (n=455)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1653 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.127` → IC=+0.194 (n=158)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.127 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `2923.7123` → IC=+0.157 (n=345)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2923.7123 (IC base=+0.072)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.228 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.167 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.185 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.211 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1381 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.0895` → IC=+0.167 (n=238)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.0895 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.265` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 10.265 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.678` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 4.678 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.171 (n=208)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.6754 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.078` → IC=+0.183 (n=178)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.078 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.5892` → IC=+0.191 (n=202)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.5892 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `5904.6349` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 5904.6349 (IC base=+0.154)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1403` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1403
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=144)

- **FILTRO** `ibs_20min` > `0.2457` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2457
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=173)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.138 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0044 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.161 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.7141` → IC=+0.138 (n=158)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7141 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` < `0.1403` → IC=+0.130 (n=144)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1403 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `1.7926` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7926 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `1859.8936` → IC=+0.136 (n=105)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1859.8936 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.2457` → IC=+0.123 (n=173)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2457 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.040)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.2724` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=95)

- **FILTRO** `volumen_spike_ratio` > `1.818` → IC=-0.143 (n=40)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.818
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=41)

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

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.075)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.352 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1245.0` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1245.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.216)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.216)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.216)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.269 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.216)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.216)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.352 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1245.0` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1245.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.216)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.216)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.216)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.269 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.216)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.216)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=167)

- **FILTRO** `libro_liquidez` < `2695.8014` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `libro_liquidez` < 2695.8014
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=138)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=59)

- **FILTRO** `libro_liquidez` < `10902.4411` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 10902.4411
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=60)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### LIQUIDACIONES_15M#SOL#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=3050)

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
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=122)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.045)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1113)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1067)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=703)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=386)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=367)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.146 (n=145)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.015)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=791)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=791)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=625)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=647)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=647)

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

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=161)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=185)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=198)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=316)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=316)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=227)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.145 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=168)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=1613)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1732)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.136 (n=218)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=114)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.135 (n=209)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.56 (IC base=+0.030)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=179)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.5 (IC base=-0.007)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.173 (n=99)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=118)

- **PATRÓN** `py_entrada` < `0.54` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.54 (IC base=+0.037)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.131 (n=220)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=75)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.180 (n=73)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=222)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.245 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=239)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.46 (IC base=-0.027)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.124 (n=240)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=136)

- **FILTRO** `restante_min` < `3.33` → IC=-0.182 (n=124)

  - _Acción_: SKIP cuando `restante_min` < 3.33
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=252)

- **FILTRO** `lag_apertura_s` > `98.98` → IC=-0.190 (n=127)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.98
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=249)

- **FILTRO** `profundidad_ratio` < `23.0` → IC=-0.121 (n=101)

  - _Acción_: SKIP cuando `profundidad_ratio` < 23.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=207)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=233)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=101)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=-0.002)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.142 (n=230)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=121)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.187 (n=97)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=333)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.157 (n=5276)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=15849)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.167 (n=5409)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=16362)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.185 (n=943)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2840)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.157 (n=904)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2990)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.120 (n=1802)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.173 (n=751)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2378)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.173 (n=932)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2896)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=988)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=2973)

- **PATRÓN** `ibs_20min` > `0.9653` → IC=+0.120 (n=1302)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.9653 (IC base=+0.037)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2242)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2651)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3391)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `libro_liquidez` < `16920.0467` → IC=-0.163 (n=176)

  - _Acción_: SKIP cuando `libro_liquidez` < 16920.0467
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=359)

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
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=321)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=815)

- **FILTRO** `libro_liquidez` < `2042.3274` → IC=-0.163 (n=342)

  - _Acción_: SKIP cuando `libro_liquidez` < 2042.3274
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=696)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=14560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=32700)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=11323)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=35937)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=11739)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=35521)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=15626)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=31634)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=14497)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=45409)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.179 (n=14917)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=44989)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5783)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.234 (n=4013)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4117)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.248 (n=2677)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=5453)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.173 (n=1928)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=6202)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2544)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=7849)

- **FILTRO** `ibs_7min` > `0.7755` → IC=-0.208 (n=2598)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7755
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7795)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=1923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6110)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.245 (n=2008)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=6025)

- **FILTRO** `ibs_7min` < `0.7371` → IC=-0.195 (n=2006)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7371
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6027)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.187 (n=1995)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6038)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1967)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6207)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.195 (n=2043)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6131)

- **FILTRO** `ballena_activa_n` > `147.0` → IC=-0.182 (n=2040)

  - _Acción_: SKIP cuando `ballena_activa_n` > 147.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6134)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=1896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5831)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=1848)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5879)

- **FILTRO** `ibs_7min` < `0.7032` → IC=-0.246 (n=2549)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7032
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5178)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.222 (n=1652)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6075)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.247 (n=2502)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=8559)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.175 (n=2765)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8296)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=2509)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=5236)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1931)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=5814)

- **FILTRO** `ibs_7min` < `0.7354` → IC=-0.185 (n=1936)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7354
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5809)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.190 (n=1927)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5818)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1991)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=6010)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.179 (n=1999)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6002)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.179 (n=1968)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6033)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1924)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5955)

- **FILTRO** `ibs_7min` < `0.2353` → IC=-0.234 (n=1958)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2353
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=5921)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2706)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8735)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.281 (n=1898)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=5848)

- **FILTRO** `ibs_7min` < `0.2308` → IC=-0.223 (n=1934)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2308
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5812)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1819)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=5927)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.208 (n=2636)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=8200)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=979)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1263)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.160 (n=51)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=630)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=370)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.138 (n=158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=314)

- **FILTRO** `libro_liquidez` < `3312.3658` → IC=-0.151 (n=167)

  - _Acción_: SKIP cuando `libro_liquidez` < 3312.3658
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=501)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=334)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3979` → IC=+0.140 (n=1017)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3979 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `3732.187` → IC=+0.144 (n=678)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 3732.187 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3737.086` → IC=+0.129 (n=461)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3737.086 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.143 (n=345)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 14.0 (IC base=+0.125)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.154 (n=79)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.218 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2631.223` → IC=+0.241 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2631.223 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 10.0 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.132 (n=202)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.124 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 14.0 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.123 (n=237)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.150 (n=98)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 10.0 (IC base=+0.113)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.174 (n=136)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.146 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 4.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `7216.6532` → IC=+0.132 (n=183)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7216.6532 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 73.0 (IC base=+0.124)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4332` → IC=+0.241 (n=83)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.179 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `7882.091` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 7882.091 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3096.9147` → IC=+0.163 (n=182)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3096.9147 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 28.0 (IC base=+0.152)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=121)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `3656.7944` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3656.7944 (IC base=+0.093)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.270 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=294)

- **FILTRO** `T_h` > `130.2581` → IC=-0.221 (n=145)

  - _Acción_: SKIP cuando `T_h` > 130.2581
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=438)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.131 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0042 (IC base=-0.088)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.264 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=88)

- **FILTRO** `T_h` > `88.1896` → IC=-0.300 (n=43)

  - _Acción_: SKIP cuando `T_h` > 88.1896
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=132)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.304 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.042)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7112` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.7112 (IC base=-0.042)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=70)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.221 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=135)

- **FILTRO** `pct_vs_K` |x|> `2.2275` → IC=-0.386 (n=226)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.2275
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=228)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=138)

- **FILTRO** `T_h` > `79.3043` → IC=-0.177 (n=122)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `pct_vs_K` |x|> `2.067` → IC=-0.393 (n=82)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.067
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=84)

### PRICE_TARGET_GBM_FADE#BTC#reach
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
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.288 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=102)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.361 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=106)

- **FILTRO** `pct_vs_K` |x|> `2.6475` → IC=-0.401 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6475
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.245 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=94)

- **FILTRO** `T_h` > `111.9844` → IC=-0.176 (n=69)

  - _Acción_: SKIP cuando `T_h` > 111.9844
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=70)

- **FILTRO** `sigma_h` > `0.0132` → IC=-0.348 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `T_h` > `46.6251` → IC=-0.391 (n=62)

  - _Acción_: SKIP cuando `T_h` > 46.6251
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=32)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.475 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.341)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.365 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.386 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.341)

- **PATRÓN** `T_h` < `0.9781` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9781 (IC base=+0.341)

- **PATRÓN** `T_h` > `1.1834` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1834 (IC base=+0.341)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.361 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.341)

- **PATRÓN** `edge` > `0.096` → IC=+0.446 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.441 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.418)

- **PATRÓN** `T_h` < `1.014` → IC=+0.426 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.014 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.3874` → IC=+0.465 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3874 (IC base=+0.418)

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
- **PATRÓN** `edge` > `0.1975` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.432)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.464 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.432)

- **PATRÓN** `T_h` > `0.639` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.639 (IC base=+0.432)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.432)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.477 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.2025` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2025 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4455` → IC=+0.485 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4455 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=266)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=352)

- **PATRÓN** `streak_estiramiento` < `0.4345` → IC=+0.137 (n=89)

  - _Acción_: Kelly boost +0.69€ cuando `streak_estiramiento` < 0.4345 (IC base=+0.023)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `2526.423` → IC=+0.123 (n=128)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2526.423 (IC base=+0.041)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.4782` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.4782 (IC base=+0.021)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.092)

- **PATRÓN** `streak_estiramiento` < `0.3243` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.3243 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 45.0 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2659.6588` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2659.6588 (IC base=+0.092)

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
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=681)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=886)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1324)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1022)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1034)

### STRUCT_NO_15M
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3681)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1960)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.204 (n=1010)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.231 (n=1010)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1654` → IC=+0.200 (n=2666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1654 (IC base=+0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2285` → IC=+0.193 (n=1011)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2285 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3524` → IC=+0.205 (n=2694)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3524 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=2818)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=2770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.5876` → IC=+0.268 (n=3029)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5876 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.185 (n=1433)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.2984` → IC=+0.180 (n=2273)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2984 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.594` → IC=+0.272 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.594 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `5486.381` → IC=+0.202 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5486.381 (IC base=+0.192)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1177)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.239 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.262 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.217)

- **PATRÓN** `delta_ratio_macro` |x|> `0.255` → IC=+0.268 (n=179)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.255 (IC base=+0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2323` → IC=+0.231 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2323 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.279 (n=537)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.250 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.196` → IC=+0.294 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.196 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16272.4583` → IC=+0.251 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16272.4583 (IC base=+0.217)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=674)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.183 (n=200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0033 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0671` → IC=+0.158 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0671 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.3987` → IC=+0.148 (n=200)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.3987 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.149` → IC=+0.162 (n=400)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.149 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.165 (n=231)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.155 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.153 (n=626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.242 (n=598)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1126` → IC=+0.148 (n=382)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1126 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.2646` → IC=+0.152 (n=556)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2646 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.288 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3532.4883` → IC=+0.153 (n=534)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3532.4883 (IC base=+0.147)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `19.46` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.46
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=241)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.147 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0055 (IC base=+0.116)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.167 (n=187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0095 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.2361` → IC=+0.137 (n=562)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.2361 (IC base=+0.116)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3426` → IC=+0.137 (n=511)

  - _Acción_: Kelly boost +0.69€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3426 (IC base=+0.116)

- **PATRÓN** `ibs_15` > `0.5082` → IC=+0.195 (n=500)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.5082 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.1875` → IC=+0.138 (n=495)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1875 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.263` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.263 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=312)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.116)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `16.21` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 16.21 (IC base=+0.013)

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
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.365 (n=383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.371 (n=574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.385 (n=382)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.394 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.398 (n=574)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4131` → IC=+0.384 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4131 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.88` → IC=+0.385 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.88 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `3496.0889` → IC=+0.370 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3496.0889 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.360 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.5078` → IC=+0.359 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5078 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.394 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.392 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.386 (n=306)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.2544` → IC=+0.393 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2544 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.144` → IC=+0.382 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.144 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `15252.9657` → IC=+0.387 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15252.9657 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.408 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.363 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.374 (n=269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.368 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0904` → IC=+0.376 (n=240)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0904 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.388 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.407 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.363 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.408 (n=269)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4372` → IC=+0.364 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4372 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2765` → IC=+0.370 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2765 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.394 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.387 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.372 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 140.0 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.221 (n=983)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2952)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1528)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2407)

- **FILTRO** `libro_liquidez` < `4106.9198` → IC=-0.145 (n=2597)

  - _Acción_: SKIP cuando `libro_liquidez` < 4106.9198
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=1338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1424` → IC=+0.189 (n=628)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1424 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.283 (n=942)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1071` → IC=+0.205 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1071 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2619` → IC=+0.201 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2619 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1326` → IC=+0.263 (n=2124)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1326 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3519` → IC=+0.281 (n=3185)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3519 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.64` → IC=+0.281 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.64 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.203 (n=543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1632)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.225 (n=717)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=1458)

- **FILTRO** `sigma_ewma_delta_pct` > `23.806` → IC=-0.269 (n=314)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.806
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1861)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.198 (n=61)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=2114)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.170 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0026 (IC base=+0.093)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.306 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=+0.093)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.137 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.335 (n=288)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.299 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.293 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.877` → IC=+0.139 (n=153)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 24.877 (IC base=+0.093)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.236 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.311 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.192)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=613)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.166 (n=423)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0037 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1112` → IC=+0.182 (n=316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1112 (IC base=+0.153)

- **PATRÓN** `drift_15min` |x|≤ `0.4036` → IC=+0.156 (n=158)

  - _Acción_: Kelly boost +0.78€ cuando `drift_15min` |x|≤ 0.4036 (IC base=+0.153)

- **PATRÓN** `delta_ratio_macro` |x|> `0.141` → IC=+0.159 (n=315)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.141 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.198 (n=356)

  - _Acción_: Kelly boost +0.99€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.177 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.254 (n=473)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.158 (n=443)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.266 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.260 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=613)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10832.5702` → IC=+0.169 (n=158)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10832.5702 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.260 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.3441` → IC=+0.243 (n=956)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3441 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.7457` → IC=+0.252 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7457 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1556` → IC=+0.256 (n=724)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1556 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.243 (n=965)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3657` → IC=+0.270 (n=1087)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3657 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.7664` → IC=+0.288 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7664 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.365` → IC=+0.263 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.365 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.558` → IC=+0.244 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.558 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1716` → IC=-0.253 (n=306)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1716
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=595)

- **FILTRO** `drift_15min` |x|> `0.8763` → IC=-0.271 (n=225)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8763
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=676)

- **FILTRO** `sigma_ewma_delta_pct` > `6.585` → IC=-0.192 (n=219)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.585
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=682)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.180)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.180)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.180)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.180)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0646` → IC=+0.245 (n=493)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0646 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.288 (n=493)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.038)

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
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.030)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.030)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.297 (n=839)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.292 (n=953)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.322 (n=318)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.248` → IC=+0.300 (n=318)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.248 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2248` → IC=+0.311 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2248 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.323 (n=953)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.318 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.005` → IC=+0.365 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.005 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12796.3088` → IC=+0.309 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12796.3088 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.308 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.310 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2616` → IC=+0.316 (n=172)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2616 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8267` → IC=+0.310 (n=515)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8267 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.326 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.371` → IC=+0.373 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.371 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16341.0554` → IC=+0.322 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16341.0554 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.307 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.298 (n=438)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.326 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1536` → IC=+0.303 (n=292)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1536 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.320 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.317 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.334 (n=438)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.866` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.866 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0857` → IC=-0.250 (n=78)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0857
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=241)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.172 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=352)

- **FILTRO** `ballena_activa_n` > `51.0` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `ballena_activa_n` > 51.0
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=158)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1289` → IC=-0.167 (n=46)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1289
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=140)

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

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `81.6124` → IC=+0.199 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6124 (IC base=+0.195)

- **PATRÓN** `ratio` < `0.9749` → IC=+0.431 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9749 (IC base=+0.195)

- **PATRÓN** `T_h` > `145.7324` → IC=+0.385 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7324 (IC base=+0.338)

- **PATRÓN** `ratio` > `1.0083` → IC=+0.319 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0083 (IC base=+0.338)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.3426` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.3426 (IC base=+0.174)

- **PATRÓN** `ratio` < `0.972` → IC=+0.423 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.174)

- **PATRÓN** `T_h` > `107.4888` → IC=+0.305 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 107.4888 (IC base=+0.294)

- **PATRÓN** `ratio` > `1.0467` → IC=+0.399 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0467 (IC base=+0.294)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `81.6471` → IC=+0.241 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6471 (IC base=+0.228)

- **PATRÓN** `ratio` < `0.985` → IC=+0.432 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.985 (IC base=+0.228)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.352 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.327)

- **PATRÓN** `ratio` > `1.01` → IC=+0.365 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.327)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1062` → IC=+0.450 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1062 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5876 sube el IC de +0.192 a +0.268 en UPDOWN_GBM#15min (n=3029). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.217 a +0.279 en UPDOWN_GBM#BTC#15min (n=537). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.147 a +0.242 en UPDOWN_GBM#ETH#15min (n=598). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5082 sube el IC de +0.116 a +0.195 en UPDOWN_GBM#SOL#15min (n=500). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5745 sube el IC de +0.222 a +0.303 en UPDOWN_GBM#XRP#15min (n=699). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.065 a +0.162 en UPDOWN_GBM#XRP#15min (n=722). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.066 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=942). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3519 sube el IC de -0.012 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=3185). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.093 a +0.335 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=288). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.192 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.153 a +0.254 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=473). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3657 sube el IC de +0.241 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1087). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.180 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.038 a +0.288 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=493). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.202 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.027 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=778). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.292 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=953). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8267 sube el IC de +0.286 a +0.310 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=515). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.297 a +0.334 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=438). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.363 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=574). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.361 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=306). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.364 a +0.408 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=269). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1708 | +0.089 | +204.19€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1708 | +0.089 | +204.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1334 | +0.094 | +176.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1334 | +0.094 | +176.33€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 271 | +0.068 | +12.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 271 | +0.068 | +12.14€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 404 | -0.003 | +68.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 404 | -0.003 | +68.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 290 | -0.003 | +46.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 290 | -0.003 | +46.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 89 | +0.005 | +16.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 89 | +0.005 | +16.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 36564 | -0.083 | -4681.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1922 | +0.003 | -242.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 34642 | -0.088 | -4438.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4423 | -0.116 | -760.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4423 | -0.116 | -760.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1922 | +0.003 | -242.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1922 | +0.003 | -242.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4121 | -0.113 | -845.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4121 | -0.113 | -845.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9519 | +0.002 | -862.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9519 | +0.002 | -862.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9485 | -0.108 | -704.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9485 | -0.108 | -704.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7094 | -0.149 | -1265.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7094 | -0.149 | -1265.91€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 29658 | -0.018 | +3586.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7669 | +0.004 | +1750.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 21989 | -0.025 | +1835.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 29658 | -0.018 | +3586.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7669 | +0.004 | +1750.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 21989 | -0.025 | +1835.93€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 128176 | +0.114 | -5464.35€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17269 | +0.182 | -532.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 554 | -0.034 | -64.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 102522 | +0.104 | -4588.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7831 | +0.103 | -278.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17015 | +0.105 | -1102.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 58 | -0.150 | +11.01€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 16942 | +0.107 | -1101.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 25142 | +0.129 | -403.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5017 | +0.193 | -147.10€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 16997 | +0.118 | -146.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3086 | +0.087 | -87.55€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 17066 | +0.096 | -1271.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 68 | -0.114 | -5.90€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 16983 | +0.098 | -1254.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 27245 | +0.124 | -490.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7170 | +0.176 | -124.98€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 17209 | +0.106 | -305.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2854 | +0.100 | -51.35€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 24675 | +0.114 | -1336.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4896 | +0.191 | -272.54€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 457 | +0.001 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 17431 | +0.093 | -913.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1891 | +0.133 | -139.79€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17033 | +0.104 | -859.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 60 | -0.065 | +6.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 16960 | +0.105 | -866.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 20582 | +0.194 | -1307.12€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 20582 | +0.194 | -1307.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4735 | +0.175 | -435.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4735 | +0.175 | -435.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2399 | +0.200 | -55.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2399 | +0.200 | -55.16€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4672 | +0.179 | -386.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4672 | +0.179 | -386.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4088 | +0.244 | -140.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4088 | +0.244 | -140.61€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4609 | +0.188 | -303.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4609 | +0.188 | -303.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 928 | +0.428 | -30.09€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 928 | +0.428 | -30.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 368 | +0.435 | -6.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 368 | +0.435 | -6.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 358 | +0.431 | -8.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 358 | +0.431 | -8.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 190 | +0.406 | -12.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 190 | +0.406 | -12.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 71499 | +0.201 | -5220.09€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 71499 | +0.201 | -5220.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12295 | +0.185 | -1272.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12295 | +0.185 | -1272.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11521 | +0.224 | -399.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11521 | +0.224 | -399.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12268 | +0.179 | -1339.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12268 | +0.179 | -1339.69€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11594 | +0.221 | -423.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11594 | +0.221 | -423.10€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11859 | +0.202 | -798.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11859 | +0.202 | -798.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11962 | +0.195 | -986.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11962 | +0.195 | -986.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 27291 | +0.117 | +211.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 27291 | +0.117 | +211.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 13558 | +0.121 | +182.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 13558 | +0.121 | +182.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13733 | +0.114 | +28.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13733 | +0.114 | +28.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1878 | +0.294 | +5.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1878 | +0.294 | +5.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 851 | +0.285 | -5.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 851 | +0.285 | -5.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 908 | +0.293 | +5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 908 | +0.293 | +5.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 865 | +0.442 | +6.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 865 | +0.442 | +6.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 418 | +0.441 | +0.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 418 | +0.441 | +0.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 401 | +0.445 | +4.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 401 | +0.445 | +4.88€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1455 | +0.071 | -60.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 544 | +0.062 | -36.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 911 | +0.076 | -23.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1127 | +0.077 | -27.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 216 | +0.083 | -3.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 911 | +0.076 | -23.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 259 | +0.033 | -35.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 259 | +0.033 | -35.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 53043 | +0.100 | -1354.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4294 | +0.093 | +65.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 48749 | +0.101 | -1420.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 29308 | +0.105 | -311.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4294 | +0.093 | +65.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 25014 | +0.107 | -377.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 10698 | +0.108 | -58.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 10698 | +0.108 | -58.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13037 | +0.082 | -984.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13037 | +0.082 | -984.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 882 | +0.197 | -112.43€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 882 | +0.197 | -112.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 882 | +0.197 | -112.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 882 | +0.197 | -112.43€ | 2 | 4 |
| ✅ GBM_LATE_15M | 36682 | +0.091 | +18559.43€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 36682 | +0.091 | +18559.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6160 | +0.208 | +4862.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6160 | +0.208 | +4862.42€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 5438 | +0.180 | +4009.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5438 | +0.180 | +4009.48€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 6543 | +0.203 | +5020.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6543 | +0.203 | +5020.37€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 5155 | +0.038 | +1345.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5155 | +0.038 | +1345.92€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 5245 | -0.031 | +1136.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5245 | -0.031 | +1136.93€ | 3 | 11 |
| ✅ GBM_LATE_15M#XRP | 8141 | -0.036 | +2184.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8141 | -0.036 | +2184.31€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 39687 | +0.086 | +21328.76€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 39687 | +0.086 | +21328.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7655 | +0.007 | +4018.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7655 | +0.007 | +4018.10€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8331 | +0.013 | +1842.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8331 | +0.013 | +1842.73€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5562 | +0.272 | +5837.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5562 | +0.272 | +5837.89€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6913 | +0.013 | +1597.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6913 | +0.013 | +1597.33€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6408 | +0.037 | +2562.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6408 | +0.037 | +2562.11€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4818 | +0.293 | +5470.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4818 | +0.293 | +5470.60€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 29184 | +0.177 | +23078.55€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 29184 | +0.177 | +23078.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4431 | +0.220 | +3764.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4431 | +0.220 | +3764.42€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4577 | +0.151 | +3362.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4577 | +0.151 | +3362.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4660 | +0.219 | +3921.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4660 | +0.219 | +3921.57€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4917 | +0.139 | +3688.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4917 | +0.139 | +3688.13€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5484 | +0.123 | +3991.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5484 | +0.123 | +3991.59€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5115 | +0.219 | +4350.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5115 | +0.219 | +4350.48€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7864 | +0.138 | +3798.58€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7864 | +0.138 | +3798.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 349 | +0.144 | +206.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 349 | +0.144 | +206.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2396 | +0.149 | +1348.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2396 | +0.149 | +1348.71€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 400 | +0.142 | +188.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 400 | +0.142 | +188.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2402 | +0.149 | +1169.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2402 | +0.149 | +1169.77€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1778 | +0.108 | +645.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1778 | +0.108 | +645.13€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 539 | +0.134 | +240.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 539 | +0.134 | +240.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 36868 | +0.183 | +28875.21€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 36868 | +0.183 | +28875.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5868 | +0.234 | +5300.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5868 | +0.234 | +5300.80€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5684 | +0.150 | +3795.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5684 | +0.150 | +3795.63€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6213 | +0.230 | +5486.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6213 | +0.230 | +5486.94€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6026 | +0.138 | +4254.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6026 | +0.138 | +4254.69€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6530 | +0.122 | +4444.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6530 | +0.122 | +4444.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6547 | +0.222 | +5592.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6547 | +0.222 | +5592.21€ | 0 | 20 |
| ✅ GBM_LATE_5M | 10125 | +0.188 | +7310.33€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 10125 | +0.188 | +7310.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2207 | +0.179 | +1664.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2207 | +0.179 | +1664.64€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 16 |
| ✅ GBM_LATE_5M#ETH | 3087 | +0.190 | +2142.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3087 | +0.190 | +2142.13€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1397 | +0.177 | +985.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1397 | +0.177 | +985.11€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1513 | +0.188 | +1046.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1513 | +0.188 | +1046.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2856 | +0.068 | +971.60€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 2856 | +0.068 | +971.60€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1073 | +0.086 | +381.46€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1073 | +0.086 | +381.46€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 905 | +0.069 | +357.52€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 905 | +0.069 | +357.52€ | 0 | 10 |
| ✅ GBM_LATE_60M#SOL | 878 | +0.044 | +232.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 878 | +0.044 | +232.61€ | 1 | 15 |
| 🚫 GBM_LATE_60M_FADE | 508 | -0.239 | -16.77€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 508 | -0.239 | -16.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 193 | -0.233 | -10.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 193 | -0.233 | -10.56€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 178 | -0.217 | +0.25€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 178 | -0.217 | +0.25€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 137 | -0.270 | -6.45€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 137 | -0.270 | -6.45€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1288 | +0.088 | +338.79€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1288 | +0.088 | +338.79€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 492 | +0.087 | +109.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 492 | +0.087 | +109.05€ | 0 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 471 | +0.062 | +80.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 471 | +0.062 | +80.57€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 325 | +0.127 | +149.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 325 | +0.127 | +149.17€ | 2 | 13 |
| ✅ LATE_WINDOW_5MIN | 141 | +0.255 | +122.89€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 141 | +0.255 | +122.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 141 | +0.255 | +122.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 141 | +0.255 | +122.89€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3073 | +0.099 | +764.64€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3073 | +0.099 | +764.64€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3073 | +0.099 | +764.64€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3073 | +0.099 | +764.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 450 | -0.066 | -30.87€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 450 | -0.066 | -30.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 128 | -0.023 | +0.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 128 | -0.023 | +0.02€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 73 | -0.087 | -8.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 73 | -0.087 | -8.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3256 | +0.020 | +85.82€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3256 | +0.020 | +85.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 158 | +0.019 | -3.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 158 | +0.019 | -3.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 572 | +0.031 | +43.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 572 | +0.031 | +43.79€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1163 | +0.030 | +32.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1163 | +0.030 | +32.99€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 744 | +0.011 | +0.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 744 | +0.011 | +0.71€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 416 | +0.007 | +16.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 416 | +0.007 | +16.60€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1533 | -0.044 | -30.87€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1533 | -0.044 | -30.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 433 | -0.036 | -12.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 433 | -0.036 | -12.00€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 512 | -0.021 | +1.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 512 | -0.021 | +1.86€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 588 | -0.070 | -20.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 588 | -0.070 | -20.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 6156 | -0.024 | +29.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2935 | -0.030 | -29.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3221 | -0.018 | +58.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 177 | -0.014 | +4.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 86 | +0.023 | +8.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 91 | -0.048 | -4.02€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1531 | -0.012 | +31.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 733 | -0.016 | +5.76€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 798 | -0.009 | +25.48€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 686 | -0.028 | -0.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 348 | -0.040 | -9.03€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 338 | -0.015 | +8.85€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1271 | -0.036 | -37.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 587 | -0.052 | -41.62€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 684 | -0.023 | +3.86€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1204 | -0.017 | +27.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 583 | -0.020 | +14.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 621 | -0.014 | +12.83€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1287 | -0.030 | +3.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 598 | -0.037 | -7.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 689 | -0.024 | +11.13€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 42896 | -0.002 | +2058.30€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 42896 | -0.002 | +2058.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7677 | +0.025 | +990.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7677 | +0.025 | +990.60€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6297 | -0.034 | -111.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6297 | -0.034 | -111.69€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7789 | +0.022 | +770.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7789 | +0.022 | +770.80€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6124 | -0.050 | -172.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6124 | -0.050 | -172.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7241 | -0.006 | +234.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7241 | -0.006 | +234.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7768 | +0.014 | +346.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7768 | +0.014 | +346.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6351 | -0.060 | -155.97€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6351 | -0.060 | -155.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1221 | +0.000 | -14.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1221 | +0.000 | -14.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1608 | -0.079 | -39.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1608 | -0.079 | -39.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 741 | -0.122 | -33.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 741 | -0.122 | -33.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1872 | -0.079 | -40.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1872 | -0.079 | -40.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M | 3359 | +0.004 | -2.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3359 | +0.004 | -2.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1322 | +0.005 | +5.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1322 | +0.005 | +5.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 107166 | -0.074 | +1743.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 107166 | -0.074 | +1743.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 18523 | -0.074 | +986.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 18523 | -0.074 | +986.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 16207 | -0.099 | -884.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 16207 | -0.099 | -884.33€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 18788 | -0.066 | +1056.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 18788 | -0.066 | +1056.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 15746 | -0.095 | -465.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 15746 | -0.095 | -465.29€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 19320 | -0.053 | +385.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 19320 | -0.053 | +385.34€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 18582 | -0.065 | +665.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 18582 | -0.065 | +665.92€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8556 | -0.033 | -181.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8556 | -0.033 | -181.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1959 | -0.045 | -21.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1959 | -0.045 | -21.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2557 | -0.028 | -48.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2557 | -0.028 | -48.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1141 | -0.049 | -23.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1141 | -0.049 | -23.99€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 895 | -0.032 | -34.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 895 | -0.032 | -34.59€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1490 | +0.119 | +580.28€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1354 | +0.125 | +567.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 315 | +0.140 | +161.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 315 | +0.140 | +161.83€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 269 | +0.113 | +85.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 269 | +0.113 | +85.67€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 272 | +0.124 | +118.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 272 | +0.124 | +118.15€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 242 | +0.152 | +132.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 242 | +0.152 | +132.61€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 256 | +0.093 | +69.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 256 | +0.093 | +69.42€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1138 | -0.023 | -30.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1138 | -0.023 | -30.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 216 | -0.014 | +1.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 216 | -0.014 | +1.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 189 | -0.013 | +1.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 189 | -0.013 | +1.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 296 | -0.040 | -20.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 296 | -0.040 | -20.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 240 | -0.004 | -3.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 240 | -0.004 | -3.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 197 | -0.038 | -9.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 197 | -0.038 | -9.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 812 | -0.070 | -31.73€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 373 | -0.121 | -73.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 293 | -0.154 | -66.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 288 | -0.031 | +28.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 209 | -0.026 | +27.73€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 151 | -0.016 | +13.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 624 | -0.086 | -30.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 992 | -0.206 | -51.26€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 404 | -0.204 | -36.13€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 349 | -0.209 | -36.92€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 336 | -0.216 | -28.39€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 292 | -0.225 | -33.96€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 252 | -0.193 | +13.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 233 | -0.189 | +10.12€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 874 | -0.210 | -60.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 414 | +0.397 | +398.12€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 104 | +0.377 | +93.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 104 | +0.377 | +93.44€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 257 | +0.458 | +258.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 257 | +0.458 | +258.55€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 414 | +0.397 | +398.12€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 656 | +0.033 | +34.31€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 656 | +0.033 | +34.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 51 | -0.009 | -4.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 51 | -0.009 | -4.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 67 | -0.007 | -0.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 67 | -0.007 | -0.79€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 242 | +0.066 | +36.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 242 | +0.066 | +36.30€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3358 | -0.021 | -128.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3358 | -0.021 | -128.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 586 | -0.025 | -25.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 586 | -0.025 | -25.10€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 160 | -0.043 | -14.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 160 | -0.043 | -14.37€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1561 | -0.016 | -51.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1561 | -0.016 | -51.97€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 94 | -0.052 | -9.37€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 94 | -0.052 | -9.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10193 | +0.018 | +102.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10193 | +0.018 | +102.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2570 | +0.023 | +43.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2570 | +0.023 | +43.67€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2877 | +0.009 | -1.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2877 | +0.009 | -1.62€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2098 | +0.022 | +33.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2098 | +0.022 | +33.45€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9297 | +0.013 | -45.72€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9297 | +0.013 | -45.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3700 | +0.018 | -4.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3700 | +0.018 | -4.07€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3603 | +0.011 | -28.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3603 | +0.011 | -28.25€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1994 | +0.009 | -13.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1994 | +0.009 | -13.40€ | 1 | 0 |
| ✅ UPDOWN_GBM | 67307 | +0.051 | +5826.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 16798 | +0.085 | +3815.32€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2217 | +0.007 | +13.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 44255 | +0.046 | +1935.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3809 | +0.009 | +64.44€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 13392 | +0.053 | +1108.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2071 | +0.091 | +501.00€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 566 | +0.012 | +6.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 8970 | +0.057 | +552.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1702 | +0.006 | +46.04€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 83 | -0.076 | +2.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8043 | +0.066 | +843.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6436 | +0.047 | +237.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 14808 | +0.041 | +896.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3844 | +0.061 | +536.44€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 561 | +0.008 | +9.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9029 | +0.041 | +336.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1298 | +0.011 | +11.02€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 76 | -0.103 | +2.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 14778 | +0.028 | +626.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4015 | +0.035 | +345.41€ | 0 | 8 |
| ✅ UPDOWN_GBM#SOL#240min | 548 | -0.002 | +0.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9339 | +0.030 | +278.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 809 | +0.008 | +7.38€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 67 | -0.138 | -5.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9466 | +0.062 | +1282.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3796 | +0.103 | +1130.42€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 387 | +0.012 | +0.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5283 | +0.035 | +151.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 226 | -0.105 | +0.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 765 | +0.363 | +274.33€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 765 | +0.363 | +274.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 407 | +0.361 | +138.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 407 | +0.361 | +138.22€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 358 | +0.364 | +136.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 358 | +0.364 | +136.11€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18040 | -0.024 | +4372.80€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18040 | -0.024 | +4372.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3060 | -0.110 | +140.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3060 | -0.110 | +140.07€ | 4 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2078 | +0.215 | +1333.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2078 | +0.215 | +1333.74€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5118 | -0.063 | +694.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5118 | -0.063 | +694.29€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5184 | -0.064 | +936.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5184 | -0.064 | +936.25€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 198 | +0.035 | +5.98€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 198 | +0.035 | +5.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 198 | +0.035 | +5.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 198 | +0.035 | +5.98€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1270 | +0.292 | +1065.08€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1270 | +0.292 | +1065.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 686 | +0.286 | +538.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 686 | +0.286 | +538.26€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 584 | +0.297 | +526.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 584 | +0.297 | +526.81€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 788 | -0.114 | -84.30€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 788 | -0.114 | -84.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 235 | -0.091 | -19.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 235 | -0.091 | -19.70€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 84 | -0.151 | -7.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 84 | -0.151 | -7.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 86 | -0.193 | -7.63€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 86 | -0.193 | -7.63€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3204 | +0.306 | +1565.13€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1155 | +0.260 | +170.46€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1227 | +0.299 | +543.56€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 822 | +0.379 | +851.11€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.014 n=830 — no justifica filtro, seguir monitorizando
  - _Datos_: n=830 IC=+0.014 PNL=+32.09€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 668 celda(s) pasan gate riguroso completo de 2577 evaluadas (n>=40) y 3559 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=4015 IC=+0.035 PNL=+345.41€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1227/15 IC=+0.299 PNL=+543.56€ | BTC: n=1155/15 IC=+0.260 PNL=+170.46€ | SOL: n=822/15 IC=+0.379 PNL=+851.11€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=711/60 | contraria IC=+0.203 n=738 | gap=-0.062 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=413, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1298/40 IC=+0.011 PNL=+11.02€ | BTC#60min: n=1702/40 IC=+0.006 PNL=+46.04€ | SOL#60min: n=809/40 IC=+0.008 PNL=+7.38€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=486634 | tras_1loss IC=+0.092 n=371596 | tras_2loss IC=+0.061 n=151613/40 | gap=-0.013 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.215 > 0.08 con n=615 PNL=+491.96€
  - _Datos_: n=615 IC=+0.215 PNL=+491.96€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.08 con n=699 PNL=+468.50€
  - _Datos_: n=699 IC=+0.193 PNL=+468.50€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=2614 PNL=+1465.21€
  - _Datos_: n=2614 IC=+0.335 PNL=+1465.21€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=553 IC=+0.073 PNL=+61.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=553 IC=+0.073 PNL=+61.77€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=73 IC=+0.180 PNL=+47.41€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=73 IC=+0.180 PNL=+47.41€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.067 PNL=+7.14€)
  - _Datos_: n=4 IC=+0.067 PNL=+7.14€

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
  - _Estado_: n=2578 IC=+0.011 PNL=+13.07€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2578 IC=+0.011 PNL=+13.07€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1231 IC=+0.004 PNL=+51.37€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1231 IC=+0.004 PNL=+51.37€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=830 IC=+0.014 PNL=+32.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=830 IC=+0.014 PNL=+32.09€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.192 > 0.1 con n=4036 PNL=+2731.17€
  - _Datos_: n=4036 IC=+0.192 PNL=+2731.17€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2068 IC=+0.091 PNL=+499.02€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2068 IC=+0.091 PNL=+499.02€

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
  - _Estado_: n=858 IC=+0.042 PNL=+89.85€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=858 IC=+0.042 PNL=+89.85€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=96 IC=+0.031 PNL=+3.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=96 IC=+0.031 PNL=+3.09€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.255 n=141) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=141 IC=+0.255 PNL=+122.89€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.02 con n=855 PNL=+358.66€
  - _Datos_: n=855 IC=+0.127 PNL=+358.66€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=191 IC=-0.070 PNL=+27.59€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=191 IC=-0.070 PNL=+27.59€

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
  - _Estado_: n=25830 IC=+0.075 PNL=+3827.24€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=25830 IC=+0.075 PNL=+3827.24€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=392 PNL=+49.47€
  - _Datos_: n=392 IC=-0.135 PNL=+49.47€

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
  - _Estado_: n=123 IC=-0.116 PNL=+2.24€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=123 IC=-0.116 PNL=+2.24€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.1 con n=679 PNL=+176.27€
  - _Datos_: n=679 IC=+0.115 PNL=+176.27€

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
  - _Estado_: n=27157 IC=-0.135 PNL=+2041.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=27157 IC=-0.135 PNL=+2041.29€

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
  - _Estado_: n=2711 IC=+0.138 PNL=+1611.76€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2711 IC=+0.138 PNL=+1611.76€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6911 IC=+0.045 PNL=+514.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6911 IC=+0.045 PNL=+514.83€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=2980 PNL=+1574.64€
  - _Datos_: n=2980 IC=+0.089 PNL=+1574.64€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=2783 PNL=-208.49€
  - _Datos_: n=2783 IC=-0.224 PNL=-208.49€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=1562) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1562 IC=+0.096 PNL=+331.20€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=525) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=525 IC=+0.413 PNL=+753.32€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=12288 IC=+0.185 PNL=-1269.83€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=12288 IC=+0.185 PNL=-1269.83€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=205 PNL=+128.93€
  - _Datos_: n=205 IC=+0.210 PNL=+128.93€
