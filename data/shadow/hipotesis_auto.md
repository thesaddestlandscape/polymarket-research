# Hipótesis automáticas — 2026-11-05 00:13 UTC
_Generado por shadow_postmortem.py sobre 1196597 resoluciones (PNL=+163042.65€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=686)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.201 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.183 (n=314)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.6154` → IC=+0.249 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6154 (IC base=+0.132)

- **PATRÓN** `banda_z` > `8.7` → IC=+0.207 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.7 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.132 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=1017)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3352.3155` → IC=+0.132 (n=623)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3352.3155 (IC base=+0.132)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.293 (n=167)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=484)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.200 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.135)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.186 (n=272)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 66.0 (IC base=+0.135)

- **PATRÓN** `banda_hit_calibrado` > `0.8135` → IC=+0.271 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8135 (IC base=+0.135)

- **PATRÓN** `banda_z` > `9.021` → IC=+0.208 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.021 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=917)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3075.5292` → IC=+0.136 (n=717)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3075.5292 (IC base=+0.135)

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
- **FILTRO** `ballenas_wallet_edge_medio` < `2.833` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballenas_wallet_edge_medio` < 2.833
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.495 (IC base=+0.162)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.162)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.162)

- **PATRÓN** `banda_hit_calibrado` > `0.6068` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6068 (IC base=+0.162)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.162)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.269 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2453.7234` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2453.7234 (IC base=+0.162)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `134.75` → IC=-0.217 (n=11353)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.75
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=34059)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.19` → IC=-0.253 (n=1177)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.19
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3532)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.11` → IC=-0.309 (n=1172)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.11
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3517)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `118.35` → IC=-0.161 (n=3103)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 118.35
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9309)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.49` → IC=-0.238 (n=3070)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.49
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9211)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.44` → IC=-0.255 (n=2160)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.44
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=6481)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.211 (n=25963)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8505.326` → IC=+0.161 (n=2250)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8505.326 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=22341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=26980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=20487)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=7999)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6747.5472` → IC=+0.148 (n=3088)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 6747.5472 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2663)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `9415.8912` → IC=+0.181 (n=1853)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9415.8912 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2715)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16106.2132` → IC=+0.184 (n=701)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16106.2132 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=2082)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=567)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=1324)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=4735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=4219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.376 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=2246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.345 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=1082)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.257 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=1029)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.257 (n=927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `947.2335` → IC=-0.128 (n=154)

  - _Acción_: SKIP cuando `libro_liquidez` < 947.2335
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=313)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=454)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=1176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.121)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=22317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=18836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=9278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=4303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.176 (n=5055)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4840)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=2917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1936)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.290 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.211)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=4999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5166)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=3893)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.356 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.249)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=3648)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.429 (n=814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4440.8454` → IC=+0.445 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4440.8454 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.459 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `12485.1016` → IC=+0.448 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12485.1016 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4649.4982` → IC=+0.443 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4649.4982 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.399 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.397)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.397)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.397)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=17)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=25132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=29373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.191 (n=4353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=9261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=13260)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=12213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.288 (n=4164)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.193 (n=4317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.200 (n=10298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=6144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.270 (n=4101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.213 (n=4163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=4281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=4180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=4813)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=10429)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=10793)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.36` → IC=+0.139 (n=9672)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.36 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5092)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4884)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=6366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.63` → IC=+0.144 (n=4809)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.63 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=5337)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=5909)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.23` → IC=+0.138 (n=4846)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.23 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.368 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=928)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.339)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.388 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.371 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.339)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.465 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.448)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.449 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.404)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=91)

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

- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=91)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4747` → IC=+0.139 (n=16430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4747 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=16641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=11410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3735` → IC=+0.165 (n=16431)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3735 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8011` → IC=+0.282 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8011 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.551` → IC=+0.185 (n=8212)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.551 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6963` → IC=+0.266 (n=4352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6963 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3041` → IC=+0.246 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3041 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.7388` → IC=+0.233 (n=3927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7388 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=8247)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4697.5865` → IC=+0.146 (n=5477)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4697.5865 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.122 (n=10206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.006 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.6798` → IC=+0.132 (n=23194)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6798 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.6164` → IC=+0.191 (n=1437)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6164 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1626` → IC=+0.189 (n=7880)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1626 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.192 (n=5491)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8622 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.228 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `1.4564` → IC=+0.205 (n=14001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4564 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.226 (n=13895)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.080)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3654` → IC=+0.211 (n=3520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3654 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.280 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.566` → IC=+0.280 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.566 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.263 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.212 (n=3370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=3852)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2062.95` → IC=+0.211 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2062.95 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.223 (n=3182)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.242 (n=3066)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.242 (n=1392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.273 (n=1022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=1140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.283 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0942` → IC=+0.245 (n=2769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0942 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.253 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.247 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.8597` → IC=+0.244 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8597 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1772.5987` → IC=+0.249 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1772.5987 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.230 (n=1958)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0813` → IC=+0.259 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0813 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3071)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2079)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9138` → IC=+0.263 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9138 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1882` → IC=+0.233 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1882 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.5335` → IC=+0.227 (n=3173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5335 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.011` → IC=+0.260 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.011 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2262` → IC=+0.224 (n=2932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2262 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.228 (n=2932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.272 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4278` → IC=+0.252 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4278 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.151 (n=3094)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0062 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.152 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=2199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.7115` → IC=+0.167 (n=3094)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7115 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1378` → IC=+0.144 (n=2941)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1378 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.727` → IC=+0.131 (n=499)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 10.727 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.009` → IC=+0.134 (n=2836)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.009 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.135 (n=3093)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2032 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.150 (n=1129)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.1366` → IC=+0.136 (n=2612)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1366 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4012)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.166 (n=1290)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 205.0 (IC base=+0.128)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.217 (n=1240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.09` → IC=+0.276 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.09 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.197 (n=3323)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.218 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7278` → IC=+0.211 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7278 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=4475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1389.8992` → IC=+0.197 (n=3714)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1389.8992 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.224 (n=2985)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.177` → IC=+0.235 (n=1491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.177 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=1537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0417` → IC=+0.270 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0417 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.261 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.255 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.761` → IC=+0.217 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.761 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.226 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1919.2584` → IC=+0.223 (n=1537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.2584 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.222 (n=3216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.161 (n=187)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=4473)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.235 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.339 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.7764` → IC=+0.334 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7764 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.078` → IC=+0.202 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.078 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `1.2478` → IC=+0.357 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2478 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.334 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.334 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.340 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.2782` → IC=+0.340 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2782 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.338 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.0921` → IC=+0.181 (n=1166)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.0921 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.744` → IC=+0.159 (n=300)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.744 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.1401` → IC=+0.145 (n=2026)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1401 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8345` → IC=+0.157 (n=1459)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8345 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.202 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.7746` → IC=+0.149 (n=1404)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7746 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.1484` → IC=+0.156 (n=955)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1484 (IC base=+0.046)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.187 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=704)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.178 (n=209)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=627)

- **FILTRO** `ibs_20min` > `0.2051` → IC=-0.132 (n=4390)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2051
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=2165)

- **FILTRO** `sigma_ewma_delta_pct` > `8.401` → IC=-0.225 (n=708)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.401
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=5847)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.176 (n=285)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7547 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.6236` → IC=+0.263 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6236 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.045` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 5.045 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.284 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.4484` → IC=+0.281 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4484 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.266 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.272 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.017)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.155 (n=2165)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2051 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.2171` → IC=+0.289 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2171 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.310 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.299 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.1472` → IC=+0.304 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1472 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7786` → IC=-0.154 (n=3289)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7786
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=1695)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.167 (n=1126)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3858)

- **FILTRO** `ibs_20min` > `0.7457` → IC=-0.199 (n=1745)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7457
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5237)

- **PATRÓN** `ibs_20min` > `0.7786` → IC=+0.121 (n=1695)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.7786 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `1.0473` → IC=+0.357 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0473 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.2511` → IC=+0.304 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2511 (IC base=-0.060)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.318 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.060)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.305 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=-0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.305 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.5757` → IC=+0.307 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5757 (IC base=-0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.5237` → IC=+0.318 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5237 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `1.0548` → IC=+0.276 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0548 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` < `0.2224` → IC=+0.265 (n=1961)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2224 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.274 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `1.0635` → IC=+0.284 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0635 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.1702` → IC=+0.284 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1702 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `2.1758` → IC=+0.267 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1758 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.271 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.200 (n=7104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.8732` → IC=+0.288 (n=9654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8732 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.9517` → IC=+0.302 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9517 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.528` → IC=+0.168 (n=9524)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.528 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `1.1762` → IC=+0.268 (n=7818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1762 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.276 (n=6986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.290 (n=2347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `2.651` → IC=+0.283 (n=4133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.651 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.307 (n=12005)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.090)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.157 (n=6840)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.01 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.6442` → IC=+0.151 (n=20518)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6442 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.2561` → IC=+0.276 (n=6766)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2561 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.281 (n=2943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.1918` → IC=+0.275 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1918 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.322 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `1.5759` → IC=+0.300 (n=4318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5759 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `2.2801` → IC=+0.296 (n=4449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2801 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.307 (n=9760)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.080)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8018` → IC=-0.121 (n=3821)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8018
  - _Potencial_: sin este filtro IC_bueno=+0.295 (n=1969)

- **FILTRO** `ibs_20min` > `0.7209` → IC=-0.231 (n=1267)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7209
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3803)

- **FILTRO** `sigma_ewma_delta_pct` > `4.182` → IC=-0.229 (n=1093)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.182
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3977)

- **PATRÓN** `ibs_20min` > `0.9341` → IC=+0.337 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9341 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.057` → IC=+0.190 (n=1936)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.057 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2286` → IC=+0.326 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2286 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4469` → IC=+0.278 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4469 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2415` → IC=+0.298 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2415 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.315 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.1724` → IC=+0.160 (n=1268)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1724 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.404 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.425 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.401 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1728` → IC=+0.221 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1728 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.206 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.210 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.246 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.230 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `266.0` → IC=+0.240 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 266.0 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.1296` → IC=+0.250 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1296 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.245 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.309 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5292` → IC=+0.250 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5292 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1537` → IC=+0.259 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1537 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.258 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 213.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.319 (n=2010)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.290 (n=3022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.632` → IC=+0.301 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.632 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.293 (n=2643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.287 (n=2926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.291 (n=3603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2038.0004` → IC=+0.294 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.0004 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.305 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.321 (n=2410)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.1777` → IC=+0.320 (n=1188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1777 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=1038)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.304 (n=1217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.0132` → IC=+0.304 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0132 (IC base=+0.302)

- **PATRÓN** `ibs_20min` > `0.1385` → IC=+0.312 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1385 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.319` → IC=+0.311 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.319 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` < `0.1986` → IC=+0.303 (n=2654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1986 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.307 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `1.7459` → IC=+0.302 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7459 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.7258` → IC=+0.314 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7258 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.305 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `1920.3052` → IC=+0.313 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1920.3052 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.309 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.302)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7283` → IC=-0.182 (n=1326)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7283
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3980)

- **PATRÓN** `ibs_20min` > `0.8542` → IC=+0.167 (n=1297)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8542 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.232 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.3648` → IC=+0.234 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3648 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.1635` → IC=+0.233 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1635 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6711` → IC=+0.233 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6711 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.234 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.238 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4586` → IC=+0.236 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4586 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.255 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7363` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7363 (IC base=+0.004)

- **PATRÓN** `dist_vwap_pct` < `0.3517` → IC=+0.245 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3517 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `1.0163` → IC=+0.253 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0163 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.309 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.7888` → IC=+0.282 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7888 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.267 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.277 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7455` → IC=-0.241 (n=2205)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7455
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2205)

- **FILTRO** `ibs_20min` > `0.6271` → IC=-0.232 (n=1057)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6271
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=3173)

- **FILTRO** `sigma_ewma_delta_pct` > `8.312` → IC=-0.253 (n=484)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.312
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=3746)

- **PATRÓN** `ibs_20min` > `0.7455` → IC=+0.313 (n=2205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7455 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.2184` → IC=+0.348 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2184 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.481` → IC=+0.154 (n=1779)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.481 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8458` → IC=+0.342 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8458 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.6974` → IC=+0.336 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6974 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1582` → IC=+0.336 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1582 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.361 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.4333` → IC=+0.363 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4333 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.355 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6271` → IC=+0.147 (n=3173)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.6271 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.3047` → IC=+0.262 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3047 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.034` → IC=+0.126 (n=2983)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.034 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.288 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.279 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `1.8067` → IC=+0.277 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8067 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.283 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.052)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=2025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=2290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.669` → IC=+0.345 (n=2264)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.669 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.339 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.814` → IC=+0.332 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.814 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `0.8706` → IC=+0.331 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8706 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.345 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.43` → IC=+0.325 (n=2178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.43 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `2969.2175` → IC=+0.319 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2969.2175 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.343 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.346 (n=1599)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.322 (n=1220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.3806` → IC=+0.334 (n=2398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3806 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` < `0.24` → IC=+0.320 (n=2299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.24 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.330 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.7201` → IC=+0.321 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7201 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2085` → IC=+0.343 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2085 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.361 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.325 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1376` → IC=+0.317 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1376 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.227 (n=5308)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.1229` → IC=+0.193 (n=7010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1229 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=16542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.5407` → IC=+0.233 (n=15917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5407 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1641` → IC=+0.206 (n=6236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1641 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.911` → IC=+0.260 (n=3119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.911 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.157 (n=10598)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1862 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.6259` → IC=+0.156 (n=10596)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6259 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.209 (n=2307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.192 (n=5157)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.196 (n=14828)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 89.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.191 (n=6810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0057 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.221 (n=5159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5217` → IC=+0.239 (n=15468)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5217 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1817` → IC=+0.177 (n=11088)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1817 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.682` → IC=+0.194 (n=2464)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.682 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.57` → IC=+0.187 (n=13771)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.57 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1803` → IC=+0.165 (n=11025)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1803 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.215 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6337` → IC=+0.189 (n=4891)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6337 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.197 (n=14428)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 93.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1052` → IC=+0.258 (n=1155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1052 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.8091` → IC=+0.276 (n=2345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8091 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.627` → IC=+0.330 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.627 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.293 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8338` → IC=+0.225 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8338 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.228 (n=2500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=2896)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.258 (n=2102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.306 (n=925)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=2173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4264` → IC=+0.272 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4264 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.259 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.278 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4445` → IC=+0.281 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4445 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7108` → IC=+0.257 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7108 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1513.3152` → IC=+0.264 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1513.3152 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.256 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.199 (n=811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.003 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1598` → IC=+0.163 (n=1621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1598 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=2550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.2681` → IC=+0.209 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2681 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1867` → IC=+0.213 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1867 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.763` → IC=+0.208 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.763 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6949` → IC=+0.144 (n=1070)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6949 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0616` → IC=+0.139 (n=1102)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0616 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.181 (n=377)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5013` → IC=+0.143 (n=1051)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5013 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.148 (n=797)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `403.0` → IC=+0.139 (n=2355)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 403.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.172 (n=2557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0063 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2376` → IC=+0.169 (n=2247)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2376 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=1227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6102` → IC=+0.206 (n=2554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6102 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1462` → IC=+0.172 (n=2642)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1462 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.071` → IC=+0.180 (n=479)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.071 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.05` → IC=+0.148 (n=2235)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.05 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.160 (n=2554)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2024 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.094` → IC=+0.149 (n=2212)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.094 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.1286` → IC=+0.151 (n=2138)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1286 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.184 (n=1041)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 213.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.236 (n=1227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.3961` → IC=+0.225 (n=2373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3961 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.173` → IC=+0.305 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.173 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3549` → IC=+0.238 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3549 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7274` → IC=+0.227 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7274 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1925.8986` → IC=+0.222 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1925.8986 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.246 (n=2062)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4171` → IC=+0.262 (n=2062)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4171 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0313` → IC=+0.291 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0313 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.280 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3584` → IC=+0.285 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3584 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.241 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1766` → IC=+0.248 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1766 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1915.1084` → IC=+0.248 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1084 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.244 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.198 (n=1150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0042 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.193 (n=871)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.2661` → IC=+0.199 (n=2609)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.2661 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1416` → IC=+0.187 (n=1559)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1416 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.42` → IC=+0.202 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.42 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8476` → IC=+0.142 (n=1740)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8476 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1857` → IC=+0.141 (n=870)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1857 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.182 (n=388)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.5272` → IC=+0.160 (n=851)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5272 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6915.1659` → IC=+0.199 (n=1183)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6915.1659 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.143 (n=2546)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 130.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.167 (n=2425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0066 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.145 (n=2752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6735` → IC=+0.187 (n=2752)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6735 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1602` → IC=+0.156 (n=2745)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1602 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.35` → IC=+0.146 (n=664)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.35 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.851` → IC=+0.156 (n=1835)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.851 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.174 (n=412)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.132 (n=1736)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4194` → IC=+0.128 (n=2603)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4194 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6256.4769` → IC=+0.189 (n=1248)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 6256.4769 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.149 (n=883)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 51.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.167 (n=1318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0111 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.210 (n=2904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.2015` → IC=+0.190 (n=1604)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2015 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.124` → IC=+0.292 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.124 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1755` → IC=+0.133 (n=2906)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1755 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.124 (n=2596)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7044 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.130 (n=2960)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5419` → IC=+0.136 (n=1241)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5419 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=3031)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2664.3504` → IC=+0.201 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2664.3504 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.148 (n=1192)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 20.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.143 (n=3023)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0117 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.163 (n=1008)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6442` → IC=+0.219 (n=3022)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6442 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2128` → IC=+0.145 (n=2925)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2128 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.313` → IC=+0.138 (n=2669)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.313 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.129 (n=3022)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1756 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1611` → IC=+0.123 (n=2961)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1611 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.131 (n=415)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5362` → IC=+0.130 (n=1253)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5362 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4294` → IC=+0.126 (n=949)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4294 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2536.4746` → IC=+0.185 (n=1370)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2536.4746 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.124 (n=2848)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.250 (n=2371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.241 (n=1168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.259 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.235 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8292` → IC=+0.227 (n=2719)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8292 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.53` → IC=+0.261 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.53 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6249` → IC=+0.234 (n=2655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6249 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2349` → IC=+0.270 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2349 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8145` → IC=+0.235 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8145 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2558.3544` → IC=+0.233 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2558.3544 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.239 (n=1188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.251 (n=1226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.262 (n=901)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.254 (n=1329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1099` → IC=+0.255 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1099 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.205` → IC=+0.267 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.205 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.243 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.641` → IC=+0.241 (n=2698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.641 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.287 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.5331` → IC=+0.235 (n=2535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5331 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.240 (n=2535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.208 (n=1363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.1319` → IC=+0.181 (n=1789)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1319 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=3639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4437` → IC=+0.210 (n=3633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4437 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.8265` → IC=+0.191 (n=667)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8265 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.558` → IC=+0.197 (n=1720)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.558 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.863` → IC=+0.181 (n=2465)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.863 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.1931` → IC=+0.172 (n=1232)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1931 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.173 (n=1637)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.534` → IC=+0.172 (n=1743)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.534 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=4563)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2639.7171` → IC=+0.177 (n=3633)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2639.7171 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.1972` → IC=+0.195 (n=1917)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1972 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.130 (n=1858)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 26.0 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.196 (n=1106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.006 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.1011` → IC=+0.228 (n=487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1011 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.212 (n=1002)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.2177` → IC=+0.210 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2177 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.3106` → IC=+0.215 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3106 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.958` → IC=+0.202 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.958 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.399` → IC=+0.178 (n=1163)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.399 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.192 (n=739)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8803 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` < `0.15` → IC=+0.181 (n=1163)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.15 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.188 (n=437)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `2.1871` → IC=+0.191 (n=954)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.1871 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `15859.8442` → IC=+0.194 (n=501)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 15859.8442 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.169 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0031 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.1954` → IC=+0.197 (n=589)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1954 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.141 (n=349)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.175 (n=576)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 160.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.244 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.2096` → IC=+0.188 (n=841)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2096 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.8164` → IC=+0.274 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8164 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8295` → IC=+0.197 (n=219)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8295 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2139` → IC=+0.183 (n=1117)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2139 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.215 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.196 (n=841)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8344 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.1591` → IC=+0.182 (n=420)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1591 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.209 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5271` → IC=+0.185 (n=547)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5271 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.7866` → IC=+0.194 (n=828)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7866 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.1016` → IC=+0.187 (n=413)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1016 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `5143.3099` → IC=+0.130 (n=825)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 5143.3099 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.190 (n=998)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4667 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.9779` → IC=+0.193 (n=174)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.9779 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.004` → IC=+0.237 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.004 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.0509` → IC=+0.140 (n=878)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0509 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.135 (n=891)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.704 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2257` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2257 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.145 (n=322)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.7996` → IC=+0.127 (n=642)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.7996 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=1053)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2712.3504` → IC=+0.174 (n=452)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2712.3504 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.2075` → IC=+0.218 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2075 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2844.564` → IC=+0.158 (n=358)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2844.564 (IC base=+0.057)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.233 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.73` → IC=+0.216 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.73 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.2225` → IC=+0.210 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2225 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `1.1644` → IC=+0.184 (n=371)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 1.1644 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.692` → IC=+0.207 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.692 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `1.1751` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1751 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.1069` → IC=+0.195 (n=296)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1069 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.8284` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8284 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.5422` → IC=+0.196 (n=274)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.5422 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.191 (n=370)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2525.2851` → IC=+0.216 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2525.2851 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.217 (n=164)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2786` → IC=+0.156 (n=242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2786 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.5094` → IC=+0.167 (n=319)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.5094 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `1.1471` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1471 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.232` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.232 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.234` → IC=+0.146 (n=323)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.234 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.872` → IC=+0.184 (n=242)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.872 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.113` → IC=+0.156 (n=329)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.113 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.537` → IC=+0.203 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.537 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.6826` → IC=+0.170 (n=116)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.6826 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.157 (n=345)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.233 (n=6935)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=21706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.229 (n=20788)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4333 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8954` → IC=+0.215 (n=2556)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8954 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.021` → IC=+0.254 (n=5095)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.021 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.161 (n=13977)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2177 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2416` → IC=+0.208 (n=3743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2416 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6196` → IC=+0.194 (n=6759)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6196 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.203 (n=19406)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.198 (n=8372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0059 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.200 (n=6338)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4818` → IC=+0.196 (n=19000)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4818 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=7113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.243 (n=19000)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5915 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.1797` → IC=+0.175 (n=11789)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1797 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.201 (n=2573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.435` → IC=+0.197 (n=18510)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 3.435 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.6326` → IC=+0.176 (n=4257)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6326 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.250 (n=2597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.8644` → IC=+0.199 (n=12089)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8644 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.208 (n=17906)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.193)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8625` → IC=+0.302 (n=2229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8625 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.638` → IC=+0.339 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.638 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.296 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2784` → IC=+0.241 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2784 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.250 (n=3646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2061.02` → IC=+0.235 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.02 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.258 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.268 (n=2955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1231` → IC=+0.291 (n=1297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1231 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.5398` → IC=+0.285 (n=2949)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5398 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.268 (n=2678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.288 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.562` → IC=+0.268 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.562 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.653` → IC=+0.274 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.653 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.267 (n=3380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1772.645` → IC=+0.275 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1772.645 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.274 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.179 (n=1135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.148 (n=1136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.2058` → IC=+0.189 (n=3403)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2058 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3231` → IC=+0.198 (n=1152)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3231 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.238` → IC=+0.162 (n=545)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.238 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6361` → IC=+0.157 (n=1135)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6361 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.2334` → IC=+0.139 (n=1135)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.2334 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.182 (n=488)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1552` → IC=+0.143 (n=2938)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1552 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5136` → IC=+0.140 (n=2983)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5136 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `306.0` → IC=+0.149 (n=2190)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 306.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=2892)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.172 (n=963)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=1060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6835` → IC=+0.185 (n=2890)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6835 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1412` → IC=+0.152 (n=2757)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1412 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.043` → IC=+0.144 (n=1374)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.043 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.147 (n=2889)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1917 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2189` → IC=+0.192 (n=533)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2189 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4213` → IC=+0.143 (n=2780)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4213 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.143 (n=1853)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=3750)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.152 (n=900)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 228.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.244 (n=2313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.106` → IC=+0.322 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.106 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.227 (n=3278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7392` → IC=+0.239 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7392 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=4165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1380.7866` → IC=+0.230 (n=3465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1380.7866 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.247 (n=2892)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.262 (n=1445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.056` → IC=+0.303 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.056 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.284` → IC=+0.302 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.284 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.3489` → IC=+0.304 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3489 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.1664` → IC=+0.255 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1664 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1917.34` → IC=+0.251 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.34 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.248 (n=2709)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.242)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.195 (n=1197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0036 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4335` → IC=+0.148 (n=3586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4335 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=3730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8938` → IC=+0.277 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8938 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.168 (n=1682)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1973 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.996` → IC=+0.159 (n=1595)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.996 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.155 (n=2392)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8616 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.187 (n=634)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.157 (n=1544)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1799` → IC=+0.146 (n=1589)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1799 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5436.372` → IC=+0.230 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5436.372 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.149 (n=2320)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 91.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.159 (n=3014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.444` → IC=+0.149 (n=3010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.444 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=1110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.7169` → IC=+0.193 (n=3009)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.7169 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1531` → IC=+0.152 (n=2768)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1531 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.919` → IC=+0.158 (n=448)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.919 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.103` → IC=+0.141 (n=2621)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.103 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6887` → IC=+0.158 (n=1324)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6887 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.209 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.214` → IC=+0.142 (n=2555)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.214 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5362` → IC=+0.148 (n=2593)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5362 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `6316.3219` → IC=+0.213 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6316.3219 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.151 (n=1965)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 93.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.149 (n=1649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0112 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=2576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4324` → IC=+0.193 (n=3629)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4324 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0247` → IC=+0.203 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0247 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.352` → IC=+0.267 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.352 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.126 (n=3629)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2155 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.123 (n=3442)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4818` → IC=+0.122 (n=3545)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4818 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=3791)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2715.618` → IC=+0.241 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2715.618 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.132 (n=1150)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 20.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.156 (n=3016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0107 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.1368` → IC=+0.153 (n=1142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1368 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6622` → IC=+0.217 (n=3426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6622 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.144 (n=3063)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.086` → IC=+0.151 (n=3312)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.086 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6384` → IC=+0.157 (n=1142)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6384 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2252` → IC=+0.174 (n=597)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2252 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.160 (n=1081)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2624.9762` → IC=+0.210 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2624.9762 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.141 (n=3272)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 51.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.259 (n=3002)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.241 (n=3009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.273 (n=3003)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.254 (n=1787)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.248` → IC=+0.286 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.248 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2213` → IC=+0.239 (n=3361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2213 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6439` → IC=+0.241 (n=3360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6439 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.263 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.257 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2961.5054` → IC=+0.244 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2961.5054 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.265 (n=1150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.6203` → IC=+0.241 (n=3447)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6203 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.272 (n=3447)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` < `0.8499` → IC=+0.244 (n=3917)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8499 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.148` → IC=+0.279 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.148 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `1.2141` → IC=+0.262 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2141 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.302 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.242 (n=3239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.239 (n=3198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.240)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5754)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.244 (n=1986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5049` → IC=+0.226 (n=5921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5049 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9348` → IC=+0.256 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9348 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4287` → IC=+0.222 (n=4310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4287 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.574` → IC=+0.226 (n=1939)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.574 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.229 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7088 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8838` → IC=+0.220 (n=2913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8838 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.219 (n=5520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.224 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.4513` → IC=+0.227 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4513 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=4629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `3750.739` → IC=+0.227 (n=3947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3750.739 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.212 (n=4327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=1456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.613` → IC=+0.204 (n=3808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.613 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6595` → IC=+0.209 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6595 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.779` → IC=+0.211 (n=3883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.779 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.205 (n=3630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.201 (n=3985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.200 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5316` → IC=+0.203 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5316 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1857` → IC=+0.207 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1857 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5754)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.212 (n=3747)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 169.0 (IC base=+0.199)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.297 (n=309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.279 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.8328` → IC=+0.278 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8328 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.6679` → IC=+0.277 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6679 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.271 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.8749` → IC=+0.288 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8749 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.276 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.269 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12909.5134` → IC=+0.279 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.5134 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.190 (n=1518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.185 (n=564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.197 (n=668)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.138 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.199 (n=1487)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2377` → IC=+0.185 (n=1518)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2377 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.194 (n=462)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.4929` → IC=+0.182 (n=1510)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.4929 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.180 (n=688)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.188 (n=1473)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 686.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.233 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.5907` → IC=+0.207 (n=903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5907 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.233 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.245 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.463` → IC=+0.248 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.463 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2068` → IC=+0.233 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2068 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.8037` → IC=+0.208 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8037 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.209 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

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

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.219 (n=1621)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.4542` → IC=+0.213 (n=1621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4542 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4996` → IC=+0.217 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4996 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.8568` → IC=+0.207 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8568 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.396` → IC=+0.217 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.396 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.521` → IC=+0.211 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.521 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.212 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.207 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.103` → IC=+0.210 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.103 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4455` → IC=+0.213 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4455 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.242 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.220 (n=1341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.216 (n=907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.75` → IC=+0.203 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.75 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.0909` → IC=+0.205 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0909 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6242` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6242 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.351` → IC=+0.205 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.351 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.6387` → IC=+0.231 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6387 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.227 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.207 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.202 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6506.9218` → IC=+0.206 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6506.9218 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.223 (n=625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.232 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.7666` → IC=+0.239 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7666 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.212` → IC=+0.222 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.212 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.243 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.204 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.202 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `2.1469` → IC=+0.202 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1469 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.4705` → IC=+0.201 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4705 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `4318.6372` → IC=+0.240 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4318.6372 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.201 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.237 (n=459)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.5959` → IC=+0.239 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5959 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.222 (n=641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.250 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.6479` → IC=+0.248 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6479 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.5347` → IC=+0.224 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5347 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.791` → IC=+0.235 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.791 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.0973` → IC=+0.225 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0973 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `1.2815` → IC=+0.228 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2815 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.238 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.5641` → IC=+0.261 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5641 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `3262.8742` → IC=+0.236 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3262.8742 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.259 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.221)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.149 (n=693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0037 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.190 (n=1328)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.75 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.138 (n=1003)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.523` → IC=+0.145 (n=437)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.523 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.0508` → IC=+0.265 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0508 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.1437` → IC=+0.127 (n=368)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1437 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5207` → IC=-0.126 (n=279)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5207
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=567)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.127 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0051 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.5207` → IC=+0.171 (n=567)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.5207 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.165 (n=311)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.0742` → IC=+0.281 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0742 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.051)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6934` → IC=-0.174 (n=142)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6934
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=427)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.125 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0051 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.7791` → IC=+0.223 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7791 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1273` → IC=+0.174 (n=323)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1273 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.677` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.677 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.266 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.547` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.547 (IC base=+0.022)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.205 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9861 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.213` → IC=+0.128 (n=197)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 7.213 (IC base=+0.020)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.154 (n=342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0112 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.1081` → IC=+0.247 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1081 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2779` → IC=+0.123 (n=361)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2779 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.928` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.928 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.0982` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0982 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.546` → IC=+0.121 (n=296)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.546 (IC base=+0.069)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1871` → IC=-0.295 (n=86)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=261)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=334)

- **FILTRO** `libro_liquidez` < `902.1333` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `libro_liquidez` < 902.1333
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=262)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=242)

- **FILTRO** `dist_vwap_pct` > `0.3644` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3644
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=288)

- **FILTRO** `sigma_ewma_delta_pct` > `9.955` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.955
  - _Potencial_: sin este filtro IC_bueno=-0.282 (n=291)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=199)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0059` → IC=-0.241 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=27)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `volumen_regimen` < `0.8856` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8856
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=80)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=73)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=96)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=109)

- **FILTRO** `libro_liquidez` < `5514.5282` → IC=-0.255 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 5514.5282
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5777` → IC=-0.468 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5777
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=88)

- **FILTRO** `volumen_spike_ratio` > `2.191` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.191
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.365 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=87)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.407 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=81)

- **FILTRO** `volumen_spike_ratio` < `1.7371` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7371
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=44)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.307 (n=107)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=108)

- **FILTRO** `volumen_regimen` < `0.8232` → IC=-0.314 (n=41)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8232
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=85)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=97)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.325 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=36)

- **FILTRO** `dist_vwap_pct` > `0.3005` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3005
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2471` → IC=-0.153 (n=252)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2471
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=757)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.220 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.191 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 16.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.176 (n=653)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6757 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.8184` → IC=+0.283 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8184 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.656` → IC=+0.145 (n=359)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.656 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.618` → IC=+0.140 (n=667)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 8.618 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6244 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.2099` → IC=+0.160 (n=610)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2099 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.388` → IC=+0.181 (n=183)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.388 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.818` → IC=+0.155 (n=221)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.818 (IC base=+0.035)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7779` → IC=-0.136 (n=86)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7779
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=175)

- **PATRÓN** `ibs_20min` > `0.899` → IC=+0.132 (n=131)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.899 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2252` → IC=+0.166 (n=354)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.2252 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.376` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 11.376 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.131 (n=215)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.096)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1248` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1248
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=212)

- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.121 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=239)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.144 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0041 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 8.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.798` → IC=+0.153 (n=191)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.798 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.0986` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0986 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.539` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 9.539 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0407` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0407 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `1.1935` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1935 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1248` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1248 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.1273` → IC=+0.157 (n=164)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1273 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=183)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.007)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=119)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=140)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.290 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.272 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.977` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.977 (IC base=-0.070)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=96)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4 (IC base=+0.320)

- **PATRÓN** `elapsed_s` > `225.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 225.0 (IC base=+0.320)

- **PATRÓN** `drift_15min` |x|≤ `1.2521` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2521 (IC base=+0.320)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.368 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.320)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.320)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.320)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `1.234` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.234 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.280 (n=57)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.239)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=96)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4 (IC base=+0.320)

- **PATRÓN** `elapsed_s` > `225.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 225.0 (IC base=+0.320)

- **PATRÓN** `drift_15min` |x|≤ `1.2521` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2521 (IC base=+0.320)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.368 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.320)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.320)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.320)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `1.234` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.234 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.280 (n=57)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.239)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=240)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=240)

- **FILTRO** `libro_liquidez` < `6623.9156` → IC=-0.146 (n=128)

  - _Acción_: SKIP cuando `libro_liquidez` < 6623.9156
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=128)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=608)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=96)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4139.65` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4139.65
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.058)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3887)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=118)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=118)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=272)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1587)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1541)

- **FILTRO** `liq_n` < `3.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `liq_n` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=723)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=440)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=421)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=185)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=956)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=956)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.128 (n=294)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=742)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1140)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1140)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=261)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=261)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=323)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=370)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=293)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=387)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=387)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=232)

- **FILTRO** `libro_liquidez` < `657.5195` → IC=-0.133 (n=137)

  - _Acción_: SKIP cuando `libro_liquidez` < 657.5195
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=280)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=325)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=28)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.126 (n=295)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.51 (IC base=-0.008)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.143 (n=253)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=525)

- **FILTRO** `profundidad_ratio` < `62.1` → IC=-0.124 (n=256)

  - _Acción_: SKIP cuando `profundidad_ratio` < 62.1
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=522)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.129 (n=311)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=333)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.174 (n=133)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=580)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.124 (n=471)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=256)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.145 (n=105)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=331)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.153 (n=272)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=583)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.171 (n=7292)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=23449)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=7795)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=23851)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.183 (n=1412)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=4258)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.148 (n=1875)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=3743)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1481)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `1863.43` → IC=+0.139 (n=1418)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1863.43 (IC base=+0.043)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.124 (n=2886)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1136.335` → IC=+0.152 (n=1911)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1136.335 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.169 (n=1010)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3314)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.179 (n=1108)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3362)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=1391)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4356)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.133 (n=1933)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.9643 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1352.3556` → IC=+0.121 (n=2835)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1352.3556 (IC base=+0.036)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.181 (n=1059)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=3460)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.154 (n=1413)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4290)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2427)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2351)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2939)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3891)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=351)

- **FILTRO** `ballena_activa_n` > `85.0` → IC=-0.186 (n=154)

  - _Acción_: SKIP cuando `ballena_activa_n` > 85.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=302)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=963)

- **FILTRO** `libro_liquidez` < `1813.405` → IC=-0.164 (n=245)

  - _Acción_: SKIP cuando `libro_liquidez` < 1813.405
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=737)

- **FILTRO** `ibs_20min` > `0.8824` → IC=-0.137 (n=576)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8824
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=582)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.211 (n=278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=871)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=234)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=44)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 15.0 (IC base=+0.024)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=20898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=47291)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=16189)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=52000)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.232 (n=17023)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=51166)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=22568)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=45621)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.244 (n=21317)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=64039)

- **FILTRO** `ibs_7min` > `0.284` → IC=-0.184 (n=21329)

  - _Acción_: SKIP cuando `ibs_7min` > 0.284
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=64027)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9155)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=2945)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=9151)

- **FILTRO** `ibs_7min` < `0.7103` → IC=-0.249 (n=3989)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7103
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=8107)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.150 (n=2726)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9370)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.278 (n=3556)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=11206)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.213 (n=3690)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=11072)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.259 (n=2717)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8670)

- **FILTRO** `ibs_7min` < `0.717` → IC=-0.206 (n=2846)

  - _Acción_: SKIP cuando `ibs_7min` < 0.717
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8541)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.194 (n=2827)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8560)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2648)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=8967)

- **FILTRO** `ibs_7min` > `0.2659` → IC=-0.193 (n=2902)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2659
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8713)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=2899)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8716)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=2791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=8783)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.323 (n=2740)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=8834)

- **FILTRO** `ibs_7min` < `0.2883` → IC=-0.249 (n=3819)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2883
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=7755)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.199 (n=2404)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9170)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=3745)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=11871)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.184 (n=3898)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11718)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2713)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8326)

- **FILTRO** `ibs_7min` < `0.7185` → IC=-0.193 (n=2758)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7185
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8281)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.187 (n=2736)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8303)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2643)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8862)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.174 (n=2875)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8630)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.169 (n=2855)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8650)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2568)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8408)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.229 (n=3605)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7371)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.222 (n=2548)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8428)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.196 (n=3990)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=12512)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=3551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=7566)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=2607)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8510)

- **FILTRO** `ibs_7min` < `0.1724` → IC=-0.228 (n=2778)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1724
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8339)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2524)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=8593)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3574)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=11782)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1007)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1293)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=604)

- **FILTRO** `libro_liquidez` < `10485.1399` → IC=-0.156 (n=190)

  - _Acción_: SKIP cuando `libro_liquidez` < 10485.1399
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=572)

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
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=880)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=97)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=669)

- **FILTRO** `libro_liquidez` < `3298.5458` → IC=-0.153 (n=191)

  - _Acción_: SKIP cuando `libro_liquidez` < 3298.5458
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=575)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=391)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.154 (n=642)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `418.1817` → IC=+0.164 (n=471)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 418.1817 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3538.706` → IC=+0.141 (n=641)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3538.706 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.192 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 14.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.154 (n=299)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 375.759 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2527.6661` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2527.6661 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.134 (n=129)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 5.0 (IC base=+0.132)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.153 (n=99)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.194 (n=178)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.147 (n=281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 4.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `506.4056` → IC=+0.174 (n=179)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 506.4056 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 59.0 (IC base=+0.131)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.168 (n=242)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.170 (n=213)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 6100.528 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.122 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 14.0 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=188)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.094)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `pct_vs_K` |x|> `3.42` → IC=-0.194 (n=269)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.42
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=524)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.149 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0044 (IC base=-0.085)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9952` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `T_h` > 87.9952
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=177)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.263 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.040)

- **PATRÓN** `pct_vs_K` |x|≤ `1.632` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.632 (IC base=-0.040)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `251.7955` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.210 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=76)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0109` → IC=-0.234 (n=546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=183)

- **FILTRO** `T_h` > `71.2514` → IC=-0.220 (n=488)

  - _Acción_: SKIP cuando `T_h` > 71.2514
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=241)

- **FILTRO** `sigma_h` < `0.0052` → IC=-0.215 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=469)

- **FILTRO** `pct_vs_K` |x|> `3.1226` → IC=-0.418 (n=156)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1226
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=469)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.204 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=60)

- **FILTRO** `T_h` > `87.9866` → IC=-0.208 (n=118)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=119)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.309 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=114)

- **FILTRO** `T_h` > `143.7867` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `T_h` > 143.7867
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=171)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `T_h` > `148.7378` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `T_h` > 148.7378
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.2046` → IC=-0.387 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2046
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=134)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.357 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=144)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.194 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=144)

- **FILTRO** `T_h` > `57.5396` → IC=-0.229 (n=127)

  - _Acción_: SKIP cuando `T_h` > 57.5396
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=64)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `pct_vs_K` |x|≤ 0.8 (IC base=-0.174)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.292 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=154)

- **FILTRO** `T_h` > `69.913` → IC=-0.216 (n=153)

  - _Acción_: SKIP cuando `T_h` > 69.913
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `sigma_h` > `0.014` → IC=-0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.014
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=92)

- **FILTRO** `sigma_h` < `0.0082` → IC=-0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=105)

- **FILTRO** `T_h` > `33.8406` → IC=-0.264 (n=104)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.341)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.357 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.380 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.341)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.341)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.341)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.341)

- **PATRÓN** `edge` > `0.0997` → IC=+0.438 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.404)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.408 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.404)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.430 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.404)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.443 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.404)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.408 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.404)

- **PATRÓN** `dist_50` > `0.376` → IC=+0.445 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.376 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.416 (n=321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.404)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1021` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1021 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.194)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.269 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.194)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.419 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.403 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.2415` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2415 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.414 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.175` → IC=+0.485 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.175 (IC base=+0.435)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.467 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.435)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.435)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.471 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.435)

- **PATRÓN** `edge` > `0.2005` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.473 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.462)

- **PATRÓN** `T_h` < `0.8229` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8229 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.492 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=373)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=458)

- **PATRÓN** `streak_estiramiento` < `0.2918` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.2918 (IC base=+0.026)

- **PATRÓN** `streak_estiramiento` < `0.5509` → IC=+0.182 (n=209)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.5509 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.129 (n=235)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 31.0 (IC base=+0.059)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.061)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4224` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4224
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=121)

- **PATRÓN** `streak_estiramiento` < `0.3028` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.3028 (IC base=+0.027)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `streak_estiramiento` < `0.555` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `streak_estiramiento` < 0.555 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.167 (n=142)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 31.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2555.3558` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2555.3558 (IC base=+0.096)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=100)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=109)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=36)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=35)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.045)

- **PATRÓN** `volumen_racha` < `16919.513` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 16919.513 (IC base=+0.045)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1054)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1337)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1293)

### STRUCT_NO_15M
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4600)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2655)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.188 (n=2092)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2145` → IC=+0.168 (n=4755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2145 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3545` → IC=+0.162 (n=4407)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3545 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.164 (n=4407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.220 (n=4757)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1336` → IC=+0.145 (n=2291)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1336 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.7001` → IC=+0.140 (n=4604)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.7001 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.624` → IC=+0.263 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.624 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=2850)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `4758.5399` → IC=+0.176 (n=1585)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 4758.5399 (IC base=+0.154)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1837)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.223 (n=741)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.256 (n=248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2667` → IC=+0.223 (n=247)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2667 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.224 (n=772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7103` → IC=+0.278 (n=740)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7103 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3775` → IC=+0.219 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3775 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.5214` → IC=+0.206 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5214 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.716` → IC=+0.314 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.716 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15928.6386` → IC=+0.227 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15928.6386 (IC base=+0.202)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` > `0.479` → IC=-0.164 (n=257)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=772)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.156 (n=904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0069 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.151 (n=603)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1424` → IC=+0.138 (n=603)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.1424 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1286` → IC=+0.143 (n=365)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1286 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.223 (n=904)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.151 (n=568)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.6301` → IC=+0.138 (n=1028)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.6301 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.997` → IC=+0.290 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.997 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5812.1498` → IC=+0.165 (n=410)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5812.1498 (IC base=+0.136)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8649` → IC=+0.183 (n=415)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` > 0.8649 (IC base=+0.065)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0249` → IC=+0.177 (n=1122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0249 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.013` → IC=+0.186 (n=1122)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.013 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.0678` → IC=+0.215 (n=374)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0678 (IC base=+0.175)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3542` → IC=+0.204 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3542 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=1034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.183 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 14.0 (IC base=+0.175)

- **PATRÓN** `ibs_15` > `0.4651` → IC=+0.243 (n=1125)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4651 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.196 (n=640)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.942` → IC=+0.224 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.942 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2948.5018` → IC=+0.214 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2948.5018 (IC base=+0.175)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.161 (n=915)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1111 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.384 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.379 (n=477)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1386` → IC=+0.382 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1386 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.394 (n=716)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.384 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.399 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9974.3192` → IC=+0.381 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9974.3192 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.369 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1584` → IC=+0.371 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1584 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1464` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1464 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.386 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.244` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.244 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9210.2084` → IC=+0.375 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9210.2084 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.402 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.370 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.376 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.364 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.376 (n=321)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.381 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.373 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8123` → IC=+0.401 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8123 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.376 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.6628` → IC=+0.367 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6628 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.534` → IC=+0.408 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.534 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4067.0691` → IC=+0.385 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4067.0691 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.225 (n=1720)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=3341)

- **FILTRO** `drift_15min` |x|> `0.9086` → IC=-0.140 (n=1264)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9086
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3796)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=2085)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2976)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1398` → IC=+0.223 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1398 (IC base=-0.077)

- **PATRÓN** `ibs_15` > `0.6288` → IC=+0.280 (n=1167)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6288 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.201 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` < `0.5699` → IC=+0.203 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5699 (IC base=-0.077)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2355` → IC=+0.268 (n=1518)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2355 (IC base=-0.006)

- **PATRÓN** `ibs_15` < `0.3677` → IC=+0.284 (n=4554)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3677 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` > `0.6614` → IC=+0.280 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6614 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` < `0.1666` → IC=+0.249 (n=3335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1666 (IC base=-0.006)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.221 (n=2386)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=797)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.215 (n=795)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2388)

- **FILTRO** `sigma_ewma_delta_pct` > `18.835` → IC=-0.258 (n=577)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.835
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=2606)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.148 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0034 (IC base=+0.075)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.328 (n=399)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.279 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.4958` → IC=+0.286 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4958 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.8` → IC=+0.144 (n=209)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 22.8 (IC base=+0.075)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.240 (n=71)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0839` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0839 (IC base=-0.185)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.322 (n=71)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.185)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.185)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.185)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=763)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.158 (n=586)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.182 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.202 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.243 (n=585)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.115` → IC=+0.151 (n=365)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.115 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.153 (n=453)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=763)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `5052.7931` → IC=+0.156 (n=390)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5052.7931 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.262 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1041` → IC=+0.246 (n=573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1041 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.778` → IC=+0.256 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.778 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2173` → IC=+0.263 (n=778)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2173 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.244 (n=643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3771` → IC=+0.274 (n=1717)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3771 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.6193` → IC=+0.269 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6193 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.364` → IC=+0.246 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.364 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.260 (n=394)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=770)

- **FILTRO** `drift_15min` |x|> `0.9084` → IC=-0.284 (n=290)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9084
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=874)

- **FILTRO** `sigma_ewma_delta_pct` > `6.283` → IC=-0.206 (n=270)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.283
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=894)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.194)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.194)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 29.0 (IC base=-0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0652` → IC=+0.232 (n=778)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0652 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.3902` → IC=+0.297 (n=778)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3902 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6848` → IC=+0.232 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6848 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1985` → IC=+0.248 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1985 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1499` → IC=-0.230 (n=353)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1499
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=1060)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.242 (n=691)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=722)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.213)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.117` → IC=+0.271 (n=693)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.117 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1189` → IC=+0.292 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1189 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.1346` → IC=+0.308 (n=691)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1346 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7641` → IC=+0.336 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7641 (IC base=-0.022)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.146 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0062 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.146 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.375` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.375 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.370 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4193` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4193 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3511.4523` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3511.4523 (IC base=+0.103)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.146 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0062 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.146 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.375` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.375 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.370 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4193` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4193 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3511.4523` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3511.4523 (IC base=+0.103)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.291 (n=1266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.312 (n=558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.290 (n=843)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.294 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.314 (n=1266)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.313 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.387 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `13449.5003` → IC=+0.307 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13449.5003 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.311 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.315 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.279)

- **PATRÓN** `drift_15min` |x|≤ `0.3847` → IC=+0.280 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3847 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.284 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.303 (n=674)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2523` → IC=+0.310 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2523 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.279 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.389 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `15942.3752` → IC=+0.315 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15942.3752 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.308 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.311 (n=395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.296 (n=592)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.338 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.299 (n=540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.323 (n=592)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.310 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` < `0.4611` → IC=+0.292 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4611 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.130 (n=90)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=273)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.159 (n=89)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=274)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.129 (n=246)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=85)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=369)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=367)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.14` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.14
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=156)

- **FILTRO** `sigma_h` < `0.0053` → IC=-0.184 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2127` → IC=-0.233 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2127
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1149` → IC=-0.206 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1149
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=46)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

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
- **PATRÓN** `ratio` < `0.9701` → IC=+0.396 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9701 (IC base=+0.182)

- **PATRÓN** `T_h` > `118.8029` → IC=+0.353 (n=2646)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 118.8029 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0204` → IC=+0.379 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0204 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9936` → IC=+0.145 (n=249)

  - _Acción_: Kelly boost +0.73€ cuando `T_h` > 111.9936 (IC base=+0.143)

- **PATRÓN** `ratio` < `0.979` → IC=+0.320 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.979 (IC base=+0.143)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.314 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0178` → IC=+0.355 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0178 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9849` → IC=+0.422 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.228)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.352 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.320)

- **PATRÓN** `ratio` > `1.0298` → IC=+0.398 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0298 (IC base=+0.320)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.426 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.154 a +0.220 en UPDOWN_GBM#15min (n=4757). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7103 sube el IC de +0.202 a +0.278 en UPDOWN_GBM#BTC#15min (n=740). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.136 a +0.223 en UPDOWN_GBM#ETH#15min (n=904). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8649 sube el IC de +0.065 a +0.183 en UPDOWN_GBM#SOL#15min (n=415). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4651 sube el IC de +0.175 a +0.243 en UPDOWN_GBM#XRP#15min (n=1125). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.067 a +0.161 en UPDOWN_GBM#XRP#15min (n=915). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6288 sube el IC de -0.077 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1167). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3677 sube el IC de -0.006 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4554). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.075 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=399). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.185 a +0.322 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=71). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.150 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=585). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3771 sube el IC de +0.243 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1717). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.194 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3902 sube el IC de -0.031 a +0.297 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=778). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.213 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1346 sube el IC de -0.022 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=691). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.103 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7 (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.103 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.286 a +0.314 en UPDOWN_GBM_IBS_ALTO (n=1266). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.279 a +0.303 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=674). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.293 a +0.323 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=592). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.364 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=716). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8123 sube el IC de +0.365 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2126 | +0.086 | +232.81€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2126 | +0.086 | +232.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1721 | +0.086 | +193.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1721 | +0.086 | +193.52€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 988 | -0.019 | +77.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 988 | -0.019 | +77.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 756 | -0.040 | +52.89€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 756 | -0.040 | +52.89€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 154 | +0.083 | +26.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 154 | +0.083 | +26.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 72 | -0.027 | -4.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 72 | -0.027 | -4.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 45412 | -0.085 | -5624.24€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2680 | +0.056 | -282.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 42732 | -0.094 | -5342.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4709 | -0.111 | -763.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4709 | -0.111 | -763.72€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2680 | +0.056 | -282.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2680 | +0.056 | -282.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4689 | -0.116 | -912.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4689 | -0.116 | -912.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12412 | -0.039 | -1140.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12412 | -0.039 | -1140.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12281 | -0.113 | -1186.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12281 | -0.113 | -1186.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8641 | -0.124 | -1339.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8641 | -0.124 | -1339.43€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 45104 | -0.013 | +3045.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11642 | +0.005 | +1582.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 33462 | -0.019 | +1463.11€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 45104 | -0.013 | +3045.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11642 | +0.005 | +1582.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 33462 | -0.019 | +1463.11€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 175826 | +0.113 | -7183.35€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21000 | +0.181 | -650.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 798 | +0.001 | -75.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 143864 | +0.106 | -6078.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10164 | +0.092 | -378.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 23840 | +0.105 | -1578.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 71 | -0.158 | +15.94€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 23754 | +0.106 | -1582.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 33549 | +0.124 | -567.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5566 | +0.179 | -224.10€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 23822 | +0.120 | -178.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4119 | +0.078 | -142.97€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 23890 | +0.099 | -1704.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 83 | -0.112 | +7.08€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 23792 | +0.100 | -1700.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 37518 | +0.124 | -740.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9530 | +0.178 | -211.39€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 24191 | +0.106 | -463.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3785 | +0.102 | -56.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 33164 | +0.112 | -1527.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5668 | +0.199 | -249.58€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 701 | +0.029 | -21.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 24535 | +0.096 | -1077.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2260 | +0.102 | -178.42€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 23865 | +0.106 | -1065.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 82 | -0.107 | +11.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 23770 | +0.107 | -1076.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 28458 | +0.194 | -1874.38€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 28458 | +0.194 | -1874.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6427 | +0.175 | -594.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6427 | +0.175 | -594.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3982 | +0.198 | -139.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3982 | +0.198 | -139.59€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6339 | +0.177 | -540.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6339 | +0.177 | -540.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5382 | +0.249 | -193.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5382 | +0.249 | -193.43€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6249 | +0.186 | -419.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6249 | +0.186 | -419.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1188 | +0.426 | -42.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1188 | +0.426 | -42.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 485 | +0.441 | -3.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 485 | +0.441 | -3.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 478 | +0.425 | -17.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 478 | +0.425 | -17.08€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 211 | +0.397 | -18.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 211 | +0.397 | -18.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 100244 | +0.201 | -7228.77€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 100244 | +0.201 | -7228.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 17276 | +0.182 | -1885.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 17276 | +0.182 | -1885.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16167 | +0.226 | -510.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16167 | +0.226 | -510.65€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 17202 | +0.181 | -1800.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 17202 | +0.181 | -1800.03€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 16302 | +0.218 | -647.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 16302 | +0.218 | -647.25€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 16581 | +0.203 | -1056.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 16581 | +0.203 | -1056.99€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 16716 | +0.197 | -1328.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 16716 | +0.197 | -1328.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 38518 | +0.116 | +253.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 38518 | +0.116 | +253.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 19177 | +0.117 | +168.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 19177 | +0.117 | +168.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 19341 | +0.115 | +84.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 19341 | +0.115 | +84.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2443 | +0.293 | -7.43€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2443 | +0.293 | -7.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1118 | +0.281 | -26.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1118 | +0.281 | -26.21€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1190 | +0.298 | +14.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1190 | +0.298 | +14.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 135 | +0.339 | +3.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 135 | +0.339 | +3.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1122 | +0.441 | +3.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1122 | +0.441 | +3.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 538 | +0.435 | -6.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 538 | +0.435 | -6.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 534 | +0.448 | +8.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 534 | +0.448 | +8.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 50 | +0.404 | +1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 50 | +0.404 | +1.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1876 | +0.068 | -81.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1151 | +0.082 | -17.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1442 | +0.076 | -36.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1151 | +0.082 | -17.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 77641 | +0.101 | -1863.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6253 | +0.095 | +123.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 71388 | +0.101 | -1986.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 42498 | +0.105 | -420.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6253 | +0.095 | +123.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 36245 | +0.107 | -544.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 16362 | +0.109 | -93.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 16362 | +0.109 | -93.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 18781 | +0.082 | -1349.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 18781 | +0.082 | -1349.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ GBM_LATE_15M | 52830 | +0.098 | +29091.95€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 52830 | +0.098 | +29091.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8777 | +0.224 | +7523.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8777 | +0.224 | +7523.99€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8032 | +0.175 | +6247.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8032 | +0.175 | +6247.16€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 9469 | +0.206 | +7423.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9469 | +0.206 | +7423.99€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7195 | +0.051 | +2216.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7195 | +0.051 | +2216.13€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7391 | -0.031 | +1910.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7391 | -0.031 | +1910.21€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 11966 | -0.025 | +3770.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11966 | -0.025 | +3770.47€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 55749 | +0.085 | +32095.49€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 55749 | +0.085 | +32095.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10860 | -0.002 | +5792.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10860 | -0.002 | +5792.09€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11923 | +0.005 | +3113.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11923 | +0.005 | +3113.71€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7617 | +0.291 | +8589.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7617 | +0.291 | +8589.63€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10494 | +0.014 | +3175.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10494 | +0.014 | +3175.10€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8640 | +0.044 | +3856.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8640 | +0.044 | +3856.67€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6215 | +0.314 | +7568.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6215 | +0.314 | +7568.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 41845 | +0.179 | +34552.59€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 41845 | +0.179 | +34552.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6300 | +0.239 | +5868.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6300 | +0.239 | +5868.00€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6645 | +0.140 | +4895.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6645 | +0.140 | +4895.52€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6718 | +0.224 | +5822.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6718 | +0.224 | +5822.10€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7147 | +0.133 | +5584.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7147 | +0.133 | +5584.50€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7901 | +0.121 | +5948.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7901 | +0.121 | +5948.49€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7134 | +0.232 | +6433.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7134 | +0.232 | +6433.98€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11229 | +0.126 | +5618.41€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11229 | +0.126 | +5618.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 463 | +0.158 | +306.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 463 | +0.158 | +306.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3257 | +0.134 | +1803.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3257 | +0.134 | +1803.93€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3329 | +0.128 | +1640.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3329 | +0.128 | +1640.53€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2761 | +0.091 | +1055.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2761 | +0.091 | +1055.06€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 928 | +0.163 | +552.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 928 | +0.163 | +552.02€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 53042 | +0.186 | +43395.64€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 53042 | +0.186 | +43395.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8387 | +0.249 | +8090.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8387 | +0.249 | +8090.49€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8388 | +0.137 | +5750.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8388 | +0.137 | +5750.20€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8996 | +0.233 | +8069.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8996 | +0.233 | +8069.93€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8791 | +0.140 | +6443.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8791 | +0.140 | +6443.76€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9405 | +0.124 | +6692.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9405 | +0.124 | +6692.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9075 | +0.239 | +8348.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9075 | +0.239 | +8348.63€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13663 | +0.210 | +11079.47€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13663 | +0.210 | +11079.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3256 | +0.211 | +2806.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3256 | +0.211 | +2806.84€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1282 | +0.203 | +984.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1282 | +0.203 | +984.65€ | 0 | 16 |
| ✅ GBM_LATE_5M#ETH | 3947 | +0.203 | +2965.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3947 | +0.203 | +2965.38€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 2166 | +0.207 | +1787.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2166 | +0.207 | +1787.11€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4623 | +0.051 | +1222.01€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4623 | +0.051 | +1222.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1633 | +0.063 | +504.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1633 | +0.063 | +504.07€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1494 | +0.052 | +437.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1494 | +0.052 | +437.13€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1496 | +0.037 | +280.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1496 | +0.037 | +280.81€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 667 | -0.250 | -35.29€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 667 | -0.250 | -35.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 251 | -0.251 | -20.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 251 | -0.251 | -20.27€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 239 | -0.247 | -7.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 239 | -0.247 | -7.78€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 177 | -0.249 | -7.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 177 | -0.249 | -7.24€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1879 | +0.082 | +477.59€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1879 | +0.082 | +477.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 732 | +0.074 | +179.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 732 | +0.074 | +179.02€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 646 | +0.056 | +110.80€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 646 | +0.056 | +110.80€ | 2 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 501 | +0.128 | +187.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 501 | +0.128 | +187.77€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 211 | +0.279 | +225.02€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 211 | +0.279 | +225.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 211 | +0.279 | +225.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 211 | +0.279 | +225.02€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4178 | +0.097 | +957.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4178 | +0.097 | +957.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4178 | +0.097 | +957.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4178 | +0.097 | +957.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 885 | -0.013 | +13.57€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 885 | -0.013 | +13.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 35 | -0.041 | -1.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 35 | -0.041 | -1.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 254 | -0.016 | +4.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 254 | -0.016 | +4.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 242 | +0.029 | +20.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 242 | +0.029 | +20.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 271 | +0.002 | +5.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 271 | +0.002 | +5.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 54 | -0.161 | -9.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 54 | -0.161 | -9.89€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4111 | +0.016 | +102.19€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4111 | +0.016 | +102.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 197 | +0.033 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 197 | +0.033 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 824 | +0.016 | +41.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 824 | +0.016 | +41.61€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 217 | -0.002 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 217 | -0.002 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1639 | +0.020 | +28.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1639 | +0.020 | +28.88€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 764 | +0.012 | +2.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 764 | +0.012 | +2.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2191 | -0.034 | -14.58€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2191 | -0.034 | -14.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 661 | -0.025 | -7.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 661 | -0.025 | -7.83€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 773 | -0.012 | +13.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 773 | -0.012 | +13.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 757 | -0.064 | -19.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 757 | -0.064 | -19.93€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 13411 | -0.032 | -123.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6426 | -0.035 | -100.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6985 | -0.029 | -23.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 479 | -0.047 | -21.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 243 | -0.010 | +8.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 236 | -0.084 | -30.49€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3503 | -0.024 | +2.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1667 | -0.023 | +5.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1836 | -0.025 | -2.82€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1346 | -0.025 | +24.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 685 | -0.031 | +1.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 661 | -0.017 | +23.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3019 | -0.037 | -75.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1422 | -0.041 | -54.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1597 | -0.033 | -20.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2578 | -0.029 | -4.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1246 | -0.036 | -19.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1332 | -0.023 | +15.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2486 | -0.040 | -49.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1163 | -0.049 | -41.38€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1323 | -0.032 | -7.74€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 62387 | +0.000 | +3434.64€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 62387 | +0.000 | +3434.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11288 | +0.028 | +1545.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11288 | +0.028 | +1545.22€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8794 | -0.035 | -94.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8794 | -0.035 | -94.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11416 | +0.025 | +1249.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11416 | +0.025 | +1249.22€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8700 | -0.050 | -172.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8700 | -0.050 | -172.98€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10595 | -0.004 | +307.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10595 | -0.004 | +307.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11594 | +0.018 | +599.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11594 | +0.018 | +599.57€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7036 | -0.055 | -117.57€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7036 | -0.055 | -117.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1242 | -0.002 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1242 | -0.002 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1928 | -0.067 | -30.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1928 | -0.067 | -30.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 70 | +0.000 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 70 | +0.000 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 798 | -0.120 | -35.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 798 | -0.120 | -35.05€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2140 | -0.068 | -11.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2140 | -0.068 | -11.59€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3375 | +0.003 | -2.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3375 | +0.003 | -2.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 132 | -0.037 | -1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 132 | -0.037 | -1.23€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 195 | +0.008 | -2.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 195 | +0.008 | -2.19€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 153545 | -0.077 | +2190.66€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 153545 | -0.077 | +2190.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 26858 | -0.077 | +1510.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 26858 | -0.077 | +1510.07€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 23002 | -0.100 | -1070.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 23002 | -0.100 | -1070.38€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 27190 | -0.069 | +1280.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 27190 | -0.069 | +1280.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 22544 | -0.097 | -634.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 22544 | -0.097 | -634.90€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 27478 | -0.058 | +315.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 27478 | -0.058 | +315.67€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 26473 | -0.070 | +789.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 26473 | -0.070 | +789.83€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8985 | -0.035 | -185.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8985 | -0.035 | -185.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2070 | -0.047 | -29.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2070 | -0.047 | -29.48€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2631 | -0.026 | -39.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2631 | -0.026 | -39.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1266 | -0.065 | -32.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1266 | -0.065 | -32.98€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1007 | -0.031 | -33.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1007 | -0.031 | -33.05€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2019 | +0.119 | +799.36€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1883 | +0.124 | +786.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 452 | +0.132 | +216.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 452 | +0.132 | +216.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 388 | +0.118 | +135.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 388 | +0.118 | +135.32€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 356 | +0.131 | +168.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 356 | +0.131 | +168.15€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 322 | +0.142 | +165.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 322 | +0.142 | +165.86€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 365 | +0.094 | +100.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 365 | +0.094 | +100.48€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1948 | -0.016 | -18.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1948 | -0.016 | -18.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 370 | +0.013 | +22.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 370 | +0.013 | +22.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 353 | -0.035 | -14.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 353 | -0.035 | -14.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 493 | -0.045 | -36.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 493 | -0.045 | -36.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 392 | -0.003 | -0.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 392 | -0.003 | -0.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 340 | -0.003 | +11.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 340 | -0.003 | +11.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1082 | -0.082 | -56.57€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 498 | -0.114 | -79.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 386 | -0.131 | -61.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 380 | -0.042 | +18.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 269 | -0.028 | +27.62€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 204 | -0.078 | +4.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 168 | -0.076 | +2.99€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 823 | -0.087 | -30.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1354 | -0.209 | -85.90€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 531 | -0.209 | -47.81€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 464 | -0.208 | -43.50€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 452 | -0.211 | -38.72€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 394 | -0.222 | -45.62€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 371 | -0.202 | +0.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 344 | -0.199 | -1.77€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1202 | -0.211 | -90.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 516 | +0.386 | +476.17€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 94 | +0.167 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 94 | +0.167 | +63.15€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 122 | +0.371 | +105.56€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 122 | +0.371 | +105.56€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 300 | +0.457 | +307.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 300 | +0.457 | +307.46€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 516 | +0.386 | +476.17€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 869 | +0.044 | +79.43€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 869 | +0.044 | +79.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 325 | +0.032 | +9.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 325 | +0.032 | +9.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 71 | +0.007 | +0.21€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 71 | +0.007 | +0.21€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 390 | +0.066 | +63.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 390 | +0.066 | +63.86€ | 1 | 5 |
| ✅ STREAK_FADE_5M | 3545 | -0.023 | -141.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3545 | -0.023 | -141.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 606 | -0.028 | -26.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 606 | -0.028 | -26.80€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 169 | -0.038 | -13.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 169 | -0.038 | -13.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1643 | -0.020 | -60.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1643 | -0.020 | -60.99€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 116 | -0.042 | -10.16€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 116 | -0.042 | -10.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 72 | -0.013 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 72 | -0.013 | -5.54€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11450 | +0.015 | +75.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11450 | +0.015 | +75.85€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2985 | +0.018 | +23.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2985 | +0.018 | +23.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2973 | +0.018 | +37.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2973 | +0.018 | +37.64€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2913 | +0.009 | -2.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2913 | +0.009 | -2.28€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11098 | +0.015 | -34.57€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 11098 | +0.015 | -34.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4619 | +0.021 | +1.92€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4619 | +0.021 | +1.92€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3790 | +0.011 | -26.08€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3790 | +0.011 | -26.08€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2689 | +0.011 | -10.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2689 | +0.011 | -10.42€ | 1 | 0 |
| ✅ UPDOWN_GBM | 96936 | +0.059 | +9222.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 23663 | +0.082 | +5041.37€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 2961 | +0.001 | +31.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 64230 | +0.059 | +4051.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5744 | +0.001 | +100.00€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8080 | +0.104 | +1483.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1780 | +0.164 | +821.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6210 | +0.088 | +663.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 22148 | +0.057 | +1937.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3196 | +0.082 | +731.90€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 829 | +0.003 | +15.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 15426 | +0.065 | +1119.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2575 | -0.003 | +65.63€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 122 | -0.065 | +4.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 10435 | +0.078 | +1215.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 8588 | +0.062 | +477.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 22987 | +0.049 | +1603.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5627 | +0.072 | +864.98€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 800 | +0.005 | +16.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 14342 | +0.051 | +692.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2105 | +0.004 | +26.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 113 | -0.100 | +2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 20763 | +0.038 | +1146.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6170 | +0.034 | +427.70€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 759 | -0.010 | +3.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12669 | +0.047 | +714.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1064 | +0.004 | +7.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 101 | -0.141 | -7.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 12521 | +0.072 | +1839.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5129 | +0.099 | +1456.87€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6995 | +0.057 | +384.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 336 | -0.101 | +0.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 954 | +0.364 | +345.11€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 954 | +0.364 | +345.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 476 | +0.362 | +165.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 476 | +0.362 | +165.49€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 478 | +0.365 | +179.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 478 | +0.365 | +179.62€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 23632 | -0.021 | +5852.99€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 23632 | -0.021 | +5852.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4407 | -0.113 | +228.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4407 | -0.113 | +228.07€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3068 | +0.219 | +1964.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3068 | +0.219 | +1964.68€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6667 | -0.059 | +980.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6667 | -0.059 | +980.44€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6438 | -0.064 | +1218.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6438 | -0.064 | +1218.74€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 281 | +0.062 | +26.33€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 281 | +0.062 | +26.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 281 | +0.062 | +26.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 281 | +0.062 | +26.33€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1687 | +0.286 | +1419.55€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1687 | +0.286 | +1419.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 898 | +0.279 | +706.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 898 | +0.279 | +706.41€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 789 | +0.293 | +713.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 789 | +0.293 | +713.14€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 851 | -0.113 | -84.27€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 851 | -0.113 | -84.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 264 | -0.083 | -20.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 264 | -0.083 | -20.26€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 110 | -0.179 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 110 | -0.179 | -4.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4380 | +0.302 | +2025.13€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1656 | +0.259 | +218.05€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1686 | +0.296 | +734.22€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1038 | +0.381 | +1072.86€ | 0 | 1 |