# Hipótesis automáticas — 2026-10-24 17:39 UTC
_Generado por shadow_postmortem.py sobre 1038796 resoluciones (PNL=+136392.31€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=630)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.228 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.180 (n=298)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 64.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.6191` → IC=+0.264 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6191 (IC base=+0.134)

- **PATRÓN** `banda_z` > `9.008` → IC=+0.216 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.008 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.139 (n=427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=959)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2664.264` → IC=+0.135 (n=786)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2664.264 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.224 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.197 (n=252)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 68.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.6157` → IC=+0.257 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6157 (IC base=+0.138)

- **PATRÓN** `banda_z` > `7.603` → IC=+0.193 (n=340)

  - _Acción_: Kelly boost +0.96€ cuando `banda_z` > 7.603 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.142 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 8.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=860)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `9753.7972` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 9753.7972 (IC base=+0.017)

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
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=108)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=107)

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
- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.149)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.149)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.719` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballenas_wallet_edge_medio` > 0.719 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2466.3517` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2466.3517 (IC base=+0.149)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `141.39` → IC=-0.201 (n=10456)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.39
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=31372)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.1` → IC=-0.257 (n=1143)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.1
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3429)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.11` → IC=-0.291 (n=1125)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.11
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3376)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.21` → IC=-0.205 (n=2776)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.21
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8329)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.92` → IC=-0.273 (n=2015)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.92
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6048)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=22721)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=4475)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `8916.101` → IC=+0.169 (n=2045)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8916.101 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=19386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=35005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=18175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=7398)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6988.154` → IC=+0.156 (n=2859)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 6988.154 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=2075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=2539)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `16445.3611` → IC=+0.191 (n=659)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 16445.3611 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 7.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2025)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.317 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=2596)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `16273.4091` → IC=+0.185 (n=669)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16273.4091 (IC base=+0.182)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=489)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `6764.7813` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 6764.7813 (IC base=+0.079)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1172)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=4420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=3751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.376 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.218 (n=1971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.350 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.148 (n=952)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.260 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=875)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2210.9325` → IC=+0.156 (n=483)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2210.9325 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=867)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.153 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.106)

- **PATRÓN** `py_entrada` > `0.56` → IC=+0.191 (n=383)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.56 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=1146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.246 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=149)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.293 (n=138)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=73)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=19358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=16448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7945)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3740)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4355)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=3644)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.179)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.221 (n=2357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1574)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.303 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.220)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=4374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3415)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=3777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.360 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=4287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3168)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.426 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4242.86` → IC=+0.438 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.86 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.444 (n=212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `20948.5418` → IC=+0.444 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20948.5418 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3610.6662` → IC=+0.443 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3610.6662 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.428 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=27)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=25056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=25339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=8034)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=11306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=5153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=3656)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=4293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5744)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=3570)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3728)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=4199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=4375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9131)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=9073)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.71` → IC=+0.137 (n=10989)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.71 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4514)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4142)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.69` → IC=+0.144 (n=4141)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.69 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=4617)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=4931)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.3` → IC=+0.136 (n=5523)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.3 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.311 (n=1160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.292 (n=522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.358 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5060.4398` → IC=+0.286 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5060.4398 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.299 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.339 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.340)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.372 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.340)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.371 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.340)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.444 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.435 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.440 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `5392.4277` → IC=+0.443 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5392.4277 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.455 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.451)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.454 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.451)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.453 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.451)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.452 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.451)

- **PATRÓN** `libro_liquidez` > `1994.4351` → IC=+0.469 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.4351 (IC base=+0.451)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.389 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.393 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.398)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.283 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=60)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.283 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=60)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4732` → IC=+0.138 (n=14129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4732 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=14287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.3769` → IC=+0.165 (n=14129)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.3769 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.7974` → IC=+0.276 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7974 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.647` → IC=+0.181 (n=7031)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 3.647 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.259 (n=4120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2024 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6173` → IC=+0.265 (n=4120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6173 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.240 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.354` → IC=+0.229 (n=4567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.354 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=11654)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5681` → IC=+0.143 (n=17468)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5681 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.6164` → IC=+0.187 (n=1143)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6164 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.190 (n=3029)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6955 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `1.0521` → IC=+0.182 (n=3120)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0521 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.2974` → IC=+0.233 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2974 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.6901` → IC=+0.209 (n=3899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6901 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.223 (n=11562)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.205 (n=1022)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.206 (n=3065)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=1488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=2054)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.279 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.782` → IC=+0.279 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.782 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.257 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.3` → IC=+0.213 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2065.3048` → IC=+0.209 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2065.3048 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.218 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.240 (n=2588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.245 (n=1172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.275 (n=864)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=946)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5345` → IC=+0.259 (n=2585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5345 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0956` → IC=+0.242 (n=2324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0956 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.262 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4441` → IC=+0.243 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4441 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.7122` → IC=+0.245 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7122 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=2921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1584.8386` → IC=+0.244 (n=2309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1584.8386 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.242 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.238 (n=1110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.232 (n=1146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.256 (n=1110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=1791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9447` → IC=+0.275 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9447 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.235 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.32` → IC=+0.267 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.32 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2306` → IC=+0.229 (n=2522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2306 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.232 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.268 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4399` → IC=+0.256 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4399 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.152 (n=2614)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.166 (n=874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7244` → IC=+0.175 (n=2614)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7244 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1372` → IC=+0.152 (n=2471)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1372 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.063` → IC=+0.150 (n=424)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.063 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.144` → IC=+0.142 (n=2379)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.144 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.142 (n=2614)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2046 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1572` → IC=+0.164 (n=709)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1572 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.455` → IC=+0.143 (n=2493)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.455 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.7966` → IC=+0.136 (n=1662)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7966 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.170 (n=1069)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 213.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.221 (n=1066)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=3356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.182` → IC=+0.271 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.182 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.199 (n=2840)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.210 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.709` → IC=+0.210 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.709 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=3835)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1953.345` → IC=+0.202 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1953.345 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.223 (n=2545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1774` → IC=+0.235 (n=1273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1774 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0263` → IC=+0.276 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0263 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.277` → IC=+0.260 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.277 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.262 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7373` → IC=+0.227 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7373 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1937.383` → IC=+0.222 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1937.383 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.221 (n=2385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=157)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=3867)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.163 (n=564)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0037 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.9523` → IC=+0.233 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9523 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1402` → IC=+0.335 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1402 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1949` → IC=+0.330 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1949 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.146` → IC=+0.193 (n=1214)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 5.146 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.8589` → IC=+0.335 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8589 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.352 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` < `0.077` → IC=+0.329 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.077 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.344 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.357 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.335 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0931` → IC=+0.179 (n=1007)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.0931 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7363` → IC=+0.157 (n=228)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.7363 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8397` → IC=+0.150 (n=1212)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8397 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.1684` → IC=+0.137 (n=606)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.1684 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.200 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.7747` → IC=+0.140 (n=1163)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7747 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.1569` → IC=+0.156 (n=791)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1569 (IC base=+0.039)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.170 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=590)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.178 (n=175)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=525)

- **FILTRO** `ibs_20min` > `0.2143` → IC=-0.132 (n=3786)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2143
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=1871)

- **FILTRO** `sigma_ewma_delta_pct` > `8.607` → IC=-0.232 (n=599)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.607
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=5058)

- **PATRÓN** `ibs_20min` > `0.78` → IC=+0.183 (n=238)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.78 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.133 (n=246)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1586` → IC=+0.276 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1586 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.288 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.029)

- **PATRÓN** `ibs_20min` < `0.2143` → IC=+0.150 (n=1871)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2143 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.192` → IC=+0.280 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.192 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.305 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` < `0.1048` → IC=+0.290 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1048 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.297 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.303 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6048` → IC=-0.184 (n=1044)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6048
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3136)

- **FILTRO** `ibs_20min` < `0.7585` → IC=-0.154 (n=2758)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7585
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=1422)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.166 (n=1008)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3172)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.204 (n=1490)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=4509)

- **PATRÓN** `dist_vwap_pct` > `1.0914` → IC=+0.345 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0914 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2464` → IC=+0.306 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2464 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `1.1407` → IC=+0.300 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1407 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.319 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7005 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.304 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.305 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.322 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8422` → IC=+0.312 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8422 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8191` → IC=+0.285 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8191 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `0.6427` → IC=+0.265 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6427 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `1.0695` → IC=+0.286 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0695 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.1051` → IC=+0.290 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1051 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.264 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.268 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4309 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.209 (n=6175)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.3142` → IC=+0.167 (n=18515)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3142 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.9582` → IC=+0.301 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9582 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.586` → IC=+0.163 (n=8301)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.586 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `1.1711` → IC=+0.265 (n=6829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1711 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` > `0.6878` → IC=+0.271 (n=6102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6878 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` < `0.1069` → IC=+0.264 (n=10490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1069 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.277 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.4603` → IC=+0.265 (n=3623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4603 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `2.6525` → IC=+0.273 (n=3622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6525 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.298 (n=10468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.158 (n=5966)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0094 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.6541` → IC=+0.146 (n=17884)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6541 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.266 (n=2508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1973` → IC=+0.267 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1973 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2953` → IC=+0.319 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2953 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5802` → IC=+0.291 (n=3623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5802 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.2739` → IC=+0.287 (n=3733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2739 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.297 (n=8167)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5796` → IC=-0.140 (n=2529)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5796
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=2530)

- **FILTRO** `ibs_20min` > `0.7338` → IC=-0.214 (n=1078)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7338
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=3236)

- **FILTRO** `sigma_ewma_delta_pct` > `4.345` → IC=-0.213 (n=938)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.345
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3376)

- **PATRÓN** `ibs_20min` > `0.9217` → IC=+0.319 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9217 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.946` → IC=+0.219 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.946 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.306 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.256 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.2635` → IC=+0.282 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2635 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.289 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.027)

- **PATRÓN** `ibs_20min` < `0.1657` → IC=+0.162 (n=1080)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1657 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.417 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.6803` → IC=+0.405 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6803 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.404 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1157` → IC=+0.215 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1157 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.197 (n=1815)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.1961 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.6848` → IC=+0.202 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6848 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.0746` → IC=+0.194 (n=1667)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0746 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.239 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4273` → IC=+0.220 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4273 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.194 (n=596)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `270.0` → IC=+0.232 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 270.0 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1716` → IC=+0.231 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1716 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.619` → IC=+0.236 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.619 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.300 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5373` → IC=+0.244 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5373 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.253 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.246 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 198.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.314 (n=892)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.278 (n=2807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.311 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.678` → IC=+0.302 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.678 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.282 (n=2469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `1.6097` → IC=+0.275 (n=2585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6097 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.280 (n=3185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2041.8956` → IC=+0.287 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2041.8956 (IC base=+0.270)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.290 (n=1619)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.319 (n=1571)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1799` → IC=+0.313 (n=1035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1799 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.322 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.294 (n=818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.295 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.2668` → IC=+0.300 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2668 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.44` → IC=+0.309 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.44 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` < `0.1975` → IC=+0.293 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1975 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.3423` → IC=+0.306 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3423 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.298 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.6782` → IC=+0.305 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6782 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1935.36` → IC=+0.308 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1935.36 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.295 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.293)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.736` → IC=-0.184 (n=1131)

  - _Acción_: SKIP cuando `ibs_20min` > 0.736
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=3395)

- **PATRÓN** `ibs_20min` > `0.8727` → IC=+0.169 (n=1084)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8727 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.154` → IC=+0.234 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.154 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.227 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.238 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6661` → IC=+0.229 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6661 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.234 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.237 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4563` → IC=+0.236 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4563 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.252 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0289` → IC=+0.245 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0289 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.252 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.794` → IC=+0.277 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.794 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4393` → IC=+0.260 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4393 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.263 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 123.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.221 (n=1947)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.309 (n=1947)

- **FILTRO** `ibs_20min` > `0.6418` → IC=-0.232 (n=949)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6418
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=2849)

- **FILTRO** `sigma_ewma_delta_pct` > `8.436` → IC=-0.244 (n=439)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.436
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=3359)

- **PATRÓN** `ibs_20min` > `0.7576` → IC=+0.309 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7576 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.339 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.441` → IC=+0.185 (n=610)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.441 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.335 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.6999` → IC=+0.330 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6999 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.327 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.352 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.344 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.6418` → IC=+0.125 (n=2849)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.6418 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.269 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1018` → IC=+0.245 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1018 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.0776` → IC=+0.258 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0776 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `2.4448` → IC=+0.250 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4448 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.5523` → IC=+0.243 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5523 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.271 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.035)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.350 (n=1809)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.310 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.316 (n=962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.339 (n=2026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.307)

- **PATRÓN** `dist_vwap_pct` > `0.2094` → IC=+0.332 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2094 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.847` → IC=+0.327 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.847 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.11` → IC=+0.309 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.11 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` > `0.6267` → IC=+0.316 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6267 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.346 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `1.4303` → IC=+0.319 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4303 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `2961.0378` → IC=+0.311 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2961.0378 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.341 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.307)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.340 (n=1433)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.308 (n=1051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.3696` → IC=+0.331 (n=2150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3696 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.321 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.313 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.308)

- **PATRÓN** `volumen_regimen` > `1.2266` → IC=+0.339 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2266 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.359 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.317 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.1396` → IC=+0.312 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1396 (IC base=+0.308)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.223 (n=4565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.200 (n=4560)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=14189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.556` → IC=+0.233 (n=13674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.556 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1641` → IC=+0.208 (n=5454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1641 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.313` → IC=+0.257 (n=3577)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.313 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.165 (n=9076)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1861 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6215` → IC=+0.162 (n=9074)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6215 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.204 (n=1984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.191 (n=4425)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `1952.2878` → IC=+0.179 (n=12215)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1952.2878 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.196 (n=12611)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 93.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.185 (n=11654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0093 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.227 (n=4413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=6270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5062` → IC=+0.239 (n=13238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5062 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.943` → IC=+0.198 (n=2152)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.943 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.658` → IC=+0.184 (n=11706)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.658 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1842` → IC=+0.164 (n=9433)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1842 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.228 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6456` → IC=+0.191 (n=4158)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6456 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.195 (n=12216)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 98.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.231 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.234 (n=2289)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.224 (n=1549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.931` → IC=+0.292 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.931 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.858` → IC=+0.327 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.858 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.278 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.8413` → IC=+0.212 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8413 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.217 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2065.6902` → IC=+0.218 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2065.6902 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.253 (n=1793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.267 (n=812)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.0667` → IC=+0.311 (n=597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0667 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=1846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.255 (n=854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.3129` → IC=+0.278 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3129 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.258 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.284 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.4424` → IC=+0.273 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4424 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.7354` → IC=+0.259 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7354 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=2027)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1580.9154` → IC=+0.258 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1580.9154 (IC base=+0.253)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.258 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.216 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0646` → IC=+0.193 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0646 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=2167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3266` → IC=+0.219 (n=2062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3266 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.135` → IC=+0.213 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.135 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.242` → IC=+0.220 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.242 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6901` → IC=+0.164 (n=908)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6901 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.189 (n=326)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.172 (n=674)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.4963` → IC=+0.164 (n=674)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4963 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `418.0` → IC=+0.154 (n=1986)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 418.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=2170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2346` → IC=+0.173 (n=1905)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2346 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=1030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.209 (n=2165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6182 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.446` → IC=+0.196 (n=412)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.446 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.162 (n=2165)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2053 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.150 (n=1855)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.149 (n=664)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4921` → IC=+0.154 (n=2045)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4921 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `224.0` → IC=+0.180 (n=870)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 224.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.236 (n=772)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.394` → IC=+0.220 (n=2035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.394 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.324` → IC=+0.304 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.324 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.211 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.226 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.211 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7129` → IC=+0.224 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7129 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1941.8898` → IC=+0.224 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.8898 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.242 (n=2015)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.2477` → IC=+0.265 (n=1344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2477 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0157` → IC=+0.299 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0157 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.277 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3589` → IC=+0.286 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3589 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.75` → IC=+0.234 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.75 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1602` → IC=+0.240 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1602 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1927.08` → IC=+0.240 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.08 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.235 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.200 (n=986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.203 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3022` → IC=+0.208 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3022 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1444` → IC=+0.195 (n=1336)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1444 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.735` → IC=+0.202 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.735 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0228` → IC=+0.153 (n=1957)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0228 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6152` → IC=+0.146 (n=2224)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6152 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.172 (n=910)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.8237` → IC=+0.146 (n=1454)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.8237 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5085` → IC=+0.165 (n=727)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5085 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7453.7366` → IC=+0.191 (n=1009)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7453.7366 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.155 (n=1909)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 115.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.157 (n=2354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.145 (n=2354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=1120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6805` → IC=+0.186 (n=2354)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6805 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.151 (n=580)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8568` → IC=+0.156 (n=1570)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8568 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.3001` → IC=+0.194 (n=358)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3001 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.136 (n=1475)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5555` → IC=+0.135 (n=737)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5555 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7017.6746` → IC=+0.190 (n=1067)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7017.6746 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.135 (n=1911)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 114.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.177 (n=1133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0104 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4865` → IC=+0.215 (n=2496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4865 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.191 (n=1426)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.457` → IC=+0.282 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.457 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.1718` → IC=+0.140 (n=2496)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1718 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1594` → IC=+0.131 (n=2538)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1594 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5416` → IC=+0.144 (n=1067)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5416 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2604)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2715.618` → IC=+0.210 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2715.618 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.150 (n=822)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 19.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.143 (n=2567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0109 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.170 (n=856)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=2624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6087` → IC=+0.222 (n=2566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6087 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.754` → IC=+0.129 (n=392)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.754 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.453` → IC=+0.136 (n=2267)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.453 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1786` → IC=+0.131 (n=2566)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1786 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.8638` → IC=+0.126 (n=1711)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8638 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1648` → IC=+0.127 (n=2491)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1648 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.150 (n=347)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4426` → IC=+0.128 (n=801)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4426 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.142 (n=799)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2595.0847` → IC=+0.187 (n=1164)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2595.0847 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.131 (n=2098)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 41.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.246 (n=2050)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1719` → IC=+0.240 (n=1010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1719 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=2375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1826` → IC=+0.229 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1826 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.4795` → IC=+0.223 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4795 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.64` → IC=+0.252 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.64 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1704` → IC=+0.224 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1704 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6184` → IC=+0.231 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6184 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.264 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4647` → IC=+0.228 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4647 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8094` → IC=+0.230 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8094 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=2989)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2947.9372` → IC=+0.228 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.9372 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.235 (n=1034)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.243 (n=1065)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.261 (n=784)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.260 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.3011` → IC=+0.243 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3011 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.304` → IC=+0.265 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.304 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `0.8698` → IC=+0.233 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8698 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `0.6394` → IC=+0.236 (n=2349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6394 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.287 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.235 (n=2194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.206 (n=1532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.191 (n=1155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.009 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1297` → IC=+0.203 (n=1525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1297 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4871` → IC=+0.218 (n=3096)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4871 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7975` → IC=+0.205 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7975 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.213 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.204 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6935` → IC=+0.186 (n=2791)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6935 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.191 (n=1242)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.193 (n=1124)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4825` → IC=+0.188 (n=1123)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4825 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3917)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2665.5454` → IC=+0.188 (n=3096)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2665.5454 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.7226` → IC=+0.120 (n=3775)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.7226 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.210 (n=419)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3257` → IC=+0.206 (n=951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3257 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.6393` → IC=+0.241 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6393 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.203 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.073` → IC=+0.202 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.073 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.211 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8745 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.188 (n=376)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.1959` → IC=+0.196 (n=819)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1959 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `14694.0598` → IC=+0.189 (n=634)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 14694.0598 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.203 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 161.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.130 (n=1145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0057 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.6372` → IC=+0.155 (n=1006)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.6372 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1616` → IC=+0.157 (n=304)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1616 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.171 (n=494)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 160.0 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.242 (n=726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.1256` → IC=+0.224 (n=479)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1256 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=1142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.3758` → IC=+0.249 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3758 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.8048` → IC=+0.209 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8048 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2103` → IC=+0.211 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2103 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.923` → IC=+0.245 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.923 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.0228` → IC=+0.212 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0228 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6025` → IC=+0.206 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6025 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2665` → IC=+0.243 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2665 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.217 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.7739` → IC=+0.218 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7739 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.1105` → IC=+0.166 (n=366)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1105 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `8971.7775` → IC=+0.145 (n=497)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8971.7775 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.122 (n=466)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 43.0 (IC base=+0.068)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.194 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0109 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.97` → IC=+0.247 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.97 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.095` → IC=+0.239 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.095 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8886` → IC=+0.194 (n=579)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8886 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.714` → IC=+0.177 (n=775)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.714 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2307` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2307 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.190 (n=279)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.1532` → IC=+0.173 (n=380)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1532 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=894)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3010.8204` → IC=+0.191 (n=289)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3010.8204 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.127 (n=855)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5714 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `2636.7224` → IC=+0.145 (n=440)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2636.7224 (IC base=+0.048)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0239` → IC=+0.161 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0239 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.203 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2536` → IC=+0.176 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2536 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.56 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.738` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 7.738 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.275` → IC=+0.182 (n=187)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.275 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.6893` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6893 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.177 (n=255)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2474.2976` → IC=+0.176 (n=146)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2474.2976 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.175 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0228 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.614` → IC=+0.128 (n=253)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.614 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.9016 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.3609` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.3609 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.228 (n=5952)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=18592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.231 (n=17852)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4444 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.9054` → IC=+0.214 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9054 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.2` → IC=+0.254 (n=4353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.2 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.169 (n=11964)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2203 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2404` → IC=+0.204 (n=3230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2404 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6168` → IC=+0.194 (n=5788)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6168 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1760.6844` → IC=+0.183 (n=17836)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1760.6844 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.208 (n=14525)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.195 (n=7169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0056 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.4868` → IC=+0.193 (n=16269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4868 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5862` → IC=+0.243 (n=16276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5862 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.766` → IC=+0.204 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.766 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.533` → IC=+0.193 (n=15735)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.533 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6319` → IC=+0.168 (n=3660)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6319 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.254 (n=2215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.631` → IC=+0.201 (n=5144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.631 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.236 (n=5254)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.232 (n=970)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.3463` → IC=+0.229 (n=2903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3463 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.231 (n=1957)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.32` → IC=+0.349 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.32 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.291 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.226 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.2972` → IC=+0.239 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2972 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=3117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2064.6149` → IC=+0.232 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2064.6149 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.251 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.267 (n=2492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.1182` → IC=+0.288 (n=1097)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1182 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.290 (n=2490)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5152 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.029` → IC=+0.268 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.029 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.267 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.289 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5652` → IC=+0.267 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5652 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.280 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.265 (n=2819)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1584.833` → IC=+0.268 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1584.833 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.274 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.199 (n=966)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1041` → IC=+0.164 (n=1273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1041 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.24` → IC=+0.201 (n=2892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.24 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.197 (n=1324)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.162 (n=471)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.172` → IC=+0.150 (n=2529)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 3.172 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6302` → IC=+0.177 (n=964)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6302 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.152 (n=2580)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.182 (n=416)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1743` → IC=+0.157 (n=2491)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1743 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5326` → IC=+0.153 (n=2529)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5326 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.184 (n=924)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 236.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.164 (n=2448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0059 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3257` → IC=+0.155 (n=2448)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3257 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=906)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6939` → IC=+0.195 (n=2448)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.6939 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.222` → IC=+0.158 (n=407)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.222 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.454` → IC=+0.143 (n=2462)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.454 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.194` → IC=+0.153 (n=2448)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.194 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.219` → IC=+0.206 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.219 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.434` → IC=+0.147 (n=2343)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.434 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7827` → IC=+0.153 (n=1562)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7827 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=3177)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.154 (n=991)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 268.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.257 (n=992)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=2667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.242` → IC=+0.321 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.242 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.228 (n=2792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.1929` → IC=+0.239 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1929 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=3559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1952.96` → IC=+0.238 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.96 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.245 (n=2473)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.262 (n=1237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.304 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.298 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.304 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1457` → IC=+0.251 (n=1787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1457 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1931.7443` → IC=+0.253 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.7443 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.254 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.202 (n=1024)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4204` → IC=+0.158 (n=3065)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4204 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=3183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2437` → IC=+0.191 (n=3065)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2437 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1433` → IC=+0.171 (n=1601)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1433 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.035` → IC=+0.159 (n=1386)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.035 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.056` → IC=+0.158 (n=2698)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.056 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.187 (n=407)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5228` → IC=+0.163 (n=1316)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5228 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1683` → IC=+0.153 (n=1357)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1683 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5698.1383` → IC=+0.238 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5698.1383 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.165 (n=1307)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 72.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.154 (n=2567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0075 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4356` → IC=+0.140 (n=2566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4356 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7344` → IC=+0.186 (n=2566)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7344 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.261` → IC=+0.158 (n=515)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.261 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.167` → IC=+0.133 (n=2231)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.167 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6927` → IC=+0.146 (n=1129)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6927 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.220 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.5394` → IC=+0.140 (n=2207)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5394 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6772.9839` → IC=+0.211 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6772.9839 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.133 (n=1666)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 99.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.162 (n=1406)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0105 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4375` → IC=+0.199 (n=3102)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4375 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.048` → IC=+0.208 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.048 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.631` → IC=+0.263 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.631 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8815` → IC=+0.144 (n=2065)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8815 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.125 (n=3223)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.8238` → IC=+0.128 (n=2017)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8238 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.1852` → IC=+0.124 (n=1372)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.1852 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=3219)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2756.0726` → IC=+0.242 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2756.0726 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.143 (n=981)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 23.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.154 (n=2591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0101 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1356` → IC=+0.154 (n=982)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1356 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=3037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6562` → IC=+0.214 (n=2943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6562 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.222` → IC=+0.138 (n=2826)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.222 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6411` → IC=+0.146 (n=982)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6411 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.171 (n=505)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.151 (n=921)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2630.3387` → IC=+0.201 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2630.3387 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.133 (n=2444)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 46.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.254 (n=2599)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=3037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.238 (n=2102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6106` → IC=+0.272 (n=2599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6106 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.249 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.721` → IC=+0.272 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.721 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.2231` → IC=+0.239 (n=2910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2231 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.236 (n=2910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2338` → IC=+0.255 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2338 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.4773` → IC=+0.249 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4773 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=3782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2948.1944` → IC=+0.239 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2948.1944 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.255 (n=1005)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.241 (n=2843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.5155` → IC=+0.267 (n=3014)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5155 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.222` → IC=+0.272 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.222 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `1.2286` → IC=+0.262 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2286 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.300 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.236 (n=2810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.231 (n=2738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.234)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=5087)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.245 (n=1762)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5067` → IC=+0.220 (n=5282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5067 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=1910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9411` → IC=+0.253 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9411 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.7011` → IC=+0.213 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7011 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4334` → IC=+0.213 (n=3763)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4334 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.93` → IC=+0.217 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.93 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.58` → IC=+0.212 (n=4700)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.58 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.225 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.212 (n=4935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.1665` → IC=+0.219 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1665 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.220 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=4030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `3710.0405` → IC=+0.220 (n=3521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3710.0405 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3882` → IC=+0.214 (n=3368)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3882 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=1284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=1702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.1863` → IC=+0.207 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1863 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.202 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2399` → IC=+0.190 (n=3500)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2399 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.812` → IC=+0.202 (n=3440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.812 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.201 (n=3198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.196 (n=3512)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.198 (n=773)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5345` → IC=+0.198 (n=1659)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5345 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.8153` → IC=+0.200 (n=2513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8153 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=5087)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.209 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.276 (n=680)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.296 (n=258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.274 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.263 (n=777)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.2568` → IC=+0.289 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2568 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.278 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.269 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `0.8676` → IC=+0.274 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8676 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.353 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.8216` → IC=+0.269 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8216 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `16281.4445` → IC=+0.273 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16281.4445 (IC base=+0.262)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.253 (n=598)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.369` → IC=+0.191 (n=1338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.369 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.198 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.206 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1409 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.176 (n=607)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6084 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.7015` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.7015 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.195 (n=1322)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.190 (n=1338)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.2212 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2206` → IC=+0.205 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2206 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.5027` → IC=+0.183 (n=1330)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.5027 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.8071` → IC=+0.184 (n=887)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.8071 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14914.2556` → IC=+0.188 (n=607)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 14914.2556 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `692.0` → IC=+0.187 (n=1292)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 692.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.196 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.007 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.215 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.204 (n=820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.196 (n=547)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7037 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.234 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2099` → IC=+0.238 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2099 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.8704` → IC=+0.205 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8704 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2543.292` → IC=+0.219 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2543.292 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.197 (n=553)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 10.0 (IC base=+0.193)

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

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.213 (n=1393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.1477` → IC=+0.211 (n=613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1477 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.5182` → IC=+0.208 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5182 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.7583` → IC=+0.199 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7583 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.105` → IC=+0.204 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.105 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.8752` → IC=+0.200 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8752 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `1.2312` → IC=+0.204 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2312 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.204 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=1429)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.205 (n=1142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3869` → IC=+0.218 (n=1005)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3869 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.201 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.200 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.3991` → IC=+0.195 (n=762)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3991 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.6239` → IC=+0.194 (n=518)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.6239 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6607` → IC=+0.198 (n=200)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6607 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.199 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2445 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` > `0.721` → IC=+0.188 (n=1020)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.721 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.214 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.195 (n=983)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.7855` → IC=+0.192 (n=745)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.7855 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `6625.7808` → IC=+0.198 (n=1142)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6625.7808 (IC base=+0.188)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.205 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.208 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9219` → IC=+0.251 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9219 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.206 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.229 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7016 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.195 (n=706)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `2.1551` → IC=+0.187 (n=669)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.1551 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.195 (n=254)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=915)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `4300.4118` → IC=+0.227 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4300.4118 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.195 (n=771)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 52.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.217 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.208 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4982` → IC=+0.230 (n=509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4982 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.242 (n=394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.232 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.512` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.512 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.3065` → IC=+0.208 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3065 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.216 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.9331` → IC=+0.211 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9331 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.225 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.239 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `3011.3904` → IC=+0.226 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3011.3904 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.250 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.206)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.156 (n=788)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0041 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.206 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7778 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.146 (n=870)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.904` → IC=+0.147 (n=491)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.904 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2318` → IC=+0.220 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2318 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.288` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 10.288 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.146` → IC=+0.155 (n=279)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.146 (IC base=+0.056)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.135 (n=589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.3558` → IC=+0.170 (n=558)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3558 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.166 (n=279)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.281 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.2123` → IC=+0.198 (n=84)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2123 (IC base=+0.067)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.128 (n=514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.4203` → IC=+0.172 (n=552)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4203 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.190 (n=279)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.09` → IC=+0.234 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.09 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.239 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.106 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.025)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7302` → IC=+0.155 (n=389)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.7302 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.7321` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7321 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.219` → IC=+0.151 (n=124)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.219 (IC base=+0.028)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.156 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0109 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.231 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.1716` → IC=+0.138 (n=230)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1716 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0818 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.193` → IC=+0.148 (n=191)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.193 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `1.5022` → IC=+0.162 (n=193)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5022 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `837.374` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 837.374 (IC base=+0.076)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.238 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=162)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=307)

- **FILTRO** `volumen_regimen` < `0.7721` → IC=-0.295 (n=81)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7721
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=243)

- **FILTRO** `volumen_spike_ratio` > `2.7682` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.7682
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=188)

- **FILTRO** `libro_liquidez` < `903.6493` → IC=-0.211 (n=81)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.6493
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=243)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.307 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=224)

- **FILTRO** `ibs_20min` > `0.5429` → IC=-0.337 (n=139)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5429
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=140)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=260)

- **FILTRO** `sigma_ewma_delta_pct` > `10.358` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.358
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=253)

- **FILTRO** `volumen_pendiente_norm` > `0.0435` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=161)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=53)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=75)

- **FILTRO** `volumen_spike_ratio` > `3.276` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.276
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=58)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.318 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=96)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.348 (n=31)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=96)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=82)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=82)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.387 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=53)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=54)

- **FILTRO** `libro_liquidez` < `1289.9986` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 1289.9986
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=78)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.158)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=98)

- **FILTRO** `dist_vwap_pct` > `0.0608` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0608
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=90)

- **FILTRO** `volumen_spike_ratio` > `2.3459` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3459
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=61)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.316 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.159 (n=575)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.6667 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.5394` → IC=+0.238 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5394 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.589` → IC=+0.134 (n=129)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 10.589 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6187` → IC=+0.180 (n=192)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6187 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.0677` → IC=+0.153 (n=401)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0677 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5055` → IC=+0.175 (n=207)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5055 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.143 (n=584)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.1435 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.168 (n=194)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `3253.1348` → IC=+0.128 (n=442)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3253.1348 (IC base=+0.054)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6991` → IC=-0.178 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6991
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=174)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.165 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0035 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.137 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.150 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.190 (n=311)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1681 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.168` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 10.168 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0363` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.0363 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.07` → IC=+0.137 (n=246)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.07 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2688` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2688 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.7964` → IC=+0.154 (n=186)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7964 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `5391.3885` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 5391.3885 (IC base=+0.127)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=182)

- **FILTRO** `ibs_20min` > `0.1696` → IC=-0.151 (n=107)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1696
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=208)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.147 (n=171)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.8015 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.0908` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0908 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.146 (n=142)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6141 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.014)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2391` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2391
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=103)

- **FILTRO** `dist_vwap_pct` > `0.1699` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1699
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.286 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.291 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.259 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.2358` → IC=+0.226 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2358 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.152` → IC=+0.333 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.152 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.278 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4815` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4815 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.060)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.321 (n=76)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.324)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.324)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.324)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.392 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.324)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.324)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.296 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.237)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.321 (n=76)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.324)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.324)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.324)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.392 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.324)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.324)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.296 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.237)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2928.7278` → IC=+0.133 (n=445)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2928.7278 (IC base=+0.100)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2928.7278` → IC=+0.133 (n=445)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2928.7278 (IC base=+0.100)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=204)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=203)

- **FILTRO** `libro_liquidez` < `5529.6254` → IC=-0.176 (n=109)

  - _Acción_: SKIP cuando `libro_liquidez` < 5529.6254
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=412)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=73)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3632)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=108)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.271 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=96)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=108)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=132)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1377)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1331)

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
- **FILTRO** `py_entrada` > `0.505` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=709)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=717)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=437)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=418)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=182)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.019)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=871)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=871)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=901)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=901)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.129 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=176)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=168)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=263)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=287)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=268)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=250)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=359)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=359)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=204)

- **FILTRO** `libro_liquidez` < `632.1854` → IC=-0.131 (n=128)

  - _Acción_: SKIP cuando `libro_liquidez` < 632.1854
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=261)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=272)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=200)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.75` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 10.75
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.58 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=36)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `restante_min` < `3.93` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `restante_min` < 3.93
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=34)

- **FILTRO** `lag_apertura_s` > `64.36` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `lag_apertura_s` > 64.36
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.5 (IC base=+0.019)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.157 (n=65)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=299)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=154)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.156 (n=123)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=252)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.124 (n=360)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=205)

- **FILTRO** `profundidad_ratio` < `43.4` → IC=-0.164 (n=141)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.4
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=424)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.196 (n=90)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=382)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.170 (n=98)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=436)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=524)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6497)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=19742)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=6531)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=20525)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.192 (n=1173)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=3633)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.173 (n=1120)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3703)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1265)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `1180.4932` → IC=+0.137 (n=2403)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1180.4932 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=2258)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1395.78` → IC=+0.152 (n=1640)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1395.78 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.150 (n=914)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=2880)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.178 (n=931)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2907)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=1147)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=3782)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.130 (n=1639)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1470.7` → IC=+0.122 (n=2402)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1470.7 (IC base=+0.037)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.158 (n=1184)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=3623)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2407)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2331)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.189 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2747)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=3637)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=430)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=941)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.192 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=305)

- **FILTRO** `drift_20min_pct` |x|> `0.2047` → IC=-0.140 (n=112)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2047
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=337)

- **FILTRO** `libro_liquidez` < `3170.1466` → IC=-0.180 (n=148)

  - _Acción_: SKIP cuando `libro_liquidez` < 3170.1466
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=301)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=943)

- **FILTRO** `libro_liquidez` < `1786.4389` → IC=-0.161 (n=240)

  - _Acción_: SKIP cuando `libro_liquidez` < 1786.4389
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=722)

- **FILTRO** `ibs_20min` > `0.8939` → IC=-0.131 (n=532)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8939
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=534)

- **FILTRO** `libro_liquidez` < `2096.2738` → IC=-0.169 (n=351)

  - _Acción_: SKIP cuando `libro_liquidez` < 2096.2738
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=715)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=234)

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

- **FILTRO** `py_entrada` > `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=68)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=18070)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=40396)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.286 (n=14568)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=43898)

- **FILTRO** `ibs_7min` < `0.2327` → IC=-0.231 (n=14616)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2327
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=43850)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=19214)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=39252)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.241 (n=18031)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=55377)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.183 (n=18084)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=55324)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.148 (n=2547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7725)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2465)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7807)

- **FILTRO** `ibs_7min` < `0.7123` → IC=-0.245 (n=3389)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7123
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6883)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.182 (n=2071)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8201)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.272 (n=2973)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=9751)

- **FILTRO** `ibs_7min` > `0.7667` → IC=-0.211 (n=3180)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7667
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=9544)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.129 (n=2357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7454)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2314)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=7497)

- **FILTRO** `ibs_7min` < `0.7214` → IC=-0.201 (n=2450)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7214
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7361)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.191 (n=2447)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7364)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=2458)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=7567)

- **FILTRO** `ibs_7min` > `0.266` → IC=-0.194 (n=2506)

  - _Acción_: SKIP cuando `ibs_7min` > 0.266
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7519)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=2490)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7535)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=2392)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=7368)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2414)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=7346)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.247 (n=3219)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6541)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2246)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7514)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.256 (n=3147)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=10366)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.177 (n=3378)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=10135)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.125 (n=3107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6396)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2262)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7241)

- **FILTRO** `ibs_7min` < `0.7241` → IC=-0.193 (n=2373)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7241
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7130)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.191 (n=2304)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7199)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.263 (n=2230)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7648)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.177 (n=2469)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7409)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.173 (n=2467)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7411)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.286 (n=2345)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7197)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.223 (n=3108)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=6434)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2286)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=7256)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.192 (n=3443)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10569)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.295 (n=2293)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7285)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.225 (n=2392)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7186)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.198 (n=2342)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=7236)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.220 (n=3240)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=10016)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=986)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1270)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=564)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=855)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=220)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=332)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=449)

- **FILTRO** `libro_liquidez` < `3257.9143` → IC=-0.156 (n=181)

  - _Acción_: SKIP cuando `libro_liquidez` < 3257.9143
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=543)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.139 (n=1230)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.137 (n=544)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `437.4823` → IC=+0.160 (n=410)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 437.4823 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3558.8016` → IC=+0.146 (n=557)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3558.8016 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.149 (n=420)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 11.0 (IC base=+0.131)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4385` → IC=+0.139 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4385 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.191 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 14.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `371.804` → IC=+0.148 (n=251)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 371.804 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2387.2349` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2387.2349 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.138 (n=252)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.138 (n=227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 14.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.131 (n=304)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.04 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2039.5706` → IC=+0.136 (n=226)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2039.5706 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.137 (n=166)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 12.0 (IC base=+0.121)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.189 (n=162)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7586.8038` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7586.8038 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.194 (n=109)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 69.0 (IC base=+0.140)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4318` → IC=+0.223 (n=99)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4318 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.186 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.151)

- **PATRÓN** `total_vol_5m` < `4901.52` → IC=+0.189 (n=146)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 4901.52 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3171.8207` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3171.8207 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 26.0 (IC base=+0.151)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.140 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 10.0 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=151)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `3566.692` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3566.692 (IC base=+0.099)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `T_h` > `129.5348` → IC=-0.191 (n=173)

  - _Acción_: SKIP cuando `T_h` > 129.5348
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=523)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.178 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0036 (IC base=-0.080)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9872` → IC=-0.255 (n=51)

  - _Acción_: SKIP cuando `T_h` > 87.9872
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=156)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.296 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.031)

- **PATRÓN** `pct_vs_K` |x|≤ `1.5815` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `pct_vs_K` |x|≤ 1.5815 (IC base=-0.031)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.258 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=95)

- **FILTRO** `T_h` < `90.336` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `T_h` < 90.336
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=63)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.206 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=-0.102)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.235 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=219)

- **FILTRO** `T_h` > `109.3211` → IC=-0.210 (n=319)

  - _Acción_: SKIP cuando `T_h` > 109.3211
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=320)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.234 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=413)

- **FILTRO** `pct_vs_K` |x|> `2.8988` → IC=-0.404 (n=185)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8988
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=365)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0057` → IC=-0.182 (n=105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=105)

- **FILTRO** `pct_vs_K` |x|> `2.7768` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7768
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=158)

- **FILTRO** `T_h` > `73.0783` → IC=-0.258 (n=147)

  - _Acción_: SKIP cuando `T_h` > 73.0783
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=50)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.422 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=148)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.321 (n=121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=63)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.364 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=130)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.227 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=130)

- **PATRÓN** `pct_vs_K` |x|≤ `0.7672` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `pct_vs_K` |x|≤ 0.7672 (IC base=-0.178)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=135)

- **FILTRO** `T_h` > `71.5479` → IC=-0.196 (n=133)

  - _Acción_: SKIP cuando `T_h` > 71.5479
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **FILTRO** `sigma_h` > `0.0152` → IC=-0.375 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0152
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=92)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.286 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=82)

- **FILTRO** `T_h` > `33.8406` → IC=-0.263 (n=91)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=31)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.478 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.333)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.356 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.333)

- **PATRÓN** `T_h` > `0.7452` → IC=+0.382 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7452 (IC base=+0.333)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.333)

- **PATRÓN** `edge` > `0.1005` → IC=+0.441 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.414)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.443 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.414)

- **PATRÓN** `T_h` < `0.608` → IC=+0.438 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.4975` → IC=+0.491 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4975 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1506` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1506 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.205)

- **PATRÓN** `dist_50` > `0.346` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.346 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.281 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.420)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.419 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.423 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.420)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.420)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.407 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.3792` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3792 (IC base=+0.420)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.420)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1838` → IC=+0.484 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1838 (IC base=+0.430)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.465 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.430)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.453 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.430)

- **PATRÓN** `dist_50` > `0.3691` → IC=+0.465 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3691 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.430)

- **PATRÓN** `edge` > `0.2005` → IC=+0.479 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.466)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.479 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.466)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.466)

- **PATRÓN** `dist_50` > `0.4605` → IC=+0.492 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4605 (IC base=+0.466)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.473 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.466)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=333)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=402)

- **PATRÓN** `streak_estiramiento` < `0.835` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.835 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 34.0 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2505.47` → IC=+0.140 (n=145)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2505.47 (IC base=+0.053)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `streak_estiramiento` < `0.4354` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.4354 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 34.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2178.9765` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2178.9765 (IC base=+0.096)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=106)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.210 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=33)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.140 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `libro_liquidez` < `3338.6704` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 3338.6704
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `streak_estiramiento` > `1.1496` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1496
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.056)

- **PATRÓN** `volumen_racha` < `17126.646` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 17126.646 (IC base=+0.056)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1037)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1335)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1233)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1267)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` > `6.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4162)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2334)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.190 (n=1689)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0054 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.188 (n=1279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0121 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.188 (n=3379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3486` → IC=+0.178 (n=3500)

  - _Acción_: Kelly boost +0.89€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3486 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=3553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.173 (n=3543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.5423` → IC=+0.246 (n=3837)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5423 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.168 (n=1846)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.3171` → IC=+0.157 (n=3079)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.3171 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.376` → IC=+0.259 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.376 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `4629.3821` → IC=+0.189 (n=1279)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 4629.3821 (IC base=+0.172)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1535)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.248 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.255 (n=288)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2541` → IC=+0.236 (n=218)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2541 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.232 (n=684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.280 (n=653)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1382` → IC=+0.230 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1382 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.295 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `9788.5606` → IC=+0.225 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9788.5606 (IC base=+0.212)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.185 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.162 (n=510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1416` → IC=+0.151 (n=511)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1416 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1262` → IC=+0.150 (n=304)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1262 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5357` → IC=+0.238 (n=765)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5357 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.160 (n=472)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.707` → IC=+0.277 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.707 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3217.9115` → IC=+0.152 (n=765)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3217.9115 (IC base=+0.145)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8831` → IC=+0.243 (n=305)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8831 (IC base=+0.087)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=487)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.087)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.781` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 15.781 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0241` → IC=+0.228 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0241 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1304` → IC=+0.222 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1304 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3415` → IC=+0.224 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3415 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.208 (n=772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.274 (n=864)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.213 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.324` → IC=+0.230 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.324 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2955.9488` → IC=+0.293 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.9488 (IC base=+0.198)

- **PATRÓN** `ibs_15` < `0.1089` → IC=+0.167 (n=793)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1089 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.390 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.382 (n=439)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1392` → IC=+0.389 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1392 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.400 (n=657)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.382 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.390 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3859.8614` → IC=+0.373 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3859.8614 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.362 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.404 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.370 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2163` → IC=+0.377 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2163 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.396 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.388 (n=336)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.1089` → IC=+0.377 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1089 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.255` → IC=+0.382 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.255 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.385 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.402 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.375 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.367)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.385 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.367)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.366 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.367)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.382 (n=287)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.367)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.385 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.367)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.392 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.367)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.378 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.367)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.410 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.388 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.370 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.367)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.408` → IC=+0.397 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.408 (IC base=+0.367)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.373 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.367)

- **PATRÓN** `libro_liquidez` > `4019.374` → IC=+0.399 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4019.374 (IC base=+0.367)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.377 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.367)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2251)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1761)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2740)

- **FILTRO** `libro_liquidez` < `4231.3519` → IC=-0.154 (n=2970)

  - _Acción_: SKIP cuando `libro_liquidez` < 4231.3519
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1531)

- **PATRÓN** `ibs_15` > `0.6332` → IC=+0.280 (n=1088)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6332 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.206 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.197 (n=928)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.272 (n=1269)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.284 (n=3802)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.6627` → IC=+0.279 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6627 (IC base=-0.011)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.216 (n=673)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=2020)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.230 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=2021)

- **FILTRO** `sigma_ewma_delta_pct` > `23.313` → IC=-0.265 (n=390)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.313
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=2303)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=2627)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.169 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0028 (IC base=+0.090)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1458` → IC=+0.273 (n=240)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1458 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.124 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.090)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.332 (n=360)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.282 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` < `0.3703` → IC=+0.288 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3703 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.813` → IC=+0.140 (n=184)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 23.813 (IC base=+0.090)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1053` → IC=+0.233 (n=58)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1053 (IC base=-0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.6128` → IC=+0.321 (n=65)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6128 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.192)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=711)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.159 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0049 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.187 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.193 (n=421)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5959` → IC=+0.248 (n=546)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5959 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4686` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.4686 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.153 (n=430)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.252 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=711)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `5211.9622` → IC=+0.156 (n=364)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5211.9622 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.246)

- **PATRÓN** `drift_15min` |x|≤ `0.7722` → IC=+0.259 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7722 (IC base=+0.246)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1552` → IC=+0.264 (n=942)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1552 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.248 (n=1256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_15` < `0.3777` → IC=+0.278 (n=1414)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3777 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.6228` → IC=+0.265 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6228 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.394` → IC=+0.253 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.394 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.432` → IC=+0.251 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.432 (IC base=+0.246)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1485` → IC=-0.230 (n=353)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1485
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=687)

- **FILTRO** `sigma_h` > `0.0106` → IC=-0.232 (n=259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=781)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.251 (n=352)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=688)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.282 (n=259)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=781)

- **FILTRO** `sigma_ewma_delta_pct` > `17.738` → IC=-0.147 (n=545)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.738
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4345)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.189)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.189)

- **PATRÓN** `ibs_15` < `0.375` → IC=+0.291 (n=629)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.375 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.2588` → IC=+0.238 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2588 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.253 (n=617)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=618)

- **FILTRO** `drift_15min` |x|> `0.7503` → IC=-0.250 (n=617)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7503
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=618)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.211)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0695` → IC=+0.277 (n=796)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0695 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1174` → IC=+0.295 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1174 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.317 (n=595)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.096)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 102.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.048)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.096)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.096)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 102.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.048)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.299 (n=501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0541` → IC=+0.322 (n=380)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0541 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2423` → IC=+0.299 (n=381)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2423 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2244` → IC=+0.301 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2244 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.305 (n=1185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8388` → IC=+0.319 (n=1139)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8388 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.322 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.379 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `13851.0679` → IC=+0.311 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13851.0679 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.311 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.303 (n=277)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.320 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.305 (n=203)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.310 (n=609)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.1465` → IC=+0.320 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1465 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.378 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.329 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.303 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.312 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.297 (n=530)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1043` → IC=+0.324 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1043 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.311 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.323 (n=530)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.321 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.375 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.132 (n=85)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=259)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.155 (n=85)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=259)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.133 (n=232)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=80)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=365)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=364)

- **FILTRO** `drift_15min` |x|> `0.4386` → IC=-0.151 (n=164)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4386
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=320)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1342` → IC=-0.154 (n=50)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1342
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=151)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2377` → IC=-0.125 (n=94)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2377
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2021` → IC=-0.250 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2021
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

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
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

- **FILTRO** `drift_15min` |x|> `0.1605` → IC=-0.340 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1605
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.075` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.075
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
- **PATRÓN** `T_h` > `87.7391` → IC=+0.192 (n=508)

  - _Acción_: Kelly boost +0.96€ cuando `T_h` > 87.7391 (IC base=+0.185)

- **PATRÓN** `ratio` < `0.973` → IC=+0.408 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.185)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.354 (n=2331)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.378 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.5528` → IC=+0.176 (n=211)

  - _Acción_: Kelly boost +0.88€ cuando `T_h` > 109.5528 (IC base=+0.152)

- **PATRÓN** `ratio` < `0.9839` → IC=+0.318 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9839 (IC base=+0.152)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.307 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.296)

- **PATRÓN** `ratio` > `1.0451` → IC=+0.408 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0451 (IC base=+0.296)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.235 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.227)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.398 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.227)

- **PATRÓN** `T_h` > `111.9952` → IC=+0.353 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9952 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.336 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.439 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5423 sube el IC de +0.172 a +0.246 en UPDOWN_GBM#15min (n=3837). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.212 a +0.280 en UPDOWN_GBM#BTC#15min (n=653). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5357 sube el IC de +0.145 a +0.238 en UPDOWN_GBM#ETH#15min (n=765). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8831 sube el IC de +0.087 a +0.243 en UPDOWN_GBM#SOL#15min (n=305). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.198 a +0.274 en UPDOWN_GBM#XRP#15min (n=864). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1089 sube el IC de +0.070 a +0.167 en UPDOWN_GBM#XRP#15min (n=793). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6332 sube el IC de -0.068 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1088). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.011 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=3802). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.090 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=360). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.192 a +0.321 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=65). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5959 sube el IC de +0.152 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=546). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3777 sube el IC de +0.246 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1414). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.375 sube el IC de -0.038 a +0.291 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=629). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.211 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.025 a +0.317 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=595). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.096 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.096 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8388 sube el IC de +0.289 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=1139). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.285 a +0.310 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=609). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.294 a +0.323 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=530). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.364 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=657). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.360 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=336). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.367 a +0.410 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1996 | +0.090 | +208.21€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1996 | +0.090 | +208.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1604 | +0.093 | +179.48€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1604 | +0.093 | +179.48€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 787 | -0.006 | +87.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 787 | -0.006 | +87.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 596 | -0.032 | +54.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 596 | -0.032 | +54.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 41828 | -0.082 | -5155.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2383 | +0.046 | -271.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 39445 | -0.090 | -4884.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4572 | -0.115 | -759.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4572 | -0.115 | -759.25€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2383 | +0.046 | -271.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2383 | +0.046 | -271.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4501 | -0.111 | -872.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4501 | -0.111 | -872.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11204 | -0.023 | -1108.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11204 | -0.023 | -1108.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11105 | -0.108 | -807.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11105 | -0.108 | -807.98€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8063 | -0.132 | -1335.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8063 | -0.132 | -1335.47€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 37840 | -0.014 | +3235.26€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9777 | +0.004 | +1634.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 28063 | -0.021 | +1600.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 37840 | -0.014 | +3235.26€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9777 | +0.004 | +1634.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 28063 | -0.021 | +1600.91€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 153785 | +0.115 | -6138.49€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19325 | +0.181 | -627.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 685 | -0.012 | -72.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 124658 | +0.107 | -5100.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9117 | +0.097 | -338.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 20665 | +0.108 | -1267.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 62 | -0.156 | +10.44€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 20588 | +0.109 | -1266.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 29641 | +0.127 | -481.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5309 | +0.184 | -208.82€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 20650 | +0.120 | -135.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3640 | +0.081 | -115.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 20721 | +0.100 | -1435.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 78 | -0.113 | -2.92€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 20628 | +0.101 | -1421.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 32732 | +0.124 | -617.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8425 | +0.177 | -180.98€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 20941 | +0.107 | -374.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3354 | +0.100 | -53.91€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 29337 | +0.115 | -1400.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5380 | +0.198 | -248.25€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 588 | +0.019 | -18.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 21246 | +0.096 | -964.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2123 | +0.120 | -169.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 20689 | +0.107 | -934.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 71 | -0.103 | +3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 20605 | +0.108 | -937.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 24761 | +0.196 | -1527.33€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 24761 | +0.196 | -1527.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5618 | +0.179 | -477.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5618 | +0.179 | -477.75€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3245 | +0.202 | -81.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3245 | +0.202 | -81.65€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5556 | +0.179 | -456.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5556 | +0.179 | -456.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4791 | +0.247 | -169.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4791 | +0.247 | -169.76€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5472 | +0.188 | -355.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5472 | +0.188 | -355.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1063 | +0.426 | -38.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1063 | +0.426 | -38.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 423 | +0.434 | -8.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 423 | +0.434 | -8.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 419 | +0.431 | -9.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 419 | +0.431 | -9.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 86788 | +0.201 | -6186.59€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 86788 | +0.201 | -6186.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14906 | +0.185 | -1538.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14906 | +0.185 | -1538.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 14014 | +0.225 | -462.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 14014 | +0.225 | -462.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14871 | +0.181 | -1562.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14871 | +0.181 | -1562.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 14114 | +0.219 | -555.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 14114 | +0.219 | -555.20€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 14402 | +0.202 | -936.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 14402 | +0.202 | -936.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 14481 | +0.198 | -1130.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 14481 | +0.198 | -1130.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 33290 | +0.117 | +223.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 33290 | +0.117 | +223.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 16556 | +0.119 | +183.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 16556 | +0.119 | +183.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 16734 | +0.114 | +40.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 16734 | +0.114 | +40.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2167 | +0.292 | -12.91€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2167 | +0.292 | -12.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 995 | +0.279 | -28.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 995 | +0.279 | -28.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1049 | +0.297 | +13.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1049 | +0.297 | +13.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 123 | +0.340 | +2.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 123 | +0.340 | +2.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 997 | +0.442 | +5.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 997 | +0.442 | +5.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 484 | +0.434 | -6.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 484 | +0.434 | -6.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 466 | +0.451 | +10.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 466 | +0.451 | +10.87€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 47 | +0.398 | +0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 47 | +0.398 | +0.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1728 | +0.067 | -82.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 675 | +0.038 | -70.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1053 | +0.085 | -11.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 78 | +0.100 | +2.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 78 | +0.100 | +2.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1323 | +0.075 | -37.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 270 | +0.037 | -26.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1053 | +0.085 | -11.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 327 | +0.023 | -47.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 327 | +0.023 | -47.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 66145 | +0.101 | -1623.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5342 | +0.092 | +64.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 60803 | +0.102 | -1687.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 36328 | +0.105 | -394.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5342 | +0.092 | +64.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 30986 | +0.108 | -458.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 13713 | +0.110 | -64.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 13713 | +0.110 | -64.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 16104 | +0.083 | -1164.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 16104 | +0.083 | -1164.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 899 | +0.192 | -110.13€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 899 | +0.192 | -110.13€ | 1 | 4 |
| ✅ GBM_LATE_15M | 45303 | +0.095 | +23963.46€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 45303 | +0.095 | +23963.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7531 | +0.219 | +6288.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7531 | +0.219 | +6288.24€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6846 | +0.179 | +5263.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6846 | +0.179 | +5263.72€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 8116 | +0.204 | +6293.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8116 | +0.204 | +6293.82€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 6274 | +0.044 | +1814.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6274 | +0.044 | +1814.90€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 6357 | -0.031 | +1403.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6357 | -0.031 | +1403.46€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 10179 | -0.029 | +2899.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10179 | -0.029 | +2899.32€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 48529 | +0.085 | +26684.64€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 48529 | +0.085 | +26684.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9373 | +0.002 | +4753.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9373 | +0.002 | +4753.95€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10341 | +0.010 | +2555.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10341 | +0.010 | +2555.04€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6698 | +0.281 | +7262.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6698 | +0.281 | +7262.94€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8859 | +0.013 | +2246.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8859 | +0.013 | +2246.16€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7692 | +0.040 | +3225.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7692 | +0.040 | +3225.89€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5566 | +0.308 | +6640.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5566 | +0.308 | +6640.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 35881 | +0.180 | +29229.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 35881 | +0.180 | +29229.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5438 | +0.233 | +4898.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5438 | +0.233 | +4898.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5635 | +0.149 | +4180.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5635 | +0.149 | +4180.24€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5768 | +0.222 | +4926.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5768 | +0.222 | +4926.41€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6103 | +0.137 | +4704.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6103 | +0.137 | +4704.31€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6748 | +0.124 | +5055.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6748 | +0.124 | +5055.31€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6189 | +0.228 | +5464.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6189 | +0.228 | +5464.07€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9653 | +0.131 | +4696.88€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9653 | +0.131 | +4696.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2790 | +0.140 | +1560.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2790 | +0.140 | +1560.00€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2912 | +0.137 | +1387.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2912 | +0.137 | +1387.89€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2448 | +0.105 | +971.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2448 | +0.105 | +971.68€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 45471 | +0.186 | +36612.05€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 45471 | +0.186 | +36612.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7189 | +0.244 | +6773.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7189 | +0.244 | +6773.96€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7118 | +0.146 | +4900.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7118 | +0.146 | +4900.05€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7709 | +0.232 | +6857.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7709 | +0.232 | +6857.65€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7507 | +0.139 | +5369.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7507 | +0.139 | +5369.63€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8051 | +0.121 | +5617.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8051 | +0.121 | +5617.40€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7897 | +0.234 | +7093.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7897 | +0.234 | +7093.36€ | 0 | 20 |
| ✅ GBM_LATE_5M | 12144 | +0.203 | +9518.71€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 12144 | +0.203 | +9518.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2813 | +0.208 | +2414.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2813 | +0.208 | +2414.96€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1167 | +0.196 | +861.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1167 | +0.196 | +861.83€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3378 | +0.192 | +2365.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3378 | +0.192 | +2365.77€ | 0 | 23 |
| ✅ GBM_LATE_5M#SOL | 1816 | +0.192 | +1396.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1816 | +0.192 | +1396.00€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1933 | +0.207 | +1501.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1933 | +0.207 | +1501.40€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3797 | +0.064 | +1172.77€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 3797 | +0.064 | +1172.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1390 | +0.080 | +474.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1390 | +0.080 | +474.07€ | 0 | 5 |
| ✅ GBM_LATE_60M#ETH | 1230 | +0.067 | +419.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1230 | +0.067 | +419.80€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1177 | +0.043 | +278.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1177 | +0.043 | +278.90€ | 0 | 12 |
| 🚫 GBM_LATE_60M_FADE | 603 | -0.245 | -22.31€ | 10 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 603 | -0.245 | -22.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 226 | -0.246 | -14.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 226 | -0.246 | -14.71€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 213 | -0.230 | +0.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 213 | -0.230 | +0.97€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 164 | -0.259 | -8.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 164 | -0.259 | -8.56€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1649 | +0.084 | +419.70€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1649 | +0.084 | +419.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 645 | +0.081 | +159.48€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 645 | +0.081 | +159.48€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 569 | +0.055 | +92.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 569 | +0.055 | +92.03€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 435 | +0.125 | +168.18€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 435 | +0.125 | +168.18€ | 2 | 10 |
| ✅ LATE_WINDOW_5MIN | 176 | +0.281 | +176.56€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 176 | +0.281 | +176.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 176 | +0.281 | +176.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 176 | +0.281 | +176.56€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3594 | +0.102 | +880.71€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3594 | +0.102 | +880.71€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3594 | +0.102 | +880.71€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3594 | +0.102 | +880.71€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 652 | -0.025 | -8.88€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 652 | -0.025 | -8.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 196 | -0.010 | +2.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 196 | -0.010 | +2.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 143 | +0.017 | +4.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 143 | +0.017 | +4.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 228 | -0.009 | -0.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 228 | -0.009 | -0.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3846 | +0.014 | +83.08€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3846 | +0.014 | +83.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 185 | +0.029 | -0.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 185 | +0.029 | -0.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 798 | +0.006 | +28.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 798 | +0.006 | +28.40€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 211 | -0.002 | +0.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 211 | -0.002 | +0.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1427 | +0.021 | +27.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1427 | +0.021 | +27.10€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 467 | +0.012 | +25.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 467 | +0.012 | +25.67€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1867 | -0.039 | -26.96€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1867 | -0.039 | -26.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 546 | -0.027 | -10.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 546 | -0.027 | -10.37€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 645 | -0.018 | +4.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 645 | -0.018 | +4.97€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 676 | -0.068 | -21.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 676 | -0.068 | -21.56€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 10130 | -0.027 | +1.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4810 | -0.035 | -82.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5320 | -0.021 | +84.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 314 | -0.035 | -8.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 160 | -0.006 | +5.41€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 154 | -0.064 | -13.45€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2580 | -0.017 | +35.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1216 | -0.021 | +5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1364 | -0.014 | +30.03€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1099 | -0.031 | -1.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 553 | -0.046 | -19.76€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 546 | -0.016 | +18.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2231 | -0.036 | -50.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1037 | -0.048 | -51.60€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1194 | -0.027 | +1.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1970 | -0.020 | +33.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 948 | -0.030 | -5.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1022 | -0.010 | +38.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1936 | -0.035 | -8.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 896 | -0.042 | -16.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1040 | -0.028 | +8.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 53295 | -0.000 | +2758.98€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 53295 | -0.000 | +2758.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9629 | +0.026 | +1254.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9629 | +0.026 | +1254.62€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7632 | -0.034 | -105.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7632 | -0.034 | -105.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9733 | +0.025 | +1031.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9733 | +0.025 | +1031.63€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7480 | -0.048 | -144.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7480 | -0.048 | -144.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9019 | -0.004 | +266.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9019 | -0.004 | +266.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9802 | +0.016 | +456.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9802 | +0.016 | +456.04€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6762 | -0.057 | -144.34€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6762 | -0.057 | -144.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1232 | -0.002 | -16.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1232 | -0.002 | -16.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1800 | -0.070 | -32.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1800 | -0.070 | -32.72€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 783 | -0.119 | -33.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 783 | -0.119 | -33.35€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2028 | -0.071 | -34.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2028 | -0.071 | -34.84€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 131874 | -0.077 | +1632.84€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 131874 | -0.077 | +1632.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 22996 | -0.077 | +1156.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 22996 | -0.077 | +1156.24€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 19836 | -0.101 | -1057.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 19836 | -0.101 | -1057.98€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 23273 | -0.068 | +1217.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 23273 | -0.068 | +1217.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 19381 | -0.098 | -653.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 19381 | -0.098 | -653.22€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 23554 | -0.058 | +323.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 23554 | -0.058 | +323.93€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 22834 | -0.067 | +645.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 22834 | -0.067 | +645.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8835 | -0.034 | -185.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8835 | -0.034 | -185.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2005 | -0.047 | -26.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2005 | -0.047 | -26.39€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2606 | -0.026 | -42.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2606 | -0.026 | -42.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1223 | -0.058 | -29.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1223 | -0.058 | -29.86€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 990 | -0.031 | -36.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 990 | -0.031 | -36.09€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1774 | +0.125 | +735.75€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1638 | +0.131 | +723.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 379 | +0.138 | +190.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 379 | +0.138 | +190.59€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 336 | +0.121 | +120.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 336 | +0.121 | +120.94€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 323 | +0.140 | +162.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 323 | +0.140 | +162.45€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 290 | +0.151 | +159.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 290 | +0.151 | +159.33€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 310 | +0.099 | +89.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 310 | +0.099 | +89.84€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1608 | -0.021 | -34.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1608 | -0.021 | -34.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 308 | -0.006 | +6.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 308 | -0.006 | +6.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 283 | -0.033 | -7.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 283 | -0.033 | -7.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 407 | -0.050 | -37.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 407 | -0.050 | -37.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 347 | +0.004 | +3.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 347 | +0.004 | +3.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 263 | -0.009 | +0.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 263 | -0.009 | +0.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 947 | -0.071 | -45.63€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 440 | -0.109 | -78.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 344 | -0.136 | -66.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 332 | -0.030 | +24.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 241 | -0.018 | +27.10€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 175 | -0.054 | +8.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 144 | -0.062 | +3.95€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 729 | -0.083 | -34.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1189 | -0.205 | -68.44€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 464 | -0.206 | -42.85€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 407 | -0.209 | -42.62€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 404 | -0.207 | -32.20€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 356 | -0.218 | -39.21€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 321 | -0.200 | +6.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 300 | -0.195 | +4.49€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1063 | -0.209 | -77.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 477 | +0.391 | +450.78€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#BTC | 80 | +0.171 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 80 | +0.171 | +63.15€ | 0 | 4 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 287 | +0.459 | +284.81€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 287 | +0.459 | +284.81€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 477 | +0.391 | +450.78€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 773 | +0.032 | +50.22€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 773 | +0.032 | +50.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | -0.008 | -1.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | -0.008 | -1.05€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 78 | +0.000 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 78 | +0.000 | +3.29€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 325 | +0.057 | +45.11€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 325 | +0.057 | +45.11€ | 0 | 4 |
| ✅ STREAK_FADE_5M | 3458 | -0.022 | -136.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3458 | -0.022 | -136.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1060 | -0.021 | -35.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1060 | -0.021 | -35.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 596 | -0.030 | -28.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 596 | -0.030 | -28.08€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 167 | -0.038 | -13.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 167 | -0.038 | -13.79€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1635 | -0.019 | -58.95€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1635 | -0.019 | -58.95€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11204 | +0.015 | +81.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11204 | +0.015 | +81.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2843 | +0.020 | +28.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2843 | +0.020 | +28.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2915 | +0.017 | +32.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2915 | +0.017 | +32.86€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2904 | +0.009 | -2.92€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2904 | +0.009 | -2.92€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2542 | +0.016 | +22.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2542 | +0.016 | +22.98€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10170 | +0.013 | -47.76€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10170 | +0.013 | -47.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4181 | +0.018 | -5.08€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4181 | +0.018 | -5.08€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3621 | +0.010 | -28.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3621 | +0.010 | -28.64€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2368 | +0.009 | -14.04€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2368 | +0.009 | -14.04€ | 1 | 0 |
| ✅ UPDOWN_GBM | 81412 | +0.054 | +7255.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 20066 | +0.084 | +4364.23€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2596 | +0.003 | +28.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 53614 | +0.051 | +2773.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4846 | +0.005 | +93.25€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 18108 | +0.056 | +1552.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2670 | +0.089 | +638.39€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 710 | +0.007 | +12.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 12452 | +0.062 | +833.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2171 | +0.003 | +65.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 105 | -0.070 | +2.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8711 | +0.070 | +925.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7078 | +0.054 | +316.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 19056 | +0.046 | +1255.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4822 | +0.069 | +719.57€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 688 | +0.006 | +16.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 11726 | +0.045 | +499.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1723 | +0.008 | +18.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 97 | -0.106 | +2.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17883 | +0.034 | +929.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5123 | +0.035 | +416.95€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 655 | -0.008 | +1.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11067 | +0.040 | +507.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 952 | +0.006 | +10.02€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 86 | -0.136 | -6.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10801 | +0.066 | +1518.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4320 | +0.104 | +1280.29€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6093 | +0.043 | +237.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 288 | -0.103 | -1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 876 | +0.364 | +320.12€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 876 | +0.364 | +320.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 448 | +0.360 | +151.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 448 | +0.360 | +151.99€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 428 | +0.367 | +168.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 428 | +0.367 | +168.13€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20708 | -0.024 | +4895.43€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20708 | -0.024 | +4895.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3759 | -0.112 | +148.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3759 | -0.112 | +148.48€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2612 | +0.220 | +1709.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2612 | +0.220 | +1709.84€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5930 | -0.064 | +750.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5930 | -0.064 | +750.95€ | 5 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5741 | -0.065 | +1012.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5741 | -0.065 | +1012.89€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 247 | +0.058 | +19.74€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 247 | +0.058 | +19.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 247 | +0.058 | +19.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 247 | +0.058 | +19.74€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1518 | +0.289 | +1291.16€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1518 | +0.289 | +1291.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 812 | +0.285 | +650.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 812 | +0.285 | +650.51€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 706 | +0.294 | +640.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 706 | +0.294 | +640.65€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 828 | -0.112 | -82.31€ | 6 | 0 |
| ✅ UPDOWN_OU_5M#5min | 828 | -0.112 | -82.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 254 | -0.082 | -19.18€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 254 | -0.082 | -19.18€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 89 | -0.170 | -10.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 89 | -0.170 | -10.17€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 102 | -0.173 | -3.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 102 | -0.173 | -3.61€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3824 | +0.304 | +1811.38€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1417 | +0.258 | +182.56€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1468 | +0.299 | +658.44€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 939 | +0.380 | +970.38€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.025 n=1018 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1018 IC=+0.025 PNL=+46.53€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 725 celda(s) pasan gate riguroso completo de 2745 evaluadas (n>=40) y 3803 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=5122 IC=+0.035 PNL=+416.63€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1468/15 IC=+0.299 PNL=+658.44€ | BTC: n=1417/15 IC=+0.258 PNL=+182.56€ | SOL: n=939/15 IC=+0.380 PNL=+970.38€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.141 n=828/60 | contraria IC=+0.192 n=861 | gap=-0.051 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=495, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1721/40 IC=+0.008 PNL=+18.13€ | BTC#60min: n=2169/40 IC=+0.003 PNL=+65.10€ | SOL#60min: n=952/40 IC=+0.006 PNL=+10.02€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=589879 | tras_1loss IC=+0.096 n=448112 | tras_2loss IC=+0.066 n=180957/40 | gap=-0.018 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.08 con n=798 PNL=+587.54€
  - _Datos_: n=798 IC=+0.194 PNL=+587.54€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.08 con n=901 PNL=+497.77€
  - _Datos_: n=901 IC=+0.165 PNL=+497.77€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=66 PNL=+33.08€
  - _Datos_: n=66 IC=+0.162 PNL=+33.08€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=3123 PNL=+1748.79€
  - _Datos_: n=3123 IC=+0.334 PNL=+1748.79€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=746 IC=+0.070 PNL=+80.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=746 IC=+0.070 PNL=+80.82€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=89 IC=+0.181 PNL=+58.85€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=89 IC=+0.181 PNL=+58.85€

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
  - _Estado_: 2/20 ops en el filtro definido (IC actual=+0.000 PNL=-0.08€)
  - _Datos_: n=2 IC=+0.000 PNL=-0.08€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=3255 IC=+0.007 PNL=+6.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3255 IC=+0.007 PNL=+6.11€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1587 IC=+0.003 PNL=+87.15€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1587 IC=+0.003 PNL=+87.15€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1018 IC=+0.025 PNL=+46.53€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1018 IC=+0.025 PNL=+46.53€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.1 con n=5115 PNL=+3086.40€
  - _Datos_: n=5115 IC=+0.172 PNL=+3086.40€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2669 IC=+0.088 PNL=+637.86€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2669 IC=+0.088 PNL=+637.86€

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
  - _Estado_: n=1044 IC=+0.037 PNL=+89.22€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1044 IC=+0.037 PNL=+89.22€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=132 IC=+0.000 PNL=-0.12€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=132 IC=+0.000 PNL=-0.12€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.280 n=175) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=175 IC=+0.280 PNL=+174.56€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=1026 PNL=+430.87€
  - _Datos_: n=1026 IC=+0.124 PNL=+430.87€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=213 IC=-0.091 PNL=+19.65€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=213 IC=-0.091 PNL=+19.65€

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
  - _Estado_: n=32172 IC=+0.073 PNL=+4603.73€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=32172 IC=+0.073 PNL=+4603.73€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=538 PNL=+71.86€
  - _Datos_: n=538 IC=-0.137 PNL=+71.86€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3169 IC=+0.070 PNL=+417.35€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3169 IC=+0.070 PNL=+417.35€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=152 IC=-0.097 PNL=+3.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=152 IC=-0.097 PNL=+3.71€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=859 PNL=+231.70€
  - _Datos_: n=859 IC=+0.111 PNL=+231.70€

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
  - _Estado_: n=34553 IC=-0.134 PNL=+2670.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=34553 IC=-0.134 PNL=+2670.11€

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
  - _Estado_: n=3483 IC=+0.133 PNL=+2182.72€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3483 IC=+0.133 PNL=+2182.72€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8363 IC=+0.053 PNL=+672.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8363 IC=+0.053 PNL=+672.62€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=3697 PNL=+2042.10€
  - _Datos_: n=3697 IC=+0.096 PNL=+2042.10€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=3602 PNL=-321.02€
  - _Datos_: n=3602 IC=-0.224 PNL=-321.02€

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
  - _Estado_: n=74 IC=+0.026 PNL=+9.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=74 IC=+0.026 PNL=+9.96€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1817) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1817 IC=+0.102 PNL=+399.69€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=597) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=597 IC=+0.410 PNL=+854.62€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=14898 IC=+0.185 PNL=-1538.86€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=14898 IC=+0.185 PNL=-1538.86€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.221 > 0.1 con n=238 PNL=+157.70€
  - _Datos_: n=238 IC=+0.221 PNL=+157.70€
