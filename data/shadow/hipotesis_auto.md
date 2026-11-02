# Hipótesis automáticas — 2026-11-02 20:30 UTC
_Generado por shadow_postmortem.py sobre 1165793 resoluciones (PNL=+157691.11€)_

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=998)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `3323.3759` → IC=+0.138 (n=612)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3323.3759 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.220 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.192 (n=264)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 67.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.6114` → IC=+0.242 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6114 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.107` → IC=+0.206 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.107 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=898)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3054.6814` → IC=+0.140 (n=703)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3054.6814 (IC base=+0.138)

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

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.49 (IC base=+0.156)

- **PATRÓN** `n_ballena_banda` > `33.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 33.0 (IC base=+0.156)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.156)

- **PATRÓN** `banda_hit_calibrado` > `0.6045` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `banda_hit_calibrado` > 0.6045 (IC base=+0.156)

- **PATRÓN** `banda_z` > `2.461` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.461 (IC base=+0.156)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `2452.7664` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2452.7664 (IC base=+0.156)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `135.72` → IC=-0.215 (n=11167)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.72
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=33503)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.68` → IC=-0.256 (n=1169)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.68
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3508)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.37` → IC=-0.306 (n=1155)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.37
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3468)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.68` → IC=-0.245 (n=3018)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.68
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9056)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.0` → IC=-0.258 (n=2135)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=6407)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.211 (n=25386)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8557.9163` → IC=+0.162 (n=2223)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8557.9163 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=21679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=39144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=20024)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=7904)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6766.8992` → IC=+0.149 (n=3054)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6766.8992 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2068)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2653)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `9392.7207` → IC=+0.182 (n=1846)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9392.7207 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2705)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16111.278` → IC=+0.186 (n=698)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16111.278 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=548)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=1290)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.166 (n=4137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.374 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=2195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.345 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=2547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=1054)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.260 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=1371)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3079.6088` → IC=+0.135 (n=231)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3079.6088 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.256 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=712)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.158 (n=451)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.55 (IC base=+0.050)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=1171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=21738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=18401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.229 (n=9033)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.176 (n=4945)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4743)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.175 (n=4134)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.215 (n=2806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.216 (n=2492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.293 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.213)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=4878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=5054)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3800)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=4163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.357 (n=1423)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=4072)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=3559)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.429 (n=903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4389.547` → IC=+0.444 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4389.547 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.458 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12295.9377` → IC=+0.447 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12295.9377 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.434 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.432 (n=353)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.434 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `2746.8442` → IC=+0.432 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2746.8442 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.398 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.396)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=28417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=28670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=4219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=9039)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=12882)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4075)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=4878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=10026)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=5974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=4535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.270 (n=4025)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` > `0.745` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.745
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **FILTRO** `libro_liquidez` < `3254.1654` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 3254.1654
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=4039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=4209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=4724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=4689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=4933)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=10154)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.141 (n=10423)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.37` → IC=+0.140 (n=9402)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.37 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=4958)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.146 (n=4712)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.66` → IC=+0.146 (n=4678)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.66 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=5196)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=5711)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.23` → IC=+0.139 (n=6232)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.23 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.309 (n=1281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.366 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.303 (n=905)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.299 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.299)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.360 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.336)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.382 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.368 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.336)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.465 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.450)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.454 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.450)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.453 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.450)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.451 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.450)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.414 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.402)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

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
- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4734` → IC=+0.138 (n=15956)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4734 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=16137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=11108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.3732` → IC=+0.164 (n=15957)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.3732 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7718` → IC=+0.278 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7718 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.573` → IC=+0.182 (n=7960)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.573 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.696` → IC=+0.266 (n=4196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.696 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.242 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3525` → IC=+0.228 (n=5173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3525 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=8064)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `4686.8683` → IC=+0.145 (n=5319)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4686.8683 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.121 (n=9942)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.006 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.6792` → IC=+0.132 (n=22597)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6792 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.5986` → IC=+0.186 (n=1306)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5986 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.159` → IC=+0.188 (n=7744)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.159 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.8636` → IC=+0.190 (n=5336)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8636 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.231 (n=1978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `1.4565` → IC=+0.204 (n=13608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4565 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.226 (n=13490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.080)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3615` → IC=+0.210 (n=3423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3615 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=1661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9843` → IC=+0.280 (n=1552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9843 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.61` → IC=+0.280 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.61 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.261 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.210 (n=3276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=3767)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2061.02` → IC=+0.210 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.02 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.220 (n=3100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.242 (n=2983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0893` → IC=+0.276 (n=995)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0893 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=1101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5529` → IC=+0.259 (n=2982)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5529 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.245 (n=2696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.258 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.2756` → IC=+0.241 (n=2496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2756 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.5498` → IC=+0.241 (n=2534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5498 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=3436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1255.04` → IC=+0.245 (n=2982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1255.04 (IC base=+0.240)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.229 (n=1894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1079` → IC=+0.257 (n=1250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1079 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=2019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9185` → IC=+0.266 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9185 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1851` → IC=+0.235 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1851 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.038` → IC=+0.258 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.038 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.225 (n=2842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6992` → IC=+0.229 (n=2538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6992 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.267 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.225 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.4279` → IC=+0.251 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4279 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.149 (n=3033)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0062 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.153 (n=1011)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=1125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.7115` → IC=+0.165 (n=3031)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7115 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.735` → IC=+0.136 (n=492)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 10.735 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.01` → IC=+0.131 (n=2775)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.01 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.134 (n=3031)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2004 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.149 (n=1106)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.1376` → IC=+0.134 (n=2559)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1376 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=3931)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `205.0` → IC=+0.164 (n=1257)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 205.0 (IC base=+0.127)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.216 (n=1205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=3794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.109` → IC=+0.276 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.109 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.197 (n=3227)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.212 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.7237` → IC=+0.206 (n=1596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7237 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=4342)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2037.9984` → IC=+0.202 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2037.9984 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.225 (n=2906)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.239 (n=1454)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=1248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.223 (n=1500)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0387` → IC=+0.269 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0387 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.068` → IC=+0.265 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.068 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.263 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1515` → IC=+0.227 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1515 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1920.8826` → IC=+0.223 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1920.8826 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.224 (n=3104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.165 (n=183)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=4356)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.161 (n=624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.233 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.137` → IC=+0.336 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.137 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.3345` → IC=+0.329 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3345 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.199 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `0.8656` → IC=+0.328 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8656 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `0.6945` → IC=+0.339 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6945 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` < `0.0775` → IC=+0.331 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0775 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.333 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `1.4167` → IC=+0.339 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4167 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `2.258` → IC=+0.334 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.258 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.334 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.181 (n=1135)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.0909 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.3288` → IC=+0.164 (n=540)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3288 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1378` → IC=+0.143 (n=1980)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1378 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8356` → IC=+0.157 (n=1410)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8356 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.207 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.7767` → IC=+0.149 (n=1356)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7767 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1547` → IC=+0.160 (n=922)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1547 (IC base=+0.045)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=683)

- **FILTRO** `ibs_20min` < `0.2692` → IC=-0.163 (n=203)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=610)

- **FILTRO** `ibs_20min` > `0.2059` → IC=-0.132 (n=4267)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2059
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=2106)

- **FILTRO** `sigma_ewma_delta_pct` > `8.42` → IC=-0.222 (n=685)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.42
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=5688)

- **PATRÓN** `ibs_20min` > `0.7558` → IC=+0.174 (n=277)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.7558 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.045` → IC=+0.153 (n=191)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.045 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1586` → IC=+0.278 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1586 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4923` → IC=+0.283 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4923 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.4523` → IC=+0.262 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4523 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.268 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.2059` → IC=+0.153 (n=2106)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2059 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.2947` → IC=+0.278 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2947 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.6941` → IC=+0.308 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6941 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.295 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4676` → IC=+0.303 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4676 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7707` → IC=-0.153 (n=3179)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7707
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=1639)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.168 (n=1103)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3715)

- **FILTRO** `ibs_20min` > `0.7458` → IC=-0.198 (n=1696)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7458
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=5091)

- **PATRÓN** `dist_vwap_pct` > `0.9866` → IC=+0.362 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9866 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` < `0.2464` → IC=+0.309 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2464 (IC base=-0.062)

- **PATRÓN** `volumen_regimen` > `0.7071` → IC=+0.321 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7071 (IC base=-0.062)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.307 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.311 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4404 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.8711` → IC=+0.310 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8711 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.274 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` < `0.7241` → IC=+0.272 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7241 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `1.0685` → IC=+0.287 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0685 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.1693` → IC=+0.287 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1693 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.266 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.4346` → IC=+0.270 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4346 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.200 (n=6900)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.8734` → IC=+0.287 (n=9386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8734 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.9236` → IC=+0.302 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9236 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.531` → IC=+0.166 (n=9262)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.531 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `1.1757` → IC=+0.269 (n=7575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1757 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.275 (n=6768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.287 (n=2275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `1.458` → IC=+0.273 (n=4016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.458 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `2.6516` → IC=+0.280 (n=4015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6516 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.306 (n=11642)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.090)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.157 (n=6673)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0099 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.6449` → IC=+0.151 (n=20002)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6449 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.2503` → IC=+0.275 (n=6654)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2503 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.703` → IC=+0.274 (n=2865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.703 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `1.1936` → IC=+0.273 (n=2170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1936 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.325 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `1.5766` → IC=+0.298 (n=4194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5766 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` > `2.2812` → IC=+0.294 (n=4321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2812 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.304 (n=9482)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 74.0 (IC base=+0.079)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5794` → IC=-0.163 (n=2826)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5794
  - _Potencial_: sin este filtro IC_bueno=+0.206 (n=2826)

- **FILTRO** `ibs_20min` > `0.7207` → IC=-0.226 (n=1230)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7207
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=3694)

- **FILTRO** `sigma_ewma_delta_pct` > `4.203` → IC=-0.229 (n=1060)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.203
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3864)

- **PATRÓN** `ibs_20min` > `0.9307` → IC=+0.333 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9307 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.071` → IC=+0.186 (n=1894)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.071 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.325 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4454` → IC=+0.275 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4454 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.294 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.311 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.1719` → IC=+0.158 (n=1232)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1719 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.403 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4194` → IC=+0.424 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4194 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.399 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1691` → IC=+0.222 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1691 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.206 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1952 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.209 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.250 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.232 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4449` → IC=+0.210 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4449 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.240 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 267.0 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.1265` → IC=+0.249 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1265 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1631` → IC=+0.238 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1631 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.243 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6228 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2715` → IC=+0.309 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2715 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.246 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1523` → IC=+0.256 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1523 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.252 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.324 (n=1335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=2947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.464` → IC=+0.301 (n=1779)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.464 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.293 (n=2582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.7745` → IC=+0.285 (n=2550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7745 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.289 (n=3511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2037.62` → IC=+0.295 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2037.62 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.304 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.335 (n=1196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.301)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.321 (n=1159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.303 (n=1188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.301)

- **PATRÓN** `ibs_20min` < `0.0093` → IC=+0.302 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0093 (IC base=+0.301)

- **PATRÓN** `ibs_20min` > `0.1362` → IC=+0.311 (n=1756)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1362 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.335` → IC=+0.313 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.335 (IC base=+0.301)

- **PATRÓN** `volumen_pendiente_norm` < `0.1981` → IC=+0.301 (n=2591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1981 (IC base=+0.301)

- **PATRÓN** `volumen_pendiente_norm` > `0.3437` → IC=+0.313 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3437 (IC base=+0.301)

- **PATRÓN** `volumen_spike_ratio` < `1.5881` → IC=+0.300 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5881 (IC base=+0.301)

- **PATRÓN** `volumen_spike_ratio` > `2.7263` → IC=+0.315 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7263 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.305 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `1923.24` → IC=+0.312 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1923.24 (IC base=+0.301)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.308 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.301)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7292` → IC=-0.184 (n=1288)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7292
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3867)

- **PATRÓN** `ibs_20min` > `0.8588` → IC=+0.165 (n=1252)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8588 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1447` → IC=+0.233 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1447 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.2055` → IC=+0.232 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2055 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.236 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6711` → IC=+0.231 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6711 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.236 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.235 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4586` → IC=+0.238 (n=1733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4586 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.255 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1481` → IC=+0.244 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1481 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `1.1889` → IC=+0.248 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1889 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.302 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.7888` → IC=+0.281 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7888 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.4311` → IC=+0.262 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4311 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.276 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7447` → IC=-0.241 (n=2146)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7447
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=2146)

- **FILTRO** `ibs_20min` > `0.6311` → IC=-0.233 (n=1034)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6311
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=3106)

- **FILTRO** `sigma_ewma_delta_pct` > `8.342` → IC=-0.248 (n=474)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.342
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=3666)

- **PATRÓN** `ibs_20min` > `0.7447` → IC=+0.311 (n=2146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7447 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.2146` → IC=+0.345 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2146 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.484` → IC=+0.148 (n=1729)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 2.484 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.340 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6967` → IC=+0.335 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6967 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1582` → IC=+0.335 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1582 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.356 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4313` → IC=+0.361 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4313 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.354 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6311` → IC=+0.142 (n=3106)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.6311 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.2963` → IC=+0.259 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2963 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.03` → IC=+0.120 (n=2914)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` < 3.03 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.281 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.275 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.4448` → IC=+0.263 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4448 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.277 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.049)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=1974)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.314 (n=2234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.764` → IC=+0.350 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.764 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.337 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.01` → IC=+0.331 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.01 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.077` → IC=+0.314 (n=2516)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.077 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.63` → IC=+0.322 (n=2208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.63 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.351 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.4273` → IC=+0.325 (n=2124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4273 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `2956.4998` → IC=+0.318 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2956.4998 (IC base=+0.313)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.344 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.345 (n=1567)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.322 (n=1186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.316 (n=1147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.335 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` < `0.2343` → IC=+0.320 (n=2272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2343 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.64` → IC=+0.331 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.64 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.320 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.212` → IC=+0.344 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.212 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.368 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` < `1.4114` → IC=+0.325 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4114 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `2.1339` → IC=+0.317 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1339 (IC base=+0.314)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.227 (n=5155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.1218` → IC=+0.194 (n=6800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1218 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=16035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.5417` → IC=+0.233 (n=15456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5417 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1618` → IC=+0.207 (n=5997)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1618 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.136` → IC=+0.254 (n=4030)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.136 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.157 (n=10292)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1861 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.6257` → IC=+0.156 (n=10291)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6257 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.206 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6068` → IC=+0.188 (n=5007)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6068 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.196 (n=14382)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 90.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.190 (n=6660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0056 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.222 (n=5030)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=5679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5192` → IC=+0.239 (n=15088)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5192 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.194 (n=2410)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.578` → IC=+0.186 (n=13423)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.578 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1807` → IC=+0.164 (n=10746)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1807 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.222 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6394` → IC=+0.190 (n=4767)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6394 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.196 (n=14075)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 95.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.260 (n=1122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.807` → IC=+0.274 (n=2279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.807 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.692` → IC=+0.329 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.692 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.289 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.8355` → IC=+0.222 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8355 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.225 (n=2427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2829)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.258 (n=2054)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0974` → IC=+0.307 (n=904)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0974 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=2128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=1873)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4232` → IC=+0.271 (n=2054)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4232 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.259 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.280 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.280 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7197` → IC=+0.254 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7197 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1499.4991` → IC=+0.265 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1499.4991 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.256 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.200 (n=787)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1573` → IC=+0.162 (n=1573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1573 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=2469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.2688` → IC=+0.212 (n=2358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2688 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.213 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.848` → IC=+0.206 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.848 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.145 (n=1038)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6958 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.0617` → IC=+0.137 (n=1069)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0617 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.179 (n=366)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.5038` → IC=+0.150 (n=1019)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5038 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.4689` → IC=+0.146 (n=772)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4689 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `406.0` → IC=+0.139 (n=2280)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 406.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.172 (n=2493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0063 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2365` → IC=+0.168 (n=2195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2365 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=1196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.206 (n=2493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6112 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.1` → IC=+0.180 (n=470)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.1 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.063` → IC=+0.145 (n=2184)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.063 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.159 (n=2493)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2004 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.148 (n=2156)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.1332` → IC=+0.148 (n=2085)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1332 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.184 (n=1022)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 215.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.236 (n=1186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.3959` → IC=+0.224 (n=2301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3959 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.306 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.212 (n=2268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3544` → IC=+0.229 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3544 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7634` → IC=+0.211 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7634 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.222 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1926.5448` → IC=+0.223 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.5448 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.247 (n=2016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4179` → IC=+0.262 (n=2015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4179 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.285 (n=876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0308` → IC=+0.289 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0308 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.202` → IC=+0.284 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.202 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3589` → IC=+0.293 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3589 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.7622` → IC=+0.239 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7622 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1736` → IC=+0.248 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1736 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1915.9344` → IC=+0.249 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.9344 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.245 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.204 (n=847)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.192 (n=843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2661` → IC=+0.199 (n=2530)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2661 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1379` → IC=+0.188 (n=1493)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1379 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.422` → IC=+0.197 (n=434)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.422 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8476` → IC=+0.145 (n=1686)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8476 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.178 (n=377)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.8252` → IC=+0.139 (n=1651)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8252 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.5272` → IC=+0.157 (n=826)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5272 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `6834.4767` → IC=+0.202 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6834.4767 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.144 (n=2465)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 131.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.165 (n=2363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0065 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3947` → IC=+0.142 (n=2686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3947 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6725` → IC=+0.185 (n=2686)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6725 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.158` → IC=+0.154 (n=2701)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.158 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.148 (n=649)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.153 (n=1792)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8525 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.181 (n=403)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8084` → IC=+0.130 (n=1692)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8084 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4241` → IC=+0.127 (n=2537)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4241 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6206.6509` → IC=+0.184 (n=1218)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 6206.6509 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.133 (n=2199)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 109.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.166 (n=1283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.011 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=1356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4762` → IC=+0.211 (n=2823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4762 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.190 (n=1547)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.189` → IC=+0.289 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.189 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.175` → IC=+0.133 (n=2823)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.175 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.7039` → IC=+0.123 (n=2522)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7039 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.131 (n=2880)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5416` → IC=+0.137 (n=1207)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5416 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=2947)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2643.3921` → IC=+0.200 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2643.3921 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.142 (n=1192)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 21.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.142 (n=2938)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0116 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.162 (n=980)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1103 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3004)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.64` → IC=+0.219 (n=2937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.64 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2083` → IC=+0.146 (n=2870)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2083 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.32` → IC=+0.137 (n=2594)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.32 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1763` → IC=+0.128 (n=2937)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1763 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.140 (n=403)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5411` → IC=+0.124 (n=1216)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.5411 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4425` → IC=+0.127 (n=921)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.4425 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2529.6356` → IC=+0.183 (n=1332)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2529.6356 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.125 (n=2739)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.248 (n=2307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1667` → IC=+0.244 (n=1136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1667 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.231 (n=2319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6646` → IC=+0.259 (n=2581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6646 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1804` → IC=+0.233 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1804 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.566` → IC=+0.260 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.566 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.8443` → IC=+0.236 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8443 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2328` → IC=+0.269 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2328 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.229 (n=2517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8104` → IC=+0.234 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8104 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2947.9372` → IC=+0.237 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.9372 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.240 (n=1158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.249 (n=1196)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.5667` → IC=+0.246 (n=2633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5667 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.255 (n=1287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.263 (n=2643)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3018` → IC=+0.242 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3018 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.222` → IC=+0.270 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.222 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.240 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.869 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6418` → IC=+0.242 (n=2633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6418 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.290 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8332` → IC=+0.234 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8332 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.434` → IC=+0.239 (n=2470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.434 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.207 (n=1303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.1306` → IC=+0.184 (n=1718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1306 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=3495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.3266` → IC=+0.202 (n=3905)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3266 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.7907` → IC=+0.198 (n=587)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.7907 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.551` → IC=+0.197 (n=1669)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.551 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8628` → IC=+0.183 (n=2357)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8628 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.174 (n=1179)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1939 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.173 (n=1577)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4285` → IC=+0.176 (n=1268)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4285 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=4380)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2598.5436` → IC=+0.175 (n=3489)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2598.5436 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.189 (n=1851)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1986 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.126 (n=1828)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.197 (n=1059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0059 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1001` → IC=+0.235 (n=466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1001 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.214 (n=962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.2178` → IC=+0.214 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2178 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.212 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.957` → IC=+0.200 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.957 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.414` → IC=+0.182 (n=1113)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.414 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.196 (n=706)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8799 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1502` → IC=+0.185 (n=1114)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1502 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0702` → IC=+0.184 (n=422)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0702 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1871` → IC=+0.196 (n=913)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1871 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16016.8351` → IC=+0.195 (n=480)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16016.8351 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.171 (n=433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.003 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.6298` → IC=+0.142 (n=1139)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.6298 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.1609` → IC=+0.135 (n=338)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1609 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.171 (n=561)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 162.0 (IC base=+0.089)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.227 (n=805)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.190 (n=805)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=1261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.635` → IC=+0.252 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.635 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.7717` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.7717 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2032` → IC=+0.182 (n=1091)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2032 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.838` → IC=+0.217 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.838 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8339` → IC=+0.196 (n=805)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8339 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.203 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.187 (n=397)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.7866` → IC=+0.194 (n=794)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7866 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.1034` → IC=+0.178 (n=396)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1034 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `8078.9503` → IC=+0.143 (n=538)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8078.9503 (IC base=+0.072)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.6923` → IC=-0.167 (n=352)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6923
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=1058)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.157 (n=429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.171 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.4828` → IC=+0.196 (n=972)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.4828 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.97` → IC=+0.218 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.97 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.017` → IC=+0.239 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.017 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0549` → IC=+0.148 (n=855)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0549 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.146 (n=869)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7037 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.161 (n=181)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.157 (n=313)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1481` → IC=+0.136 (n=426)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.1481 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=1021)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2733.5431` → IC=+0.173 (n=441)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2733.5431 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.3793` → IC=+0.176 (n=707)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3793 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `2858.4736` → IC=+0.156 (n=353)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2858.4736 (IC base=+0.052)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0164` → IC=+0.228 (n=200)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0164 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.2664` → IC=+0.173 (n=200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2664 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.231 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.7321` → IC=+0.206 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7321 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.3016` → IC=+0.191 (n=147)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3016 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `1.1352` → IC=+0.175 (n=336)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 1.1352 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.697` → IC=+0.196 (n=294)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 5.697 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `1.1751` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1751 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` < `0.078` → IC=+0.182 (n=256)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.078 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.8264` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.8264 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.4339` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.4339 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.189 (n=345)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.03 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `2477.985` → IC=+0.192 (n=199)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2477.985 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.172 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0129 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2894` → IC=+0.148 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.2894 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.1967` → IC=+0.169 (n=143)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1967 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1803` → IC=+0.142 (n=266)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1803 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.232` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 5.232 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8744` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8744 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1104` → IC=+0.143 (n=295)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1104 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2284` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2284 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5322` → IC=+0.207 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5322 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.7332` → IC=+0.148 (n=103)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.7332 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1974.5144` → IC=+0.142 (n=325)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1974.5144 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.158 (n=302)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 19.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.230 (n=6733)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=21072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.434` → IC=+0.229 (n=20196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.434 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.8701` → IC=+0.210 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8701 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.054` → IC=+0.253 (n=4958)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.054 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.161 (n=13581)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2185 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.203 (n=3643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6207` → IC=+0.192 (n=6565)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6207 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.202 (n=18818)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.198 (n=8165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0059 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.198 (n=6176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.012 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.4821` → IC=+0.195 (n=18526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4821 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.59` → IC=+0.242 (n=18525)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.59 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.575` → IC=+0.204 (n=2526)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.575 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.448` → IC=+0.196 (n=18021)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 3.448 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `1.0569` → IC=+0.166 (n=10965)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.0569 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.255 (n=2533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.8642` → IC=+0.199 (n=11778)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.8642 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.207 (n=17424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.192)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.8598` → IC=+0.300 (n=2167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8598 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.692` → IC=+0.336 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.692 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.289 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.445` → IC=+0.232 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.445 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.288` → IC=+0.238 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.288 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=3563)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `2058.92` → IC=+0.237 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2058.92 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.253 (n=1999)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.232)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.269 (n=2867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1225` → IC=+0.292 (n=1262)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1225 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.268 (n=2606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.5333` → IC=+0.286 (n=2867)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5333 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0967` → IC=+0.268 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0967 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.293 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5629` → IC=+0.268 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5629 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6599` → IC=+0.273 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6599 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.267 (n=3309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1773.87` → IC=+0.274 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1773.87 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.273 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.184 (n=1101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.003 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1047` → IC=+0.151 (n=1453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1047 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=3442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.2055` → IC=+0.190 (n=3303)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2055 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3177` → IC=+0.202 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3177 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.249` → IC=+0.158 (n=530)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.249 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.069` → IC=+0.136 (n=2899)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.069 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.158 (n=1102)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6362 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0745` → IC=+0.138 (n=1498)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0745 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.0724` → IC=+0.139 (n=2948)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.0724 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.177 (n=475)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1556` → IC=+0.143 (n=2850)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1556 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5212` → IC=+0.138 (n=2894)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5212 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `227.0` → IC=+0.158 (n=1065)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 227.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.160 (n=2831)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.175 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=1033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.6835` → IC=+0.184 (n=2830)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6835 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.047` → IC=+0.144 (n=1354)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.047 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.146 (n=2830)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1913 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2189` → IC=+0.193 (n=525)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2189 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.141 (n=908)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7755` → IC=+0.142 (n=1815)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7755 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=3672)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.150 (n=884)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 230.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.256 (n=1123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.161` → IC=+0.320 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.161 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.227 (n=2996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7399` → IC=+0.237 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7399 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1933.909` → IC=+0.239 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.909 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.248 (n=2816)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.263 (n=1409)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.266 (n=1211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0526` → IC=+0.303 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0526 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.326` → IC=+0.302 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.326 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3487` → IC=+0.307 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3487 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1605` → IC=+0.257 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1605 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1918.06` → IC=+0.252 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.06 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.251 (n=2648)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.186 (n=1535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0041 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4315` → IC=+0.149 (n=3484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4315 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=3622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8958` → IC=+0.276 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8958 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1949` → IC=+0.167 (n=1605)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1949 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.96` → IC=+0.157 (n=1559)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.96 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.861` → IC=+0.155 (n=2323)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.861 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.184 (n=616)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5206` → IC=+0.158 (n=1497)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5206 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7283.8545` → IC=+0.239 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7283.8545 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.152 (n=1494)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 69.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.159 (n=2931)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0077 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.149 (n=2929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=1076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.715` → IC=+0.193 (n=2929)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.715 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1496` → IC=+0.150 (n=2719)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1496 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.109` → IC=+0.162 (n=584)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.109 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6144` → IC=+0.155 (n=977)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6144 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.222 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.22` → IC=+0.142 (n=2485)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.22 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5368` → IC=+0.147 (n=2523)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5368 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `6239.7898` → IC=+0.211 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6239.7898 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.149 (n=1909)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 94.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.149 (n=1603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.011 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=2502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.192 (n=3528)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4333 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0121` → IC=+0.207 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0121 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.391` → IC=+0.264 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.391 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8786` → IC=+0.134 (n=2353)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8786 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.123 (n=3348)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.491` → IC=+0.122 (n=3447)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.491 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=3684)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2705.6346` → IC=+0.240 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2705.6346 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.128 (n=1156)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.156 (n=2938)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0106 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1367` → IC=+0.153 (n=1113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1367 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=1569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6627` → IC=+0.214 (n=3338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6627 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.103` → IC=+0.148 (n=3217)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.103 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.151 (n=1113)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6385 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.174 (n=584)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4348` → IC=+0.157 (n=1052)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4348 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2587.456` → IC=+0.206 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.456 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.136 (n=3161)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 51.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.258 (n=2920)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=3416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.241 (n=2929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.6146` → IC=+0.272 (n=2919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6146 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1912` → IC=+0.252 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1912 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.248` → IC=+0.281 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.248 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2221` → IC=+0.240 (n=3269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2221 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.645` → IC=+0.241 (n=3267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.645 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.260 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5041` → IC=+0.258 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5041 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2947.266` → IC=+0.246 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.266 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.263 (n=1122)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.272 (n=3366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.169` → IC=+0.279 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.169 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `1.2193` → IC=+0.261 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2193 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.306 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.241 (n=3158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.238 (n=3103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.240)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5706)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.245 (n=1951)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.5012` → IC=+0.225 (n=5851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5012 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9329` → IC=+0.253 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9329 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.427` → IC=+0.221 (n=4285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.427 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.57` → IC=+0.223 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.57 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.552` → IC=+0.217 (n=5204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.552 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.7091` → IC=+0.228 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7091 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.8841` → IC=+0.219 (n=2885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8841 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.1055` → IC=+0.218 (n=5457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1055 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.1653` → IC=+0.222 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1653 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.4524` → IC=+0.225 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4524 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `3743.9504` → IC=+0.226 (n=3901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3743.9504 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4908` → IC=+0.213 (n=4291)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4908 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=1445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=1895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.6115` → IC=+0.204 (n=3776)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6115 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6563` → IC=+0.209 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6563 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2381` → IC=+0.196 (n=3992)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2381 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.786` → IC=+0.210 (n=3849)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.786 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.205 (n=3598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.201 (n=3950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2222` → IC=+0.201 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2222 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5327` → IC=+0.203 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5327 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1859` → IC=+0.207 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1859 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.215 (n=2826)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.199)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.293 (n=400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.277 (n=907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.2427` → IC=+0.288 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2427 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` < `0.3186` → IC=+0.280 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3186 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.096` → IC=+0.288 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.096 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.699` → IC=+0.266 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.699 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.269 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `0.8748` → IC=+0.285 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8748 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.345 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `2.4928` → IC=+0.271 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4928 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.269 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `12854.4059` → IC=+0.277 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12854.4059 (IC base=+0.266)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.262 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.191 (n=1502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.186 (n=556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.1372` → IC=+0.195 (n=661)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1372 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.6858` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6858 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.299` → IC=+0.198 (n=1473)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.299 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.0935` → IC=+0.189 (n=1323)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.0935 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.195 (n=457)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.4957` → IC=+0.183 (n=1494)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.4957 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.180 (n=996)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `14608.6008` → IC=+0.181 (n=681)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 14608.6008 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `685.0` → IC=+0.189 (n=1456)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 685.0 (IC base=+0.177)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.197 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0065 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.212 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.204 (n=876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` < `0.7118` → IC=+0.200 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7118 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.238 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.244 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2073` → IC=+0.235 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2073 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.8074` → IC=+0.203 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8074 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.199 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 5.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

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

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.220 (n=1606)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4542` → IC=+0.214 (n=1606)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4542 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4986` → IC=+0.221 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4986 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.8568` → IC=+0.206 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8568 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.3963` → IC=+0.216 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3963 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.026` → IC=+0.214 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.026 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.707` → IC=+0.212 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.707 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.208 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1033` → IC=+0.211 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1033 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.214 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.242 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.4848` → IC=+0.219 (n=1327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4848 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.213 (n=893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.201 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7466 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.0897` → IC=+0.203 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0897 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.6225` → IC=+0.213 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6225 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.927` → IC=+0.198 (n=213)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.927 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.352` → IC=+0.201 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.352 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.6401` → IC=+0.224 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6401 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.225 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.204 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.200 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `6544.4636` → IC=+0.203 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6544.4636 (IC base=+0.198)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.222 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.231 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.7494` → IC=+0.239 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7494 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.222 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.244 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.1058` → IC=+0.204 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1058 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.0799` → IC=+0.201 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0799 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.1486` → IC=+0.200 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1486 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.201 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4745 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.203 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4317.119` → IC=+0.237 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4317.119 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.238 (n=456)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.5971` → IC=+0.244 (n=682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5971 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.255 (n=475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.252 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.5326` → IC=+0.228 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5326 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.3137` → IC=+0.230 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3137 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.797` → IC=+0.237 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.797 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.0973` → IC=+0.228 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0973 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `1.2826` → IC=+0.230 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2826 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.241 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.5701` → IC=+0.263 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5701 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2990.8964` → IC=+0.244 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2990.8964 (IC base=+0.225)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.265 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.225)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.151 (n=675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.190 (n=1293)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.75 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1461` → IC=+0.141 (n=958)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1461 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.621` → IC=+0.145 (n=424)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.621 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.264 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.1457` → IC=+0.133 (n=352)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.1457 (IC base=+0.045)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.3776` → IC=-0.159 (n=206)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3776
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=619)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.121 (n=650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0059 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.3776` → IC=+0.152 (n=619)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.3776 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.173 (n=298)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.0639` → IC=+0.286 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0639 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.052)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.155 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0034 (IC base=+0.073)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.123 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.7791` → IC=+0.224 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7791 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.175 (n=309)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.65` → IC=+0.196 (n=136)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.65 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.0296` → IC=+0.255 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0296 (IC base=+0.017)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.199 (n=227)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.981 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.773` → IC=+0.140 (n=145)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.773 (IC base=+0.021)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.152 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.011 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.4545` → IC=+0.177 (n=336)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.4545 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.928` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.928 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.0982` → IC=+0.175 (n=112)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0982 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0764` → IC=+0.152 (n=153)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0764 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8346` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.8346 (IC base=+0.067)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0072` → IC=-0.229 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=118)

- **FILTRO** `drift_60min` |x|> `0.1888` → IC=-0.305 (n=85)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1888
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=258)

- **FILTRO** `dist_vwap_pct` > `0.2422` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2422
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=330)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=240)

- **FILTRO** `ibs_20min` > `0.8119` → IC=-0.325 (n=78)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8119
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=238)

- **FILTRO** `dist_vwap_pct` > `0.3644` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3644
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=286)

- **FILTRO** `sigma_ewma_delta_pct` > `9.965` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.965
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=290)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=198)

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
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=72)

- **FILTRO** `drift_60min` |x|> `0.0933` → IC=-0.319 (n=70)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0933
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=72)

- **FILTRO** `ibs_20min` > `0.754` → IC=-0.260 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.754
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=96)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.328 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=89)

- **FILTRO** `volumen_regimen` < `0.7708` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=87)

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
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=105)

- **FILTRO** `volumen_regimen` < `0.7553` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7553
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=93)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=94)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.321 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=35)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.426 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=25)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2609` → IC=-0.159 (n=244)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=736)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.214 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.6732` → IC=+0.180 (n=623)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6732 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.5397` → IC=+0.259 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5397 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.469` → IC=+0.146 (n=142)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.469 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.709` → IC=+0.142 (n=459)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 2.709 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.181 (n=208)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6242 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.2697` → IC=+0.162 (n=607)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.2697 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.186 (n=173)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1415` → IC=+0.124 (n=647)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.1415 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.783` → IC=+0.148 (n=214)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.783 (IC base=+0.037)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7064` → IC=-0.167 (n=61)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7064
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=184)

- **PATRÓN** `dist_vwap_pct` > `0.5453` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5453 (IC base=+0.022)

- **PATRÓN** `ibs_20min` < `0.2374` → IC=+0.172 (n=343)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.2374 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.706` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 9.706 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `1.7729` → IC=+0.136 (n=207)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7729 (IC base=+0.098)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=197)

- **FILTRO** `ibs_20min` > `0.1511` → IC=-0.125 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1511
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=231)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.142 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.004 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.139 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.003 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.1876` → IC=+0.128 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1876 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.148 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.167 (n=181)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8015 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.0967` → IC=+0.151 (n=167)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.0967 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.162 (n=211)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6242 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1915 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.178 (n=197)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.7967` → IC=+0.198 (n=117)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.7967 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=171)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.186 (n=202)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.828` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.828 (IC base=+0.007)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=117)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=138)

- **FILTRO** `volumen_spike_ratio` > `2.3635` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3635
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=104)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.289 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6053` → IC=+0.270 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6053 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.977` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.977 (IC base=-0.065)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.308 (n=92)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.4341` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4341 (IC base=+0.239)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.239)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.308 (n=92)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.4341` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4341 (IC base=+0.239)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.239)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2944.9354` → IC=+0.132 (n=506)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2944.9354 (IC base=+0.100)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2944.9354` → IC=+0.132 (n=506)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2944.9354 (IC base=+0.100)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=234)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9999` → IC=-0.131 (n=82)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9999
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=168)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=234)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=547)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4139.65` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4139.65
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **PATRÓN** `liq_n` > `2.0` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `liq_n` > 2.0 (IC base=+0.061)

- **PATRÓN** `liq_usd_total` > `1116.83` → IC=+0.121 (n=122)

  - _Acción_: Kelly boost +0.60€ cuando `liq_usd_total` > 1116.83 (IC base=+0.061)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.061)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3852)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=117)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=135)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=267)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1565)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1519)

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
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=938)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=938)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.128 (n=294)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=724)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1093)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1093)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=252)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=252)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.145 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=193)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=360)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=286)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=385)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=385)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=230)

- **FILTRO** `libro_liquidez` < `655.65` → IC=-0.138 (n=136)

  - _Acción_: SKIP cuando `libro_liquidez` < 655.65
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=279)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=314)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=67)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.186 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=81)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.51 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.131 (n=293)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=309)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=422)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=451)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=127)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=550)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.125 (n=451)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=242)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.131 (n=101)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=314)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.131 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=287)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.153 (n=266)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=552)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=7070)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=22805)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=7526)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=23254)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.184 (n=1373)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=4123)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.148 (n=1819)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=3651)

- **PATRÓN** `libro_liquidez` > `1867.2415` → IC=+0.141 (n=1374)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1867.2415 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.124 (n=2820)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1140.364` → IC=+0.150 (n=1860)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1140.364 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.180 (n=1065)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3283)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.207 (n=1346)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4247)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.130 (n=1877)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1746.57` → IC=+0.122 (n=1873)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1746.57 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.157 (n=1372)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4162)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2421)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2345)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.182 (n=959)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2923)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3861)

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

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=348)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.133 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=305)

- **FILTRO** `libro_liquidez` < `3195.1545` → IC=-0.182 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 3195.1545
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=309)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=957)

- **FILTRO** `libro_liquidez` < `1811.4604` → IC=-0.163 (n=244)

  - _Acción_: SKIP cuando `libro_liquidez` < 1811.4604
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=732)

- **FILTRO** `ibs_20min` > `0.8846` → IC=-0.135 (n=573)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8846
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=574)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.211 (n=278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=860)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=20409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=45917)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.298 (n=15679)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=50647)

- **FILTRO** `ibs_7min` < `0.224` → IC=-0.232 (n=16581)

  - _Acción_: SKIP cuando `ibs_7min` < 0.224
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=49745)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=22079)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=44247)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=20684)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=62470)

- **FILTRO** `ibs_7min` > `0.283` → IC=-0.182 (n=20784)

  - _Acción_: SKIP cuando `ibs_7min` > 0.283
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=62370)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8863)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=2849)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=8888)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.250 (n=3872)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=7865)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.151 (n=2700)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9037)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3438)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=10944)

- **FILTRO** `ibs_7min` > `0.7715` → IC=-0.214 (n=3595)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=10787)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2653)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=8440)

- **FILTRO** `ibs_7min` < `0.7175` → IC=-0.207 (n=2773)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7175
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8320)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.195 (n=2755)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8338)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2580)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=8734)

- **FILTRO** `ibs_7min` > `0.2662` → IC=-0.192 (n=2828)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2662
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8486)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=2822)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8492)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=2726)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=8496)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.322 (n=2650)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=8572)

- **FILTRO** `ibs_7min` < `0.2864` → IC=-0.248 (n=3703)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2864
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=7519)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.198 (n=2366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8856)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=3636)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=11591)

- **FILTRO** `ibs_7min` > `0.7297` → IC=-0.183 (n=3803)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7297
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=11424)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2630)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8112)

- **FILTRO** `ibs_7min` < `0.7193` → IC=-0.193 (n=2685)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7193
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8057)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.188 (n=2676)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8066)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2575)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=8631)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.173 (n=2801)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8405)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.170 (n=2792)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8414)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2488)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8222)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.230 (n=3495)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7215)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.223 (n=2488)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8222)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.193 (n=3845)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=12221)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=2513)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8309)

- **FILTRO** `ibs_7min` < `0.179` → IC=-0.230 (n=2705)

  - _Acción_: SKIP cuando `ibs_7min` < 0.179
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8117)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.202 (n=2495)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=8327)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.226 (n=3734)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=11225)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=600)

- **FILTRO** `libro_liquidez` < `10478.3164` → IC=-0.154 (n=189)

  - _Acción_: SKIP cuando `libro_liquidez` < 10478.3164
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=569)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=875)

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
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=662)

- **FILTRO** `libro_liquidez` < `3289.6554` → IC=-0.154 (n=189)

  - _Acción_: SKIP cuando `libro_liquidez` < 3289.6554
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=570)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4308` → IC=+0.152 (n=628)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4308 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `421.6695` → IC=+0.167 (n=461)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 421.6695 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3557.0392` → IC=+0.144 (n=627)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3557.0392 (IC base=+0.125)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.193 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 14.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `377.422` → IC=+0.158 (n=290)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 377.422 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2534.4132` → IC=+0.223 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2534.4132 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.139 (n=142)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 6.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4309` → IC=+0.141 (n=129)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4309 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.134 (n=266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 15.0 (IC base=+0.114)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.197 (n=176)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.154 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `507.685` → IC=+0.182 (n=177)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 507.685 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5192.827` → IC=+0.139 (n=264)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 5192.827 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.210 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.136)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.171 (n=238)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.190 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.146)

- **PATRÓN** `total_vol_5m` < `4679.172` → IC=+0.183 (n=159)

  - _Acción_: Kelly boost +0.92€ cuando `total_vol_5m` < 4679.172 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3694.6173` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3694.6173 (IC base=+0.146)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.126 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.093)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `pct_vs_K` |x|> `3.4207` → IC=-0.194 (n=263)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4207
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=513)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.144 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0044 (IC base=-0.081)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2515` → IC=-0.297 (n=57)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2515
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=173)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.256 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=-0.035)

- **PATRÓN** `pct_vs_K` |x|≤ `1.632` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `pct_vs_K` |x|≤ 1.632 (IC base=-0.035)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `251.7955` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.9444` → IC=-0.212 (n=71)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9444
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=75)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0109` → IC=-0.232 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.137 (n=180)

- **FILTRO** `T_h` > `98.1124` → IC=-0.228 (n=358)

  - _Acción_: SKIP cuando `T_h` > 98.1124
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=360)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.221 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=458)

- **FILTRO** `pct_vs_K` |x|> `3.1826` → IC=-0.422 (n=152)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1826
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=458)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.009` → IC=-0.207 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.009
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=61)

- **FILTRO** `T_h` > `143.7867` → IC=-0.250 (n=54)

  - _Acción_: SKIP cuando `T_h` > 143.7867
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=166)

- **FILTRO** `pct_vs_K` |x|> `1.9121` → IC=-0.374 (n=109)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.9121
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=111)

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
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.327 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=69)

- **FILTRO** `T_h` > `99.3756` → IC=-0.292 (n=99)

  - _Acción_: SKIP cuando `T_h` > 99.3756
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=101)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.354 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=141)

- **FILTRO** `sigma_h` < `0.0053` → IC=-0.188 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=141)

- **FILTRO** `T_h` > `57.2198` → IC=-0.232 (n=125)

  - _Acción_: SKIP cuando `T_h` > 57.2198
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=62)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.308 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=151)

- **FILTRO** `T_h` > `70.3179` → IC=-0.215 (n=149)

  - _Acción_: SKIP cuando `T_h` > 70.3179
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `sigma_h` < `0.0081` → IC=-0.271 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=102)

- **FILTRO** `pct_vs_K` |x|> `3.2111` → IC=-0.435 (n=44)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2111
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=91)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.345)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.366 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.345)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.378 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.345)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.395 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.345)

- **PATRÓN** `T_h` > `0.7285` → IC=+0.378 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7285 (IC base=+0.345)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.345)

- **PATRÓN** `edge` > `0.0997` → IC=+0.437 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.406)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.429 (n=167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.406)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.442 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.376` → IC=+0.445 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.376 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.406)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.204)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.289 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.415)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.417 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.415)

- **PATRÓN** `T_h` < `1.2618` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2618 (IC base=+0.415)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.481 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.415)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.415)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=368)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=440)

- **PATRÓN** `streak_estiramiento` < `0.2918` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `streak_estiramiento` < 0.2918 (IC base=+0.025)

- **PATRÓN** `streak_estiramiento` < `0.5383` → IC=+0.178 (n=200)

  - _Acción_: Kelly boost +0.89€ cuando `streak_estiramiento` < 0.5383 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.131 (n=231)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 33.0 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `2533.0371` → IC=+0.131 (n=158)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2533.0371 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=22)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.038)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4315` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4315
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=122)

- **PATRÓN** `streak_estiramiento` < `0.3805` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.3805 (IC base=+0.030)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.190 (n=127)

  - _Acción_: Kelly boost +0.95€ cuando `streak_estiramiento` < 0.437 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.155 (n=140)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 33.0 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2229.7597` → IC=+0.133 (n=145)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2229.7597 (IC base=+0.095)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=99)

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
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1052)

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
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4509)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2594)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.190 (n=1984)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0058 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.013` → IC=+0.160 (n=1503)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.013 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.2119` → IC=+0.172 (n=4508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2119 (IC base=+0.158)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3523` → IC=+0.167 (n=4164)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3523 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.166 (n=4183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.5001` → IC=+0.228 (n=4508)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5001 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1302` → IC=+0.153 (n=2118)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1302 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.671` → IC=+0.264 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.671 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `5063.7944` → IC=+0.180 (n=1503)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 5063.7944 (IC base=+0.158)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1774)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.222 (n=720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.256 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2654` → IC=+0.224 (n=241)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2654 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.223 (n=750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.713` → IC=+0.278 (n=720)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.713 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.3703` → IC=+0.226 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3703 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.1096` → IC=+0.204 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1096 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.716` → IC=+0.312 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.716 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `15953.0262` → IC=+0.231 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15953.0262 (IC base=+0.203)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.156 (n=881)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0069 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.152 (n=588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1432` → IC=+0.137 (n=587)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.1432 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2833` → IC=+0.141 (n=709)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2833 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=924)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5034` → IC=+0.226 (n=881)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5034 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.150 (n=549)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.945` → IC=+0.287 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.945 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5808.0125` → IC=+0.167 (n=400)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5808.0125 (IC base=+0.136)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.6216` → IC=+0.160 (n=769)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` > 0.6216 (IC base=+0.070)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0194` → IC=+0.187 (n=692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0194 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.183 (n=926)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0151 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.209` → IC=+0.193 (n=1037)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.209 (IC base=+0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0971` → IC=+0.239 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0971 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.187 (n=927)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 14.0 (IC base=+0.180)

- **PATRÓN** `ibs_15` > `0.5758` → IC=+0.279 (n=927)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5758 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.4843` → IC=+0.219 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4843 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.756` → IC=+0.228 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.756 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2347.917` → IC=+0.198 (n=1037)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2347.917 (IC base=+0.180)

- **PATRÓN** `ibs_15` < `0.1087` → IC=+0.171 (n=868)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` < 0.1087 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.385 (n=319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.379 (n=469)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1074` → IC=+0.380 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1074 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.398 (n=704)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.384 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.159` → IC=+0.397 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.159 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3489.2833` → IC=+0.372 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3489.2833 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.367 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1565` → IC=+0.369 (n=235)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1565 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.394 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.388 (n=354)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.3736` → IC=+0.387 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3736 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.163` → IC=+0.386 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.163 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.385 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.404 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.367 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.381 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.366)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.364 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.376 (n=313)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.378 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.373 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.377 (n=160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8149` → IC=+0.402 (n=313)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8149 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.377 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.368 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.408 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.371 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `4035.6016` → IC=+0.394 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4035.6016 (IC base=+0.366)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0101` → IC=-0.219 (n=1669)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=3240)

- **FILTRO** `drift_15min` |x|> `0.9082` → IC=-0.132 (n=1226)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9082
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3682)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.215 (n=1993)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2916)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.221 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.075)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.281 (n=1143)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.202 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2658` → IC=+0.201 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2658 (IC base=-0.075)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2357` → IC=+0.268 (n=1461)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2357 (IC base=-0.007)

- **PATRÓN** `ibs_15` < `0.3683` → IC=+0.283 (n=4383)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3683 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` > `0.8624` → IC=+0.276 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8624 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.1641` → IC=+0.246 (n=3253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1641 (IC base=-0.007)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.223 (n=2309)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=770)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.217 (n=769)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=2310)

- **FILTRO** `sigma_ewma_delta_pct` > `18.853` → IC=-0.261 (n=559)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.853
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=2520)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.157 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.003 (IC base=+0.075)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.269 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.075)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.329 (n=389)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.280 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.3658` → IC=+0.285 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3658 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.457` → IC=+0.143 (n=261)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 18.457 (IC base=+0.075)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.250 (n=70)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1389` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1389 (IC base=-0.186)

- **PATRÓN** `ibs_15` < `0.6221` → IC=+0.319 (n=70)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6221 (IC base=-0.186)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.186)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.186)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=745)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.161 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.189 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.197 (n=443)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5784` → IC=+0.244 (n=572)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5784 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.115` → IC=+0.153 (n=353)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.115 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.157 (n=447)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.263 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=745)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `9402.7179` → IC=+0.158 (n=191)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9402.7179 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.248 (n=1660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.3568` → IC=+0.242 (n=1460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3568 (IC base=+0.240)

- **PATRÓN** `drift_15min` |x|≤ `0.7694` → IC=+0.254 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7694 (IC base=+0.240)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1573` → IC=+0.256 (n=1107)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1573 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.243 (n=1198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.241 (n=1472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.240)

- **PATRÓN** `ibs_15` < `0.3777` → IC=+0.273 (n=1660)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3777 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `0.7917` → IC=+0.267 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7917 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.369` → IC=+0.244 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.369 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.262` → IC=+0.247 (n=1733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.262 (IC base=+0.240)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0472` → IC=-0.208 (n=845)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0472
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=283)

- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.248 (n=383)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=745)

- **FILTRO** `drift_15min` |x|> `0.907` → IC=-0.284 (n=281)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.907
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=847)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.190)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=-0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0653` → IC=+0.226 (n=749)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0653 (IC base=-0.032)

- **PATRÓN** `ibs_15` < `0.3939` → IC=+0.293 (n=750)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3939 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.1942` → IC=+0.242 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1942 (IC base=-0.032)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1506` → IC=-0.227 (n=339)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1506
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=1020)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.243 (n=644)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=715)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.212)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1187` → IC=+0.278 (n=659)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1187 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.292 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.1351` → IC=+0.309 (n=659)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1351 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7525` → IC=+0.335 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7525 (IC base=-0.022)

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

- **PATRÓN** `dist_vwap_pct` > `0.1526` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1526 (IC base=+0.055)

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

- **PATRÓN** `dist_vwap_pct` > `0.1526` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1526 (IC base=+0.055)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.291 (n=1240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0725` → IC=+0.314 (n=546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0725 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1514` → IC=+0.289 (n=826)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1514 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2227` → IC=+0.298 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2227 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=1285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.316 (n=1241)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2676` → IC=+0.315 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2676 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.095` → IC=+0.380 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.095 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13537.0285` → IC=+0.305 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13537.0285 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.307 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0592` → IC=+0.320 (n=220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0592 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `0.3847` → IC=+0.279 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3847 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2215` → IC=+0.281 (n=299)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2215 (IC base=+0.280)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.388` → IC=+0.284 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.388 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.299 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.305 (n=660)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.308 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.394` → IC=+0.381 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.394 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `16027.7188` → IC=+0.315 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16027.7188 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.310 (n=582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.321 (n=194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.145` → IC=+0.297 (n=387)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.145 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.341 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.300 (n=529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8745` → IC=+0.330 (n=520)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8745 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.320 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.387 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.159 (n=89)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=270)

- **FILTRO** `ballena_activa_n` > `51.0` → IC=-0.129 (n=219)

  - _Acción_: SKIP cuando `ballena_activa_n` > 51.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=108)

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
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=138)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.311` → IC=-0.143 (n=40)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.311
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.2455` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2455
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

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
- **PATRÓN** `ratio` < `0.9711` → IC=+0.389 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9711 (IC base=+0.175)

- **PATRÓN** `T_h` > `115.5985` → IC=+0.353 (n=2589)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.5985 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0203` → IC=+0.378 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0203 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9836` → IC=+0.138 (n=241)

  - _Acción_: Kelly boost +0.69€ cuando `T_h` > 111.9836 (IC base=+0.137)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.260 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.137)

- **PATRÓN** `T_h` > `111.9824` → IC=+0.312 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9824 (IC base=+0.299)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.353 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.299)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.985` → IC=+0.419 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.985 (IC base=+0.222)

- **PATRÓN** `T_h` > `111.996` → IC=+0.352 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0298` → IC=+0.400 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0298 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.431 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5001 sube el IC de +0.158 a +0.228 en UPDOWN_GBM#15min (n=4508). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.713 sube el IC de +0.203 a +0.278 en UPDOWN_GBM#BTC#15min (n=720). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5034 sube el IC de +0.136 a +0.226 en UPDOWN_GBM#ETH#15min (n=881). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6216 sube el IC de +0.070 a +0.160 en UPDOWN_GBM#SOL#15min (n=769). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5758 sube el IC de +0.180 a +0.279 en UPDOWN_GBM#XRP#15min (n=927). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1087 sube el IC de +0.068 a +0.171 en UPDOWN_GBM#XRP#15min (n=868). Ya aplicado como kelly_boost=+0.86€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.075 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1143). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3683 sube el IC de -0.007 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=4383). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.075 a +0.329 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=389). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6221 sube el IC de -0.186 a +0.319 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5784 sube el IC de +0.152 a +0.244 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=572). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3777 sube el IC de +0.240 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1660). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3939 sube el IC de -0.032 a +0.293 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=750). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.212 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1351 sube el IC de -0.022 a +0.309 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=659). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7 (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.093 a +0.364 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.287 a +0.316 en UPDOWN_GBM_IBS_ALTO (n=1241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.280 a +0.305 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=660). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8745 sube el IC de +0.294 a +0.330 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=520). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.365 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=704). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.363 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8149 sube el IC de +0.366 a +0.402 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=313). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2091 | +0.085 | +220.13€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2091 | +0.085 | +220.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1690 | +0.086 | +184.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1690 | +0.086 | +184.61€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 86 | +0.125 | +24.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 86 | +0.125 | +24.55€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 941 | -0.026 | +75.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 941 | -0.026 | +75.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 720 | -0.047 | +53.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 720 | -0.047 | +53.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 150 | +0.086 | +25.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 65 | -0.052 | -5.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 65 | -0.052 | -5.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 44670 | -0.085 | -5553.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2653 | +0.057 | -281.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 42017 | -0.094 | -5272.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4677 | -0.114 | -760.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4677 | -0.114 | -760.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2653 | +0.057 | -281.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2653 | +0.057 | -281.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4623 | -0.116 | -906.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4623 | -0.116 | -906.42€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12101 | -0.032 | -1028.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12101 | -0.032 | -1028.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12074 | -0.119 | -1212.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12074 | -0.119 | -1212.64€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8542 | -0.125 | -1365.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8542 | -0.125 | -1365.07€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 43757 | -0.013 | +3108.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11301 | +0.005 | +1596.03€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 32456 | -0.019 | +1511.99€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 43757 | -0.013 | +3108.02€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11301 | +0.005 | +1596.03€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 32456 | -0.019 | +1511.99€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 171822 | +0.114 | -6905.13€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 20737 | +0.181 | -644.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 777 | -0.002 | -76.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 140324 | +0.106 | -5817.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9984 | +0.092 | -366.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 23251 | +0.106 | -1499.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 69 | -0.176 | +10.12€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 23167 | +0.107 | -1498.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 32860 | +0.125 | -535.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5546 | +0.180 | -225.84€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 23238 | +0.121 | -148.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4034 | +0.078 | -138.64€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 23303 | +0.099 | -1652.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 83 | -0.112 | +7.08€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 23205 | +0.100 | -1648.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 36635 | +0.124 | -694.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9329 | +0.178 | -191.21€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 23593 | +0.106 | -439.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3701 | +0.101 | -55.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL | 32494 | +0.113 | -1502.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5630 | +0.199 | -254.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 680 | +0.026 | -22.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 23935 | +0.096 | -1053.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2249 | +0.103 | -172.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 23279 | +0.107 | -1020.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 80 | -0.110 | +9.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 23186 | +0.108 | -1029.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 27763 | +0.194 | -1829.65€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 27763 | +0.194 | -1829.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6271 | +0.175 | -581.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6271 | +0.175 | -581.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3842 | +0.199 | -128.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3842 | +0.199 | -128.00€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6195 | +0.175 | -538.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6195 | +0.175 | -538.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5276 | +0.249 | -187.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5276 | +0.249 | -187.00€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6100 | +0.186 | -408.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6100 | +0.186 | -408.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1165 | +0.426 | -41.07€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1165 | +0.426 | -41.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 475 | +0.439 | -4.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 475 | +0.439 | -4.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 467 | +0.427 | -14.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 467 | +0.427 | -14.08€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 209 | +0.396 | -18.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 209 | +0.396 | -18.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 97655 | +0.200 | -7096.07€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 97655 | +0.200 | -7096.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 16824 | +0.182 | -1824.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 16824 | +0.182 | -1824.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 15747 | +0.225 | -507.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 15747 | +0.225 | -507.77€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 16762 | +0.180 | -1771.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 16762 | +0.180 | -1771.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 15886 | +0.218 | -645.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 15886 | +0.218 | -645.43€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 16167 | +0.202 | -1055.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 16167 | +0.202 | -1055.90€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 16269 | +0.197 | -1290.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 16269 | +0.197 | -1290.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 37526 | +0.117 | +332.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 37526 | +0.117 | +332.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 18679 | +0.118 | +211.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 18679 | +0.118 | +211.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 18847 | +0.116 | +120.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 18847 | +0.116 | +120.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2382 | +0.294 | -2.47€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2382 | +0.294 | -2.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1088 | +0.282 | -22.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1088 | +0.282 | -22.79€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1162 | +0.299 | +18.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1162 | +0.299 | +18.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 132 | +0.336 | +2.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 132 | +0.336 | +2.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1093 | +0.443 | +8.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1093 | +0.443 | +8.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 526 | +0.438 | -3.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 526 | +0.438 | -3.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 518 | +0.450 | +10.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 518 | +0.450 | +10.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 49 | +0.402 | +0.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 49 | +0.402 | +0.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1853 | +0.067 | -84.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1128 | +0.081 | -20.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1419 | +0.075 | -39.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1128 | +0.081 | -20.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 75455 | +0.101 | -1805.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6078 | +0.095 | +114.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 69377 | +0.101 | -1919.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 41321 | +0.106 | -403.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6078 | +0.095 | +114.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 35243 | +0.108 | -517.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 15866 | +0.110 | -63.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 15866 | +0.110 | -63.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 18268 | +0.081 | -1338.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 18268 | +0.081 | -1338.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 1 | 4 |
| ✅ GBM_LATE_15M | 51391 | +0.097 | +28202.54€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 51391 | +0.097 | +28202.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8538 | +0.223 | +7284.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8538 | +0.223 | +7284.91€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 7828 | +0.174 | +6066.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7828 | +0.174 | +6066.76€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 9215 | +0.206 | +7218.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9215 | +0.206 | +7218.10€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 7019 | +0.049 | +2108.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7019 | +0.049 | +2108.91€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 7186 | -0.031 | +1874.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7186 | -0.031 | +1874.00€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 11605 | -0.026 | +3649.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11605 | -0.026 | +3649.86€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 54268 | +0.085 | +30926.07€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 54268 | +0.085 | +30926.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10576 | -0.001 | +5455.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10576 | -0.001 | +5455.14€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11586 | +0.004 | +2975.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11586 | +0.004 | +2975.53€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7436 | +0.290 | +8343.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7436 | +0.290 | +8343.63€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10161 | +0.014 | +3056.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10161 | +0.014 | +3056.10€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8432 | +0.042 | +3705.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8432 | +0.042 | +3705.96€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6077 | +0.314 | +7389.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6077 | +0.314 | +7389.70€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 40721 | +0.179 | +33450.85€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 40721 | +0.179 | +33450.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6136 | +0.238 | +5675.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6136 | +0.238 | +5675.95€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6467 | +0.140 | +4741.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6467 | +0.140 | +4741.24€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6539 | +0.225 | +5674.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6539 | +0.225 | +5674.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6951 | +0.132 | +5387.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6951 | +0.132 | +5387.62€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7678 | +0.121 | +5707.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7678 | +0.121 | +5707.12€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6950 | +0.232 | +6264.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6950 | +0.232 | +6264.09€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 10815 | +0.124 | +5312.35€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 10815 | +0.124 | +5312.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 462 | +0.157 | +298.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 462 | +0.157 | +298.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3136 | +0.130 | +1710.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3136 | +0.130 | +1710.04€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3190 | +0.127 | +1549.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3190 | +0.127 | +1549.20€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2705 | +0.092 | +1030.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2705 | +0.092 | +1030.60€ | 1 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 831 | +0.155 | +463.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 831 | +0.155 | +463.90€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 51624 | +0.186 | +42050.56€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 51624 | +0.186 | +42050.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8155 | +0.248 | +7823.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8155 | +0.248 | +7823.73€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8175 | +0.136 | +5566.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8175 | +0.136 | +5566.64€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8749 | +0.234 | +7858.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8749 | +0.234 | +7858.37€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8548 | +0.139 | +6234.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8548 | +0.139 | +6234.26€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9154 | +0.122 | +6451.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9154 | +0.122 | +6451.70€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8843 | +0.238 | +8115.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8843 | +0.238 | +8115.86€ | 0 | 19 |
| ✅ GBM_LATE_5M | 13522 | +0.209 | +10925.55€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 13522 | +0.209 | +10925.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3209 | +0.210 | +2756.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3209 | +0.210 | +2756.35€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1246 | +0.198 | +932.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1246 | +0.198 | +932.96€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 3908 | +0.202 | +2932.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3908 | +0.202 | +2932.82€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 2147 | +0.207 | +1767.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2147 | +0.207 | +1767.94€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4467 | +0.051 | +1226.80€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4467 | +0.051 | +1226.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1583 | +0.064 | +502.41€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1583 | +0.064 | +502.41€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1449 | +0.051 | +439.09€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1449 | +0.051 | +439.09€ | 0 | 6 |
| ✅ GBM_LATE_60M#SOL | 1435 | +0.036 | +285.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1435 | +0.036 | +285.30€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 661 | -0.251 | -35.23€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 661 | -0.251 | -35.23€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 250 | -0.250 | -19.76€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 250 | -0.250 | -19.76€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 238 | -0.246 | -7.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 238 | -0.246 | -7.27€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 173 | -0.254 | -8.20€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 173 | -0.254 | -8.20€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1810 | +0.083 | +472.15€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1810 | +0.083 | +472.15€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 701 | +0.072 | +168.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 701 | +0.072 | +168.57€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 618 | +0.060 | +115.79€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 618 | +0.060 | +115.79€ | 2 | 15 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 491 | +0.127 | +187.80€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 491 | +0.127 | +187.80€ | 3 | 9 |
| ✅ LATE_WINDOW_5MIN | 199 | +0.271 | +205.69€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 199 | +0.271 | +205.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 199 | +0.271 | +205.69€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 199 | +0.271 | +205.69€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4114 | +0.098 | +954.24€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4114 | +0.098 | +954.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4114 | +0.098 | +954.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4114 | +0.098 | +954.24€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 818 | -0.016 | +7.51€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 818 | -0.016 | +7.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 12 | -0.043 | -0.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 12 | -0.043 | -0.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 247 | -0.014 | +4.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 247 | -0.014 | +4.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 216 | +0.028 | +15.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 216 | +0.028 | +15.32€ | 2 | 3 |
| ✅ LIQUIDACIONES_15M#SOL | 262 | -0.004 | +3.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 262 | -0.004 | +3.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4075 | +0.016 | +98.72€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4075 | +0.016 | +98.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 190 | +0.031 | -0.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 190 | +0.031 | -0.23€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 819 | +0.015 | +40.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 819 | +0.015 | +40.38€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 216 | +0.000 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1617 | +0.018 | +25.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1617 | +0.018 | +25.66€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 763 | +0.011 | +1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 763 | +0.011 | +1.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2126 | -0.036 | -18.92€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2126 | -0.036 | -18.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 642 | -0.028 | -10.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 642 | -0.028 | -10.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 740 | -0.013 | +11.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 740 | -0.013 | +11.31€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 744 | -0.064 | -19.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 744 | -0.064 | -19.92€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 12694 | -0.032 | -117.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6095 | -0.036 | -97.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6599 | -0.029 | -19.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 448 | -0.042 | -15.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 228 | -0.009 | +8.89€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 220 | -0.077 | -24.67€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3298 | -0.023 | +14.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1572 | -0.024 | +6.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1726 | -0.022 | +8.16€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1301 | -0.023 | +28.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 662 | -0.032 | +3.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 639 | -0.015 | +25.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2838 | -0.036 | -63.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1346 | -0.040 | -43.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1492 | -0.033 | -20.24€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2440 | -0.031 | -16.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1179 | -0.039 | -28.34€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1261 | -0.023 | +11.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2369 | -0.044 | -64.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1108 | -0.051 | -44.37€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1261 | -0.037 | -20.23€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 60655 | +0.000 | +3228.35€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 60655 | +0.000 | +3228.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 10966 | +0.027 | +1469.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 10966 | +0.027 | +1469.50€ | 2 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8571 | -0.035 | -95.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8571 | -0.035 | -95.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11100 | +0.024 | +1161.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11100 | +0.024 | +1161.06€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8469 | -0.049 | -161.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8469 | -0.049 | -161.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10304 | -0.004 | +288.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10304 | -0.004 | +288.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11245 | +0.017 | +566.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11245 | +0.017 | +566.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7000 | -0.055 | -120.26€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7000 | -0.055 | -120.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1241 | -0.002 | -15.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1241 | -0.002 | -15.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1914 | -0.068 | -33.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1914 | -0.068 | -33.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 69 | -0.007 | +0.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 69 | -0.007 | +0.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 795 | -0.120 | -34.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 795 | -0.120 | -34.70€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2123 | -0.068 | -11.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2123 | -0.068 | -11.71€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3374 | +0.004 | -1.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3374 | +0.004 | -1.03€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M#XRP | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 149480 | -0.077 | +2039.29€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 149480 | -0.077 | +2039.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 26119 | -0.078 | +1412.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 26119 | -0.078 | +1412.00€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 22407 | -0.100 | -1074.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 22407 | -0.100 | -1074.64€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 26449 | -0.069 | +1273.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 26449 | -0.069 | +1273.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 21948 | -0.097 | -659.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 21948 | -0.097 | -659.26€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 26776 | -0.057 | +337.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 26776 | -0.057 | +337.49€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 25781 | -0.069 | +750.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 25781 | -0.069 | +750.14€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8966 | -0.035 | -184.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8966 | -0.035 | -184.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2066 | -0.047 | -29.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2066 | -0.047 | -29.54€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2626 | -0.026 | -39.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2626 | -0.026 | -39.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1259 | -0.063 | -31.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1259 | -0.063 | -31.54€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1004 | -0.031 | -32.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1004 | -0.031 | -32.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1979 | +0.120 | +791.20€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1843 | +0.125 | +778.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 438 | +0.134 | +213.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 438 | +0.134 | +213.71€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 379 | +0.114 | +127.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 379 | +0.114 | +127.60€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 352 | +0.136 | +172.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 352 | +0.136 | +172.27€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 317 | +0.146 | +168.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 317 | +0.146 | +168.10€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 357 | +0.093 | +96.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 357 | +0.093 | +96.93€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1869 | -0.015 | -19.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1869 | -0.015 | -19.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 350 | +0.009 | +17.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 350 | +0.009 | +17.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 338 | -0.035 | -12.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 338 | -0.035 | -12.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 479 | -0.041 | -31.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 479 | -0.041 | -31.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 380 | +0.003 | +2.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 380 | +0.003 | +2.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 322 | -0.003 | +5.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 322 | -0.003 | +5.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1065 | -0.079 | -53.39€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 490 | -0.112 | -79.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 378 | -0.129 | -60.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 375 | -0.038 | +20.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 264 | -0.023 | +29.81€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 200 | -0.074 | +5.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 164 | -0.072 | +3.76€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 806 | -0.083 | -27.32€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1328 | -0.210 | -89.14€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 520 | -0.211 | -51.46€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 453 | -0.210 | -47.15€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 445 | -0.214 | -39.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 387 | -0.225 | -46.70€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 363 | -0.201 | +2.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 336 | -0.198 | -0.29€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1176 | -0.212 | -94.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 511 | +0.389 | +478.63€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 92 | +0.181 | +67.23€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 92 | +0.181 | +67.23€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 119 | +0.368 | +103.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 119 | +0.368 | +103.94€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 300 | +0.457 | +307.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 300 | +0.457 | +307.46€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 511 | +0.389 | +478.63€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 846 | +0.044 | +77.14€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 846 | +0.044 | +77.14€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 314 | +0.029 | +6.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 314 | +0.029 | +6.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 69 | +0.007 | +1.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 69 | +0.007 | +1.00€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 82 | +0.024 | +7.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 82 | +0.024 | +7.24€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 381 | +0.067 | +61.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 381 | +0.067 | +61.92€ | 1 | 5 |
| ✅ STREAK_FADE_5M | 3540 | -0.023 | -141.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3540 | -0.023 | -141.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 602 | -0.028 | -26.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 602 | -0.028 | -26.89€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 169 | -0.038 | -13.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 169 | -0.038 | -13.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1642 | -0.019 | -60.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1642 | -0.019 | -60.48€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 111 | -0.040 | -7.85€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 111 | -0.040 | -7.85€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 68 | +0.000 | -2.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 68 | +0.000 | -2.78€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11408 | +0.015 | +77.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11408 | +0.015 | +77.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2955 | +0.018 | +25.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2955 | +0.018 | +25.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2964 | +0.018 | +37.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2964 | +0.018 | +37.00€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2910 | +0.009 | -1.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2910 | +0.009 | -1.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10809 | +0.015 | -39.56€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10809 | +0.015 | -39.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4528 | +0.019 | -3.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4528 | +0.019 | -3.72€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3653 | +0.011 | -26.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3653 | +0.011 | -26.83€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2628 | +0.012 | -9.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2628 | +0.012 | -9.01€ | 1 | 0 |
| ✅ UPDOWN_GBM | 93422 | +0.059 | +8839.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 22712 | +0.083 | +4908.61€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 2896 | +0.001 | +28.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 61937 | +0.058 | +3806.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5548 | +0.001 | +99.86€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 7765 | +0.102 | +1399.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1730 | +0.164 | +802.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5945 | +0.086 | +599.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 21369 | +0.057 | +1859.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3076 | +0.082 | +697.03€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 808 | +0.001 | +12.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 14874 | +0.065 | +1077.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2492 | -0.001 | +69.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 119 | -0.070 | +3.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 9995 | +0.077 | +1158.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1708 | +0.156 | +722.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 8201 | +0.061 | +436.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 22199 | +0.049 | +1533.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5452 | +0.073 | +838.25€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 777 | +0.007 | +18.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 13823 | +0.049 | +649.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2037 | +0.005 | +25.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 110 | -0.107 | +1.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 20071 | +0.038 | +1127.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5893 | +0.035 | +439.89€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 738 | -0.011 | +2.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12323 | +0.047 | +687.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1019 | +0.001 | +4.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 98 | -0.140 | -7.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 12021 | +0.072 | +1762.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4853 | +0.100 | +1408.35€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6771 | +0.055 | +355.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 327 | -0.105 | -2.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 938 | +0.365 | +343.67€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 938 | +0.365 | +343.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 471 | +0.363 | +166.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 471 | +0.363 | +166.01€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 467 | +0.366 | +177.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 467 | +0.366 | +177.66€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 22873 | -0.021 | +5603.57€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 22873 | -0.021 | +5603.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1920 | -0.053 | +536.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1920 | -0.053 | +536.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4270 | -0.114 | +209.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4270 | -0.114 | +209.16€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1039 | +0.223 | +877.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1039 | +0.223 | +877.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2974 | +0.218 | +1891.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2974 | +0.218 | +1891.27€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6465 | -0.060 | +939.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6465 | -0.060 | +939.55€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6205 | -0.064 | +1149.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6205 | -0.064 | +1149.70€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 273 | +0.064 | +25.77€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 273 | +0.064 | +25.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 273 | +0.064 | +25.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 273 | +0.064 | +25.77€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1653 | +0.287 | +1397.16€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1653 | +0.287 | +1397.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 879 | +0.280 | +690.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 879 | +0.280 | +690.45€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 774 | +0.294 | +706.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 774 | +0.294 | +706.70€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 846 | -0.114 | -84.71€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 846 | -0.114 | -84.71€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 260 | -0.088 | -21.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 260 | -0.088 | -21.21€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 109 | -0.176 | -3.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 109 | -0.176 | -3.72€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4278 | +0.301 | +1975.14€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1613 | +0.257 | +203.51€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1645 | +0.295 | +715.03€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1020 | +0.381 | +1056.60€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.024 n=1167 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1167 IC=+0.024 PNL=+56.87€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 782 celda(s) pasan gate riguroso completo de 2818 evaluadas (n>=40) y 3925 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=5889 IC=+0.036 PNL=+442.13€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1645/15 IC=+0.295 PNL=+715.03€ | BTC: n=1613/15 IC=+0.257 PNL=+203.51€ | SOL: n=1020/15 IC=+0.381 PNL=+1056.60€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.149 n=990/60 | contraria IC=+0.191 n=1027 | gap=-0.042 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=543, boost estimado=+0.015. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2035/40 IC=+0.005 PNL=+26.03€ | BTC#60min: n=2491/40 IC=-0.001 PNL=+69.25€ | SOL#60min: n=1018/40 IC=+0.000 PNL=+3.67€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=662392 | tras_1loss IC=+0.098 n=502613 | tras_2loss IC=+0.068 n=201988/40 | gap=-0.021 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=893 PNL=+607.34€
  - _Datos_: n=893 IC=+0.179 PNL=+607.34€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1090 PNL=+565.64€
  - _Datos_: n=1090 IC=+0.150 PNL=+565.64€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.158 > 0.08 con n=74 PNL=+36.32€
  - _Datos_: n=74 IC=+0.158 PNL=+36.32€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3495 PNL=+1948.89€
  - _Datos_: n=3495 IC=+0.333 PNL=+1948.89€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=923 IC=+0.070 PNL=+93.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=923 IC=+0.070 PNL=+93.46€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=98 IC=+0.190 PNL=+68.62€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=98 IC=+0.190 PNL=+68.62€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.075 PNL=+7.10€)
  - _Datos_: n=6 IC=+0.075 PNL=+7.10€

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
  - _Estado_: n=3718 IC=+0.002 PNL=-12.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3718 IC=+0.002 PNL=-12.05€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1826 IC=-0.001 PNL=+110.99€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1826 IC=-0.001 PNL=+110.99€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1167 IC=+0.024 PNL=+56.87€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1167 IC=+0.024 PNL=+56.87€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.158 > 0.1 con n=6003 PNL=+3374.92€
  - _Datos_: n=6003 IC=+0.158 PNL=+3374.92€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3074 IC=+0.082 PNL=+698.30€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3074 IC=+0.082 PNL=+698.30€

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
  - _Estado_: n=1175 IC=+0.040 PNL=+102.31€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1175 IC=+0.040 PNL=+102.31€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=152 IC=-0.006 PNL=-1.49€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=152 IC=-0.006 PNL=-1.49€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.271 n=199) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=199 IC=+0.271 PNL=+205.69€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.02 con n=1161 PNL=+482.37€
  - _Datos_: n=1161 IC=+0.122 PNL=+482.37€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=251 IC=-0.117 PNL=+7.41€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=251 IC=-0.117 PNL=+7.41€

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
  - _Estado_: n=37797 IC=+0.074 PNL=+5392.30€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=37797 IC=+0.074 PNL=+5392.30€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.136 < -0.1 con n=680 PNL=+96.04€
  - _Datos_: n=680 IC=-0.136 PNL=+96.04€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3468 IC=+0.069 PNL=+466.01€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3468 IC=+0.069 PNL=+466.01€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=173 IC=-0.117 PNL=-1.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=173 IC=-0.117 PNL=-1.71€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.1 con n=983 PNL=+252.67€
  - _Datos_: n=983 IC=+0.105 PNL=+252.67€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 5/20 ops en el filtro definido (IC actual=-0.089 PNL=-2.55€)
  - _Datos_: n=5 IC=-0.089 PNL=-2.55€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=39183 IC=-0.137 PNL=+2565.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=39183 IC=-0.137 PNL=+2565.84€

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
  - _Estado_: n=4038 IC=+0.127 PNL=+2590.29€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4038 IC=+0.127 PNL=+2590.29€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=9540 IC=+0.058 PNL=+828.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=9540 IC=+0.058 PNL=+828.22€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=4156 PNL=+2319.42€
  - _Datos_: n=4156 IC=+0.099 PNL=+2319.42€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4222 PNL=-329.66€
  - _Datos_: n=4222 IC=-0.220 PNL=-329.66€

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
  - _Estado_: n=86 IC=+0.045 PNL=+14.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=86 IC=+0.045 PNL=+14.24€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2088) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2088 IC=+0.096 PNL=+424.22€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=649) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=649 IC=+0.411 PNL=+936.10€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=16821 IC=+0.182 PNL=-1824.35€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=16821 IC=+0.182 PNL=-1824.35€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.1 con n=265 PNL=+180.88€
  - _Datos_: n=265 IC=+0.227 PNL=+180.88€
