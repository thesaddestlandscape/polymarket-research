# Hipótesis automáticas — 2026-10-31 17:17 UTC
_Generado por shadow_postmortem.py sobre 1136652 resoluciones (PNL=+152407.86€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.225 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.185 (n=312)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.6161` → IC=+0.252 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6161 (IC base=+0.134)

- **PATRÓN** `banda_z` > `8.831` → IC=+0.211 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.831 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.133 (n=448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 8.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=997)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2306.7816` → IC=+0.138 (n=918)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2306.7816 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.220 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.192 (n=264)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 67.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.6117` → IC=+0.243 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6117 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.122` → IC=+0.204 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.122 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=897)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3049.8849` → IC=+0.140 (n=703)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3049.8849 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `9072.653` → IC=+0.121 (n=217)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9072.653 (IC base=+0.005)

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

- **PATRÓN** `py_entrada` < `0.49` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.49 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.5 (IC base=+0.161)

- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.161)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.161)

- **PATRÓN** `banda_hit_calibrado` > `0.6044` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `banda_hit_calibrado` > 0.6044 (IC base=+0.161)

- **PATRÓN** `banda_z` > `2.518` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.518 (IC base=+0.161)

- **PATRÓN** `ballenas_wallet_edge_medio` > `2.641` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `ballenas_wallet_edge_medio` > 2.641 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.235 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `2434.9249` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2434.9249 (IC base=+0.161)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `137.01` → IC=-0.211 (n=11008)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=33026)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.45` → IC=-0.259 (n=1159)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.45
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3480)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.67` → IC=-0.303 (n=1148)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.67
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3447)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.17` → IC=-0.243 (n=2977)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.17
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8933)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.89` → IC=-0.260 (n=2112)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.89
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=6343)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.212 (n=24786)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8657.61` → IC=+0.162 (n=2188)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8657.61 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=21140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=25859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=19604)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=7807)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6766.8992` → IC=+0.150 (n=3017)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6766.8992 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=2151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2630)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `9429.1216` → IC=+0.182 (n=1830)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9429.1216 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2683)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16125.479` → IC=+0.186 (n=692)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16125.479 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=531)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=1262)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.081)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.165 (n=4064)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.375 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=2151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.348 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=2499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=1032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.259 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=1335)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=904)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.552` → IC=+0.168 (n=432)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.552 (IC base=+0.058)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=144)

- **FILTRO** `py_entrada` > `0.75` → IC=-0.291 (n=161)

  - _Acción_: SKIP cuando `py_entrada` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=55)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=21236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=18020)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=8779)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.177 (n=4836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4666)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.177 (n=4031)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.217 (n=2708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.219 (n=2414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.294 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.215)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=4777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4068)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=4954)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3716)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.249 (n=3463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.359 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.248)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=3996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.187 (n=3590)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.71 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=3481)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.429 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4385.1965` → IC=+0.443 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4385.1965 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.446 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.432 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.432 (n=350)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `4649.4982` → IC=+0.441 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4649.4982 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.398 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.395)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.395)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.395)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=27549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=27868)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=4755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=8844)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=12532)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=3975)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=4729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.200 (n=9763)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=4437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=3914)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=10563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=4091)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=4584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=4598)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=4809)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=9873)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=10125)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.38` → IC=+0.139 (n=9179)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.38 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4838)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=4592)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6070)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.66` → IC=+0.145 (n=4558)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.66 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=5035)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5533)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.24` → IC=+0.137 (n=6070)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.24 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=1250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `3875.4788` → IC=+0.296 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3875.4788 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.364 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.303 (n=886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.399 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.300)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.359 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.333)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.380 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.367 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.333)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.449 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.446 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.453 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.439 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.444 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.471 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.453)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.455 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.453)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.457 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.453)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.454 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.453)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.393 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.414 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.400)

- **PATRÓN** `libro_liquidez` > `702.9243` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 702.9243 (IC base=+0.400)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=85)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=85)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4766` → IC=+0.139 (n=15542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4766 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=15709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=10845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.165 (n=15550)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.375 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7815` → IC=+0.281 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7815 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.604` → IC=+0.182 (n=7766)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.604 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.265 (n=4568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3027` → IC=+0.246 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3027 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3458` → IC=+0.228 (n=5042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3458 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=7903)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4536.9294` → IC=+0.150 (n=5181)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4536.9294 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.121 (n=9695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0059 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.6809` → IC=+0.131 (n=21980)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6809 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.6071` → IC=+0.188 (n=1291)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6071 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.187 (n=7460)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1603 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.8636` → IC=+0.189 (n=5174)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8636 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.229 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.6806` → IC=+0.207 (n=4397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6806 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.224 (n=13073)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.079)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.362` → IC=+0.209 (n=3347)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.362 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=1249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=2243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.9843` → IC=+0.280 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9843 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.654` → IC=+0.281 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.654 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.259 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4359` → IC=+0.207 (n=3204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4359 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=3667)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2048.3196` → IC=+0.207 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.3196 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.224 (n=2010)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.242 (n=2900)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.277 (n=966)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=3022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.239 (n=1344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.5515` → IC=+0.259 (n=2897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5515 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.242 (n=2618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.257 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4441` → IC=+0.241 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4441 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.6894` → IC=+0.242 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6894 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=3325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1475.9` → IC=+0.244 (n=2588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1475.9 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.235 (n=930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1073` → IC=+0.256 (n=1221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1073 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=1974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9242` → IC=+0.271 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9242 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.187` → IC=+0.234 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.187 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.129` → IC=+0.260 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.129 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.231 (n=2775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.271 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.230 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4264` → IC=+0.255 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4264 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.150 (n=2957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0778` → IC=+0.163 (n=985)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0778 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=1093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.716` → IC=+0.168 (n=2955)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.716 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.139` → IC=+0.146 (n=2815)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.139 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.861` → IC=+0.141 (n=483)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.861 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.03` → IC=+0.134 (n=2700)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.03 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.135 (n=2956)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.204 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.150 (n=1076)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.1403` → IC=+0.135 (n=2491)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1403 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.7906` → IC=+0.130 (n=1887)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.7906 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=3832)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.169 (n=1222)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 206.0 (IC base=+0.128)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.213 (n=1174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=3703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.101` → IC=+0.279 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.101 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.196 (n=3141)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.222 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7012` → IC=+0.207 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7012 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=4229)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2031.4184` → IC=+0.204 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.4184 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.221 (n=2826)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.232 (n=1413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.221 (n=1466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.037` → IC=+0.269 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.037 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.105` → IC=+0.261 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.105 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.262 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7601` → IC=+0.227 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7601 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1912.5584` → IC=+0.219 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.5584 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.216 (n=2680)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.155 (n=175)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=4238)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.158 (n=609)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9497` → IC=+0.236 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9497 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1377` → IC=+0.335 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1377 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.3351` → IC=+0.328 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3351 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.218` → IC=+0.198 (n=1311)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.218 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `0.7003` → IC=+0.338 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7003 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.0775` → IC=+0.327 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0775 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.335 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4167` → IC=+0.341 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4167 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.2606` → IC=+0.331 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2606 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.332 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0916` → IC=+0.183 (n=1104)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.0916 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.7231` → IC=+0.165 (n=264)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7231 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1377` → IC=+0.144 (n=1904)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1377 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8348` → IC=+0.159 (n=1364)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8348 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2843` → IC=+0.209 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2843 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.7762` → IC=+0.148 (n=1312)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7762 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.166 (n=892)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.045)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.174 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=657)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.170 (n=195)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=589)

- **FILTRO** `ibs_20min` > `0.2069` → IC=-0.132 (n=4153)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2069
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=2052)

- **FILTRO** `sigma_ewma_delta_pct` > `8.48` → IC=-0.224 (n=669)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.48
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5536)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.173 (n=267)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.76 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `1.672` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.672 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.844` → IC=+0.167 (n=91)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.844 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1586` → IC=+0.281 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1586 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4897` → IC=+0.287 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4897 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.4528` → IC=+0.263 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4528 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.270 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.2069` → IC=+0.149 (n=2052)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2069 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1993` → IC=+0.275 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1993 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.310 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0783` → IC=+0.291 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0783 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.302 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7692` → IC=-0.152 (n=3078)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=1589)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.169 (n=1072)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3595)

- **FILTRO** `ibs_20min` > `0.7468` → IC=-0.197 (n=1652)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7468
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=4959)

- **PATRÓN** `dist_vwap_pct` > `1.0603` → IC=+0.358 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0603 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.308 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=-0.062)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.321 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.062)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.308 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.4319` → IC=+0.320 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4319 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.8615` → IC=+0.312 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8615 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` > `0.8038` → IC=+0.274 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8038 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.2233` → IC=+0.260 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2233 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7259` → IC=+0.270 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7259 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `1.0651` → IC=+0.282 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0651 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.1045` → IC=+0.276 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1045 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.1732` → IC=+0.264 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1732 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.4281` → IC=+0.265 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4281 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.205 (n=6753)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.875` → IC=+0.286 (n=9195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.875 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.9321` → IC=+0.302 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9321 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.552` → IC=+0.167 (n=9075)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.552 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `1.1733` → IC=+0.269 (n=7429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1733 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` > `0.6923` → IC=+0.275 (n=6637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6923 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.288 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `1.4575` → IC=+0.271 (n=3936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4575 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `2.645` → IC=+0.279 (n=3935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.645 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.304 (n=11417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.092)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.156 (n=6525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0098 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.6466` → IC=+0.148 (n=19561)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.6466 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.2489` → IC=+0.271 (n=6432)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2489 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.271 (n=2792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.1945` → IC=+0.269 (n=2115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1945 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.320 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.5758` → IC=+0.294 (n=4071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5758 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.2745` → IC=+0.290 (n=4194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2745 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.301 (n=9205)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.078)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5792` → IC=-0.158 (n=2759)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5792
  - _Potencial_: sin este filtro IC_bueno=+0.205 (n=2760)

- **FILTRO** `ibs_20min` > `0.7224` → IC=-0.221 (n=1197)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7224
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=3593)

- **FILTRO** `sigma_ewma_delta_pct` > `4.255` → IC=-0.226 (n=1033)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.255
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=3757)

- **PATRÓN** `ibs_20min` > `0.929` → IC=+0.331 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.929 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.105` → IC=+0.184 (n=1854)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.105 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2286` → IC=+0.321 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2286 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4454` → IC=+0.273 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4454 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.253` → IC=+0.291 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.253 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.310 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.1702` → IC=+0.158 (n=1201)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1702 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.404 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.6471` → IC=+0.405 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6471 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.398 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1189` → IC=+0.219 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1189 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.206 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.195 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.210 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.253 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.232 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.210 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.240 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1263` → IC=+0.246 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1263 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `1.1678` → IC=+0.236 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1678 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.241 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6228 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.305 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.243 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5333 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1537` → IC=+0.254 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1537 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.249 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.321 (n=1311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.285 (n=2888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.319 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.672` → IC=+0.310 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.672 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.289 (n=2520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.282 (n=2796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.287 (n=3436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `2029.9632` → IC=+0.294 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2029.9632 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.300 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.334 (n=1162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.317 (n=1128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.301 (n=887)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` < `0.0074` → IC=+0.302 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0074 (IC base=+0.298)

- **PATRÓN** `ibs_20min` > `0.1333` → IC=+0.306 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1333 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.337` → IC=+0.309 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.337 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` < `0.198` → IC=+0.297 (n=2520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.198 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` > `0.3434` → IC=+0.307 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3434 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` < `1.5868` → IC=+0.299 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5868 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `2.7169` → IC=+0.310 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7169 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.302 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `1914.2984` → IC=+0.305 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.2984 (IC base=+0.298)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.303 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.298)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7312` → IC=-0.182 (n=1255)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7312
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3768)

- **PATRÓN** `ibs_20min` > `0.8633` → IC=+0.166 (n=1218)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8633 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1479` → IC=+0.233 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1479 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.3615` → IC=+0.235 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3615 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0074` → IC=+0.239 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0074 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6697` → IC=+0.233 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6697 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.102` → IC=+0.241 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.102 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4521` → IC=+0.239 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4521 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.254 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1468` → IC=+0.240 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1468 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.244 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1913 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.297 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.7847` → IC=+0.277 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7847 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.261 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.271 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.235 (n=2097)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2106)

- **FILTRO** `ibs_20min` > `0.6333` → IC=-0.233 (n=1011)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6333
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=3051)

- **FILTRO** `sigma_ewma_delta_pct` > `8.374` → IC=-0.254 (n=465)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.374
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=3597)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.312 (n=2106)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.345 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.308` → IC=+0.195 (n=657)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.308 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.340 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.6998` → IC=+0.334 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6998 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1588` → IC=+0.335 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1588 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.354 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.361 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.354 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.6333` → IC=+0.135 (n=3051)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.6333 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.2102` → IC=+0.253 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2102 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.6965` → IC=+0.278 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6965 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.268 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4505` → IC=+0.258 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4505 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.272 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.043)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.355 (n=1942)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.311)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.312 (n=2195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.311)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.314 (n=2281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.311)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.348 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.311)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.336 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.311)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.824` → IC=+0.329 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.824 (IC base=+0.311)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.098` → IC=+0.312 (n=2473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.098 (IC base=+0.311)

- **PATRÓN** `volumen_regimen` > `0.8704` → IC=+0.330 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8704 (IC base=+0.311)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.348 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.311)

- **PATRÓN** `volumen_spike_ratio` > `1.4265` → IC=+0.323 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4265 (IC base=+0.311)

- **PATRÓN** `libro_liquidez` > `2570.0411` → IC=+0.312 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2570.0411 (IC base=+0.311)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.342 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.311)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.343 (n=1541)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.320 (n=1161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.314 (n=1132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` < `0.3793` → IC=+0.333 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3793 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` < `0.2325` → IC=+0.317 (n=2222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2325 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.329 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` < `0.7229` → IC=+0.320 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7229 (IC base=+0.312)

- **PATRÓN** `volumen_regimen` > `1.213` → IC=+0.341 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.213 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.365 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` < `1.4108` → IC=+0.324 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4108 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `2.1343` → IC=+0.314 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1343 (IC base=+0.312)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.227 (n=5037)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.198 (n=5036)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=15677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.5455` → IC=+0.233 (n=15098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5455 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1636` → IC=+0.206 (n=5922)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1636 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.191` → IC=+0.255 (n=3933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.191 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.185` → IC=+0.160 (n=10039)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.185 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6242` → IC=+0.159 (n=10039)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6242 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.208 (n=2184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.5997` → IC=+0.188 (n=4890)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.5997 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=14020)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.190 (n=6462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0056 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.222 (n=4894)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=5477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5181` → IC=+0.237 (n=14674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5181 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.1785` → IC=+0.176 (n=10554)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1785 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.785` → IC=+0.195 (n=2351)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.785 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.571` → IC=+0.184 (n=15178)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 5.571 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.163 (n=10463)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1819 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2955` → IC=+0.220 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2955 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6402` → IC=+0.188 (n=4630)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6402 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.194 (n=13637)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.225 (n=834)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1042` → IC=+0.259 (n=1099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1042 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9379` → IC=+0.297 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9379 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.718` → IC=+0.330 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.718 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.289 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.8357` → IC=+0.221 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8357 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.223 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2760)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.233 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.256 (n=1994)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.0971` → IC=+0.307 (n=877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0971 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=2063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.256 (n=1827)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.0395` → IC=+0.301 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0395 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.258 (n=1752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.276 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `2.298` → IC=+0.262 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.298 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.7197` → IC=+0.256 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7197 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1461.8154` → IC=+0.260 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1461.8154 (IC base=+0.253)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.255 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.253)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.204 (n=769)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1598` → IC=+0.171 (n=1529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1598 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.2856` → IC=+0.213 (n=2292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2856 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.214 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.015` → IC=+0.211 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.015 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.153 (n=1009)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6938 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.0611` → IC=+0.143 (n=1040)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0611 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.187 (n=353)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5047` → IC=+0.158 (n=991)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5047 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.155 (n=751)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.146 (n=2218)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 409.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.175 (n=2426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0061 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.239` → IC=+0.170 (n=2134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.239 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=1155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.207 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6155 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.202` → IC=+0.182 (n=457)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.202 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.099` → IC=+0.148 (n=2114)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.099 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2014` → IC=+0.159 (n=2425)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2014 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0702` → IC=+0.149 (n=2000)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0702 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4814` → IC=+0.150 (n=2302)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4814 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.185 (n=994)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 216.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.238 (n=1161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.401` → IC=+0.225 (n=2250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.401 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=930)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.267` → IC=+0.307 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.267 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.213 (n=2218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.238 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7614` → IC=+0.212 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7614 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7054` → IC=+0.226 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7054 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3067)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1919.67` → IC=+0.224 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.67 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.240 (n=2219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.2465` → IC=+0.267 (n=1480)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2465 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0282` → IC=+0.290 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0282 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.282 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.290 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7622` → IC=+0.235 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7622 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1738` → IC=+0.244 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1738 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1907.76` → IC=+0.247 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.76 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.240 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.198 (n=1088)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0041 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0784` → IC=+0.197 (n=822)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0784 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=2556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2777` → IC=+0.203 (n=2465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2777 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1409` → IC=+0.188 (n=1465)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1409 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.557` → IC=+0.192 (n=427)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.557 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0199` → IC=+0.146 (n=2169)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0199 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1015` → IC=+0.168 (n=997)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1015 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.824` → IC=+0.142 (n=1611)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.824 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.5111` → IC=+0.159 (n=805)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5111 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `6908.9474` → IC=+0.199 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6908.9474 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.146 (n=2404)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 132.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.165 (n=2304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3955` → IC=+0.142 (n=2615)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3955 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.184 (n=2615)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6801 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1588` → IC=+0.154 (n=2625)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1588 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.432` → IC=+0.146 (n=631)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.432 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.154 (n=1745)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8521 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.188 (n=395)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8074` → IC=+0.129 (n=1646)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8074 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4232` → IC=+0.127 (n=2469)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4232 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6178.6677` → IC=+0.179 (n=1186)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 6178.6677 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.132 (n=2139)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 110.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.168 (n=1254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0109 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4762` → IC=+0.212 (n=2762)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4762 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.190 (n=1541)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.254` → IC=+0.290 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.254 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1752` → IC=+0.133 (n=2761)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1752 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7045` → IC=+0.125 (n=2466)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7045 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.132 (n=2820)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.5435` → IC=+0.141 (n=1180)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5435 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=2883)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2634.7685` → IC=+0.199 (n=1252)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2634.7685 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.144 (n=1148)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.142 (n=2854)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0115 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1102` → IC=+0.166 (n=950)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1102 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=2908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6351` → IC=+0.219 (n=2849)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6351 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2006` → IC=+0.147 (n=2746)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2006 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.383` → IC=+0.136 (n=2514)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.383 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.128 (n=2849)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1819 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.164` → IC=+0.122 (n=2782)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.164 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2758` → IC=+0.134 (n=391)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2758 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5398` → IC=+0.125 (n=1178)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.5398 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.7985` → IC=+0.124 (n=1784)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.7985 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2516.696` → IC=+0.181 (n=1292)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2516.696 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.125 (n=2640)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.248 (n=2255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1681` → IC=+0.239 (n=1110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1681 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.661` → IC=+0.257 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.661 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.232 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.8327` → IC=+0.225 (n=2599)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8327 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.594` → IC=+0.255 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.594 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.1659` → IC=+0.225 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1659 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.232 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2843` → IC=+0.266 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2843 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `2.461` → IC=+0.227 (n=2459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.461 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.8052` → IC=+0.233 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8052 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2084.6402` → IC=+0.227 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2084.6402 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.240 (n=1134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.245 (n=1170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.261 (n=859)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=1153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.4379` → IC=+0.263 (n=2575)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4379 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.3046` → IC=+0.243 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3046 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.295` → IC=+0.272 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.295 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.237 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.869 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `1.0409` → IC=+0.242 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0409 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.283 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `2.5151` → IC=+0.232 (n=2414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5151 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.236 (n=2414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.235)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.205 (n=1662)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.194 (n=1664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=3581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.4626` → IC=+0.216 (n=3373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4626 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.8082` → IC=+0.196 (n=576)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8082 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.204 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.189 (n=2272)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8605 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.179 (n=1523)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4274` → IC=+0.182 (n=1226)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4274 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=4245)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `8471.0872` → IC=+0.188 (n=1712)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 8471.0872 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.1999` → IC=+0.184 (n=1800)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1999 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.124 (n=1732)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 26.0 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.198 (n=1019)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0057 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3276` → IC=+0.205 (n=1019)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3276 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.219 (n=923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.6327` → IC=+0.246 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6327 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.215 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.013` → IC=+0.208 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.013 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.56` → IC=+0.185 (n=1075)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 6.56 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.8788` → IC=+0.202 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8788 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1536` → IC=+0.189 (n=1072)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1536 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.193 (n=408)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.1853` → IC=+0.200 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1853 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `10271.3236` → IC=+0.190 (n=1019)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 10271.3236 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.162 (n=551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0033 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.6372` → IC=+0.140 (n=1102)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6372 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.170 (n=541)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 164.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.245 (n=524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.2122` → IC=+0.200 (n=791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2122 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=1235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.34` → IC=+0.228 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.34 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.197 (n=186)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.2053` → IC=+0.186 (n=1070)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.2053 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.215 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.199 (n=791)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8331 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.205 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.4253` → IC=+0.192 (n=391)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4253 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.7833` → IC=+0.193 (n=780)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7833 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.1012` → IC=+0.181 (n=387)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1012 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `5071.0672` → IC=+0.125 (n=774)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 5071.0672 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.153 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0069 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.156 (n=315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0114 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.204 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.9822` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9822 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.059` → IC=+0.242 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.059 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0549` → IC=+0.158 (n=831)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0549 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.7048` → IC=+0.158 (n=844)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7048 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.173 (n=304)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.151 (n=414)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1499 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=988)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2751.379` → IC=+0.180 (n=429)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2751.379 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.575` → IC=+0.132 (n=921)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.575 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `2589.7365` → IC=+0.143 (n=474)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2589.7365 (IC base=+0.047)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0261` → IC=+0.171 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0261 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2792` → IC=+0.174 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2792 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.7333` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.7333 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.617` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.617 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `1.2207` → IC=+0.167 (n=289)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 1.2207 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.349` → IC=+0.187 (n=228)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 3.349 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.9954` → IC=+0.170 (n=228)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.9954 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.6843` → IC=+0.175 (n=232)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6843 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1036` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1036 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.8054` → IC=+0.194 (n=155)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.8054 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.187 (n=308)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.03 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2825.677` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2825.677 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.165 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0131 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.3393` → IC=+0.148 (n=194)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.3393 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `1.2291` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2291 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.338` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.338 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.701` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.701 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.139 (n=267)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.7332` → IC=+0.138 (n=92)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.7332 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2027.646` → IC=+0.130 (n=260)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2027.646 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.150 (n=272)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 19.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.230 (n=6565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=20539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4375` → IC=+0.229 (n=19699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4375 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8806` → IC=+0.212 (n=2374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8806 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.11` → IC=+0.255 (n=4826)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.11 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2171` → IC=+0.163 (n=13241)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2171 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.206 (n=3554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.192 (n=6401)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.202 (n=18340)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.196 (n=7952)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0058 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.194 (n=6011)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.012 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.4855` → IC=+0.193 (n=18031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4855 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=6673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.5903` → IC=+0.241 (n=18031)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5903 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.1779` → IC=+0.172 (n=11230)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1779 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.634` → IC=+0.204 (n=2464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.634 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.47` → IC=+0.194 (n=17518)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 3.47 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `1.0571` → IC=+0.165 (n=10684)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0571 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.252 (n=2461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.631` → IC=+0.201 (n=5727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.631 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.221 (n=11442)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.190)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3604` → IC=+0.232 (n=3176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3604 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=1538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.8598` → IC=+0.299 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8598 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.137` → IC=+0.347 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.137 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.294 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.4439` → IC=+0.233 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4439 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.2757` → IC=+0.237 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2757 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `2046.307` → IC=+0.234 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.307 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.253 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.231)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.269 (n=2786)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.0883` → IC=+0.297 (n=929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0883 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5314` → IC=+0.286 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5314 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.266 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.291 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5621` → IC=+0.265 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5621 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.6638` → IC=+0.276 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6638 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=3200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1752.1286` → IC=+0.272 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1752.1286 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.273 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.186 (n=1071)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.003 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1046` → IC=+0.156 (n=1412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1046 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=3341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.2178` → IC=+0.194 (n=3207)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2178 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.3213` → IC=+0.200 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3213 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.486` → IC=+0.158 (n=673)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.486 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.136` → IC=+0.143 (n=2813)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.136 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.6335` → IC=+0.166 (n=1069)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6335 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.2372` → IC=+0.143 (n=1069)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2372 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.183 (n=458)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.1552` → IC=+0.150 (n=2766)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1552 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.145 (n=2808)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `427.0` → IC=+0.152 (n=3083)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 427.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.162 (n=2761)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0061 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.180 (n=921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6871` → IC=+0.188 (n=2759)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6871 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1415` → IC=+0.154 (n=2640)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1415 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.052` → IC=+0.145 (n=1321)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.052 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.0503` → IC=+0.152 (n=2428)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0503 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2185` → IC=+0.194 (n=514)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2185 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.143 (n=885)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7756` → IC=+0.145 (n=1768)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7756 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=3581)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.154 (n=862)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 233.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.252 (n=1097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.161` → IC=+0.326 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.161 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1311` → IC=+0.226 (n=3088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1311 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.3487` → IC=+0.224 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3487 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.6151` → IC=+0.229 (n=3196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6151 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2031.067` → IC=+0.241 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.067 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.244 (n=2737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1801` → IC=+0.258 (n=1368)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1801 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0517` → IC=+0.305 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0517 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.663` → IC=+0.299 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.663 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.307 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.154` → IC=+0.254 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.154 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1910.86` → IC=+0.251 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.86 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.246 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.190 (n=1500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0041 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4326` → IC=+0.150 (n=3400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4326 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=3532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.9035` → IC=+0.276 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9035 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1967` → IC=+0.167 (n=1574)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1967 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.027` → IC=+0.156 (n=1522)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.027 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6165` → IC=+0.163 (n=1136)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6165 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.183 (n=601)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5191` → IC=+0.155 (n=1461)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5191 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1723` → IC=+0.145 (n=1506)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1723 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7316.3109` → IC=+0.239 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7316.3109 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.153 (n=1441)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 69.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.157 (n=2841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4443` → IC=+0.147 (n=2839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4443 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=1034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7195` → IC=+0.191 (n=2839)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.7195 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1508` → IC=+0.148 (n=2625)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1508 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.014` → IC=+0.171 (n=426)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.014 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6926` → IC=+0.154 (n=1250)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6926 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.222 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.215` → IC=+0.139 (n=2411)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.215 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.5362` → IC=+0.147 (n=2447)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5362 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6178.8421` → IC=+0.206 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6178.8421 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.143 (n=1849)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 95.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.151 (n=1559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.011 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=2426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.193 (n=3441)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4333 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0143` → IC=+0.209 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0143 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.45` → IC=+0.269 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.45 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8777` → IC=+0.133 (n=2292)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8777 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.124 (n=3266)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.491` → IC=+0.122 (n=3359)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.491 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=3589)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2688.9018` → IC=+0.242 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2688.9018 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.154 (n=2862)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0106 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1356` → IC=+0.154 (n=1085)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1356 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=3362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.209 (n=3271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.213` → IC=+0.139 (n=2895)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.213 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.149` → IC=+0.143 (n=3130)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.149 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.149 (n=1085)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6401 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.167 (n=569)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4343` → IC=+0.153 (n=1024)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4343 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2566.3406` → IC=+0.196 (n=1084)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2566.3406 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.131 (n=3058)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.258 (n=2856)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=3342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=2871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.997` → IC=+0.316 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.997 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.251 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.298` → IC=+0.282 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.298 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.240 (n=3198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6423` → IC=+0.240 (n=3197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6423 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.236` → IC=+0.255 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.236 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.5426` → IC=+0.243 (n=2787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5426 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2082.0245` → IC=+0.236 (n=3197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2082.0245 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0257` → IC=+0.259 (n=1097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0257 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=3103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.270 (n=3296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.52 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` < `0.2983` → IC=+0.242 (n=3218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2983 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.221` → IC=+0.277 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.221 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `1.2176` → IC=+0.260 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2176 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.299 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8103` → IC=+0.235 (n=2059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8103 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.4276` → IC=+0.238 (n=3086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4276 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.235 (n=3019)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.237)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.198 (n=5616)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=1922)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5025` → IC=+0.224 (n=5760)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5025 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9338` → IC=+0.254 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9338 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.4248` → IC=+0.219 (n=4178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4248 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.856` → IC=+0.222 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.856 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.577` → IC=+0.217 (n=5125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.577 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.227 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.8828` → IC=+0.218 (n=2836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8828 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.1055` → IC=+0.218 (n=5374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1055 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.222 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4515` → IC=+0.225 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4515 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=4509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3716.3028` → IC=+0.225 (n=3839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3716.3028 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.238 (n=1414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4908` → IC=+0.211 (n=4224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4908 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.205 (n=4224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.6506` → IC=+0.209 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6506 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.1771` → IC=+0.193 (n=3741)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1771 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.803` → IC=+0.208 (n=3780)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.803 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.0971` → IC=+0.203 (n=3539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0971 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.199 (n=3886)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.201 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.203 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.1886` → IC=+0.206 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1886 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=5616)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.208 (n=3652)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 172.0 (IC base=+0.197)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.273 (n=792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.291 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.272 (n=952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.4609` → IC=+0.282 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4609 (IC base=+0.264)

- **PATRÓN** `dist_vwap_pct` < `0.1962` → IC=+0.278 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1962 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.694` → IC=+0.266 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.694 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` < `1.2234` → IC=+0.267 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2234 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` > `0.8676` → IC=+0.282 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8676 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.270 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.267 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.264)

- **PATRÓN** `libro_liquidez` > `12817.5218` → IC=+0.274 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12817.5218 (IC base=+0.264)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.261 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.193 (n=1492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.188 (n=555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.200 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1373 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.6858` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6858 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.329` → IC=+0.201 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.329 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2393` → IC=+0.188 (n=1492)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2393 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.196 (n=688)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.4957` → IC=+0.185 (n=1485)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.4957 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.8036` → IC=+0.182 (n=990)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8036 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `14608.6008` → IC=+0.185 (n=677)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14608.6008 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `685.0` → IC=+0.190 (n=1447)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 685.0 (IC base=+0.179)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.203 (n=858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.3897` → IC=+0.198 (n=286)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3897 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.239 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.238 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8172` → IC=+0.204 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8172 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2760.165` → IC=+0.226 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2760.165 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.197 (n=381)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 5.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.224 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.228)

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

- **PATRÓN** `libro_liquidez` > `2388.306` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2388.306 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.219 (n=1594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.453` → IC=+0.213 (n=1594)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.453 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4986` → IC=+0.221 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4986 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3977` → IC=+0.216 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3977 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.026` → IC=+0.214 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.026 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.707` → IC=+0.211 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.707 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2236` → IC=+0.205 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2236 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.209 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1452` → IC=+0.216 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1452 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.4848` → IC=+0.216 (n=1310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4848 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.207 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.209 (n=882)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.4046` → IC=+0.199 (n=874)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.4046 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.089` → IC=+0.200 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.089 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.6265` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6265 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.376` → IC=+0.198 (n=1191)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.376 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.222 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6401 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.224 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.201 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.7867` → IC=+0.196 (n=856)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7867 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `6502.907` → IC=+0.201 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6502.907 (IC base=+0.195)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.227 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.226 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.7276` → IC=+0.238 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7276 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.261` → IC=+0.218 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.261 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.6342` → IC=+0.237 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6342 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.203 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.194 (n=390)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.1715` → IC=+0.197 (n=746)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1715 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.4746` → IC=+0.205 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4746 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `4251.7342` → IC=+0.237 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4251.7342 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.216 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.218 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.5971` → IC=+0.238 (n=643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5971 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.245 (n=449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.7347` → IC=+0.241 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7347 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.512` → IC=+0.226 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.512 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.3028` → IC=+0.217 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3028 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.91` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.91 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.825` → IC=+0.225 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.825 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.7477` → IC=+0.217 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7477 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.231 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.255 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2965.6586` → IC=+0.233 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2965.6586 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.243 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.216)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.153 (n=660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0036 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.7551` → IC=+0.195 (n=1254)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.7551 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.1474` → IC=+0.141 (n=955)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1474 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.69` → IC=+0.147 (n=412)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.69 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.260 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.146` → IC=+0.142 (n=333)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.146 (IC base=+0.044)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3718` → IC=-0.150 (n=201)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3718
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=605)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.130 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0058 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.3718` → IC=+0.159 (n=605)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.3718 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.172 (n=297)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.282 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.055)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7041` → IC=-0.162 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7041
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=386)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.128 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.005 (IC base=+0.077)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` > `0.7833` → IC=+0.225 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7833 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.179 (n=306)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.717` → IC=+0.204 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.717 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.256 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.014)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.593` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.593 (IC base=+0.014)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.199 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.84` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 8.84 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.148 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.011 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.4412` → IC=+0.170 (n=316)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.4412 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1045 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.1522` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1522 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.8346` → IC=+0.138 (n=194)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.8346 (IC base=+0.062)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.336 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=269)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=324)

- **FILTRO** `volumen_regimen` < `0.7761` → IC=-0.305 (n=85)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7761
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=255)

- **FILTRO** `libro_liquidez` < `903.6493` → IC=-0.213 (n=85)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.6493
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=255)

- **FILTRO** `drift_60min` |x|> `0.1941` → IC=-0.331 (n=75)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=227)

- **FILTRO** `dist_vwap_pct` > `0.4722` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4722
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=290)

- **FILTRO** `sigma_ewma_delta_pct` > `9.983` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.983
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=282)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=189)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.296 (n=52)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.263 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **FILTRO** `ibs_20min` < `0.3442` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3442
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=93)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.333 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=104)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0027` → IC=-0.293 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=87)

- **FILTRO** `ibs_20min` < `0.5843` → IC=-0.467 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5843
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=86)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.365 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=85)

- **FILTRO** `ibs_20min` > `0.702` → IC=-0.405 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` > 0.702
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=80)

- **FILTRO** `dist_vwap_pct` > `0.1281` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1281
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.313 (n=105)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=104)

- **FILTRO** `volumen_regimen` < `0.7553` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7553
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=92)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.321 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=35)

- **FILTRO** `dist_vwap_pct` < `0.238` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.238
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.210 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.176 (n=616)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6667 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.5443` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5443 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.137 (n=337)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.636` → IC=+0.141 (n=452)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.636 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6221` → IC=+0.181 (n=205)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6221 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.173 (n=441)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4061` → IC=+0.161 (n=509)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4061 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.121 (n=624)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.1429 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.935` → IC=+0.155 (n=207)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.935 (IC base=+0.034)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.154 (n=79)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=163)

- **PATRÓN** `dist_vwap_pct` > `0.5497` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5497 (IC base=+0.016)

- **PATRÓN** `ibs_20min` < `0.224` → IC=+0.174 (n=329)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.224 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.999` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 9.999 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2251` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2251 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `1.786` → IC=+0.130 (n=198)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.786 (IC base=+0.102)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=195)

- **FILTRO** `ibs_20min` > `0.1566` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1566
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=222)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.132 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0062 (IC base=+0.124)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.135 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.003 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.126 (n=89)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.163 (n=179)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8015 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.0953` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0953 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.160 (n=210)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6229 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.1409` → IC=+0.169 (n=152)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.1409 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1623.6709` → IC=+0.185 (n=201)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1623.6709 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2045` → IC=-0.229 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2045
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=113)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.292 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.276 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.6827` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6827 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.271 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.2653` → IC=+0.259 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2653 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.308` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.308 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.003` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.003 (IC base=-0.076)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=91)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.304)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.304)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.371 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.304)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.380 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `1067.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1067.0 (IC base=+0.304)

- **PATRÓN** `drift_ventana_pct` |x|> `0.345` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.345 (IC base=+0.236)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.236)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `1395.0` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1395.0 (IC base=+0.236)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=91)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.304)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.304)

- **PATRÓN** `drift_15min` |x|≤ `2.6528` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.6528 (IC base=+0.304)

- **PATRÓN** `drift_60min` |x|≤ `0.9568` → IC=+0.371 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9568 (IC base=+0.304)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.380 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.304)

- **PATRÓN** `ballena_activa_n` < `1067.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1067.0 (IC base=+0.304)

- **PATRÓN** `drift_ventana_pct` |x|> `0.345` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.345 (IC base=+0.236)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.236)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.236)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `1395.0` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1395.0 (IC base=+0.236)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=224)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=224)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=505)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.128 (n=92)

  - _Acción_: Kelly boost +0.64€ cuando `liq_n` > 2.0 (IC base=+0.057)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.132 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 8.0 (IC base=+0.057)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3800)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=74)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=104)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=264)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1517)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1471)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=722)

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
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=921)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=921)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1053)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1053)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=247)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=247)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.140 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=189)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=305)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=346)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=282)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=377)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=377)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=222)

- **FILTRO** `libro_liquidez` < `652.2458` → IC=-0.140 (n=134)

  - _Acción_: SKIP cuando `libro_liquidez` < 652.2458
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=273)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=302)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.72` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `restante_min` < 10.72
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=59)

- **FILTRO** `lag_apertura_s` > `256.96` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `lag_apertura_s` > 256.96
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=59)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.197 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=79)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.145 (n=263)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.51 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=176)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.127 (n=140)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=563)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.138 (n=280)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=301)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=124)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=524)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.146 (n=258)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=530)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=6871)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=22203)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.178 (n=7265)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=22637)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=1300)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=4050)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.176 (n=1234)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=4080)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1404)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1040.2746` → IC=+0.139 (n=2675)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1040.2746 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.132 (n=2503)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1145.769` → IC=+0.150 (n=1807)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1145.769 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.182 (n=1030)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3200)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1298)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=4135)

- **PATRÓN** `ibs_20min` > `0.9644` → IC=+0.128 (n=1821)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.9644 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1732.9258` → IC=+0.121 (n=1821)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1732.9258 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.153 (n=1328)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4033)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2417)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2341)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3800)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.135 (n=1277)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2511)

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
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=344)

- **FILTRO** `drift_20min_pct` |x|> `0.2038` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2038
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=343)

- **FILTRO** `libro_liquidez` < `3186.5516` → IC=-0.184 (n=150)

  - _Acción_: SKIP cuando `libro_liquidez` < 3186.5516
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=307)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=953)

- **FILTRO** `libro_liquidez` < `1797.2058` → IC=-0.161 (n=243)

  - _Acción_: SKIP cuando `libro_liquidez` < 1797.2058
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=729)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.196 (n=366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=731)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.030)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=19916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=44600)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=15143)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=49373)

- **FILTRO** `ibs_7min` < `0.2261` → IC=-0.232 (n=16129)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2261
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=48387)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=21595)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=42921)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=20075)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=60922)

- **FILTRO** `ibs_7min` > `0.283` → IC=-0.182 (n=20241)

  - _Acción_: SKIP cuando `ibs_7min` > 0.283
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=60756)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2807)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8580)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=2771)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8616)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.248 (n=3756)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=7631)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.149 (n=2662)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8725)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3342)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=10660)

- **FILTRO** `ibs_7min` > `0.7716` → IC=-0.214 (n=3500)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7716
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=10502)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2578)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=8226)

- **FILTRO** `ibs_7min` < `0.7173` → IC=-0.204 (n=2701)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7173
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8103)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.193 (n=2700)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8104)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=2743)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8282)

- **FILTRO** `ibs_7min` > `0.2651` → IC=-0.191 (n=2756)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2651
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8269)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=2743)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8282)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=2653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=8228)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=2710)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=8171)

- **FILTRO** `ibs_7min` < `0.2875` → IC=-0.247 (n=3590)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2875
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=7291)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.197 (n=2334)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8547)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=3528)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=11303)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.183 (n=3706)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11125)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2536)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=7928)

- **FILTRO** `ibs_7min` < `0.7195` → IC=-0.195 (n=2616)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7195
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=7848)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.189 (n=2521)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=7943)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2500)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8411)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.173 (n=2726)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8185)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.175 (n=2631)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8280)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=2603)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=7839)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.227 (n=3424)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=7018)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.221 (n=2450)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7992)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.194 (n=3714)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=11925)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=3387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=7151)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=2624)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7914)

- **FILTRO** `ibs_7min` < `0.1831` → IC=-0.231 (n=2634)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1831
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7904)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2454)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=8084)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.227 (n=3628)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=10961)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1006)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1292)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=593)

- **FILTRO** `libro_liquidez` < `10471.8477` → IC=-0.151 (n=187)

  - _Acción_: SKIP cuando `libro_liquidez` < 10471.8477
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=564)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=872)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `libro_liquidez` < `3267.213` → IC=-0.160 (n=186)

  - _Acción_: SKIP cuando `libro_liquidez` < 3267.213
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=560)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4309` → IC=+0.153 (n=606)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4309 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.131 (n=589)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 5.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `428.7014` → IC=+0.154 (n=446)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 428.7014 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3495.451` → IC=+0.146 (n=606)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3495.451 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.171 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 14.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.147 (n=276)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 375.759 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2523.0565` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2523.0565 (IC base=+0.121)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.139 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=334)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2304.5801` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2304.5801 (IC base=+0.115)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.195 (n=172)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.156 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 4.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `511.5491` → IC=+0.186 (n=173)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 511.5491 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5172.0718` → IC=+0.142 (n=258)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 5172.0718 (IC base=+0.139)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.168 (n=233)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.190 (n=169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.144)

- **PATRÓN** `total_vol_5m` < `4901.52` → IC=+0.190 (n=156)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 4901.52 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3155.1686` → IC=+0.167 (n=208)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3155.1686 (IC base=+0.144)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.140 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 10.0 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=172)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3557.0392` → IC=+0.144 (n=116)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3557.0392 (IC base=+0.103)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `sigma_h` > `0.0074` → IC=-0.306 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=570)

- **FILTRO** `T_h` > `129.6188` → IC=-0.181 (n=189)

  - _Acción_: SKIP cuando `T_h` > 129.6188
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=570)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.177 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0037 (IC base=-0.081)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.293 (n=56)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=170)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.297 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=-0.035)

- **PATRÓN** `pct_vs_K` |x|≤ `1.617` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.617 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.223 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=53)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.230 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=107)

- **FILTRO** `T_h` < `92.8406` → IC=-0.185 (n=71)

  - _Acción_: SKIP cuando `T_h` < 92.8406
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=71)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0105` → IC=-0.230 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=173)

- **FILTRO** `T_h` > `74.6449` → IC=-0.217 (n=461)

  - _Acción_: SKIP cuando `T_h` > 74.6449
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=228)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.225 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=443)

- **FILTRO** `pct_vs_K` |x|> `3.1913` → IC=-0.426 (n=147)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1913
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=443)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0089` → IC=-0.211 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=57)

- **FILTRO** `T_h` > `88.3739` → IC=-0.204 (n=113)

  - _Acción_: SKIP cuando `T_h` > 88.3739
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=115)

- **FILTRO** `T_h` > `72.749` → IC=-0.247 (n=160)

  - _Acción_: SKIP cuando `T_h` > 72.749
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=54)

- **FILTRO** `pct_vs_K` |x|> `2.9641` → IC=-0.423 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9641
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=164)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.326 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=67)

- **FILTRO** `T_h` > `102.0012` → IC=-0.290 (n=98)

  - _Acción_: SKIP cuando `T_h` > 102.0012
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=99)

- **FILTRO** `sigma_h` < `0.0052` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=138)

- **FILTRO** `pct_vs_K` |x|> `2.3708` → IC=-0.414 (n=91)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3708
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=92)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `T_h` > `126.9278` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` > 126.9278
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.304 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=147)

- **FILTRO** `T_h` > `70.3179` → IC=-0.209 (n=146)

  - _Acción_: SKIP cuando `T_h` > 70.3179
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=50)

- **FILTRO** `sigma_h` > `0.0135` → IC=-0.348 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0135
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=87)

- **FILTRO** `sigma_h` < `0.0088` → IC=-0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `T_h` > `39.1242` → IC=-0.286 (n=87)

  - _Acción_: SKIP cuando `T_h` > 39.1242
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=44)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.469 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.343)

- **PATRÓN** `sigma_h` < `0.0147` → IC=+0.361 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0147 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.377 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.343)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.343)

- **PATRÓN** `T_h` > `0.7258` → IC=+0.377 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7258 (IC base=+0.343)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.343)

- **PATRÓN** `edge` > `0.0997` → IC=+0.439 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.408)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.432 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.408)

- **PATRÓN** `T_h` < `0.608` → IC=+0.440 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.408)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.416 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.408)

- **PATRÓN** `dist_50` > `0.3765` → IC=+0.447 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3765 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.408)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1444` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1444 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.300 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.203)

- **PATRÓN** `T_h` < `0.659` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.659 (IC base=+0.203)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.294 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1015` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1015 (IC base=+0.410)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.412 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.410)

- **PATRÓN** `T_h` < `1.2716` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2716 (IC base=+0.410)

- **PATRÓN** `dist_50` > `0.3792` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3792 (IC base=+0.410)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.410)

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

- **PATRÓN** `edge` > `0.1961` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.473 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.462)

- **PATRÓN** `T_h` < `0.8279` → IC=+0.456 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8279 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4605` → IC=+0.492 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4605 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=358)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=433)

- **PATRÓN** `streak_estiramiento` < `0.2685` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2685 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.128 (n=224)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 33.0 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2756.3002` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2756.3002 (IC base=+0.057)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.495 (IC base=+0.064)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=21)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.026)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.092)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.437 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2125.6013` → IC=+0.123 (n=157)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2125.6013 (IC base=+0.092)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=99)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=108)

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
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.069)

- **PATRÓN** `volumen_racha` < `24607.606` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 24607.606 (IC base=+0.069)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1051)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1336)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1293)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` > `5.0` → IC=-0.158 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4431)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.158 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2538)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.189 (n=1870)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0056 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.173 (n=1416)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0128 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2093` → IC=+0.176 (n=4249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2093 (IC base=+0.163)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3489` → IC=+0.172 (n=3904)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3489 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.169 (n=4491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 4.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=3942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `ibs_15` > `0.519` → IC=+0.234 (n=4249)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.519 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.1317` → IC=+0.157 (n=2042)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1317 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.3204` → IC=+0.148 (n=3447)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.3204 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.866` → IC=+0.265 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.866 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `4888.5648` → IC=+0.186 (n=1416)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4888.5648 (IC base=+0.163)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1713)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.220 (n=704)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.255 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2639` → IC=+0.230 (n=235)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2639 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.226 (n=735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.7143` → IC=+0.279 (n=704)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7143 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.2372` → IC=+0.220 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2372 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.327` → IC=+0.310 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.327 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `8049.1341` → IC=+0.214 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8049.1341 (IC base=+0.205)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.157 (n=860)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0068 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1507` → IC=+0.148 (n=757)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1507 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2833` → IC=+0.138 (n=691)

  - _Acción_: Kelly boost +0.69€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2833 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.138 (n=902)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.5056` → IC=+0.227 (n=860)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5056 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.148 (n=535)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.132` → IC=+0.283 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.132 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `5784.5699` → IC=+0.168 (n=390)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5784.5699 (IC base=+0.135)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.875` → IC=+0.221 (n=364)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.875 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=541)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.079)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0194` → IC=+0.193 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0194 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0245` → IC=+0.212 (n=317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0245 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.2051` → IC=+0.204 (n=949)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2051 (IC base=+0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3454` → IC=+0.223 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3454 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.198 (n=855)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 14.0 (IC base=+0.191)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.267 (n=955)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1329` → IC=+0.215 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1329 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.612` → IC=+0.231 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.612 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=665)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2977.154` → IC=+0.268 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2977.154 (IC base=+0.191)

- **PATRÓN** `ibs_15` < `0.1071` → IC=+0.170 (n=831)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1071 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.387 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.380 (n=464)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.385 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.398 (n=696)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.385 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.396 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `3837.2318` → IC=+0.375 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3837.2318 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.361 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.365 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.5207` → IC=+0.360 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5207 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.156` → IC=+0.368 (n=233)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.156 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.378 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.386 (n=350)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.386 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.244` → IC=+0.385 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.244 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `8041.1866` → IC=+0.384 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8041.1866 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.403 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.369 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.368)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.384 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.368)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.367 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.368)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.381 (n=310)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.368)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.383 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.368)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.383 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.368)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.376 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.368)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.405 (n=347)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.368)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.376 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.368)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.372 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.368)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.408` → IC=+0.406 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.408 (IC base=+0.368)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.374 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.368)

- **PATRÓN** `libro_liquidez` > `4035.6016` → IC=+0.400 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4035.6016 (IC base=+0.368)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=2363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2364)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=1872)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2855)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.219 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.070)

- **PATRÓN** `ibs_15` > `0.6332` → IC=+0.281 (n=1125)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6332 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.203 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.424` → IC=+0.200 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.424 (IC base=-0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2317` → IC=+0.268 (n=1393)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2317 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.281 (n=4179)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.6551` → IC=+0.275 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6551 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1661` → IC=+0.244 (n=3109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1661 (IC base=-0.009)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0334` → IC=-0.223 (n=2241)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0334
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=750)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.221 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=2244)

- **FILTRO** `sigma_ewma_delta_pct` > `22.871` → IC=-0.267 (n=428)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.871
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=2563)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.155 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0029 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.271 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.330 (n=381)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.283 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.286 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.864` → IC=+0.149 (n=249)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 18.864 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.246 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.189)

- **PATRÓN** `ibs_15` < `0.6221` → IC=+0.319 (n=70)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6221 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.189)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=732)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.162 (n=495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.184 (n=248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.193 (n=435)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5867` → IC=+0.243 (n=563)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5867 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.4673` → IC=+0.162 (n=146)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.4673 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.155 (n=439)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=732)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `9475.4181` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9475.4181 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.252 (n=1411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.243 (n=536)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7722` → IC=+0.257 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7722 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1554` → IC=+0.262 (n=1069)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1554 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.245 (n=1089)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3777` → IC=+0.275 (n=1603)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3777 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.6112` → IC=+0.272 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6112 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.392` → IC=+0.244 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.392 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.346` → IC=+0.248 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.346 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.245 (n=370)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=720)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.277 (n=272)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=818)

- **FILTRO** `sigma_ewma_delta_pct` > `6.512` → IC=-0.209 (n=252)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.512
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=838)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.187)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.187)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 29.0 (IC base=-0.187)

- **PATRÓN** `ibs_15` < `0.4054` → IC=+0.292 (n=715)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.4054 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.4507` → IC=+0.230 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4507 (IC base=-0.034)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0578` → IC=-0.228 (n=967)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0578
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=324)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.244 (n=585)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=706)

- **FILTRO** `libro_liquidez` < `2955.9488` → IC=-0.221 (n=968)

  - _Acción_: SKIP cuando `libro_liquidez` < 2955.9488
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=323)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.209)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0515` → IC=+0.270 (n=943)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0515 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1182` → IC=+0.287 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1182 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.1364` → IC=+0.306 (n=628)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1364 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7812` → IC=+0.338 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7812 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.093)

- **PATRÓN** `drift_15min` |x|≤ `0.3696` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3696 (IC base=+0.093)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.364 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.056)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.093)

- **PATRÓN** `drift_15min` |x|≤ `0.3696` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3696 (IC base=+0.093)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.364 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.056)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.292 (n=1222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.315 (n=538)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1507` → IC=+0.289 (n=814)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1507 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.223` → IC=+0.300 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.223 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=1266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.317 (n=1221)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2676` → IC=+0.318 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2676 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.387 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13583.6664` → IC=+0.307 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13583.6664 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.308 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.298 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.317 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.284 (n=216)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.287 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.306 (n=649)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.316 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.379 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.317 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.309 (n=573)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1076` → IC=+0.315 (n=382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1076 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1451` → IC=+0.297 (n=382)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1451 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.344 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8503` → IC=+0.324 (n=573)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8503 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.318 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.384 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.159 (n=89)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=268)

- **FILTRO** `ballena_activa_n` > `36.0` → IC=-0.134 (n=241)

  - _Acción_: SKIP cuando `ballena_activa_n` > 36.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=84)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=368)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=366)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.157` → IC=-0.138 (n=67)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.157
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=137)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2065` → IC=-0.259 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2065
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

- **FILTRO** `ballena_activa_n` > `595.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 595.0
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=32)

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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2685` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2685
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0061` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0061
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.075` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.075
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `drift_15min` |x|> `0.2309` → IC=-0.225 (n=38)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2309
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

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
- **PATRÓN** `ratio` < `0.9726` → IC=+0.397 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9726 (IC base=+0.177)

- **PATRÓN** `T_h` > `115.8544` → IC=+0.354 (n=2510)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.8544 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0211` → IC=+0.379 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0211 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9836` → IC=+0.154 (n=232)

  - _Acción_: Kelly boost +0.77€ cuando `T_h` > 111.9836 (IC base=+0.144)

- **PATRÓN** `ratio` < `0.9811` → IC=+0.324 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9811 (IC base=+0.144)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.312 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.298)

- **PATRÓN** `ratio` > `1.0422` → IC=+0.417 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0422 (IC base=+0.298)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9854` → IC=+0.392 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.218)

- **PATRÓN** `T_h` > `111.996` → IC=+0.353 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0298` → IC=+0.395 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0298 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.435 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.519 sube el IC de +0.163 a +0.234 en UPDOWN_GBM#15min (n=4249). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7143 sube el IC de +0.205 a +0.279 en UPDOWN_GBM#BTC#15min (n=704). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5056 sube el IC de +0.135 a +0.227 en UPDOWN_GBM#ETH#15min (n=860). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.875 sube el IC de +0.079 a +0.221 en UPDOWN_GBM#SOL#15min (n=364). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.191 a +0.267 en UPDOWN_GBM#XRP#15min (n=955). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1071 sube el IC de +0.067 a +0.170 en UPDOWN_GBM#XRP#15min (n=831). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6332 sube el IC de -0.070 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1125). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3684 sube el IC de -0.009 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=4179). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.081 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=381). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.189 a +0.319 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5867 sube el IC de +0.150 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=563). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3777 sube el IC de +0.242 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1603). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.187 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.4054 sube el IC de -0.034 a +0.292 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=715). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.209 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1364 sube el IC de -0.025 a +0.306 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=628). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.287 a +0.317 en UPDOWN_GBM_IBS_ALTO (n=1221). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.281 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=649). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8503 sube el IC de +0.293 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=573). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.366 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=696). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.361 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=350). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.368 a +0.405 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=347). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2085 | +0.086 | +219.86€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2085 | +0.086 | +219.86€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1686 | +0.087 | +184.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1686 | +0.087 | +184.22€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 84 | +0.128 | +24.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 84 | +0.128 | +24.67€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 928 | -0.025 | +78.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 928 | -0.025 | +78.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 716 | -0.045 | +57.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 716 | -0.045 | +57.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 56 | -0.069 | -6.66€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 56 | -0.069 | -6.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 44034 | -0.084 | -5632.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2609 | +0.059 | -283.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 41425 | -0.093 | -5349.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4639 | -0.117 | -760.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4639 | -0.117 | -760.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2609 | +0.059 | -283.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2609 | +0.059 | -283.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4595 | -0.115 | -892.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4595 | -0.115 | -892.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11826 | -0.025 | -1151.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11826 | -0.025 | -1151.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11910 | -0.119 | -1169.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11910 | -0.119 | -1169.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8455 | -0.127 | -1375.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8455 | -0.127 | -1375.36€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 42457 | -0.013 | +3222.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10945 | +0.005 | +1615.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 31512 | -0.019 | +1607.20€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 42457 | -0.013 | +3222.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10945 | +0.005 | +1615.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 31512 | -0.019 | +1607.20€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 167899 | +0.114 | -6810.11€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 20453 | +0.180 | -680.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 758 | -0.004 | -77.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 136888 | +0.106 | -5709.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9800 | +0.093 | -342.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 22682 | +0.106 | -1441.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 68 | -0.186 | +4.73€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 22599 | +0.108 | -1434.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 32154 | +0.125 | -530.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5497 | +0.180 | -232.08€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 22670 | +0.120 | -150.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3945 | +0.078 | -125.24€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 22736 | +0.098 | -1624.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 82 | -0.119 | -3.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 22639 | +0.100 | -1609.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 35792 | +0.124 | -699.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9144 | +0.177 | -199.18€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 23012 | +0.106 | -440.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3624 | +0.101 | -50.83€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 31826 | +0.112 | -1505.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5584 | +0.198 | -257.98€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 661 | +0.025 | -23.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 23350 | +0.095 | -1057.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2231 | +0.106 | -166.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 22709 | +0.107 | -1009.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 78 | -0.113 | +6.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 22618 | +0.108 | -1015.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 27129 | +0.194 | -1763.75€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 27129 | +0.194 | -1763.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6130 | +0.176 | -557.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6130 | +0.176 | -557.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3713 | +0.200 | -112.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3713 | +0.200 | -112.67€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6066 | +0.176 | -520.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6066 | +0.176 | -520.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5170 | +0.248 | -186.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5170 | +0.248 | -186.93€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5971 | +0.186 | -399.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5971 | +0.186 | -399.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1149 | +0.425 | -42.88€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1149 | +0.425 | -42.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 466 | +0.438 | -5.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 466 | +0.438 | -5.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 461 | +0.427 | -14.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 461 | +0.427 | -14.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 208 | +0.395 | -19.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 208 | +0.395 | -19.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 95295 | +0.201 | -6863.78€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 95295 | +0.201 | -6863.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 16412 | +0.183 | -1758.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 16412 | +0.183 | -1758.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15369 | +0.225 | -500.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15369 | +0.225 | -500.10€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16350 | +0.181 | -1710.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16350 | +0.181 | -1710.72€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 15494 | +0.218 | -617.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 15494 | +0.218 | -617.69€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 15787 | +0.202 | -1020.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 15787 | +0.202 | -1020.50€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 15883 | +0.197 | -1256.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 15883 | +0.197 | -1256.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 36578 | +0.117 | +300.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 36578 | +0.117 | +300.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 18201 | +0.118 | +194.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 18201 | +0.118 | +194.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 18377 | +0.115 | +106.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 18377 | +0.115 | +106.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2335 | +0.295 | +5.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2335 | +0.295 | +5.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1068 | +0.283 | -17.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1068 | +0.283 | -17.73€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1137 | +0.300 | +21.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1137 | +0.300 | +21.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 130 | +0.333 | +1.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 130 | +0.333 | +1.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1069 | +0.445 | +11.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1069 | +0.445 | +11.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 517 | +0.438 | -2.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 517 | +0.438 | -2.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 504 | +0.453 | +13.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 504 | +0.453 | +13.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 48 | +0.400 | +0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 48 | +0.400 | +0.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1830 | +0.068 | -81.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 724 | +0.047 | -63.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1106 | +0.081 | -18.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1397 | +0.075 | -37.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1106 | +0.081 | -18.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 351 | +0.027 | -47.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 351 | +0.027 | -47.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 73399 | +0.101 | -1767.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5912 | +0.093 | +93.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 67487 | +0.101 | -1860.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 40208 | +0.105 | -408.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5912 | +0.093 | +93.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 34296 | +0.108 | -501.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 15388 | +0.110 | -66.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 15388 | +0.110 | -66.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 17803 | +0.082 | -1292.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 17803 | +0.082 | -1292.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 908 | +0.188 | -109.47€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 908 | +0.188 | -109.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 908 | +0.188 | -109.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 908 | +0.188 | -109.47€ | 1 | 4 |
| ✅ GBM_LATE_15M | 50027 | +0.097 | +27310.79€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 50027 | +0.097 | +27310.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8324 | +0.222 | +7042.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8324 | +0.222 | +7042.93€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 7638 | +0.176 | +5962.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7638 | +0.176 | +5962.72€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 8971 | +0.204 | +6964.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8971 | +0.204 | +6964.22€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6827 | +0.050 | +2034.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6827 | +0.050 | +2034.75€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 6989 | -0.032 | +1777.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6989 | -0.032 | +1777.59€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 11278 | -0.027 | +3528.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11278 | -0.027 | +3528.59€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 53075 | +0.085 | +30081.66€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 53075 | +0.085 | +30081.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10309 | +0.000 | +5319.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10309 | +0.000 | +5319.29€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11369 | +0.007 | +2939.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11369 | +0.007 | +2939.74€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7262 | +0.287 | +8055.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7262 | +0.287 | +8055.20€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9893 | +0.014 | +2949.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9893 | +0.014 | +2949.77€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8265 | +0.041 | +3594.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8265 | +0.041 | +3594.57€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5977 | +0.312 | +7223.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5977 | +0.312 | +7223.08€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 39687 | +0.179 | +32506.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 39687 | +0.179 | +32506.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5986 | +0.237 | +5489.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5986 | +0.237 | +5489.08€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6288 | +0.144 | +4706.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6288 | +0.144 | +4706.60€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6367 | +0.223 | +5477.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6367 | +0.223 | +5477.65€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6772 | +0.133 | +5225.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6772 | +0.133 | +5225.99€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7478 | +0.121 | +5550.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7478 | +0.121 | +5550.82€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6796 | +0.230 | +6056.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6796 | +0.230 | +6056.20€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10487 | +0.125 | +5129.77€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10487 | +0.125 | +5129.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 457 | +0.158 | +289.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 457 | +0.158 | +289.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3027 | +0.130 | +1650.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3027 | +0.130 | +1650.60€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3127 | +0.131 | +1522.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3127 | +0.131 | +1522.46€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2653 | +0.095 | +1029.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2653 | +0.095 | +1029.28€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 732 | +0.146 | +378.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 732 | +0.146 | +378.06€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 50297 | +0.185 | +40834.80€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 50297 | +0.185 | +40834.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7945 | +0.247 | +7573.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7945 | +0.247 | +7573.59€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7953 | +0.141 | +5545.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7953 | +0.141 | +5545.17€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8514 | +0.233 | +7598.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8514 | +0.233 | +7598.13€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8317 | +0.139 | +6010.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8317 | +0.139 | +6010.77€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8919 | +0.120 | +6244.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8919 | +0.120 | +6244.64€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8649 | +0.236 | +7862.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8649 | +0.236 | +7862.51€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13308 | +0.208 | +10689.10€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 13308 | +0.208 | +10689.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3188 | +0.211 | +2755.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3188 | +0.211 | +2755.02€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1222 | +0.198 | +913.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1222 | +0.198 | +913.92€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3870 | +0.200 | +2866.86€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3870 | +0.200 | +2866.86€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 2020 | +0.202 | +1621.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2020 | +0.202 | +1621.62€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1954 | +0.209 | +1531.41€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1954 | +0.209 | +1531.41€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4323 | +0.053 | +1208.79€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4323 | +0.053 | +1208.79€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1539 | +0.069 | +508.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1539 | +0.069 | +508.10€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1402 | +0.053 | +423.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1402 | +0.053 | +423.22€ | 1 | 7 |
| ✅ GBM_LATE_60M#SOL | 1382 | +0.037 | +277.47€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1382 | +0.037 | +277.47€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 648 | -0.249 | -31.14€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 648 | -0.249 | -31.14€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 242 | -0.246 | -16.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 242 | -0.246 | -16.88€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 234 | -0.246 | -6.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 234 | -0.246 | -6.56€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 172 | -0.253 | -7.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 172 | -0.253 | -7.69€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1762 | +0.081 | +432.52€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1762 | +0.081 | +432.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 680 | +0.072 | +152.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 680 | +0.072 | +152.02€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 603 | +0.055 | +99.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 603 | +0.055 | +99.77€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 479 | +0.124 | +180.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 479 | +0.124 | +180.73€ | 1 | 10 |
| ✅ LATE_WINDOW_5MIN | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 198 | +0.270 | +203.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 198 | +0.270 | +203.69€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3987 | +0.097 | +920.92€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3987 | +0.097 | +920.92€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3987 | +0.097 | +920.92€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3987 | +0.097 | +920.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 766 | -0.013 | +6.72€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 766 | -0.013 | +6.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 7 | -0.058 | -1.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 231 | +0.002 | +8.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 231 | +0.002 | +8.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 199 | +0.027 | +12.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 199 | +0.027 | +12.22€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#SOL | 250 | -0.004 | +2.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 250 | -0.004 | +2.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4023 | +0.017 | +104.15€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4023 | +0.017 | +104.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 189 | +0.034 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 816 | +0.015 | +39.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 816 | +0.015 | +39.04€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1569 | +0.023 | +31.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1569 | +0.023 | +31.91€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 763 | +0.011 | +1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 763 | +0.011 | +1.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2069 | -0.040 | -29.10€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2069 | -0.040 | -29.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 623 | -0.034 | -15.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 623 | -0.034 | -15.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 722 | -0.015 | +9.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 722 | -0.015 | +9.26€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 724 | -0.069 | -23.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 724 | -0.069 | -23.31€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 12216 | -0.031 | -76.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5849 | -0.034 | -74.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6367 | -0.028 | -2.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 426 | -0.044 | -16.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 213 | -0.016 | +4.33€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 213 | -0.072 | -21.06€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3163 | -0.020 | +31.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1501 | -0.021 | +15.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1662 | -0.020 | +16.17€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1262 | -0.025 | +21.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 643 | -0.033 | +1.00€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 619 | -0.017 | +20.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2716 | -0.037 | -62.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1284 | -0.041 | -43.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1432 | -0.033 | -18.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2357 | -0.031 | -13.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1137 | -0.037 | -21.33€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1220 | -0.025 | +7.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2292 | -0.039 | -36.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1071 | -0.046 | -29.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1221 | -0.033 | -6.93€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 58976 | -0.000 | +3042.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 58976 | -0.000 | +3042.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10664 | +0.027 | +1400.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10664 | +0.027 | +1400.82€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8359 | -0.036 | -118.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8359 | -0.036 | -118.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10787 | +0.024 | +1121.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10787 | +0.024 | +1121.65€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8256 | -0.049 | -177.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8256 | -0.049 | -177.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10005 | -0.004 | +261.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10005 | -0.004 | +261.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10905 | +0.017 | +555.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10905 | +0.017 | +555.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6935 | -0.056 | -139.28€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6935 | -0.056 | -139.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1237 | -0.002 | -17.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1905 | -0.069 | -33.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1905 | -0.069 | -33.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 66 | -0.015 | -0.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 66 | -0.015 | -0.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 791 | -0.119 | -33.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 791 | -0.119 | -33.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2078 | -0.070 | -28.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2078 | -0.070 | -28.14€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M | 3373 | +0.004 | -0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3373 | +0.004 | -0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 132 | -0.037 | -1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 132 | -0.037 | -1.23€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 194 | +0.010 | -0.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 194 | +0.010 | -0.77€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 145513 | -0.077 | +1933.38€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 145513 | -0.077 | +1933.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 25389 | -0.078 | +1351.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 25389 | -0.078 | +1351.70€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 21829 | -0.100 | -1042.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 21829 | -0.100 | -1042.97€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 25712 | -0.069 | +1251.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 25712 | -0.069 | +1251.00€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 21375 | -0.097 | -656.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 21375 | -0.097 | -656.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 26081 | -0.057 | +326.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 26081 | -0.057 | +326.31€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 25127 | -0.069 | +703.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 25127 | -0.069 | +703.46€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8941 | -0.035 | -184.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8941 | -0.035 | -184.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2058 | -0.047 | -28.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2058 | -0.047 | -28.71€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2623 | -0.026 | -40.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2623 | -0.026 | -40.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1246 | -0.061 | -31.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1246 | -0.061 | -31.69€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1003 | -0.030 | -32.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1918 | +0.120 | +761.21€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1782 | +0.124 | +748.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 418 | +0.121 | +183.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 418 | +0.121 | +183.45€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 369 | +0.115 | +125.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 369 | +0.115 | +125.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 344 | +0.139 | +172.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 344 | +0.139 | +172.66€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 310 | +0.144 | +162.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 310 | +0.144 | +162.38€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 341 | +0.103 | +104.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 341 | +0.103 | +104.70€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1800 | -0.017 | -23.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1800 | -0.017 | -23.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 341 | +0.002 | +11.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 341 | +0.002 | +11.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 326 | -0.037 | -13.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 326 | -0.037 | -13.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 460 | -0.041 | -31.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 460 | -0.041 | -31.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 371 | +0.004 | +3.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 371 | +0.004 | +3.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 302 | -0.007 | +5.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 302 | -0.007 | +5.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1023 | -0.074 | -45.15€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 473 | -0.106 | -76.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 371 | -0.130 | -62.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 102 | -0.019 | -14.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 358 | -0.033 | +24.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 260 | -0.023 | +28.35€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 98 | -0.060 | -3.59€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 192 | -0.067 | +6.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 160 | -0.074 | +3.00€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 32 | -0.029 | +3.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 791 | -0.084 | -31.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 232 | -0.038 | -13.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1279 | -0.209 | -83.39€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 500 | -0.209 | -48.36€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 442 | -0.212 | -47.62€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 58 | -0.183 | -0.74€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 429 | -0.215 | -38.94€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 380 | -0.225 | -45.44€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 49 | -0.128 | +6.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 350 | -0.199 | +3.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 327 | -0.196 | +1.20€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 23 | -0.220 | +2.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1149 | -0.212 | -91.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 130 | -0.174 | +8.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 497 | +0.390 | +469.54€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 84 | +0.174 | +61.71€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 84 | +0.174 | +61.71€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 114 | +0.362 | +101.57€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 114 | +0.362 | +101.57€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 299 | +0.457 | +306.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 299 | +0.457 | +306.27€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 497 | +0.390 | +469.54€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 829 | +0.039 | +68.14€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 829 | +0.039 | +68.14€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 310 | +0.026 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 69 | +0.007 | +1.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 69 | +0.007 | +1.00€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 81 | +0.018 | +6.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 81 | +0.018 | +6.10€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 369 | +0.061 | +55.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 369 | +0.061 | +55.13€ | 0 | 4 |
| ✅ STREAK_FADE_5M | 3537 | -0.023 | -142.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3537 | -0.023 | -142.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 600 | -0.030 | -28.00€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 600 | -0.030 | -28.00€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 169 | -0.038 | -13.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 169 | -0.038 | -13.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1641 | -0.020 | -60.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1641 | -0.020 | -60.99€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 110 | -0.036 | -7.34€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 110 | -0.036 | -7.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 67 | +0.007 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 67 | +0.007 | -2.27€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11388 | +0.015 | +77.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11388 | +0.015 | +77.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2942 | +0.019 | +26.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2942 | +0.019 | +26.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2957 | +0.018 | +36.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2957 | +0.018 | +36.36€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2910 | +0.009 | -1.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2910 | +0.009 | -1.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10650 | +0.014 | -45.96€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10650 | +0.014 | -45.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4450 | +0.019 | -3.87€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4450 | +0.019 | -3.87€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3628 | +0.010 | -28.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3628 | +0.010 | -28.96€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2572 | +0.010 | -13.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2572 | +0.010 | -13.13€ | 1 | 0 |
| ✅ UPDOWN_GBM | 89853 | +0.057 | +8221.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 21765 | +0.083 | +4676.07€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2828 | +0.002 | +33.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 59583 | +0.056 | +3418.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5358 | +0.003 | +97.03€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7320 | +0.095 | +1216.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1641 | +0.161 | +744.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 85 | -0.006 | -1.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5594 | +0.077 | +472.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 20640 | +0.057 | +1791.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2999 | +0.083 | +686.08€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 790 | +0.004 | +14.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 14316 | +0.065 | +1020.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2420 | +0.000 | +67.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 115 | -0.073 | +2.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9534 | +0.073 | +1037.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1616 | +0.150 | +652.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 82 | +0.024 | -0.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7836 | +0.058 | +385.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 21426 | +0.048 | +1445.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5314 | +0.071 | +797.05€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 758 | +0.007 | +18.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 13282 | +0.048 | +606.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1965 | +0.005 | +21.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 107 | -0.105 | +1.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 19393 | +0.037 | +1079.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5608 | +0.036 | +452.03€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 719 | -0.010 | +2.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11998 | +0.044 | +623.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 973 | +0.004 | +7.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 95 | -0.139 | -6.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 11538 | +0.070 | +1653.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4587 | +0.101 | +1343.35€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 394 | +0.010 | -0.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6557 | +0.051 | +309.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 317 | -0.105 | -1.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 928 | +0.366 | +339.90€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 928 | +0.366 | +339.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 466 | +0.361 | +160.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 466 | +0.361 | +160.58€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 462 | +0.368 | +179.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 462 | +0.368 | +179.31€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 22069 | -0.022 | +5298.78€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 22069 | -0.022 | +5298.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1805 | -0.053 | +524.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1805 | -0.053 | +524.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4141 | -0.114 | +186.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4141 | -0.114 | +186.46€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 981 | +0.216 | +799.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 981 | +0.216 | +799.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2886 | +0.218 | +1834.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2886 | +0.218 | +1834.91€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6274 | -0.061 | +870.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6274 | -0.061 | +870.93€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5982 | -0.065 | +1082.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5982 | -0.065 | +1082.62€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 269 | +0.065 | +25.83€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 269 | +0.065 | +25.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 269 | +0.065 | +25.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 269 | +0.065 | +25.83€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1628 | +0.287 | +1369.72€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1628 | +0.287 | +1369.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 865 | +0.281 | +681.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 865 | +0.281 | +681.44€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 763 | +0.293 | +688.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 763 | +0.293 | +688.29€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 844 | -0.114 | -83.69€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 844 | -0.114 | -83.69€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 259 | -0.086 | -20.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 259 | -0.086 | -20.70€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 108 | -0.173 | -3.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 108 | -0.173 | -3.21€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4147 | +0.302 | +1918.86€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1552 | +0.258 | +190.79€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1593 | +0.295 | +688.71€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1002 | +0.381 | +1039.37€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.024 n=1109 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1109 IC=+0.024 PNL=+51.98€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 766 celda(s) pasan gate riguroso completo de 2801 evaluadas (n>=40) y 3894 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=5603 IC=+0.036 PNL=+447.78€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1593/15 IC=+0.295 PNL=+688.71€ | BTC: n=1552/15 IC=+0.258 PNL=+190.79€ | SOL: n=1002/15 IC=+0.381 PNL=+1039.37€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.142 n=947/60 | contraria IC=+0.188 n=976 | gap=-0.046 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=528, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1963/40 IC=+0.005 PNL=+21.75€ | BTC#60min: n=2418/40 IC=+0.000 PNL=+67.87€ | SOL#60min: n=973/40 IC=+0.004 PNL=+7.49€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=645650 | tras_1loss IC=+0.097 n=490178 | tras_2loss IC=+0.067 n=197270/40 | gap=-0.021 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=872 PNL=+625.28€
  - _Datos_: n=872 IC=+0.189 PNL=+625.28€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.153 > 0.08 con n=1008 PNL=+530.00€
  - _Datos_: n=1008 IC=+0.153 PNL=+530.00€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=71 PNL=+38.37€
  - _Datos_: n=71 IC=+0.171 PNL=+38.37€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3389 PNL=+1891.17€
  - _Datos_: n=3389 IC=+0.333 PNL=+1891.17€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=865 IC=+0.066 PNL=+85.30€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=865 IC=+0.066 PNL=+85.30€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=95 IC=+0.191 PNL=+66.70€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=95 IC=+0.191 PNL=+66.70€

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
  - _Estado_: n=3589 IC=+0.004 PNL=-3.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3589 IC=+0.004 PNL=-3.82€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1765 IC=-0.000 PNL=+100.93€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1765 IC=-0.000 PNL=+100.93€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1109 IC=+0.024 PNL=+51.98€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1109 IC=+0.024 PNL=+51.98€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.163 > 0.1 con n=5655 PNL=+3256.13€
  - _Datos_: n=5655 IC=+0.163 PNL=+3256.13€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2999 IC=+0.083 PNL=+686.08€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2999 IC=+0.083 PNL=+686.08€

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
  - _Estado_: n=1131 IC=+0.037 PNL=+93.95€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1131 IC=+0.037 PNL=+93.95€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=146 IC=+0.013 PNL=+1.57€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=146 IC=+0.013 PNL=+1.57€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.270 n=198) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=198 IC=+0.270 PNL=+203.69€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=1124 PNL=+469.05€
  - _Datos_: n=1124 IC=+0.123 PNL=+469.05€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=226 IC=-0.097 PNL=+16.29€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=226 IC=-0.097 PNL=+16.29€

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
  - _Estado_: n=36104 IC=+0.073 PNL=+5092.76€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=36104 IC=+0.073 PNL=+5092.76€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=661 PNL=+93.97€
  - _Datos_: n=661 IC=-0.135 PNL=+93.97€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3319 IC=+0.067 PNL=+432.33€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3319 IC=+0.067 PNL=+432.33€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=168 IC=-0.118 PNL=-1.49€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=168 IC=-0.118 PNL=-1.49€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.1 con n=958 PNL=+249.06€
  - _Datos_: n=958 IC=+0.105 PNL=+249.06€

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
  - _Estado_: n=38164 IC=-0.136 PNL=+2575.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=38164 IC=-0.136 PNL=+2575.65€

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
  - _Estado_: n=3939 IC=+0.128 PNL=+2534.93€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3939 IC=+0.128 PNL=+2534.93€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=9270 IC=+0.055 PNL=+784.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=9270 IC=+0.055 PNL=+784.88€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=4071 PNL=+2272.55€
  - _Datos_: n=4071 IC=+0.098 PNL=+2272.55€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.219 < -0.1 con n=4061 PNL=-320.20€
  - _Datos_: n=4061 IC=-0.219 PNL=-320.20€

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
  - _Estado_: n=80 IC=+0.037 PNL=+14.18€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=80 IC=+0.037 PNL=+14.18€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2019) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2019 IC=+0.096 PNL=+411.17€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=640) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=640 IC=+0.410 PNL=+919.25€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=16403 IC=+0.183 PNL=-1757.08€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=16403 IC=+0.183 PNL=-1757.08€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.228 > 0.1 con n=259 PNL=+177.85€
  - _Datos_: n=259 IC=+0.228 PNL=+177.85€
