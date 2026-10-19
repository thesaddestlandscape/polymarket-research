# Hipótesis automáticas — 2026-10-19 08:05 UTC
_Generado por shadow_postmortem.py sobre 962841 resoluciones (PNL=+124754.22€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.705` → IC=+0.274 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.181 (n=277)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 66.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.8014` → IC=+0.271 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8014 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.212` → IC=+0.204 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.212 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=895)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.152 (n=446)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 98.0 (IC base=+0.137)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.271 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.143)

- **PATRÓN** `n_total_lado` > `47.0` → IC=+0.184 (n=463)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 47.0 (IC base=+0.143)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.266 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.143)

- **PATRÓN** `banda_z` > `9.644` → IC=+0.209 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.644 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=796)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.153 (n=416)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 101.0 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `9770.2045` → IC=+0.131 (n=204)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 9770.2045 (IC base=+0.017)

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
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=104)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=103)

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

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.143)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.143)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.143)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.719` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballenas_wallet_edge_medio` > 0.719 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.210 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2466.3517` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2466.3517 (IC base=+0.143)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `142.39` → IC=-0.207 (n=9926)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.39
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=29784)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `129.12` → IC=-0.264 (n=1118)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.12
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3357)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.52` → IC=-0.288 (n=1078)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.52
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3234)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.27` → IC=-0.209 (n=2619)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.27
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7857)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.16` → IC=-0.280 (n=1928)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.16
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=5785)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=21299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=4279)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9161.0845` → IC=+0.178 (n=1928)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9161.0845 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=22008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=16787)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=7117)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7121.8138` → IC=+0.159 (n=2751)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7121.8138 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=1967)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=2468)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `16325.2152` → IC=+0.203 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16325.2152 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.191 (n=1770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.189 (n=1972)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2529)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `16122.9185` → IC=+0.196 (n=652)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16122.9185 (IC base=+0.185)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=465)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `6860.5651` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6860.5651 (IC base=+0.082)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1098)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.160 (n=2825)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 12.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.222 (n=1829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.360 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.217 (n=2146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1038)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.147 (n=678)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.262 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=818)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1877.4399` → IC=+0.154 (n=663)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1877.4399 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.418 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=851)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.355 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `1131.3588` → IC=+0.147 (n=242)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1131.3588 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=1122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.251 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=17934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=15231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7409)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=4141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.180 (n=4128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=4042)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.178 (n=3388)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=2085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.232 (n=1397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.309 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3464)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3197)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.362 (n=1125)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=3996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=2949)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `13089.4142` → IC=+0.445 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13089.4142 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.451 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15539.3062` → IC=+0.440 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15539.3062 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.448 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `4387.5246` → IC=+0.441 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4387.5246 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.401 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.416 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=23274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=23490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.193 (n=3453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=10419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=3982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=9455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.197 (n=3361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=4044)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=8423)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8278)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.123 (n=10265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.42` → IC=+0.138 (n=7679)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.42 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=4164)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4210)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=5096)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.78` → IC=+0.146 (n=3818)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.78 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=4259)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=4516)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.26` → IC=+0.135 (n=3862)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.26 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=1606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.281 (n=633)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5416.3978` → IC=+0.292 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5416.3978 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=773)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2111.2626` → IC=+0.312 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2111.2626 (IC base=+0.297)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.446 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.443 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.444 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.452 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.451 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.448)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.449 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

- **PATRÓN** `libro_liquidez` > `1966.3827` → IC=+0.461 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.3827 (IC base=+0.448)

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
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.340 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

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
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.340 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4778` → IC=+0.137 (n=13020)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4778 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=13143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.123 (n=9098)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.9808` → IC=+0.247 (n=4340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9808 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.7875` → IC=+0.266 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7875 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.3687` → IC=+0.257 (n=3637)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3687 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.929` → IC=+0.189 (n=4923)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.929 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.256 (n=3767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2024 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6186` → IC=+0.262 (n=3768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6186 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.239 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.3444` → IC=+0.227 (n=4194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3444 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=16020)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5682` → IC=+0.142 (n=16039)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5682 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1523` → IC=+0.186 (n=5863)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1523 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.183 (n=2739)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6961 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0507` → IC=+0.180 (n=2822)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0507 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.234 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6792` → IC=+0.208 (n=3528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6792 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.220 (n=10437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.214 (n=947)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.348` → IC=+0.200 (n=2838)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.348 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=1378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1904)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.9787` → IC=+0.278 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9787 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.964` → IC=+0.281 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.964 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2319` → IC=+0.245 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2319 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.2813` → IC=+0.208 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2813 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2083.02` → IC=+0.208 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2083.02 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.212 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.239 (n=1077)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.272 (n=795)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5236` → IC=+0.259 (n=2375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5236 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0935` → IC=+0.239 (n=2123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0935 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.251 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4369` → IC=+0.242 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4369 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.245 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1659.7886` → IC=+0.245 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1659.7886 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.243 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.238 (n=1025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.231 (n=1052)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.261 (n=1022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9523` → IC=+0.276 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9523 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.234 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.35` → IC=+0.268 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.35 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.229 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.231 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.232 (n=2322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.261 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.5138` → IC=+0.228 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5138 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4448` → IC=+0.255 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4448 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.168 (n=786)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7293` → IC=+0.176 (n=2356)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7293 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.065` → IC=+0.151 (n=382)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.065 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.197` → IC=+0.141 (n=2153)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.197 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.140 (n=2356)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2032 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.161 (n=861)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4576` → IC=+0.142 (n=2236)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4576 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.7857` → IC=+0.137 (n=1490)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.7857 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.173 (n=957)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 219.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.217 (n=984)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2638)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.273 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.199 (n=2609)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.211 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.210 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=3519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1979.8184` → IC=+0.202 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.8184 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.6031` → IC=+0.222 (n=2635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6031 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0157` → IC=+0.274 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0157 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.416` → IC=+0.248 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.416 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.261 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.213 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.73` → IC=+0.230 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.73 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2057.52` → IC=+0.225 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2057.52 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.220 (n=2188)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=147)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3574)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.164 (n=524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0036 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9552` → IC=+0.226 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9552 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1359` → IC=+0.328 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1359 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.3349` → IC=+0.325 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3349 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.111` → IC=+0.185 (n=1130)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.111 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.333 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2247` → IC=+0.348 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2247 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.346 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4099` → IC=+0.344 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4099 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.324 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.337 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0933` → IC=+0.172 (n=931)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0933 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.3208` → IC=+0.140 (n=445)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.3208 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1293` → IC=+0.134 (n=1513)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1293 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8428` → IC=+0.145 (n=1100)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8428 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `1.1679` → IC=+0.132 (n=550)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.1679 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.200 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.155` → IC=+0.151 (n=717)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.155 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=543)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.202 (n=159)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=484)

- **FILTRO** `ibs_20min` > `0.2174` → IC=-0.132 (n=3512)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2174
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=1731)

- **FILTRO** `sigma_ewma_delta_pct` > `8.655` → IC=-0.235 (n=552)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.655
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4691)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.185 (n=220)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7857 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0161` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0161 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.149 (n=226)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.5734` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5734 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.283 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5481` → IC=+0.262 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5481 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2174` → IC=+0.149 (n=1731)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2174 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.265` → IC=+0.277 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.265 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.275 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4351 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.302 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0805` → IC=+0.304 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0805 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.297 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6165` → IC=-0.178 (n=952)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6165
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2860)

- **FILTRO** `ibs_20min` < `0.7463` → IC=-0.149 (n=2515)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7463
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=1297)

- **FILTRO** `ibs_20min` > `0.7541` → IC=-0.203 (n=1379)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7541
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4139)

- **PATRÓN** `dist_vwap_pct` > `0.7462` → IC=+0.332 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7462 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2524` → IC=+0.300 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2524 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.311 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.297 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.301 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.4195` → IC=+0.322 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4195 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.299 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8149` → IC=+0.274 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8149 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0712` → IC=+0.282 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0712 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1035` → IC=+0.279 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1035 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1868` → IC=+0.262 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1868 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.263 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.207 (n=5728)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.8827` → IC=+0.282 (n=7769)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8827 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9593` → IC=+0.298 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9593 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.608` → IC=+0.160 (n=7689)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.608 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1722` → IC=+0.262 (n=6315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1722 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6881` → IC=+0.267 (n=5642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6881 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.0793` → IC=+0.259 (n=9280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0793 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.275 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4604` → IC=+0.260 (n=3361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4604 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.271 (n=3362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.293 (n=9671)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.161 (n=5502)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0093 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6599` → IC=+0.144 (n=16501)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6599 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1722` → IC=+0.264 (n=4943)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1722 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1951` → IC=+0.266 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1951 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.319 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5792` → IC=+0.288 (n=3273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5792 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2684` → IC=+0.283 (n=3372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2684 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.293 (n=7372)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3703` → IC=-0.179 (n=1554)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3703
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=3157)

- **FILTRO** `ibs_20min` > `0.7449` → IC=-0.213 (n=986)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7449
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=2959)

- **FILTRO** `sigma_ewma_delta_pct` > `4.45` → IC=-0.204 (n=865)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.45
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=3080)

- **PATRÓN** `ibs_20min` > `0.9163` → IC=+0.307 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9163 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.034` → IC=+0.213 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.034 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.297 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4428` → IC=+0.246 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4428 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.2425` → IC=+0.271 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2425 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.276 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.1631` → IC=+0.163 (n=987)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1631 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.0719` → IC=+0.417 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0719 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4828` → IC=+0.408 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4828 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.403 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.112` → IC=+0.212 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.112 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1944` → IC=+0.191 (n=1666)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1944 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6813` → IC=+0.199 (n=1489)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.6813 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.189 (n=1533)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2769` → IC=+0.224 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2769 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.214 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.5021` → IC=+0.194 (n=547)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5021 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.241 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 219.0 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.236 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.297 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.236 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5357 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1685` → IC=+0.251 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1685 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.233 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 202.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.307 (n=837)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.272 (n=2634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.284` → IC=+0.298 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.284 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.278 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.272 (n=2424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.276 (n=2977)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1973.5984` → IC=+0.284 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1973.5984 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.279 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.330 (n=979)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1832` → IC=+0.311 (n=951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1832 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.319 (n=826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.295 (n=2160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3684 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.258` → IC=+0.299 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.258 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.593` → IC=+0.317 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.593 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.290 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.3421` → IC=+0.312 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3421 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.7251` → IC=+0.300 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7251 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6661` → IC=+0.302 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6661 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2052.2204` → IC=+0.307 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2052.2204 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.292 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7378` → IC=-0.185 (n=1035)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7378
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=3109)

- **PATRÓN** `ibs_20min` > `0.8801` → IC=+0.173 (n=979)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8801 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1509` → IC=+0.233 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1509 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3631` → IC=+0.231 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3631 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.009` → IC=+0.244 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.009 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6703` → IC=+0.229 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6703 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.234 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.248 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.243 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.134` → IC=+0.237 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.134 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.265 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1901` → IC=+0.230 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1901 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.1974` → IC=+0.230 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1974 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1022` → IC=+0.245 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1022 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.297 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7992` → IC=+0.267 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7992 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4508` → IC=+0.253 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4508 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.256 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7627` → IC=-0.210 (n=1806)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7627
  - _Potencial_: sin este filtro IC_bueno=+0.305 (n=1807)

- **FILTRO** `ibs_20min` > `0.6495` → IC=-0.234 (n=887)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2664)

- **FILTRO** `sigma_ewma_delta_pct` > `8.508` → IC=-0.240 (n=410)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.508
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=3141)

- **PATRÓN** `ibs_20min` > `0.7627` → IC=+0.305 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7627 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.2146` → IC=+0.335 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2146 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.527` → IC=+0.180 (n=563)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.527 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.333 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.323 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.322 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.347 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.342 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.340 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.549` → IC=+0.144 (n=2344)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.549 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4547` → IC=+0.249 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4547 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.262 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.240 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.260 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.8143` → IC=+0.259 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8143 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.269 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.031)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.344 (n=1718)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.312 (n=924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.300)

- **PATRÓN** `ibs_20min` > `0.6596` → IC=+0.333 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6596 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.327 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.792` → IC=+0.320 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.792 (IC base=+0.300)

- **PATRÓN** `volumen_regimen` > `0.6263` → IC=+0.309 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6263 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.342 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` > `1.4247` → IC=+0.311 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4247 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `2638.0182` → IC=+0.314 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.0182 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.333 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.300)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.334 (n=1354)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.303)

- **PATRÓN** `drift_60min` |x|≤ `0.187` → IC=+0.306 (n=893)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.187 (IC base=+0.303)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.303)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.327 (n=2029)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3684 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.555` → IC=+0.316 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.555 (IC base=+0.303)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.078` → IC=+0.304 (n=2412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.078 (IC base=+0.303)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.307 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.303)

- **PATRÓN** `volumen_regimen` > `1.2246` → IC=+0.334 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2246 (IC base=+0.303)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.353 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.310 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.303)

- **PATRÓN** `volumen_spike_ratio` > `2.1346` → IC=+0.307 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1346 (IC base=+0.303)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.181 (n=4226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.224 (n=4217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0871` → IC=+0.202 (n=4213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0871 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5588` → IC=+0.234 (n=12633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5588 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1634` → IC=+0.208 (n=5137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1634 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.262` → IC=+0.258 (n=2481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.262 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.169 (n=8380)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1862 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.6236` → IC=+0.165 (n=8379)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6236 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.205 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6086` → IC=+0.191 (n=4080)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6086 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1984.2` → IC=+0.182 (n=11285)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1984.2 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.198 (n=11548)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 95.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.185 (n=8111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.007 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.226 (n=4051)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=5761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.236 (n=12180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.041` → IC=+0.197 (n=1991)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.041 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.688` → IC=+0.181 (n=10703)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.688 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1821` → IC=+0.163 (n=8671)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1821 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.227 (n=1796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6363` → IC=+0.188 (n=3801)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6363 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.192 (n=11116)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.233 (n=706)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3319` → IC=+0.229 (n=2113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3319 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=2209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=1431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9274` → IC=+0.294 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9274 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.986` → IC=+0.329 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.986 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.270 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.8388` → IC=+0.207 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8388 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.211 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=2273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2083.991` → IC=+0.216 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2083.991 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.260 (n=749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.0663` → IC=+0.310 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0663 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.255 (n=1491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.3945` → IC=+0.266 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3945 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.251 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.285 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.4284` → IC=+0.268 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4284 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.251 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1528.9218` → IC=+0.258 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1528.9218 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.255 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.249)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.217 (n=634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1598` → IC=+0.184 (n=1267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1598 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=1999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3437` → IC=+0.224 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3437 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1341` → IC=+0.215 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1341 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.386` → IC=+0.225 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.386 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6901` → IC=+0.166 (n=836)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6901 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.191 (n=302)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.180 (n=620)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.5182` → IC=+0.161 (n=620)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5182 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `422.0` → IC=+0.160 (n=1822)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 422.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.170 (n=1993)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2334` → IC=+0.173 (n=1752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2334 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6182` → IC=+0.204 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6182 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.503` → IC=+0.193 (n=379)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.503 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.161 (n=1991)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2065 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.147 (n=1684)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.145 (n=615)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.159 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.5067` → IC=+0.152 (n=1871)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5067 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.4246` → IC=+0.146 (n=1871)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4246 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.179 (n=603)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 202.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.236 (n=974)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3992` → IC=+0.224 (n=1883)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3992 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.435` → IC=+0.294 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.435 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.213 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3532` → IC=+0.227 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3532 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.214 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7054` → IC=+0.228 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7054 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1967.22` → IC=+0.227 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1967.22 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.247 (n=1612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1427` → IC=+0.274 (n=806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1427 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0066` → IC=+0.298 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0066 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.522` → IC=+0.276 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.522 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3553` → IC=+0.281 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3553 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7477` → IC=+0.235 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7477 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.1513` → IC=+0.239 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1513 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2052.1448` → IC=+0.242 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2052.1448 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.233 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.183 (n=1804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0064 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4062` → IC=+0.168 (n=2051)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4062 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.213 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1398` → IC=+0.199 (n=1257)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1398 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.767` → IC=+0.198 (n=355)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.767 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.0244` → IC=+0.159 (n=1804)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0244 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.180 (n=838)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.8191` → IC=+0.149 (n=1340)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.8191 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.167 (n=670)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4602.5142` → IC=+0.186 (n=1366)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4602.5142 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.159 (n=1990)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 140.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.155 (n=2156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.145 (n=2156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.684` → IC=+0.186 (n=2156)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.684 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.157 (n=2150)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.160 (n=533)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8568` → IC=+0.157 (n=1438)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8568 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2999` → IC=+0.201 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2999 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.135 (n=1346)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.127 (n=2019)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7579.1069` → IC=+0.191 (n=978)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7579.1069 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.146 (n=871)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 68.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.177 (n=1045)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4421` → IC=+0.130 (n=2028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4421 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.215 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `1.0756` → IC=+0.219 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0756 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.59` → IC=+0.275 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.59 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1755` → IC=+0.143 (n=2305)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1755 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1609` → IC=+0.136 (n=2337)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1609 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.148 (n=745)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2405)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2794.4942` → IC=+0.206 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2794.4942 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.166 (n=738)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.138 (n=2355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0108 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1079` → IC=+0.173 (n=786)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1079 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5952` → IC=+0.219 (n=2354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5952 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.1996` → IC=+0.148 (n=2223)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1996 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.392` → IC=+0.125 (n=473)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 7.392 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.467` → IC=+0.129 (n=2081)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 2.467 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.130 (n=2354)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.174 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1653` → IC=+0.123 (n=2273)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1653 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.150 (n=312)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4479` → IC=+0.134 (n=731)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4479 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4294` → IC=+0.139 (n=731)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4294 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2653.9292` → IC=+0.190 (n=1067)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2653.9292 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.129 (n=1902)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.245 (n=1902)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1287` → IC=+0.237 (n=710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1287 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=2204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=1912)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.1843` → IC=+0.227 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1843 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `0.4797` → IC=+0.222 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4797 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.611` → IC=+0.250 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.611 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.1768` → IC=+0.224 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1768 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.229 (n=2127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6183 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.271 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `2.4631` → IC=+0.227 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4631 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.8043` → IC=+0.229 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8043 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2618.6162` → IC=+0.226 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2618.6162 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0125` → IC=+0.236 (n=957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0125 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.240 (n=986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.261 (n=725)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=1061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.426` → IC=+0.256 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.426 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.2951` → IC=+0.234 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2951 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.349` → IC=+0.257 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.349 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.6401` → IC=+0.235 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6401 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.286 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4397` → IC=+0.231 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4397 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2597.9008` → IC=+0.230 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2597.9008 (IC base=+0.228)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.209 (n=1420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.190 (n=1075)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0089 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1293` → IC=+0.203 (n=1416)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1293 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.725` → IC=+0.232 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.725 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7907` → IC=+0.204 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7907 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.649` → IC=+0.212 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.649 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.863` → IC=+0.203 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.863 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6964` → IC=+0.185 (n=2585)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6964 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.192 (n=1158)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.196 (n=1041)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.5107` → IC=+0.188 (n=1041)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.5107 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.188 (n=3631)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `2687.8872` → IC=+0.188 (n=2872)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2687.8872 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.193 (n=2993)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 150.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.135 (n=1152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0037 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.3839` → IC=+0.161 (n=2300)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3839 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.128 (n=1122)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 19.0 (IC base=+0.087)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.204 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.198 (n=908)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.204 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.6376` → IC=+0.233 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6376 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.3049` → IC=+0.197 (n=275)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3049 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.092` → IC=+0.196 (n=390)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.092 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.702` → IC=+0.177 (n=963)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 6.702 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.8745` → IC=+0.202 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8745 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.179 (n=359)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.2086` → IC=+0.184 (n=781)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.2086 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.413` → IC=+0.177 (n=888)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.413 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14663.1359` → IC=+0.184 (n=605)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14663.1359 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.202 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.142 (n=1071)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0056 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.142 (n=942)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6382` → IC=+0.167 (n=942)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6382 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.713` → IC=+0.135 (n=209)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.713 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `1.0622` → IC=+0.149 (n=485)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.0622 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.168 (n=284)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.1178` → IC=+0.130 (n=930)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.1178 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=1385)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `310.0` → IC=+0.149 (n=915)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 310.0 (IC base=+0.119)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.248 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0943` → IC=+0.245 (n=327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0943 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=1027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6852` → IC=+0.273 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6852 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.3552` → IC=+0.220 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3552 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.2032` → IC=+0.221 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2032 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.883` → IC=+0.244 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.883 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.226 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.1649` → IC=+0.223 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1649 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1565` → IC=+0.248 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1565 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.248 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.776` → IC=+0.228 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.776 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.1073` → IC=+0.160 (n=333)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1073 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `6679.82` → IC=+0.134 (n=664)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 6679.82 (IC base=+0.059)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.175 (n=263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0108 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.5352` → IC=+0.163 (n=787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.5352 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `1.0181` → IC=+0.234 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0181 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.127` → IC=+0.231 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.127 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.0652` → IC=+0.181 (n=693)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.0652 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.170 (n=703)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.7217 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.167 (n=253)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `2.1838` → IC=+0.176 (n=344)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1838 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.169 (n=813)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3048.1866` → IC=+0.191 (n=263)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3048.1866 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.133 (n=739)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5417 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `2709.2975` → IC=+0.147 (n=381)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2709.2975 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.128 (n=535)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.052)

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

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.181 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0228 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.135 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 10.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.129 (n=251)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.61 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.232` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.232 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.132 (n=169)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.9016 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.3392` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.3392 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.128 (n=232)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 19.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.225 (n=5486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=17122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.4486` → IC=+0.230 (n=16453)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4486 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.905` → IC=+0.210 (n=2006)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.905 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.27` → IC=+0.254 (n=4018)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.27 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.2213` → IC=+0.170 (n=11030)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2213 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.207 (n=2188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.198 (n=5332)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `1800.63` → IC=+0.185 (n=16452)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1800.63 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.203 (n=15088)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.192 (n=9968)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0073 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.38` → IC=+0.192 (n=13144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.38 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=5562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.582` → IC=+0.242 (n=14937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.582 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1748` → IC=+0.171 (n=9111)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1748 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.205 (n=2073)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.584` → IC=+0.190 (n=14435)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.584 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.161 (n=4437)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7046 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.254 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.2601` → IC=+0.197 (n=6398)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2601 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.235 (n=900)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.349` → IC=+0.225 (n=2684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.349 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=1300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1811)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.539` → IC=+0.352 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.539 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.284 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.220 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.2757` → IC=+0.235 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2757 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2846)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2082.6976` → IC=+0.229 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2082.6976 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.245 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.266 (n=2289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.263)

- **PATRÓN** `drift_60min` |x|≤ `0.1195` → IC=+0.284 (n=1009)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1195 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2089)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` < `0.5083` → IC=+0.288 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5083 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.352` → IC=+0.265 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.352 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.0705` → IC=+0.263 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0705 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.284 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.264 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `2.6409` → IC=+0.271 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6409 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2569)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1659.1648` → IC=+0.269 (n=2045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1659.1648 (IC base=+0.263)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.275 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.263)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.168 (n=1169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.376` → IC=+0.226 (n=2372)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.376 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1243` → IC=+0.197 (n=1385)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1243 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.558` → IC=+0.164 (n=438)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.558 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.181` → IC=+0.156 (n=2314)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.181 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.176 (n=886)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6288 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.155 (n=2364)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.182 (n=378)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.189` → IC=+0.160 (n=2283)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.189 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5326` → IC=+0.155 (n=2318)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5326 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `266.0` → IC=+0.187 (n=1120)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 266.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2557` → IC=+0.163 (n=1951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2557 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.7006` → IC=+0.198 (n=2218)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7006 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.198` → IC=+0.157 (n=368)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.198 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.256` → IC=+0.144 (n=1996)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.256 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1895` → IC=+0.154 (n=2218)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1895 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2182` → IC=+0.198 (n=418)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2182 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4384` → IC=+0.150 (n=2113)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4384 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7759` → IC=+0.156 (n=1408)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7759 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.158 (n=890)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 275.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.259 (n=914)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.304` → IC=+0.322 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.304 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.230 (n=2419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.230 (n=2658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=3258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1837.9` → IC=+0.235 (n=1826)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1837.9 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.245 (n=2257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1826` → IC=+0.257 (n=1129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1826 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0294` → IC=+0.305 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0294 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.98` → IC=+0.294 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.98 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.300 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1336` → IC=+0.250 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1336 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2052.1448` → IC=+0.255 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2052.1448 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.258 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.197 (n=1250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4207` → IC=+0.158 (n=2831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4207 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2498` → IC=+0.194 (n=2831)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2498 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1406` → IC=+0.172 (n=1508)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1406 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.148` → IC=+0.159 (n=1149)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.148 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.165 (n=1888)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8653 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.190 (n=369)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5243` → IC=+0.160 (n=1216)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5243 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1678` → IC=+0.159 (n=1252)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1678 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6387.2063` → IC=+0.243 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6387.2063 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.173 (n=1201)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 74.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.149 (n=2355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0075 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.139 (n=2353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.7373` → IC=+0.183 (n=2353)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7373 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1467` → IC=+0.144 (n=2136)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1467 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.13` → IC=+0.170 (n=359)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.13 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8706` → IC=+0.138 (n=1570)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8706 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.226 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.136 (n=2263)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7258.1556` → IC=+0.213 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7258.1556 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.129 (n=2006)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 131.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.155 (n=1292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0103 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4432` → IC=+0.198 (n=2851)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4432 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0689` → IC=+0.207 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0689 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.745` → IC=+0.267 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.745 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2211` → IC=+0.135 (n=2850)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2211 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.125 (n=2689)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.135 (n=368)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8331` → IC=+0.127 (n=1856)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8331 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1924` → IC=+0.131 (n=1262)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.1924 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=1941)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2497.3328` → IC=+0.231 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2497.3328 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.146 (n=883)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.150 (n=2393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.01 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.154 (n=906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6463` → IC=+0.211 (n=2715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6463 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2146` → IC=+0.136 (n=2334)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2146 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.259` → IC=+0.134 (n=2616)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.259 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7102` → IC=+0.138 (n=1195)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7102 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.173 (n=463)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.442` → IC=+0.155 (n=847)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.442 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2673.4763` → IC=+0.208 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.4763 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.133 (n=2229)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.248 (n=2409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=1800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.61` → IC=+0.270 (n=2411)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.61 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1899` → IC=+0.246 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1899 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.756` → IC=+0.269 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.756 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.2284` → IC=+0.236 (n=2695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2284 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6395` → IC=+0.230 (n=2695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6395 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.254 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4995` → IC=+0.248 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4995 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=3500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `2625.644` → IC=+0.237 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2625.644 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.247 (n=1269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.236 (n=2628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.5143` → IC=+0.265 (n=2800)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5143 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.266 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.259 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.297 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4328` → IC=+0.233 (n=2597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4328 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `2376.9954` → IC=+0.229 (n=2501)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2376.9954 (IC base=+0.229)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=4878)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.244 (n=1673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.5053` → IC=+0.217 (n=5019)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5053 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=1827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9402` → IC=+0.247 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9402 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.1705` → IC=+0.208 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1705 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.4319` → IC=+0.211 (n=3603)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4319 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.02` → IC=+0.215 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.02 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.615` → IC=+0.209 (n=4471)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.615 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.220 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.207 (n=4689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.222 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4551` → IC=+0.213 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4551 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.8464` → IC=+0.209 (n=3294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8464 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=3857)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2926.5639` → IC=+0.214 (n=4483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2926.5639 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.241 (n=1225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.4893` → IC=+0.207 (n=3670)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4893 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=1246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.207 (n=1643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.199 (n=3671)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7333 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.6772` → IC=+0.198 (n=621)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6772 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.2381` → IC=+0.189 (n=3352)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2381 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.835` → IC=+0.201 (n=3290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.835 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `1.0974` → IC=+0.201 (n=3060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0974 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.196 (n=3368)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.194 (n=742)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.5334` → IC=+0.197 (n=1593)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5334 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.201 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=4878)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `174.0` → IC=+0.200 (n=3168)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 174.0 (IC base=+0.192)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.273 (n=658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.294 (n=250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.259 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.260 (n=336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.4896` → IC=+0.276 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4896 (IC base=+0.256)

- **PATRÓN** `dist_vwap_pct` < `0.1866` → IC=+0.268 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1866 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.583` → IC=+0.271 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.583 (IC base=+0.256)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.264 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.256)

- **PATRÓN** `volumen_regimen` > `0.6035` → IC=+0.260 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6035 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.8278` → IC=+0.262 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8278 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `16321.2566` → IC=+0.269 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16321.2566 (IC base=+0.256)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.235 (n=867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3682` → IC=+0.194 (n=1297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3682 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.201 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.1386` → IC=+0.210 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1386 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.7048` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7048 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.195 (n=1281)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2228` → IC=+0.191 (n=1297)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2228 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.201 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4035` → IC=+0.193 (n=431)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4035 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.1667` → IC=+0.192 (n=586)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.1667 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `14894.8693` → IC=+0.185 (n=588)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14894.8693 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `698.0` → IC=+0.190 (n=1252)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 698.0 (IC base=+0.177)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.198 (n=342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.007 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.220 (n=351)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.5864` → IC=+0.200 (n=774)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5864 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.703` → IC=+0.195 (n=516)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.703 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.238 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.463` → IC=+0.224 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.463 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2099` → IC=+0.242 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2099 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.2445` → IC=+0.198 (n=515)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.2445 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2469.2564` → IC=+0.222 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2469.2564 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.191 (n=554)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 11.0 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.227)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.213 (n=1375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.204 (n=1375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5189` → IC=+0.209 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5189 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.8776` → IC=+0.199 (n=459)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8776 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.205 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.200 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8782 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.203 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.200 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.4554` → IC=+0.205 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4554 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=1411)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.245 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.210 (n=1124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.198 (n=752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.3986` → IC=+0.196 (n=750)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3986 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.0867` → IC=+0.190 (n=1124)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0867 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.199 (n=197)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.36` → IC=+0.195 (n=1021)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 4.36 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.224 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.207 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.197 (n=968)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.191 (n=367)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `6781.2899` → IC=+0.195 (n=1124)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6781.2899 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.201 (n=644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.200 (n=752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.245 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.743` → IC=+0.238 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.743 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.210 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.6978` → IC=+0.228 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6978 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.190 (n=659)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.190 (n=327)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.5676` → IC=+0.195 (n=313)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5676 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.4918` → IC=+0.203 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4918 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=852)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `3548.6004` → IC=+0.212 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3548.6004 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.197 (n=714)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 52.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.206 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.209 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.6144` → IC=+0.223 (n=532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6144 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.238 (n=361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.7249` → IC=+0.225 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7249 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5172` → IC=+0.222 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5172 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `1.2157` → IC=+0.205 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2157 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.868` → IC=+0.211 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.868 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.7551` → IC=+0.212 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7551 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.9368` → IC=+0.211 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9368 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.224 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.2044` → IC=+0.243 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2044 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2981.8939` → IC=+0.221 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.8939 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.232 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.201)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.157 (n=720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0039 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.3933` → IC=+0.148 (n=1545)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.3933 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.160 (n=542)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.992` → IC=+0.163 (n=449)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 8.992 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.238 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.344` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 10.344 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.174 (n=228)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.132 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0056 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.516` → IC=+0.191 (n=460)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.516 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.155 (n=259)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.282 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.075)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7041` → IC=-0.185 (n=87)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7041
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=262)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.130 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0059 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6238` → IC=+0.208 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6238 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1242` → IC=+0.196 (n=264)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1242 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.128` → IC=+0.261 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.128 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.8144` → IC=+0.127 (n=336)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8144 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.021)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1333` → IC=-0.202 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1333
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=196)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.170 (n=352)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.75 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7456` → IC=+0.139 (n=128)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.7456 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.381` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.381 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.155 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0103 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.1333` → IC=+0.227 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1333 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.3973` → IC=+0.142 (n=216)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3973 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.739` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.739 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0779 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.8101` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.8101 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `1.4109` → IC=+0.171 (n=174)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4109 (IC base=+0.076)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.157 (n=167)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.06 (IC base=+0.076)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.333 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=241)

- **FILTRO** `dist_vwap_pct` > `0.2321` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2321
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=288)

- **FILTRO** `libro_liquidez` < `887.0104` → IC=-0.218 (n=76)

  - _Acción_: SKIP cuando `libro_liquidez` < 887.0104
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=229)

- **FILTRO** `ibs_20min` > `0.565` → IC=-0.330 (n=127)

  - _Acción_: SKIP cuando `ibs_20min` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=129)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=237)

- **FILTRO** `sigma_ewma_delta_pct` > `10.458` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.458
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=231)

- **FILTRO** `volumen_pendiente_norm` > `0.047` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.047
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=142)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `drift_60min` |x|> `0.1744` → IC=-0.260 (n=23)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1744
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `volumen_spike_ratio` > `2.3966` → IC=-0.237 (n=36)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3966
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=38)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.267 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=85)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=85)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `drift_60min` |x|> `0.149` → IC=-0.315 (n=25)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.149
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=76)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.160 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=74)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=76)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=83)

- **FILTRO** `libro_liquidez` < `1541.8747` → IC=-0.304 (n=49)

  - _Acción_: SKIP cuando `libro_liquidez` < 1541.8747
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=49)

- **PATRÓN** `ibs_20min` > `0.941` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.941 (IC base=-0.160)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.395 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.329 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1623` → IC=-0.123 (n=274)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1623
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=532)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.188 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.006 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.151 (n=516)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6842 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.741` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.741 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.625` → IC=+0.172 (n=172)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.625 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` < `0.2267` → IC=+0.145 (n=463)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2267 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.1768` → IC=+0.147 (n=364)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1768 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.1623` → IC=+0.152 (n=532)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1623 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.099` → IC=+0.183 (n=181)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.099 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `3239.2397` → IC=+0.137 (n=403)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3239.2397 (IC base=+0.058)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6781` → IC=-0.222 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6781
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=159)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.198 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0049 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.155 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 12.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.148 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1761` → IC=+0.196 (n=281)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1761 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.158` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.158 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0304` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.0304 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.152 (n=219)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.5202` → IC=+0.171 (n=250)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.5202 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4429` → IC=+0.149 (n=249)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4429 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5953.1362` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5953.1362 (IC base=+0.136)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=170)

- **FILTRO** `ibs_20min` > `0.1892` → IC=-0.137 (n=100)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1892
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=195)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.140 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0039 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.191 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.136 (n=163)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.8015 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` < `0.0943` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.0943 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.126 (n=188)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6229 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.167 (n=103)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.029)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=103)

- **FILTRO** `volumen_spike_ratio` > `2.1087` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.1087
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=67)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.308 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.270 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.250)

- **PATRÓN** `volumen_regimen` < `0.5821` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5821 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.252 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.090)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=68)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.312)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.312)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.369 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.312)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3369` → IC=+0.258 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3369 (IC base=+0.236)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.236)

- **PATRÓN** `elapsed_s` < `216.4` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.4 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.273 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.236)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.236)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.329 (n=68)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.312)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.312)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.369 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.312)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3369` → IC=+0.258 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3369 (IC base=+0.236)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.236)

- **PATRÓN** `elapsed_s` < `216.4` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.4 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.273 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.236)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.236)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2851.3154` → IC=+0.133 (n=559)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2851.3154 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2851.3154` → IC=+0.133 (n=559)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2851.3154 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=189)

- **FILTRO** `libro_liquidez` < `2842.6585` → IC=-0.198 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 2842.6585
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=154)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=292)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

- **FILTRO** `liq_n` < `5.0` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `liq_n` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=29)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `3561.53` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 3561.53
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=24)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `ballena_activa_n` > `55.0` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 55.0
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3473)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=103)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=103)

- **FILTRO** `ballena_activa_n` > `115.0` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `ballena_activa_n` > 115.0
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=31)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=129)

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

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1271)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1225)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=714)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=413)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=394)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.020)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=838)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=838)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=259)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=659)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=793)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=793)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=221)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=221)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.132 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=170)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.124 (n=91)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=219)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=243)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=259)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=348)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=348)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=193)

- **FILTRO** `libro_liquidez` < `612.0892` → IC=-0.135 (n=124)

  - _Acción_: SKIP cuando `libro_liquidez` < 612.0892
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=254)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=254)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=182)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.123 (n=1326)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3486)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=29)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=34)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.46 (IC base=+0.008)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=246)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.153 (n=145)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=167)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.5 (IC base=+0.065)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.130 (n=330)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=120)

- **FILTRO** `profundidad_ratio` < `56.1` → IC=-0.160 (n=148)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.1
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=302)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.133 (n=186)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=212)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `22.2` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `profundidad_ratio` < 22.2
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=285)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.171 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=348)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=277)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=301)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=5844)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=18259)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.173 (n=5980)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=18794)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.195 (n=1071)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=3305)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.172 (n=1027)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3406)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.143 (n=1151)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `1336.2` → IC=+0.135 (n=2189)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1336.2 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=2064)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1505.9972` → IC=+0.152 (n=1508)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1505.9972 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.157 (n=811)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2728)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=864)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2653)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.175 (n=1072)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=3320)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.199 (n=1057)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3463)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.131 (n=1495)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1823.98` → IC=+0.126 (n=1494)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1823.98 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.154 (n=1057)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=3322)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2360)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2298)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2780)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3520)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=436)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=423)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=863)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=353)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=907)

- **FILTRO** `libro_liquidez` < `1756.2367` → IC=-0.161 (n=231)

  - _Acción_: SKIP cuando `libro_liquidez` < 1756.2367
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=695)

- **FILTRO** `libro_liquidez` < `2083.4373` → IC=-0.168 (n=347)

  - _Acción_: SKIP cuando `libro_liquidez` < 2083.4373
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=705)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=233)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.037)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=16714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=36975)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13161)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=40528)

- **FILTRO** `ibs_7min` < `0.2398` → IC=-0.229 (n=13421)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2398
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=40268)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=17959)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=35730)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.240 (n=16567)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=51099)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=16756)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=50910)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2695)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6658)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4626)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4727)

- **FILTRO** `ibs_7min` < `0.7121` → IC=-0.244 (n=3085)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7121
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6268)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.178 (n=2013)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7340)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2908)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=8824)

- **FILTRO** `ibs_7min` > `0.7715` → IC=-0.210 (n=2932)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=8800)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2110)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=6961)

- **FILTRO** `ibs_7min` < `0.727` → IC=-0.199 (n=2267)

  - _Acción_: SKIP cuando `ibs_7min` < 0.727
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6804)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.192 (n=2247)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6824)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=2278)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6936)

- **FILTRO** `ibs_7min` > `0.2685` → IC=-0.196 (n=2303)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2685
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6911)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.184 (n=2291)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6923)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=2200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6692)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2187)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6705)

- **FILTRO** `ibs_7min` < `0.2981` → IC=-0.247 (n=2934)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2981
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=5958)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2129)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6763)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.253 (n=2905)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9584)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.177 (n=3121)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9368)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2045)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6707)

- **FILTRO** `ibs_7min` < `0.7303` → IC=-0.187 (n=2188)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7303
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6564)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.190 (n=2175)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6577)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2038)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7038)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.181 (n=2268)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6808)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.175 (n=2248)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6828)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=2101)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6719)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.232 (n=2188)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=6632)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2123)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6697)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.188 (n=3114)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=9812)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.290 (n=2057)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6744)

- **FILTRO** `ibs_7min` < `0.21` → IC=-0.220 (n=2200)

  - _Acción_: SKIP cuando `ibs_7min` < 0.21
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6601)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1970)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=6831)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.214 (n=2974)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=9255)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=984)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1268)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.121 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=491)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=544)

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
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=848)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=330)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=325)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=442)

- **FILTRO** `libro_liquidez` < `3257.5356` → IC=-0.159 (n=174)

  - _Acción_: SKIP cuando `libro_liquidez` < 3257.5356
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=525)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.140 (n=1143)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.133 (n=537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.133 (n=431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `135875.0` → IC=+0.142 (n=1006)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 135875.0 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.150 (n=518)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.149 (n=371)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 11.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.148 (n=89)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.215 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `289.181` → IC=+0.144 (n=178)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 289.181 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2584.1425` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.1425 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 7.0 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.129 (n=235)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=281)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2323.3188` → IC=+0.135 (n=157)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2323.3188 (IC base=+0.113)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.182 (n=152)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.154 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7760.8` → IC=+0.143 (n=152)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7760.8 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.196 (n=100)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 70.0 (IC base=+0.136)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.245 (n=92)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.175 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `4970.298` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4970.298 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3257.229` → IC=+0.165 (n=180)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3257.229 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 27.0 (IC base=+0.152)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.122 (n=194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 14.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=130)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.304 (n=217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=423)

- **FILTRO** `T_h` > `129.6211` → IC=-0.200 (n=158)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=482)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.181 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0034 (IC base=-0.079)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.337 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=144)

- **FILTRO** `T_h` > `87.9957` → IC=-0.276 (n=47)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=144)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.300 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.034)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.244 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=73)

- **FILTRO** `T_h` < `87.1706` → IC=-0.184 (n=55)

  - _Acción_: SKIP cuando `T_h` < 87.1706
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=55)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=-0.089)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0102` → IC=-0.220 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=151)

- **FILTRO** `T_h` > `70.6078` → IC=-0.200 (n=452)

  - _Acción_: SKIP cuando `T_h` > 70.6078
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=151)

- **FILTRO** `pct_vs_K` |x|> `3.3088` → IC=-0.438 (n=127)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3088
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=383)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0044` → IC=-0.206 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=148)

- **FILTRO** `pct_vs_K` |x|> `2.7876` → IC=-0.363 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7876
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=148)

- **FILTRO** `T_h` > `144.2373` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 144.2373
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=136)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=136)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.2523` → IC=-0.402 (n=59)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2523
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=115)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.378 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=119)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.207 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=119)

- **FILTRO** `T_h` > `57.7851` → IC=-0.283 (n=104)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0079` → IC=-0.267 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0079
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=124)

- **FILTRO** `T_h` > `94.227` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `T_h` > 94.227
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `sigma_h` > `0.0132` → IC=-0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=76)

- **FILTRO** `T_h` > `46.6251` → IC=-0.305 (n=75)

  - _Acción_: SKIP cuando `T_h` > 46.6251
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.476 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.336)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.351 (n=92)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.375 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.336)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.389 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.336)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.336)

- **PATRÓN** `edge` > `0.099` → IC=+0.440 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.099 (IC base=+0.414)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.433 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.414)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.433 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.414)

- **PATRÓN** `T_h` > `1.4833` → IC=+0.419 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4833 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.459 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.419 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.423 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.418)

- **PATRÓN** `T_h` < `1.0313` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0313 (IC base=+0.418)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.407 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.418)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.426 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.418)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1885` → IC=+0.483 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.437)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.466 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.437)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.437)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.437)

- **PATRÓN** `edge` > `0.1961` → IC=+0.479 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.479 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.465)

- **PATRÓN** `T_h` > `1.1543` → IC=+0.479 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1543 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4373` → IC=+0.486 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4373 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=301)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=379)

- **FILTRO** `streak_estiramiento` > `0.8382` → IC=-0.174 (n=84)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8382
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=254)

- **PATRÓN** `streak_estiramiento` < `0.8382` → IC=+0.121 (n=254)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.8382 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `2756.3002` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2756.3002 (IC base=+0.045)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `libro_liquidez` < `2474.7486` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 2474.7486
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=16)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2711` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.2711 (IC base=-0.004)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.088)

- **PATRÓN** `streak_estiramiento` < `0.5597` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `streak_estiramiento` < 0.5597 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 35.0 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `2229.7597` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2229.7597 (IC base=+0.088)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=102)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=748)

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

- **FILTRO** `libro_liquidez` < `3338.6704` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 3338.6704
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `streak_estiramiento` > `1.1496` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1496
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=41)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.035)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=982)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1127)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1170)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `14.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3965)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2178)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.196 (n=1542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.197 (n=1169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0119 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1737` → IC=+0.193 (n=3083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1737 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1333` → IC=+0.189 (n=1394)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1333 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.255 (n=3504)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1267` → IC=+0.171 (n=1683)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1267 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.6708` → IC=+0.166 (n=3329)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.6708 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.513` → IC=+0.253 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.513 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `4729.1233` → IC=+0.198 (n=1168)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4729.1233 (IC base=+0.179)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1386)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.243 (n=402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.264 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.219)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.249 (n=201)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.238 (n=632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.219)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.285 (n=602)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1358` → IC=+0.239 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1358 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.305 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `8999.1204` → IC=+0.229 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8999.1204 (IC base=+0.219)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.192 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.049` → IC=+0.154 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.049 (IC base=+0.145)

- **PATRÓN** `drift_15min` |x|≤ `0.3957` → IC=+0.154 (n=232)

  - _Acción_: Kelly boost +0.77€ cuando `drift_15min` |x|≤ 0.3957 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.145` → IC=+0.152 (n=463)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.145 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1323` → IC=+0.159 (n=274)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1323 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5467` → IC=+0.245 (n=695)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5467 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1175` → IC=+0.161 (n=435)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1175 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.274 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3201.2957` → IC=+0.153 (n=695)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3201.2957 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.763` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.763
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=320)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8947` → IC=+0.249 (n=257)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8947 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=423)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0238` → IC=+0.248 (n=268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0238 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.236 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3374` → IC=+0.233 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3374 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.217 (n=713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.279 (n=805)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1887` → IC=+0.212 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1887 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.825` → IC=+0.224 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.825 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2968.8332` → IC=+0.300 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.8332 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=768)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.367 (n=413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.390 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.384 (n=412)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2268` → IC=+0.385 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2268 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.402 (n=619)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1446` → IC=+0.382 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1446 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.671` → IC=+0.384 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.671 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `3840.073` → IC=+0.376 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3840.073 (IC base=+0.366)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.382 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 423.0 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.367 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.400 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.392 (n=146)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.398 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.384 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.392 (n=322)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.2448` → IC=+0.397 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2448 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.742` → IC=+0.377 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.742 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `15403.697` → IC=+0.392 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15403.697 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.414 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.363 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.383 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0903` → IC=+0.377 (n=266)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0903 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.383 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.389 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.413 (n=297)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.381 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.366 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.973` → IC=+0.387 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.973 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3940.6708` → IC=+0.391 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3940.6708 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.225 (n=1065)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3196)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.211 (n=1658)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2603)

- **FILTRO** `libro_liquidez` < `4188.399` → IC=-0.152 (n=2812)

  - _Acción_: SKIP cuando `libro_liquidez` < 4188.399
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1449)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.186 (n=687)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.283 (n=1030)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1109` → IC=+0.209 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1109 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.4229` → IC=+0.200 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4229 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.23` → IC=+0.268 (n=1176)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.23 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.36` → IC=+0.282 (n=3520)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.36 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6614` → IC=+0.280 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6614 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.222 (n=1859)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=620)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=618)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1861)

- **FILTRO** `sigma_ewma_delta_pct` > `23.313` → IC=-0.265 (n=356)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.313
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2123)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.121 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0053 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.291 (n=151)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.273 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.333 (n=333)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.292 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.545` → IC=+0.132 (n=373)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.545 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.212 (n=57)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.159` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.159 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.300 (n=58)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=669)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.161 (n=343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0048 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0692` → IC=+0.194 (n=227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0692 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.191 (n=393)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.152 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6098` → IC=+0.252 (n=515)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6098 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.4589` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4589 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.153 (n=402)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.422` → IC=+0.253 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.422 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=669)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.161 (n=172)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7675` → IC=+0.257 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7675 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1581` → IC=+0.257 (n=839)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1581 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.248 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.248 (n=490)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3685` → IC=+0.275 (n=1258)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3685 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6016` → IC=+0.272 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6016 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.117` → IC=+0.257 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.117 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.489` → IC=+0.248 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.489 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.255 (n=333)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=649)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.281 (n=245)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=737)

- **FILTRO** `sigma_ewma_delta_pct` > `6.585` → IC=-0.201 (n=229)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.585
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=753)

- **FILTRO** `sigma_ewma_delta_pct` > `17.923` → IC=-0.146 (n=512)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.923
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.189)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0649` → IC=+0.235 (n=557)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0649 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.287 (n=557)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.4499` → IC=+0.239 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4499 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.250 (n=586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=587)

- **FILTRO** `sigma_ewma_delta_pct` > `7.41` → IC=-0.209 (n=366)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.41
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=807)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=1154)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.206)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0678` → IC=+0.273 (n=756)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0678 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1155` → IC=+0.295 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1155 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=847)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7764` → IC=+0.350 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7764 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.324 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.087)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.324 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.087)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.298 (n=928)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.320 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2411` → IC=+0.308 (n=353)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2411 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.309 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=1099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8388` → IC=+0.321 (n=1055)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8388 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2684` → IC=+0.327 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2684 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.377 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12383.1611` → IC=+0.311 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12383.1611 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.314 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.291 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.312 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.311 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.316 (n=567)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.329 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.382 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.327 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.306 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.318 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0682` → IC=+0.296 (n=488)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0682 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1067` → IC=+0.334 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1067 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.316 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=442)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.325 (n=488)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.327 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=84)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=252)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.136 (n=226)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=78)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.214 (n=117)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=361)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.186 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=359)

- **FILTRO** `drift_15min` |x|> `0.4407` → IC=-0.152 (n=162)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4407
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=316)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1334` → IC=-0.147 (n=49)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1334
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=149)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2412` → IC=-0.128 (n=92)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2412
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=94)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2021` → IC=-0.241 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2021
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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3147` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3147
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0623` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0623
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=37)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.138` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.138
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `85.7585` → IC=+0.187 (n=474)

  - _Acción_: Kelly boost +0.93€ cuando `T_h` > 85.7585 (IC base=+0.186)

- **PATRÓN** `ratio` < `0.973` → IC=+0.407 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.186)

- **PATRÓN** `T_h` > `112.2605` → IC=+0.352 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 112.2605 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.373 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `107.5733` → IC=+0.167 (n=196)

  - _Acción_: Kelly boost +0.83€ cuando `T_h` > 107.5733 (IC base=+0.153)

- **PATRÓN** `ratio` < `0.9838` → IC=+0.318 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9838 (IC base=+0.153)

- **PATRÓN** `T_h` > `111.0796` → IC=+0.303 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.0796 (IC base=+0.290)

- **PATRÓN** `ratio` > `1.0455` → IC=+0.403 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0455 (IC base=+0.290)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.232 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.401 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.353 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0347` → IC=+0.395 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0347 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1003` → IC=+0.445 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1003 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de +0.179 a +0.255 en UPDOWN_GBM#15min (n=3504). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.219 a +0.285 en UPDOWN_GBM#BTC#15min (n=602). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5467 sube el IC de +0.145 a +0.245 en UPDOWN_GBM#ETH#15min (n=695). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8947 sube el IC de +0.096 a +0.249 en UPDOWN_GBM#SOL#15min (n=257). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.202 a +0.279 en UPDOWN_GBM#XRP#15min (n=805). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=768). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=1030). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.36 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3520). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.097 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=333). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.195 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6098 sube el IC de +0.153 a +0.252 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=515). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3685 sube el IC de +0.244 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1258). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.040 a +0.287 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=557). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.206 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.025 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=847). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.087 a +0.324 en UPDOWN_GBM_ETH_15M_HORA7 (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.087 a +0.324 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8388 sube el IC de +0.292 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1055). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.289 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=567). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.294 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=488). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.366 a +0.402 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=619). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.365 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=322). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.364 a +0.413 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=297). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1910 | +0.089 | +205.72€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1910 | +0.089 | +205.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1523 | +0.093 | +179.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1523 | +0.093 | +179.47€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 280 | +0.067 | +10.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 280 | +0.067 | +10.78€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 76 | +0.103 | +15.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 76 | +0.103 | +15.81€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 602 | -0.003 | +70.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 602 | -0.003 | +70.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 442 | -0.025 | +40.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 442 | -0.025 | +40.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 124 | +0.056 | +20.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 124 | +0.056 | +20.72€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 33 | +0.043 | +5.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 33 | +0.043 | +5.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 39710 | -0.083 | -5002.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2174 | +0.031 | -250.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 37536 | -0.090 | -4751.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4475 | -0.117 | -771.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4475 | -0.117 | -771.71€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2174 | +0.031 | -250.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2174 | +0.031 | -250.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4312 | -0.105 | -875.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4312 | -0.105 | -875.77€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10560 | -0.023 | -972.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10560 | -0.023 | -972.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10476 | -0.107 | -810.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10476 | -0.107 | -810.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7713 | -0.135 | -1321.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7713 | -0.135 | -1321.10€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 34311 | -0.016 | +3420.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8877 | +0.005 | +1692.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 25434 | -0.023 | +1728.40€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 34311 | -0.016 | +3420.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8877 | +0.005 | +1692.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 25434 | -0.023 | +1728.40€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 142858 | +0.115 | -5811.12€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18433 | +0.183 | -542.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 627 | -0.020 | -69.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 115223 | +0.106 | -4879.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8575 | +0.101 | -319.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19110 | +0.108 | -1174.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19034 | +0.109 | -1173.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 27704 | +0.129 | -386.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5165 | +0.189 | -169.08€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19096 | +0.121 | -100.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3401 | +0.084 | -94.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19163 | +0.098 | -1362.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 72 | -0.122 | -6.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19076 | +0.100 | -1345.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 30379 | +0.124 | -555.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7880 | +0.178 | -132.69€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19346 | +0.107 | -358.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3141 | +0.100 | -55.64€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27371 | +0.115 | -1393.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5188 | +0.196 | -251.76€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 530 | +0.013 | -15.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19620 | +0.095 | -957.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2033 | +0.131 | -169.24€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19131 | +0.105 | -937.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 67 | -0.080 | +6.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19051 | +0.106 | -943.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 22978 | +0.196 | -1397.12€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 22978 | +0.196 | -1397.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5234 | +0.178 | -452.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5234 | +0.178 | -452.55€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2889 | +0.204 | -60.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2889 | +0.204 | -60.88€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5174 | +0.181 | -409.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5174 | +0.181 | -409.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4493 | +0.247 | -149.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4493 | +0.247 | -149.64€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5109 | +0.187 | -338.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5109 | +0.187 | -338.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1004 | +0.427 | -32.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1004 | +0.427 | -32.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 394 | +0.437 | -5.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 394 | +0.437 | -5.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 394 | +0.432 | -8.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 394 | +0.432 | -8.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 202 | +0.402 | -15.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 202 | +0.402 | -15.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 80319 | +0.201 | -5752.18€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 80319 | +0.201 | -5752.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13792 | +0.185 | -1425.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13792 | +0.185 | -1425.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 12974 | +0.224 | -451.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 12974 | +0.224 | -451.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13754 | +0.181 | -1446.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13754 | +0.181 | -1446.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13047 | +0.220 | -485.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13047 | +0.220 | -485.38€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13326 | +0.202 | -873.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13326 | +0.202 | -873.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13426 | +0.197 | -1070.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13426 | +0.197 | -1070.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 30699 | +0.117 | +209.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 30699 | +0.117 | +209.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15259 | +0.120 | +184.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15259 | +0.120 | +184.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15440 | +0.114 | +25.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15440 | +0.114 | +25.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2046 | +0.293 | -5.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2046 | +0.293 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 936 | +0.280 | -22.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 936 | +0.280 | -22.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 991 | +0.297 | +12.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 991 | +0.297 | +12.21€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 945 | +0.442 | +5.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 945 | +0.442 | +5.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 459 | +0.437 | -3.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 459 | +0.437 | -3.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 440 | +0.448 | +7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 440 | +0.448 | +7.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1618 | +0.073 | -59.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 623 | +0.054 | -49.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 995 | +0.085 | -10.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1245 | +0.081 | -20.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 250 | +0.068 | -10.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 995 | +0.085 | -10.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 301 | +0.028 | -41.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 301 | +0.028 | -41.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 60534 | +0.100 | -1535.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4894 | +0.090 | +45.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 55640 | +0.101 | -1580.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 33319 | +0.105 | -374.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4894 | +0.090 | +45.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 28425 | +0.108 | -419.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12405 | +0.109 | -65.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12405 | +0.109 | -65.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14810 | +0.082 | -1094.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14810 | +0.082 | -1094.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 895 | +0.192 | -111.46€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 895 | +0.192 | -111.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 895 | +0.192 | -111.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 895 | +0.192 | -111.46€ | 3 | 4 |
| ✅ GBM_LATE_15M | 41660 | +0.094 | +21679.34€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 41660 | +0.094 | +21679.34€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6949 | +0.215 | +5694.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6949 | +0.215 | +5694.14€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6233 | +0.180 | +4722.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6233 | +0.180 | +4722.76€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7447 | +0.205 | +5795.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7447 | +0.205 | +5795.49€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 5815 | +0.041 | +1613.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5815 | +0.041 | +1613.94€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 5886 | -0.032 | +1242.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5886 | -0.032 | +1242.76€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 9330 | -0.031 | +2610.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9330 | -0.031 | +2610.25€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 44850 | +0.086 | +24372.68€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 44850 | +0.086 | +24372.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8656 | +0.004 | +4373.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8656 | +0.004 | +4373.98€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9477 | +0.010 | +2228.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9477 | +0.010 | +2228.05€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6227 | +0.278 | +6676.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6227 | +0.278 | +6676.46€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8057 | +0.013 | +1981.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8057 | +0.013 | +1981.93€ | 1 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7164 | +0.039 | +2956.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7164 | +0.039 | +2956.61€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5269 | +0.302 | +6155.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5269 | +0.302 | +6155.64€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 33040 | +0.180 | +26699.65€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 33040 | +0.180 | +26699.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5013 | +0.229 | +4438.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5013 | +0.229 | +4438.29€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5186 | +0.150 | +3829.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5186 | +0.150 | +3829.51€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5294 | +0.224 | +4567.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5294 | +0.224 | +4567.61€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5606 | +0.138 | +4248.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5606 | +0.138 | +4248.40€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6210 | +0.124 | +4620.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6210 | +0.124 | +4620.15€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5731 | +0.225 | +4995.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5731 | +0.225 | +4995.69€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8885 | +0.133 | +4318.18€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8885 | +0.133 | +4318.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2636 | +0.145 | +1513.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2636 | +0.145 | +1513.52€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2634 | +0.137 | +1240.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2634 | +0.137 | +1240.59€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2167 | +0.105 | +822.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2167 | +0.105 | +822.06€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 625 | +0.133 | +281.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 625 | +0.133 | +281.73€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 41849 | +0.185 | +33396.69€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 41849 | +0.185 | +33396.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6629 | +0.241 | +6166.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6629 | +0.241 | +6166.86€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6496 | +0.148 | +4436.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6496 | +0.148 | +4436.15€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7070 | +0.233 | +6320.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7070 | +0.233 | +6320.03€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6911 | +0.138 | +4918.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6911 | +0.138 | +4918.80€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7418 | +0.121 | +5107.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7418 | +0.121 | +5107.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7325 | +0.229 | +6447.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7325 | +0.229 | +6447.55€ | 0 | 20 |
| ✅ GBM_LATE_5M | 11584 | +0.201 | +8947.34€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11584 | +0.201 | +8947.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2725 | +0.206 | +2322.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2725 | +0.206 | +2322.17€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1106 | +0.192 | +800.57€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1106 | +0.192 | +800.57€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3331 | +0.193 | +2335.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3331 | +0.193 | +2335.31€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 1683 | +0.189 | +1264.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1683 | +0.189 | +1264.69€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1755 | +0.200 | +1308.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1755 | +0.200 | +1308.49€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3386 | +0.067 | +1111.35€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 3386 | +0.067 | +1111.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1252 | +0.082 | +462.60€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1252 | +0.082 | +462.60€ | 0 | 5 |
| ✅ GBM_LATE_60M#ETH | 1090 | +0.070 | +386.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1090 | +0.070 | +386.69€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 1044 | +0.046 | +262.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1044 | +0.046 | +262.06€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 561 | -0.246 | -25.81€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 561 | -0.246 | -25.81€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 210 | -0.245 | -14.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 210 | -0.245 | -14.04€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 199 | -0.226 | -2.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 199 | -0.226 | -2.48€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 152 | -0.266 | -9.30€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 152 | -0.266 | -9.30€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1493 | +0.084 | +385.22€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1493 | +0.084 | +385.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 585 | +0.081 | +143.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 585 | +0.081 | +143.51€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 537 | +0.058 | +81.34€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 537 | +0.058 | +81.34€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 371 | +0.125 | +160.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 371 | +0.125 | +160.37€ | 2 | 10 |
| ✅ LATE_WINDOW_5MIN | 163 | +0.276 | +158.78€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 163 | +0.276 | +158.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 163 | +0.276 | +158.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 163 | +0.276 | +158.78€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3339 | +0.100 | +819.69€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3339 | +0.100 | +819.69€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3339 | +0.100 | +819.69€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3339 | +0.100 | +819.69€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 518 | -0.048 | -22.03€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 518 | -0.048 | -22.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 143 | -0.017 | +1.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 143 | -0.017 | +1.52€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 98 | -0.060 | -6.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 98 | -0.060 | -6.20€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 196 | -0.005 | -0.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 196 | -0.005 | -0.48€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3682 | +0.016 | +82.78€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3682 | +0.016 | +82.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 181 | +0.019 | -2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 181 | +0.019 | -2.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 776 | +0.014 | +34.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 776 | +0.014 | +34.63€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 206 | -0.014 | -4.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 206 | -0.014 | -4.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1321 | +0.026 | +31.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1321 | +0.026 | +31.53€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 755 | +0.011 | +1.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 755 | +0.011 | +1.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 443 | +0.012 | +22.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 443 | +0.012 | +22.87€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1726 | -0.041 | -28.38€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1726 | -0.041 | -28.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 494 | -0.030 | -11.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 494 | -0.030 | -11.07€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 585 | -0.015 | +6.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 585 | -0.015 | +6.20€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 647 | -0.072 | -23.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 647 | -0.072 | -23.51€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8456 | -0.028 | -11.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4012 | -0.037 | -89.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4444 | -0.020 | +78.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 259 | -0.040 | -9.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 132 | -0.022 | -0.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 127 | -0.058 | -9.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2109 | -0.019 | +17.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1004 | -0.022 | -0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1105 | -0.016 | +18.50€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 930 | -0.024 | +11.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 466 | -0.043 | -14.02€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 464 | -0.004 | +25.95€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1825 | -0.043 | -66.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 848 | -0.054 | -58.07€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 977 | -0.033 | -8.12€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1652 | -0.021 | +22.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 786 | -0.035 | -12.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 866 | -0.008 | +35.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1681 | -0.029 | +12.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 776 | -0.036 | -3.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 905 | -0.023 | +16.01€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 48877 | -0.001 | +2418.09€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 48877 | -0.001 | +2418.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8809 | +0.026 | +1112.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8809 | +0.026 | +1112.34€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7056 | -0.034 | -101.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7056 | -0.034 | -101.24€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8912 | +0.024 | +925.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8912 | +0.024 | +925.47€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6899 | -0.048 | -152.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6899 | -0.048 | -152.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8261 | -0.005 | +226.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8261 | -0.005 | +226.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8940 | +0.015 | +407.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8940 | +0.015 | +407.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6598 | -0.059 | -161.55€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6598 | -0.059 | -161.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1711 | -0.079 | -45.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1711 | -0.079 | -45.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 773 | -0.119 | -32.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 773 | -0.119 | -32.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1978 | -0.075 | -39.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1978 | -0.075 | -39.81€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 857 | -0.016 | -25.51€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3367 | +0.004 | -1.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3367 | +0.004 | -1.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 121355 | -0.076 | +1765.51€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 121355 | -0.076 | +1765.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21085 | -0.077 | +1107.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21085 | -0.077 | +1107.48€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18285 | -0.100 | -947.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18285 | -0.100 | -947.59€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21381 | -0.067 | +1157.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21381 | -0.067 | +1157.12€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 17828 | -0.097 | -611.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 17828 | -0.097 | -611.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 21746 | -0.056 | +342.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 21746 | -0.056 | +342.74€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21030 | -0.066 | +717.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21030 | -0.066 | +717.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8750 | -0.034 | -181.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8750 | -0.034 | -181.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1983 | -0.046 | -24.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1983 | -0.046 | -24.80€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2599 | -0.026 | -41.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2599 | -0.026 | -41.83€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1191 | -0.055 | -28.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1191 | -0.055 | -28.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 968 | -0.030 | -34.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 968 | -0.030 | -34.42€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1659 | +0.123 | +674.32€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1523 | +0.129 | +661.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 355 | +0.141 | +184.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 355 | +0.141 | +184.09€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 313 | +0.113 | +102.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 313 | +0.113 | +102.27€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 303 | +0.136 | +146.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 303 | +0.136 | +146.74€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 268 | +0.152 | +147.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 268 | +0.152 | +147.63€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 284 | +0.098 | +80.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 284 | +0.098 | +80.99€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1416 | -0.011 | -9.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1416 | -0.011 | -9.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 273 | +0.002 | +11.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 273 | +0.002 | +11.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 242 | -0.012 | -0.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 242 | -0.012 | -0.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 366 | -0.041 | -25.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 366 | -0.041 | -25.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 304 | +0.013 | +4.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 304 | +0.013 | +4.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 231 | -0.011 | +0.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 231 | -0.011 | +0.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 891 | -0.070 | -41.98€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 416 | -0.110 | -76.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 320 | -0.140 | -64.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 316 | -0.031 | +25.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 225 | -0.020 | +27.85€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 159 | -0.040 | +9.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 128 | -0.046 | +5.17€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 673 | -0.082 | -31.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1113 | -0.208 | -68.85€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 435 | -0.209 | -41.94€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 378 | -0.213 | -41.71€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 380 | -0.212 | -33.75€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 332 | -0.225 | -40.76€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 298 | -0.197 | +6.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 277 | -0.192 | +4.72€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 987 | -0.212 | -77.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 444 | +0.392 | +413.41€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 63 | +0.131 | +49.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 63 | +0.131 | +49.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 107 | +0.362 | +89.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 107 | +0.362 | +89.61€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 274 | +0.460 | +274.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 274 | +0.460 | +274.37€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 444 | +0.392 | +413.41€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 718 | +0.028 | +33.93€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 718 | +0.028 | +33.93€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 301 | +0.021 | +2.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 301 | +0.021 | +2.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 285 | +0.051 | +31.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 285 | +0.051 | +31.95€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3438 | -0.022 | -135.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3438 | -0.022 | -135.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1055 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1055 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 590 | -0.027 | -26.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 590 | -0.027 | -26.08€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 165 | -0.039 | -13.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 165 | -0.039 | -13.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1628 | -0.018 | -58.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1628 | -0.018 | -58.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 101 | -0.063 | -11.04€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 101 | -0.063 | -11.04€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 58 | -0.033 | -5.97€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 58 | -0.033 | -5.97€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10781 | +0.017 | +92.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10781 | +0.017 | +92.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2748 | +0.021 | +28.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2748 | +0.021 | +28.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2806 | +0.018 | +35.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2806 | +0.018 | +35.63€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2339 | +0.019 | +28.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2339 | +0.019 | +28.59€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9809 | +0.013 | -52.97€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9809 | +0.013 | -52.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3984 | +0.017 | -11.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3984 | +0.017 | -11.64€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3613 | +0.011 | -26.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3613 | +0.011 | -26.65€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2212 | +0.009 | -14.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2212 | +0.009 | -14.68€ | 1 | 0 |
| ✅ UPDOWN_GBM | 75321 | +0.053 | +6634.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18723 | +0.083 | +4103.69€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2421 | +0.004 | +22.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 49504 | +0.050 | +2421.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4410 | +0.008 | +86.00€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16103 | +0.056 | +1380.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2414 | +0.089 | +587.11€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 647 | +0.010 | +10.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 10981 | +0.061 | +723.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1966 | +0.004 | +56.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 95 | -0.067 | +3.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8326 | +0.068 | +879.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6693 | +0.051 | +270.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17230 | +0.044 | +1110.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4424 | +0.065 | +640.61€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 631 | +0.005 | +15.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10541 | +0.044 | +430.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1546 | +0.013 | +20.55€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 88 | -0.100 | +3.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16485 | +0.032 | +792.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4624 | +0.034 | +375.40€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 600 | -0.008 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10285 | +0.037 | +413.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 898 | +0.009 | +8.85€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 78 | -0.125 | -4.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10324 | +0.064 | +1396.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4130 | +0.101 | +1191.53€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5806 | +0.041 | +205.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 261 | -0.097 | +2.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 825 | +0.366 | +304.38€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 825 | +0.366 | +304.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 429 | +0.365 | +150.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 429 | +0.365 | +150.53€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 396 | +0.364 | +153.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 396 | +0.364 | +153.85€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19569 | -0.025 | +4603.46€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19569 | -0.025 | +4603.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3467 | -0.111 | +137.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3467 | -0.111 | +137.92€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2363 | +0.218 | +1541.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2363 | +0.218 | +1541.57€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5576 | -0.066 | +663.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5576 | -0.066 | +663.32€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5497 | -0.064 | +987.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5497 | -0.064 | +987.38€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 224 | +0.040 | +9.80€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 224 | +0.040 | +9.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 224 | +0.040 | +9.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 224 | +0.040 | +9.80€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1406 | +0.292 | +1200.43€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1406 | +0.292 | +1200.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 756 | +0.289 | +612.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 756 | +0.289 | +612.02€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 650 | +0.294 | +588.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 650 | +0.294 | +588.41€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 814 | -0.112 | -82.65€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 814 | -0.112 | -82.65€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 248 | -0.080 | -18.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 248 | -0.080 | -18.10€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 87 | -0.163 | -9.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 87 | -0.163 | -9.15€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 96 | -0.184 | -6.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 96 | -0.184 | -6.04€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3567 | +0.302 | +1685.08€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1311 | +0.253 | +155.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1371 | +0.297 | +613.35€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 885 | +0.379 | +916.26€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.022 n=932 — no justifica filtro, seguir monitorizando
  - _Datos_: n=932 IC=+0.022 PNL=+35.81€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 711 celda(s) pasan gate riguroso completo de 2672 evaluadas (n>=40) y 3715 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4620 IC=+0.034 PNL=+375.47€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1371/15 IC=+0.297 PNL=+613.35€ | BTC: n=1311/15 IC=+0.253 PNL=+155.47€ | SOL: n=885/15 IC=+0.379 PNL=+916.26€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.138 n=775/60 | contraria IC=+0.190 n=800 | gap=-0.051 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=460, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1545/40 IC=+0.013 PNL=+21.06€ | BTC#60min: n=1964/40 IC=+0.004 PNL=+56.59€ | SOL#60min: n=897/40 IC=+0.008 PNL=+8.35€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=546300 | tras_1loss IC=+0.095 n=415658 | tras_2loss IC=+0.064 n=168461/40 | gap=-0.016 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.08 con n=731 PNL=+573.27€
  - _Datos_: n=731 IC=+0.207 PNL=+573.27€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=812 PNL=+466.16€
  - _Datos_: n=812 IC=+0.171 PNL=+466.16€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.08 con n=61 PNL=+35.11€
  - _Datos_: n=61 IC=+0.182 PNL=+35.11€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2911 PNL=+1614.92€
  - _Datos_: n=2911 IC=+0.332 PNL=+1614.92€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=669 IC=+0.075 PNL=+79.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=669 IC=+0.075 PNL=+79.22€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=84 IC=+0.198 PNL=+61.01€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=84 IC=+0.198 PNL=+61.01€

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
  - _Estado_: n=2967 IC=+0.009 PNL=+7.34€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2967 IC=+0.009 PNL=+7.34€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1439 IC=+0.007 PNL=+78.67€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1439 IC=+0.007 PNL=+78.67€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=932 IC=+0.022 PNL=+35.81€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=932 IC=+0.022 PNL=+35.81€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.1 con n=4664 PNL=+2953.15€
  - _Datos_: n=4664 IC=+0.179 PNL=+2953.15€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2409 IC=+0.090 PNL=+589.82€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2409 IC=+0.090 PNL=+589.82€

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
  - _Estado_: n=956 IC=+0.036 PNL=+92.92€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=956 IC=+0.036 PNL=+92.92€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=115 IC=+0.021 PNL=+2.50€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=115 IC=+0.021 PNL=+2.50€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.276 n=163) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=163 IC=+0.276 PNL=+158.78€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.02 con n=959 PNL=+402.12€
  - _Datos_: n=959 IC=+0.125 PNL=+402.12€

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
  - _Estado_: n=29460 IC=+0.074 PNL=+4282.78€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=29460 IC=+0.074 PNL=+4282.78€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.144 < -0.1 con n=470 PNL=+49.94€
  - _Datos_: n=470 IC=-0.144 PNL=+49.94€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3060 IC=+0.066 PNL=+373.36€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3060 IC=+0.066 PNL=+373.36€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=139 IC=-0.082 PNL=+8.08€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=139 IC=-0.082 PNL=+8.08€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=786 PNL=+215.06€
  - _Datos_: n=786 IC=+0.113 PNL=+215.06€

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
  - _Estado_: n=31354 IC=-0.134 PNL=+2510.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=31354 IC=-0.134 PNL=+2510.72€

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
  - _Estado_: n=3137 IC=+0.133 PNL=+1902.88€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3137 IC=+0.133 PNL=+1902.88€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7800 IC=+0.048 PNL=+591.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7800 IC=+0.048 PNL=+591.17€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=3421 PNL=+1866.76€
  - _Datos_: n=3421 IC=+0.095 PNL=+1866.76€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=3244 PNL=-256.04€
  - _Datos_: n=3244 IC=-0.222 PNL=-256.04€

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
  - _Estado_: n=66 IC=+0.000 PNL=+4.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=66 IC=+0.000 PNL=+4.12€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1695) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1695 IC=+0.101 PNL=+372.42€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=565) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=565 IC=+0.415 PNL=+818.04€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=13785 IC=+0.185 PNL=-1424.69€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=13785 IC=+0.185 PNL=-1424.69€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.1 con n=227 PNL=+147.67€
  - _Datos_: n=227 IC=+0.216 PNL=+147.67€
