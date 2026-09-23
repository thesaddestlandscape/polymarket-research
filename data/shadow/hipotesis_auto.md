# Hipótesis automáticas — 2026-09-23 07:56 UTC
_Generado por shadow_postmortem.py sobre 570238 resoluciones (PNL=+63894.18€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.254 (n=507)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=462)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.254 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.207 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8038` → IC=+0.254 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8038 (IC base=+0.139)

- **PATRÓN** `banda_z` > `4.244` → IC=+0.167 (n=532)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 4.244 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=568)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2945.0699` → IC=+0.150 (n=355)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2945.0699 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 96.0 (IC base=+0.043)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=403)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=335)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.261 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.147)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.208 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.147)

- **PATRÓN** `banda_hit_calibrado` > `0.8012` → IC=+0.265 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8012 (IC base=+0.147)

- **PATRÓN** `banda_z` > `4.443` → IC=+0.174 (n=425)

  - _Acción_: Kelly boost +0.87€ cuando `banda_z` > 4.443 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=480)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 96.0 (IC base=+0.045)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=90)

- **FILTRO** `banda_hit_calibrado` < `0.6284` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6284
  - _Potencial_: sin este filtro IC_bueno=+0.236 (n=89)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.261 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.112)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.236 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.112)

- **PATRÓN** `banda_z` > `6.035` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `banda_z` > 6.035 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.126 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 4.0 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `891.6461` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 891.6461 (IC base=+0.112)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

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
- **FILTRO** `restante_s_al_confirmar` < `146.26` → IC=-0.231 (n=6837)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.26
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=20519)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.44` → IC=-0.236 (n=892)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.44
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2677)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `496.69` → IC=-0.149 (n=357)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 496.69
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1074)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `133.1` → IC=-0.284 (n=846)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.1
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2538)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `163.81` → IC=-0.228 (n=1622)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 163.81
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4873)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `125.63` → IC=-0.358 (n=1367)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.63
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=4101)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.223 (n=380)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=380)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.178 (n=234)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=475)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=559)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.202 (n=13506)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=3390)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5600.4068` → IC=+0.175 (n=2160)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5600.4068 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=10974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=13463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.232 (n=10543)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=5516)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7725.6175` → IC=+0.173 (n=2075)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7725.6175 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1633)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.352 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2053)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15850.2933` → IC=+0.231 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15850.2933 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=1467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `13992.7667` → IC=+0.208 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13992.7667 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.59` → IC=+0.167 (n=454)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.59 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4624.034 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.108)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.147 (n=799)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.44 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.108)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=2327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.333 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.357 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.240 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.234)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=575)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.231 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=522)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1302.4168` → IC=+0.150 (n=636)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1302.4168 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.236 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.432 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.169 (n=1055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.316 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=716)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.164)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.165 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 13.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.743` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.743 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=186)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `1271.2794` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1271.2794 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.206 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=107)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=11026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=10570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3715)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.184 (n=1867)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.71 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.255 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.254 (n=762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.250)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.357 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.250)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=2523)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2182)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.318 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=2558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=2468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=1888)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.195)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.432 (n=452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `2069.2076` → IC=+0.438 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2069.2076 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.435 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.452 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.438 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.445 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.405 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.403)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.405 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.406 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.403)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=38528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.232 (n=17790)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=6662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=5644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6108)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=5858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=5859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=2106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=5949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6011)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=2947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2056)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=5405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=2206)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=6461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=5468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5036)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.126 (n=4617)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.15 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=4950)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=6141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.95` → IC=+0.142 (n=4593)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.95 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=2539)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.1` → IC=+0.131 (n=2284)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.1 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2451)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=3031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.44` → IC=+0.145 (n=2286)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.44 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=2497)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=2325)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=2502)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.31` → IC=+0.139 (n=2319)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.31 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `4068.869` → IC=+0.313 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4068.869 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.302 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.344 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4211.4773` → IC=+0.304 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4211.4773 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.333 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.297 (n=515)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.386 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1466.3152` → IC=+0.312 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.3152 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.347 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.340)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.363 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.340)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.340)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `2547.1781` → IC=+0.440 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2547.1781 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.447 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.449 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2024.9352` → IC=+0.460 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.9352 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.381)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.299 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.4254` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.4254 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.299 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.4254` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.4254 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4785` → IC=+0.122 (n=7720)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.4785 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9821` → IC=+0.242 (n=2574)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9821 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.8334` → IC=+0.246 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8334 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.6283` → IC=+0.247 (n=2140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6283 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.93` → IC=+0.176 (n=2972)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.93 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0481` → IC=+0.258 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0481 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.305` → IC=+0.217 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.305 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.9076` → IC=+0.206 (n=3512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9076 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.5707` → IC=+0.132 (n=9306)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5707 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.5906` → IC=+0.194 (n=719)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5906 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.1493` → IC=+0.172 (n=2878)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1493 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` < `0.6997` → IC=+0.178 (n=1421)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6997 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `0.869` → IC=+0.175 (n=2152)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.869 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.168` → IC=+0.222 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.168 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `1.5754` → IC=+0.202 (n=4825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5754 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.211 (n=5182)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.063)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.182 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.171 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.166 (n=1747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=1172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.105` → IC=+0.271 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.105 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.214 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.164 (n=1632)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.251 (n=1162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.287 (n=434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.296 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.249 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0914` → IC=+0.232 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0914 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6252` → IC=+0.250 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6252 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1792.48` → IC=+0.240 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1792.48 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.231 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.234 (n=588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.251 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=1393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.215 (n=1354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.257 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.222 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.735` → IC=+0.218 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.735 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.83` → IC=+0.251 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.83 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.218 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.8736` → IC=+0.224 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8736 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.228 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.223 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.3766` → IC=+0.223 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3766 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `12308.655` → IC=+0.218 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12308.655 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.177 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.162 (n=462)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6918` → IC=+0.170 (n=1383)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6918 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1316` → IC=+0.157 (n=1219)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1316 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.202` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.202 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.236` → IC=+0.141 (n=1258)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.236 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.148 (n=1383)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2035 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8505` → IC=+0.139 (n=922)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8505 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.176 (n=372)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4183` → IC=+0.150 (n=1273)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4183 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.147 (n=848)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `13970.8027` → IC=+0.144 (n=922)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 13970.8027 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.147 (n=1193)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 411.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.213 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=1794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.253 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.2114` → IC=+0.188 (n=1702)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2114 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3626` → IC=+0.200 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3626 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.8549` → IC=+0.207 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8549 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=1204)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.223 (n=1454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.5839` → IC=+0.216 (n=1454)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5839 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.243 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.584` → IC=+0.243 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.584 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.269 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.221` → IC=+0.223 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.221 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1871.0584` → IC=+0.232 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1871.0584 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.216 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=96)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2138)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.211 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.3625` → IC=+0.328 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3625 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.7698` → IC=+0.328 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7698 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.666` → IC=+0.154 (n=685)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.666 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.6017` → IC=+0.330 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6017 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1956 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1787` → IC=+0.319 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1787 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.326 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.330 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.1901` → IC=+0.182 (n=338)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1901 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.159 (n=528)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8504 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `1.518` → IC=+0.177 (n=660)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.518 (IC base=+0.014)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.161 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=313)

- **FILTRO** `ibs_20min` < `0.2692` → IC=-0.202 (n=92)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=278)

- **FILTRO** `ibs_20min` > `0.2576` → IC=-0.125 (n=2112)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2576
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=1041)

- **FILTRO** `sigma_ewma_delta_pct` > `8.643` → IC=-0.204 (n=339)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.643
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2814)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7913 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `1.6434` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6434 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.7682` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7682 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.6541` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6541 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `0.7836` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7836 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.311 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `1.8428` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8428 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.2576` → IC=+0.125 (n=1041)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2576 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.68 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.4301` → IC=+0.211 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4301 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` < `1.096` → IC=+0.224 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.096 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` > `0.9027` → IC=+0.216 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9027 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1038` → IC=+0.228 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1038 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.262 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=-0.043)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6492` → IC=-0.184 (n=539)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6492
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1620)

- **FILTRO** `ibs_20min` < `0.705` → IC=-0.158 (n=1423)

  - _Acción_: SKIP cuando `ibs_20min` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=736)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.200 (n=401)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1758)

- **FILTRO** `ibs_20min` > `0.7734` → IC=-0.204 (n=799)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7734
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2399)

- **PATRÓN** `dist_vwap_pct` > `0.7625` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7625 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.314 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2675 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9865` → IC=+0.291 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9865 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.307 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.309 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4256` → IC=+0.298 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4256 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.7955` → IC=+0.295 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7955 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8119` → IC=+0.273 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8119 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7387` → IC=+0.248 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7387 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.283 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1689` → IC=+0.277 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1689 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.1737` → IC=+0.249 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1737 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.247 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.243 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4721` → IC=+0.188 (n=8631)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4721 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.7477` → IC=+0.287 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7477 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.571` → IC=+0.156 (n=4565)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.571 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.688` → IC=+0.247 (n=3060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.688 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.265 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.472` → IC=+0.240 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.472 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6854` → IC=+0.237 (n=1853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6854 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.268 (n=5079)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.149 (n=3221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.009 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.5488` → IC=+0.151 (n=8497)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5488 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.2431` → IC=+0.239 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2431 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.237 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.249 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2461` → IC=+0.303 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2461 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` < `1.485` → IC=+0.256 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.485 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `2.3302` → IC=+0.258 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3302 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.262 (n=3562)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.072)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.5` → IC=-0.165 (n=509)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.5
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1713)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.261 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.746` → IC=+0.202 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.746 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.274 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.176 (n=279)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.188 (n=379)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.177 (n=370)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 15.0 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4624` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4624 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8136` → IC=-0.149 (n=696)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8136
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=2091)

- **PATRÓN** `ibs_20min` > `0.8635` → IC=+0.157 (n=645)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.8635 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.173 (n=503)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6718` → IC=+0.162 (n=791)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6718 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.214 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.198 (n=289)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `247.0` → IC=+0.192 (n=375)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 247.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.16` → IC=+0.218 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.16 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6093` → IC=+0.213 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6093 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.4584` → IC=+0.224 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4584 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.233 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `477.0` → IC=+0.216 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 477.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.287 (n=511)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.248 (n=1540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.736` → IC=+0.280 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.736 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.1384` → IC=+0.257 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1384 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `3.4416` → IC=+0.260 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4416 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.255 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1944.5584` → IC=+0.256 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1944.5584 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.307 (n=806)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.597` → IC=+0.284 (n=1209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.597 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.329 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.289 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0909 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.808` → IC=+0.300 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.808 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3433` → IC=+0.307 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3433 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.6079` → IC=+0.283 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6079 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.7825` → IC=+0.287 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7825 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.292 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1925.4429` → IC=+0.302 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1925.4429 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.286 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2817` → IC=-0.192 (n=469)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2817
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1410)

- **FILTRO** `ibs_20min` > `0.7758` → IC=-0.184 (n=571)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7758
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1718)

- **PATRÓN** `ibs_20min` > `0.8153` → IC=+0.160 (n=639)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8153 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.4471` → IC=+0.226 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4471 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `0.9969` → IC=+0.237 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9969 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.5846` → IC=+0.207 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5846 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.0768` → IC=+0.253 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0768 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.5025` → IC=+0.260 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5025 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.259 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.635` → IC=+0.194 (n=446)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.635 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1531` → IC=+0.205 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1531 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` > `0.7182` → IC=+0.193 (n=353)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.7182 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.1651` → IC=+0.269 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1651 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8289` → IC=+0.252 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8289 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1743` → IC=+0.253 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1743 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.248 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7188` → IC=-0.201 (n=1024)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7188
  - _Potencial_: sin este filtro IC_bueno=+0.279 (n=1025)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.231 (n=536)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1613)

- **FILTRO** `sigma_ewma_delta_pct` > `4.685` → IC=-0.179 (n=468)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.685
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=1681)

- **PATRÓN** `ibs_20min` > `0.7188` → IC=+0.279 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7188 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8456` → IC=+0.336 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8456 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.527` → IC=+0.157 (n=327)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.527 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8648` → IC=+0.300 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8648 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.289 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.293 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.294 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.321 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.313 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.211 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.2098` → IC=+0.223 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2098 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.250 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1552` → IC=+0.205 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1552 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.5036` → IC=+0.220 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5036 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.237 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.319 (n=839)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.300 (n=593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.63` → IC=+0.313 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.63 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2012` → IC=+0.319 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2012 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.504` → IC=+0.307 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.504 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8624` → IC=+0.305 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8624 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.323 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1627` → IC=+0.291 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1627 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2618.726` → IC=+0.295 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2618.726 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.296 (n=908)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.279 (n=477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3985` → IC=+0.304 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3985 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.2901` → IC=+0.279 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2901 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.9381` → IC=+0.271 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9381 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.006` → IC=+0.297 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.006 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.2432` → IC=+0.311 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2432 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.338 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `1.4342` → IC=+0.268 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4342 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1632` → IC=+0.276 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1632 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2607.8903` → IC=+0.277 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2607.8903 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.171 (n=2530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.203 (n=2530)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.09` → IC=+0.185 (n=2527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.09 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=7889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.5789` → IC=+0.217 (n=7581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5789 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1749` → IC=+0.196 (n=3365)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1749 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.275` → IC=+0.259 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.275 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2161` → IC=+0.161 (n=5015)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2161 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.161 (n=5015)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6285 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.197 (n=1132)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5628` → IC=+0.172 (n=3196)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5628 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6282` → IC=+0.176 (n=2421)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6282 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2399.8931` → IC=+0.169 (n=5054)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2399.8931 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.182 (n=6490)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 116.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.182 (n=4790)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.209 (n=2396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.207 (n=2395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4783` → IC=+0.226 (n=7181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4783 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.228` → IC=+0.159 (n=5177)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.228 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.193 (n=1223)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.1742` → IC=+0.151 (n=5218)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1742 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.222 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5673` → IC=+0.164 (n=2863)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5673 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.2601` → IC=+0.172 (n=2949)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.2601 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.173 (n=6142)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 118.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.224 (n=433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.186 (n=588)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3421` → IC=+0.205 (n=1295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3421 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.107` → IC=+0.313 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.107 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.237 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.181 (n=1196)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.240 (n=818)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.253 (n=829)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.294 (n=619)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3443` → IC=+0.263 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3443 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.137` → IC=+0.254 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.137 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.237 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.252 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.507` → IC=+0.259 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.507 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1961.4408` → IC=+0.262 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.4408 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.238 (n=376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.198 (n=376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=1184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.4084` → IC=+0.224 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4084 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.212 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.234 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.2679` → IC=+0.163 (n=1127)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2679 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.169 (n=511)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0767 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2316` → IC=+0.197 (n=249)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2316 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.195 (n=365)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `15859.8442` → IC=+0.165 (n=511)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 15859.8442 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.196 (n=413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.29` → IC=+0.158 (n=1228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.29 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.175 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5646` → IC=+0.185 (n=1228)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5646 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.161 (n=1206)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.756` → IC=+0.208 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.756 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2096` → IC=+0.155 (n=1228)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2096 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1572` → IC=+0.154 (n=374)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1572 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.144 (n=1117)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.169 (n=348)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 216.0 (IC base=+0.136)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.221 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.2248` → IC=+0.215 (n=848)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2248 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.868` → IC=+0.276 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.868 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.21` → IC=+0.195 (n=1232)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.21 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.1335` → IC=+0.199 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1335 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.6438` → IC=+0.196 (n=402)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.6438 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.8719` → IC=+0.209 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8719 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.209 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.237 (n=1036)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0946` → IC=+0.259 (n=346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0946 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.281 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.2407` → IC=+0.256 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2407 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.729` → IC=+0.271 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.729 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.221` → IC=+0.230 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.221 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1874.4798` → IC=+0.231 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.4798 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.221 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.173 (n=1064)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0066 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4314` → IC=+0.159 (n=1209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4314 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3795` → IC=+0.195 (n=1209)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3795 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1585` → IC=+0.180 (n=819)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1585 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.868` → IC=+0.229 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.868 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0458` → IC=+0.146 (n=1064)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0458 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.149 (n=1209)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6297 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2462` → IC=+0.199 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2462 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5368` → IC=+0.150 (n=521)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5368 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5292` → IC=+0.172 (n=395)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5292 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `6941.7258` → IC=+0.186 (n=806)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6941.7258 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.144 (n=1150)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 166.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.156 (n=1267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.383` → IC=+0.143 (n=1267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.383 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6263` → IC=+0.169 (n=1267)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6263 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.5667` → IC=+0.134 (n=1455)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.5667 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.869` → IC=+0.174 (n=446)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 6.869 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.849` → IC=+0.146 (n=845)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.849 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.197 (n=183)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7891` → IC=+0.132 (n=766)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.7891 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4865` → IC=+0.134 (n=383)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4865 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9950.2818` → IC=+0.160 (n=575)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9950.2818 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.121 (n=1084)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 166.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=621)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=1399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5169` → IC=+0.204 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5169 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.833` → IC=+0.217 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.833 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.255 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.131 (n=1369)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2233 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6388` → IC=+0.122 (n=1368)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.6388 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.165` → IC=+0.131 (n=1376)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.165 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.0711` → IC=+0.122 (n=575)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0711 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4424` → IC=+0.146 (n=441)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4424 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1434)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2898.7698` → IC=+0.195 (n=621)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2898.7698 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.137 (n=1047)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.149 (n=611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.103` → IC=+0.151 (n=460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.103 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=1391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.208 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.7305` → IC=+0.136 (n=278)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7305 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.1956` → IC=+0.137 (n=1255)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1956 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.445` → IC=+0.145 (n=285)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 7.445 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.121 (n=1379)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.1845 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.4294` → IC=+0.131 (n=410)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4294 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `3082.2041` → IC=+0.158 (n=460)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3082.2041 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.216 (n=875)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.262 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.5007` → IC=+0.219 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5007 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.541` → IC=+0.247 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.541 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2094` → IC=+0.206 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2094 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.8592` → IC=+0.223 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8592 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.271 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.1554` → IC=+0.217 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1554 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4098` → IC=+0.208 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4098 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2801.857` → IC=+0.207 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2801.857 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.234 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.212 (n=610)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.221 (n=450)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.246 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1432` → IC=+0.231 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1432 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.8635` → IC=+0.204 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8635 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.243 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6303` → IC=+0.216 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6303 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.289 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.224` → IC=+0.193 (n=1059)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.224 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4431` → IC=+0.200 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4431 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2575.228` → IC=+0.209 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2575.228 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.163 (n=591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.178 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0089 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.154 (n=591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.5522` → IC=+0.188 (n=1584)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5522 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.8449` → IC=+0.188 (n=293)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8449 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.699` → IC=+0.177 (n=818)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.699 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8749` → IC=+0.163 (n=1032)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8749 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.21` → IC=+0.154 (n=516)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.21 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.177 (n=493)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.166 (n=570)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5508` → IC=+0.159 (n=569)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5508 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=2004)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `12252.2426` → IC=+0.151 (n=591)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12252.2426 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.166 (n=1550)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 164.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.131 (n=1237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0057 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.5224` → IC=+0.140 (n=1633)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5224 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `1.458` → IC=+0.133 (n=595)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.458 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3377` → IC=+0.124 (n=445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3377 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 8.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.2517` → IC=+0.144 (n=445)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.2517 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3049` → IC=+0.161 (n=160)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3049 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.264` → IC=+0.129 (n=200)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 3.264 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6182 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `12605.7065` → IC=+0.135 (n=398)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 12605.7065 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3374` → IC=+0.148 (n=592)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3374 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6039` → IC=+0.177 (n=521)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6039 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.4754` → IC=+0.147 (n=672)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.4754 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.152 (n=231)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.7202` → IC=+0.148 (n=529)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7202 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.205 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.150 (n=513)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4203` → IC=+0.140 (n=582)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4203 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `332.0` → IC=+0.141 (n=494)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 332.0 (IC base=+0.130)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.257 (n=237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.203 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0977` → IC=+0.214 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0977 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.7033` → IC=+0.248 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7033 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3816` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3816 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.047` → IC=+0.226 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.047 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.8407` → IC=+0.204 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8407 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.209 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.156 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2572` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2572 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.3913` → IC=+0.237 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3913 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.4105` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4105 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `12307.7364` → IC=+0.203 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12307.7364 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.0811` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.0811 (IC base=+0.081)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4167` → IC=-0.125 (n=166)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4167
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=326)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=456)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.185 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0089 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.1107` → IC=+0.129 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1107 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.163 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.239 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.127` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.127 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.0712` → IC=+0.145 (n=342)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0712 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.7306` → IC=+0.150 (n=347)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.7306 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4844` → IC=+0.143 (n=124)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4844 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.2151` → IC=+0.165 (n=168)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.2151 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=423)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `3060.3888` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3060.3888 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.159 (n=326)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4167 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.063)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0068 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6778` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6778 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.155 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0091 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.178` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.178 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8853` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8853 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.136 (n=201)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6515 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.6848` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.6848 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.207 (n=3216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=10050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4715` → IC=+0.216 (n=9649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4715 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9483` → IC=+0.207 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9483 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.811` → IC=+0.235 (n=3563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.811 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8816` → IC=+0.165 (n=4301)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8816 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2398` → IC=+0.202 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2398 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6068` → IC=+0.188 (n=3087)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6068 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2342.6107` → IC=+0.172 (n=6432)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2342.6107 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.195 (n=7281)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 87.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.187 (n=7692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0092 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1463` → IC=+0.189 (n=3844)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1463 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.237 (n=8737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5667 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2434` → IC=+0.160 (n=5362)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2434 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.949` → IC=+0.200 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.949 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.72` → IC=+0.182 (n=8462)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.72 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.158 (n=2652)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7054 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.2035` → IC=+0.153 (n=2008)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2035 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.241 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.193 (n=2662)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.191 (n=5081)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 48.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.210 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.219 (n=549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3514` → IC=+0.190 (n=1639)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3514 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.978` → IC=+0.312 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.978 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.251 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.2452` → IC=+0.201 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2452 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=964)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.260 (n=1269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.264 (n=1133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1279` → IC=+0.289 (n=558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1279 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=1137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3505` → IC=+0.291 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3505 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.563` → IC=+0.266 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.563 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.289 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.86` → IC=+0.274 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.86 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1961.4408` → IC=+0.277 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.4408 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0841` → IC=+0.162 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0841 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3134` → IC=+0.201 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3134 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1304` → IC=+0.187 (n=895)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1304 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.173 (n=353)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.23` → IC=+0.151 (n=1389)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.23 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.177 (n=515)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6288 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2686` → IC=+0.201 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2686 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1158` → IC=+0.161 (n=1311)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1158 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7583` → IC=+0.155 (n=993)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7583 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `15626.4863` → IC=+0.151 (n=701)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 15626.4863 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `476.0` → IC=+0.157 (n=1420)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 476.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.180 (n=445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.175 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.653` → IC=+0.192 (n=1335)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.653 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6851` → IC=+0.150 (n=232)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6851 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.166 (n=1192)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.398` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.398 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.186` → IC=+0.160 (n=1335)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.186 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1513` → IC=+0.198 (n=362)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1513 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4038` → IC=+0.158 (n=1237)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4038 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.0873` → IC=+0.164 (n=561)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.0873 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.156 (n=1003)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 423.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.243 (n=520)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6717` → IC=+0.255 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6717 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.81` → IC=+0.295 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.81 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2115` → IC=+0.220 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2115 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8451` → IC=+0.245 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8451 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.240 (n=1443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1645` → IC=+0.241 (n=636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1645 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.3617` → IC=+0.269 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3617 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.722` → IC=+0.281 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.722 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.295 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7653` → IC=+0.234 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7653 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1985` → IC=+0.239 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1985 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1872.7884` → IC=+0.255 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1872.7884 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.232 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.235)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.183 (n=551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.436` → IC=+0.143 (n=1643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.436 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=1715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.260 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.877 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5694` → IC=+0.174 (n=482)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.5694 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.153` → IC=+0.160 (n=683)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.153 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.877` → IC=+0.157 (n=1096)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.877 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.219 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5207` → IC=+0.149 (n=699)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5207 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1421` → IC=+0.147 (n=720)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1421 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8147.128` → IC=+0.230 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8147.128 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.156 (n=512)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 80.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4451` → IC=+0.154 (n=1341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4451 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6988` → IC=+0.183 (n=1341)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6988 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.7869` → IC=+0.142 (n=1549)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.7869 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.175 (n=198)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6969` → IC=+0.147 (n=590)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6969 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.144 (n=447)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1852 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.247 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.151 (n=1269)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `10953.5869` → IC=+0.206 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10953.5869 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.143 (n=1262)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 179.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.135 (n=1088)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0081 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.190 (n=1630)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4722 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0684` → IC=+0.204 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0684 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.451` → IC=+0.233 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.451 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8906` → IC=+0.135 (n=1087)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8906 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1646)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2912.6118` → IC=+0.249 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2912.6118 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.129 (n=1251)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 54.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.172 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.160 (n=534)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=1650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.202 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.128 (n=1290)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.451` → IC=+0.124 (n=1550)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.451 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.7204` → IC=+0.151 (n=705)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.7204 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.169 (n=249)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.5228` → IC=+0.131 (n=480)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5228 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2848.7898` → IC=+0.160 (n=534)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2848.7898 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0194` → IC=+0.220 (n=1090)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0194 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1460)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.5146` → IC=+0.250 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5146 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.234 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.156` → IC=+0.271 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.156 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.0716` → IC=+0.211 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0716 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.6363` → IC=+0.218 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6363 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2344` → IC=+0.251 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2344 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.5104` → IC=+0.237 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5104 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2616.3022` → IC=+0.224 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2616.3022 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.223 (n=583)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.218 (n=584)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.208 (n=1230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.254 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `1.1776` → IC=+0.203 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1776 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.8778` → IC=+0.203 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8778 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.738` → IC=+0.263 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.738 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.238 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.263 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2066` → IC=+0.193 (n=1377)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2066 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.196 (n=1565)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=2924)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.159 (n=2471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.150 (n=2505)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0056 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5234` → IC=+0.159 (n=2804)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5234 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.156 (n=936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.166 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.212 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1891` → IC=+0.156 (n=1029)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1891 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.4925` → IC=+0.144 (n=1668)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4925 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.136` → IC=+0.180 (n=457)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.136 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9026` → IC=+0.162 (n=1195)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.9026 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1724` → IC=+0.183 (n=770)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1724 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.157 (n=924)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8857` → IC=+0.161 (n=1847)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8857 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3698.7496` → IC=+0.151 (n=1869)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3698.7496 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.156 (n=2205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.166 (n=971)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1827 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6828` → IC=+0.153 (n=433)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6828 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.4283` → IC=+0.131 (n=2168)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4283 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.22` → IC=+0.146 (n=2197)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.22 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2464` → IC=+0.143 (n=2103)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2464 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.146 (n=1023)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5347` → IC=+0.144 (n=958)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5347 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8143` → IC=+0.144 (n=1452)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8143 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=2924)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6937.818` → IC=+0.151 (n=1970)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6937.818 (IC base=+0.137)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.167 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0056 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.177 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.185 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.189 (n=249)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5413 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.212` → IC=+0.150 (n=178)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.212 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.3752` → IC=+0.154 (n=362)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.3752 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.399` → IC=+0.163 (n=398)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 2.399 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2682` → IC=+0.151 (n=373)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2682 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.8487` → IC=+0.185 (n=249)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.8487 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.3073` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3073 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.185 (n=125)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.6651` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6651 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `12451.0907` → IC=+0.190 (n=333)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 12451.0907 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.214 (n=407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1125` → IC=+0.172 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1125 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.175 (n=407)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1382 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.144 (n=419)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6078 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6984` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6984 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2186` → IC=+0.138 (n=945)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2186 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.106` → IC=+0.152 (n=1010)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.106 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.184 (n=616)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8817 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.165 (n=434)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.422` → IC=+0.144 (n=307)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.422 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.148 (n=614)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `11387.9096` → IC=+0.149 (n=924)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11387.9096 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `706.0` → IC=+0.144 (n=878)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 706.0 (IC base=+0.137)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.174 (n=623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.3499` → IC=+0.170 (n=749)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3499 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.167 (n=622)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.165)

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
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.153 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0075 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.162 (n=859)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1256` → IC=+0.157 (n=287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1256 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.168 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5617` → IC=+0.156 (n=573)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5617 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.8892` → IC=+0.170 (n=286)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.8892 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9756` → IC=+0.163 (n=200)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.9756 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.4255` → IC=+0.165 (n=788)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.4255 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.162 (n=861)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.9005` → IC=+0.153 (n=574)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.9005 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7206` → IC=+0.155 (n=767)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7206 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.111` → IC=+0.155 (n=790)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.111 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1721` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1721 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.2095` → IC=+0.158 (n=740)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2095 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5194` → IC=+0.154 (n=752)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5194 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=836)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.155 (n=720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0084 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3946` → IC=+0.172 (n=632)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3946 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.147 (n=508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.735` → IC=+0.142 (n=718)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.735 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.1015` → IC=+0.153 (n=718)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.1015 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1663` → IC=+0.158 (n=360)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1663 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.3802` → IC=+0.144 (n=717)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3802 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.716` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.716 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.143 (n=653)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0991` → IC=+0.153 (n=632)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0991 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7262` → IC=+0.144 (n=642)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7262 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.170 (n=304)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.151 (n=620)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7767` → IC=+0.157 (n=470)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7767 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7593.8032` → IC=+0.165 (n=718)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7593.8032 (IC base=+0.140)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.2671` → IC=+0.132 (n=134)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.2671 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `3421.4081` → IC=+0.144 (n=186)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3421.4081 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.142 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0069 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.3981` → IC=+0.157 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3981 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.155 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.5982` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.5982 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.774` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.774 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` < `0.0921` → IC=+0.162 (n=155)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.0921 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3255.1743` → IC=+0.142 (n=202)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3255.1743 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.151 (n=196)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 62.0 (IC base=+0.109)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.218 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=348)

- **FILTRO** `dist_vwap_pct` > `0.1781` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1781
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=294)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.200 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.132 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.53` → IC=+0.182 (n=777)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.53 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.162 (n=439)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.422` → IC=+0.220 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.422 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.0922` → IC=+0.142 (n=585)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.0922 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=627)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2424.4386` → IC=+0.145 (n=342)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2424.4386 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.0667` → IC=+0.254 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0667 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.0685` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0685 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.5683` → IC=+0.133 (n=213)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.5683 (IC base=-0.003)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.261 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.5273` → IC=+0.187 (n=266)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5273 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.581` → IC=+0.130 (n=160)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.581 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.067` → IC=+0.123 (n=234)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.067 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.178 (n=200)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=273)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `4049.9563` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4049.9563 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0889` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0889 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.5944` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.5944 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.3732` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.3732 (IC base=+0.047)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=109)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=110)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.165 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0051 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.137 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.6839` → IC=+0.229 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6839 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.792` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.792 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.8141` → IC=+0.128 (n=178)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8141 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` > `0.9558` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.9558 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.7354` → IC=+0.158 (n=144)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7354 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` > `1.4015` → IC=+0.122 (n=215)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.4015 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=176)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `1771.0926` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1771.0926 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1197` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1197 (IC base=-0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.765` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.765 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.6357` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6357 (IC base=-0.017)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=-0.017)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.2353` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2353
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=59)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.124 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0079 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.123 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 9.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.180 (n=220)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6757 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1957` → IC=+0.158 (n=144)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1957 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.203 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0643 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.0847` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0847 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.468` → IC=+0.124 (n=224)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.468 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=-0.061)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0875 (IC base=-0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.195` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.195 (IC base=-0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.1383` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1383 (IC base=-0.061)

- **PATRÓN** `volumen_spike_ratio` > `1.3803` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.3803 (IC base=-0.061)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `9.0` → IC=-0.396 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=148)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=179)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.348 (n=64)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=130)

- **FILTRO** `dist_vwap_pct` > `0.338` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.338
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=134)

- **FILTRO** `sigma_ewma_delta_pct` > `8.432` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.432
  - _Potencial_: sin este filtro IC_bueno=-0.299 (n=137)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.306 (n=65)

- **FILTRO** `volumen_spike_ratio` > `1.948` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.948
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=61)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=53)

- **FILTRO** `ibs_20min` < `0.0329` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0329
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `volumen_regimen` < `0.8127` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8127
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=51)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=47)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.309 (n=40)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `sigma_ewma_delta_pct` > `5.128` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.128
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=49)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=52)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8798` → IC=-0.409 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8798
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.346 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `ibs_20min` > `0.6482` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6482
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=28)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=45)

- **FILTRO** `volumen_spike_ratio` > `2.138` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.138
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `dist_vwap_pct` > `0.6142` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=314)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.137 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0057 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.133 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6522 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.4919` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.4919 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.038)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=89)

- **FILTRO** `ibs_20min` < `0.576` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.576
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=81)

- **PATRÓN** `volumen_spike_ratio` > `1.4652` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4652 (IC base=-0.018)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.113` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.113 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` < `0.1891` → IC=+0.144 (n=85)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1891 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.9499` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.9499 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.101)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_liquidez` < `1549.4073` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 1549.4073
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=55)

- **FILTRO** `ibs_20min` > `0.3115` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3115
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=82)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0042 (IC base=+0.059)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.125 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.059)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8361 (IC base=+0.059)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.009)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0772` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0772
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=19)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.194 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0069 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.214 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.189 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.6875` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6875 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7975` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7975 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.06 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.050)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.3675` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3675 (IC base=+0.284)

- **PATRÓN** `elapsed_s` > `209.6` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.6 (IC base=+0.284)

- **PATRÓN** `drift_15min` |x|≤ `1.2733` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2733 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.8446` → IC=+0.357 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8446 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `1559.0` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1559.0 (IC base=+0.284)

- **PATRÓN** `elapsed_s` > `190.7` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 190.7 (IC base=+0.189)

- **PATRÓN** `drift_15min` |x|≤ `2.0335` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.0335 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.292 (n=22)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.189)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.3675` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3675 (IC base=+0.284)

- **PATRÓN** `elapsed_s` > `209.6` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 209.6 (IC base=+0.284)

- **PATRÓN** `drift_15min` |x|≤ `1.2733` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2733 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.8446` → IC=+0.357 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8446 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `1559.0` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1559.0 (IC base=+0.284)

- **PATRÓN** `elapsed_s` > `190.7` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 190.7 (IC base=+0.189)

- **PATRÓN** `drift_15min` |x|≤ `2.0335` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.0335 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.292 (n=22)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.189)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=663)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2900.177` → IC=+0.173 (n=224)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2900.177 (IC base=+0.106)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=663)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2900.177` → IC=+0.173 (n=224)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2900.177 (IC base=+0.106)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=78)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=131)

- **FILTRO** `libro_liquidez` < `2415.4574` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 2415.4574
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=111)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=205)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=191)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1700)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.167 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=66)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `29085.84` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `liq_usd_total` < 29085.84
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=129)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `569.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 569.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_n` > `18.0` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.029)

- **PATRÓN** `liq_usd_total` > `80598.37` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `liq_usd_total` > 80598.37 (IC base=+0.029)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.029)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=753)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=427)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=144)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8693` → IC=-0.167 (n=40)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8693
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=120)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=85)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=616)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=616)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=488)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=334)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=334)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.148 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=263)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=171)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=171)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.122 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=99)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=197)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=85)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=78)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=233)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=233)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7387)

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

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.172 (n=3210)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=10323)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.171 (n=3469)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=10494)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.211 (n=569)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1767)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.154 (n=622)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=1879)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.203 (n=583)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1803)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.206 (n=611)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1881)

- **FILTRO** `ibs_20min` > `0.282` → IC=-0.164 (n=622)

  - _Acción_: SKIP cuando `ibs_20min` > 0.282
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1870)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.174 (n=556)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1767)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.186 (n=615)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1879)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2707)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2873)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2879)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=615)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` > `0.1705` → IC=-0.142 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1705
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=356)

- **FILTRO** `libro_liquidez` < `16909.6913` → IC=-0.141 (n=218)

  - _Acción_: SKIP cuando `libro_liquidez` < 16909.6913
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=656)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=237)

- **FILTRO** `ibs_20min` < `0.1064` → IC=-0.244 (n=76)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1064
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=226)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=192)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=581)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

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
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=9682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=21395)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=7558)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=23519)

- **FILTRO** `ibs_7min` < `0.2882` → IC=-0.234 (n=7769)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2882
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=23308)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=10537)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=20540)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9597)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=29239)

- **FILTRO** `ibs_7min` > `0.2941` → IC=-0.180 (n=9684)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=29152)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.305 (n=1221)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3904)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.249 (n=1689)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3436)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.182 (n=1185)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3940)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.260 (n=1654)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=5029)

- **FILTRO** `drift_7min_pct` |x|> `0.1117` → IC=-0.124 (n=2266)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1117
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4417)

- **FILTRO** `ibs_7min` > `0.7929` → IC=-0.207 (n=1670)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7929
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=5013)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4111)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1290)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4086)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.191 (n=1344)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4032)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.170 (n=1338)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4038)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.254 (n=1349)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4085)

- **FILTRO** `ibs_7min` > `0.2605` → IC=-0.177 (n=1358)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2605
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4076)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.186 (n=1350)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4084)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.166 (n=1393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=3457)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.305 (n=1189)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=3661)

- **FILTRO** `ibs_7min` < `0.1935` → IC=-0.258 (n=1207)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3643)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.215 (n=1138)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3712)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.239 (n=1648)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=5483)

- **FILTRO** `ibs_7min` > `0.7536` → IC=-0.178 (n=1782)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7536
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=5349)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1516)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3614)

- **FILTRO** `ibs_7min` < `0.7422` → IC=-0.180 (n=1282)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7422
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3848)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.168 (n=1256)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3874)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=1154)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4054)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.174 (n=1301)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3907)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.190 (n=1281)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3927)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.262 (n=1301)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=4133)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.240 (n=1344)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4090)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1777)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5607)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1222)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3940)

- **FILTRO** `ibs_7min` < `0.7024` → IC=-0.227 (n=1290)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7024
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3872)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1241)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3921)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.203 (n=1701)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=5295)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1054)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=525)

- **FILTRO** `libro_liquidez` < `10599.4565` → IC=-0.146 (n=142)

  - _Acción_: SKIP cuando `libro_liquidez` < 10599.4565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=429)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=865)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=546)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.149 (n=479)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.153 (n=240)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 459.6089 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4386` → IC=+0.138 (n=56)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.4386 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.140 (n=148)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 422.506 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 12.0 (IC base=+0.133)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.093)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.177 (n=97)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.095)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 69.0 (IC base=+0.095)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.180 (n=126)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.250 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 6300.756 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 37.0 (IC base=+0.145)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.151 (n=127)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.143 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 13.0 (IC base=+0.108)

- **PATRÓN** `total_vol_5m` < `258575.4` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 258575.4 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `3729.2002` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3729.2002 (IC base=+0.108)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.306 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=179)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.339 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.167 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0053 (IC base=-0.143)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

- **FILTRO** `T_h` < `39.9942` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` < 39.9942
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `110.887` → IC=-0.150 (n=181)

  - _Acción_: SKIP cuando `T_h` > 110.887
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=183)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.232 (n=181)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=183)

- **FILTRO** `pct_vs_K` |x|> `3.3681` → IC=-0.434 (n=104)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3681
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=206)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.206 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=96)

- **FILTRO** `pct_vs_K` |x|> `0.8662` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 0.8662
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=45)

- **FILTRO** `T_h` < `96.6729` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `T_h` < 96.6729
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=76)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `98.1124` → IC=-0.211 (n=50)

  - _Acción_: SKIP cuando `T_h` > 98.1124
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=52)

- **FILTRO** `pct_vs_K` |x|> `2.4552` → IC=-0.343 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4552
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=53)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.315 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=76)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=76)

- **FILTRO** `T_h` > `49.1198` → IC=-0.318 (n=75)

  - _Acción_: SKIP cuando `T_h` > 49.1198
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0144` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0144
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=64)

- **FILTRO** `T_h` > `133.663` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `T_h` > 133.663
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `pct_vs_K` |x|> `4.625` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.625
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **FILTRO** `sigma_h` < `0.0148` → IC=-0.372 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0148
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `T_h` > `74.8914` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `T_h` > 74.8914
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.131` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.131 (IC base=+0.390)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.473 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.390)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.390)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.390)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.466 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.390)

- **PATRÓN** `edge` > `0.097` → IC=+0.455 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.467 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.420)

- **PATRÓN** `T_h` < `0.639` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.639 (IC base=+0.420)

- **PATRÓN** `T_h` > `1.3581` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.3581 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.4447` → IC=+0.483 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4447 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.467 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.420)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1134` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1134 (IC base=+0.406)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.389 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.406)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.406)

- **PATRÓN** `T_h` < `1.0863` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0863 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.406)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.481)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.471 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.481)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.471 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.481)

- **PATRÓN** `T_h` < `1.3025` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.3025 (IC base=+0.481)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.481)

- **PATRÓN** `dist_50` > `0.376` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.376 (IC base=+0.481)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.481)

- **PATRÓN** `edge` > `0.096` → IC=+0.477 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.477)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.477 (n=86)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.477)

- **PATRÓN** `T_h` > `0.958` → IC=+0.475 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.958 (IC base=+0.477)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.488 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.477)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.469 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.477)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=162)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=284)

- **PATRÓN** `streak_estiramiento` < `0.4117` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.4117 (IC base=+0.031)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.034)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `990711.2` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_racha` > 990711.2
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=27)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 52.0 (IC base=+0.000)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=77)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=725)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=731)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=386)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `libro_liquidez` < `3086.3665` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 3086.3665
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=570)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=719)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=694)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2819)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1441)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1449)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.224 (n=687)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0514` → IC=+0.204 (n=505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0514 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2134` → IC=+0.192 (n=505)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2134 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1267` → IC=+0.231 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1267 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=1409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.186 (n=1526)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 16.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6077` → IC=+0.263 (n=1514)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6077 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.2989` → IC=+0.191 (n=545)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2989 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.899` → IC=+0.274 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.899 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2980.0928` → IC=+0.193 (n=1009)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2980.0928 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.206 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=550)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.211 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.298 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.199)

- **PATRÓN** `drift_15min` |x|≤ `0.3811` → IC=+0.206 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3811 (IC base=+0.199)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.248 (n=117)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.199)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1432` → IC=+0.264 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1432 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.220 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.199)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.265 (n=351)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.234 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.503` → IC=+0.252 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.503 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `15953.0262` → IC=+0.239 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15953.0262 (IC base=+0.199)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `25.169` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 25.169
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=345)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.141 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0065 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.161 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0051 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.069` → IC=+0.156 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.069 (IC base=+0.138)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.178 (n=119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.138)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.160 (n=251)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `ibs_15` > `0.665` → IC=+0.240 (n=317)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.665 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.5539` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.5539 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1651` → IC=+0.156 (n=274)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1651 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.389` → IC=+0.205 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.389 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3459.7073` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3459.7073 (IC base=+0.138)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2219` → IC=-0.224 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2219
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=83)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.294 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.213 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.211 (n=164)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.175)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2717` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2717 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.219 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.175)

- **PATRÓN** `ibs_15` > `0.6122` → IC=+0.257 (n=183)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6122 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.2696` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2696 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.786` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.786 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `3056.7878` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3056.7878 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.233 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.175)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.692` → IC=-0.154 (n=102)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.692
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=847)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.662` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 15.662 (IC base=+0.004)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.235 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0859` → IC=+0.206 (n=178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0859 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0602` → IC=+0.198 (n=362)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.0602 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.252 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.239 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.5429` → IC=+0.284 (n=405)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5429 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1302` → IC=+0.207 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1302 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.853` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.853 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.408` → IC=+0.190 (n=362)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 7.408 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2905.2468` → IC=+0.281 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2905.2468 (IC base=+0.188)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.159 (n=452)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1176 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.335 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.374 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.343 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.361 (n=264)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.371 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.357 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.380 (n=397)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4313` → IC=+0.380 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4313 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.340 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `3544.0094` → IC=+0.352 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3544.0094 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `474.0` → IC=+0.359 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 474.0 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.349 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.340)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.370 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.340)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.370 (n=75)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.340)

- **PATRÓN** `drift_15min` |x|≤ `0.4326` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4326 (IC base=+0.340)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.360 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.340)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.382 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.366 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.340)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.376 (n=223)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.343 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `15670.1365` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15670.1365 (IC base=+0.340)

- **PATRÓN** `ballena_activa_n` < `581.0` → IC=+0.387 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 581.0 (IC base=+0.340)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.378 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.340 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.349 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.355 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.393 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7403` → IC=+0.386 (n=174)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7403 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.1256` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1256 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.334 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.344 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `3553.0968` → IC=+0.356 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3553.0968 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.338 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 166.0 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.215 (n=634)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1904)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.187 (n=848)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1690)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.254 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.060)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.268 (n=614)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `0.5693` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5693 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.2752` → IC=+0.178 (n=480)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2752 (IC base=-0.060)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1178` → IC=+0.240 (n=1081)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1178 (IC base=-0.037)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1772` → IC=+0.234 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1772 (IC base=-0.037)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.274 (n=1626)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.6604` → IC=+0.280 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6604 (IC base=-0.037)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.217 (n=387)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1163)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.228 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1163)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.208 (n=977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=573)

- **FILTRO** `sigma_ewma_delta_pct` > `19.563` → IC=-0.249 (n=277)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.563
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1273)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.173 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0028 (IC base=+0.076)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.279 (n=75)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.076)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=+0.076)

- **PATRÓN** `ibs_15` > `0.7466` → IC=+0.320 (n=165)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7466 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.281 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.5415` → IC=+0.271 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5415 (IC base=+0.076)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6647` → IC=-0.197 (n=97)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6647
  - _Potencial_: sin este filtro IC_bueno=+0.263 (n=293)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=373)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0068 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.190 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0051 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.218 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.148)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.160 (n=195)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.238 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.263 (n=293)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.4713` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.4713 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.164` → IC=+0.176 (n=223)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.164 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.009` → IC=+0.157 (n=249)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 9.009 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=373)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.196 (n=133)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.262 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `0.7799` → IC=+0.232 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7799 (IC base=+0.226)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2005` → IC=+0.253 (n=294)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2005 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.226)

- **PATRÓN** `ibs_15` < `0.3469` → IC=+0.264 (n=647)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3469 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.7306` → IC=+0.302 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7306 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.823` → IC=+0.252 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.823 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.189` → IC=+0.230 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.189 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3551.8492` → IC=+0.226 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.8492 (IC base=+0.226)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.227 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=447)

- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.216 (n=202)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=393)

- **FILTRO** `drift_15min` |x|> `0.8849` → IC=-0.260 (n=148)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8849
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=447)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.162)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.162)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0756` → IC=+0.218 (n=264)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0756 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.258 (n=295)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.7377` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7377 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.9272` → IC=+0.204 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9272 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.259 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=377)

- **FILTRO** `drift_15min` |x|> `1.2346` → IC=-0.257 (n=187)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2346
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=565)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=185)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=567)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1533` → IC=+0.277 (n=146)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1533 (IC base=-0.048)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.350 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.048)

- **PATRÓN** `ibs_15` < `0.3457` → IC=+0.304 (n=438)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3457 (IC base=-0.048)

- **PATRÓN** `dist_vwap_pct` > `0.8637` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8637 (IC base=-0.048)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.200 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.064)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.200 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.064)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.292 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.288 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.057` → IC=+0.319 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.057 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.309 (n=213)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.344 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.324 (n=640)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.1578` → IC=+0.320 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1578 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.329 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `14446.4188` → IC=+0.301 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14446.4188 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.310 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.285 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.343 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.308 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3796` → IC=+0.302 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3796 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.312 (n=355)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.4357` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4357 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.326 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.306 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.298 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1882` → IC=+0.312 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1882 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.334 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.330 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.336 (n=285)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` < `0.456` → IC=+0.294 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.456 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.315 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.186 (n=68)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=205)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1131` → IC=-0.171 (n=68)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1131
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=205)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1209` → IC=-0.164 (n=108)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1209
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=325)

- **FILTRO** `drift_15min` |x|> `0.5291` → IC=-0.136 (n=108)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5291
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=325)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1445` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1445
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=107)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `drift_15min` |x|> `0.2655` → IC=-0.220 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `87.9957` → IC=+0.200 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.466 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.193)

- **PATRÓN** `T_h` > `145.7851` → IC=+0.394 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7851 (IC base=+0.333)

- **PATRÓN** `ratio` > `1.008` → IC=+0.286 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.008 (IC base=+0.333)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `88.3739` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `T_h` < 88.3739 (IC base=+0.165)

- **PATRÓN** `T_h` > `144.0548` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `T_h` > 144.0548 (IC base=+0.165)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.165)

- **PATRÓN** `T_h` > `98.314` → IC=+0.295 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 98.314 (IC base=+0.284)

- **PATRÓN** `ratio` > `1.0449` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0449 (IC base=+0.284)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9936` → IC=+0.258 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9936 (IC base=+0.239)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.408 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.239)

- **PATRÓN** `T_h` > `102.672` → IC=+0.329 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.672 (IC base=+0.309)

- **PATRÓN** `ratio` > `1.01` → IC=+0.310 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.309)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1402` → IC=+0.455 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1402 (IC base=+0.403)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6077 sube el IC de +0.186 a +0.263 en UPDOWN_GBM#15min (n=1514). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.199 a +0.265 en UPDOWN_GBM#BTC#15min (n=351). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.665 sube el IC de +0.138 a +0.240 en UPDOWN_GBM#ETH#15min (n=317). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6122 sube el IC de +0.175 a +0.257 en UPDOWN_GBM#SOL#15min (n=183). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.188 a +0.284 en UPDOWN_GBM#XRP#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.046 a +0.159 en UPDOWN_GBM#XRP#15min (n=452). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.060 a +0.268 en UPDOWN_GBM_15M_TARDIO (n=614). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.037 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=1626). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7466 sube el IC de +0.076 a +0.320 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=165). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.148 a +0.263 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=293). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3469 sube el IC de +0.226 a +0.264 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=647). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.162 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.044 a +0.258 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=295). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3457 sube el IC de -0.048 a +0.304 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=438). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.288 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=640). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.281 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=355). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.296 a +0.336 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=285). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.336 a +0.380 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=397). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.340 a +0.376 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=223). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7403 sube el IC de +0.329 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=174). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1283 | +0.096 | +181.80€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1283 | +0.096 | +181.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 952 | +0.106 | +155.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 952 | +0.106 | +155.28€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 245 | +0.051 | +7.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 245 | +0.051 | +7.87€ | 5 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 24346 | -0.090 | -3069.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1431 | -0.047 | -221.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 22915 | -0.093 | -2848.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3569 | -0.084 | -576.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3569 | -0.084 | -576.62€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1431 | -0.047 | -221.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1431 | -0.047 | -221.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7009 | -0.022 | -614.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7009 | -0.022 | -614.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6495 | -0.096 | -423.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6495 | -0.096 | -423.77€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5468 | -0.183 | -1071.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5468 | -0.183 | -1071.78€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 17094 | -0.029 | +4085.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4477 | -0.000 | +1825.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 12617 | -0.040 | +2259.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 17094 | -0.029 | +4085.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4477 | -0.000 | +1825.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 12617 | -0.040 | +2259.79€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1469 | -0.102 | -185.83€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1301 | -0.108 | -164.47€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 89441 | +0.113 | -4547.89€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13617 | +0.184 | -431.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 357 | -0.093 | -51.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 69600 | +0.100 | -3849.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5867 | +0.108 | -215.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11581 | +0.098 | -992.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11522 | +0.100 | -977.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 18094 | +0.132 | -363.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4269 | +0.202 | -142.72€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11537 | +0.112 | -171.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2246 | +0.106 | -27.14€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11620 | +0.089 | -1081.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11554 | +0.091 | -1064.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 19052 | +0.123 | -404.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5263 | +0.175 | -79.17€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11655 | +0.105 | -263.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2122 | +0.098 | -53.89€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17496 | +0.114 | -1024.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3945 | +0.188 | -208.18€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 260 | -0.053 | +2.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11792 | +0.092 | -684.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1499 | +0.126 | -134.04€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11598 | +0.101 | -681.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 45 | -0.032 | +7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11540 | +0.102 | -688.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14191 | +0.192 | -916.47€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14191 | +0.192 | -916.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3395 | +0.168 | -358.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3395 | +0.168 | -358.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1118 | +0.196 | -4.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1118 | +0.196 | -4.93€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3338 | +0.181 | -281.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3338 | +0.181 | -281.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2984 | +0.238 | -97.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2984 | +0.238 | -97.39€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3277 | +0.195 | -187.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3277 | +0.195 | -187.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 668 | +0.430 | -18.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 668 | +0.430 | -18.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 256 | +0.434 | -4.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 256 | +0.434 | -4.38€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 251 | +0.437 | -2.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 251 | +0.437 | -2.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 153 | +0.403 | -10.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 153 | +0.403 | -10.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 48780 | +0.198 | -3805.32€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 48780 | +0.198 | -3805.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8454 | +0.176 | -987.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8454 | +0.176 | -987.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7784 | +0.224 | -279.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7784 | +0.224 | -279.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8420 | +0.174 | -998.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8420 | +0.174 | -998.67€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7878 | +0.219 | -302.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7878 | +0.219 | -302.25€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8054 | +0.204 | -529.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8054 | +0.204 | -529.51€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8190 | +0.194 | -707.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8190 | +0.194 | -707.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 18370 | +0.117 | +125.70€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 18370 | +0.117 | +125.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9117 | +0.122 | +125.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9117 | +0.122 | +125.98€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9253 | +0.113 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9253 | +0.113 | -0.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1427 | +0.293 | -2.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1427 | +0.293 | -2.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 637 | +0.279 | -13.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 637 | +0.279 | -13.45€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 686 | +0.296 | +8.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 686 | +0.296 | +8.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 104 | +0.340 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 104 | +0.340 | +1.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 623 | +0.439 | +1.61€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 623 | +0.439 | +1.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 294 | +0.439 | +0.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 294 | +0.439 | +0.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 289 | +0.442 | +1.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 289 | +0.442 | +1.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 40 | +0.381 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 40 | +0.381 | -0.11€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1067 | +0.079 | -34.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 370 | +0.070 | -23.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 697 | +0.084 | -11.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 840 | +0.086 | -11.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 143 | +0.093 | -0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 697 | +0.084 | -11.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 166 | +0.030 | -26.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 166 | +0.030 | -26.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 33782 | +0.097 | -1062.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2799 | +0.089 | +17.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 30983 | +0.098 | -1079.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 19018 | +0.102 | -316.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2799 | +0.089 | +17.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 16219 | +0.104 | -333.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6281 | +0.106 | -52.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6281 | +0.106 | -52.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8483 | +0.081 | -692.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8483 | +0.081 | -692.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 783 | +0.213 | -96.69€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 783 | +0.213 | -96.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 783 | +0.213 | -96.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 783 | +0.213 | -96.69€ | 2 | 4 |
| ✅ GBM_LATE_15M | 24392 | +0.081 | +11475.99€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 24392 | +0.081 | +11475.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4062 | +0.193 | +2947.50€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4062 | +0.193 | +2947.50€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 3616 | +0.176 | +2495.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3616 | +0.176 | +2495.21€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 4214 | +0.200 | +3166.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4214 | +0.200 | +3166.14€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 3620 | +0.017 | +726.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3620 | +0.017 | +726.61€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3523 | -0.033 | +806.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3523 | -0.033 | +806.78€ | 4 | 16 |
| ✅ GBM_LATE_15M#XRP | 5357 | -0.043 | +1333.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5357 | -0.043 | +1333.76€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 25755 | +0.085 | +13423.23€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 25755 | +0.085 | +13423.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4881 | +0.016 | +2610.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4881 | +0.016 | +2610.86€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5366 | +0.013 | +1083.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5366 | +0.013 | +1083.12€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3648 | +0.262 | +3672.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3648 | +0.262 | +3672.15€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4168 | +0.000 | +768.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4168 | +0.000 | +768.63€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4198 | +0.026 | +1571.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4198 | +0.026 | +1571.24€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3494 | +0.275 | +3717.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3494 | +0.275 | +3717.24€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 19680 | +0.168 | +14644.63€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 19680 | +0.168 | +14644.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2962 | +0.206 | +2346.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2962 | +0.206 | +2346.61€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3139 | +0.148 | +2262.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3139 | +0.148 | +2262.73€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3076 | +0.209 | +2458.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3076 | +0.209 | +2458.48€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3300 | +0.134 | +2288.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3300 | +0.134 | +2288.27€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3662 | +0.115 | +2486.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3662 | +0.115 | +2486.81€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3541 | +0.204 | +2801.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3541 | +0.204 | +2801.73€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4836 | +0.124 | +1967.19€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4836 | +0.124 | +1967.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1382 | +0.119 | +604.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1382 | +0.119 | +604.39€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1385 | +0.140 | +591.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1385 | +0.140 | +591.98€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1009 | +0.096 | +299.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1009 | +0.096 | +299.20€ | 2 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 24507 | +0.174 | +18119.67€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 24507 | +0.174 | +18119.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3875 | +0.220 | +3253.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3875 | +0.220 | +3253.54€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3838 | +0.149 | +2511.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3838 | +0.149 | +2511.53€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4000 | +0.226 | +3456.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4000 | +0.226 | +3456.16€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3977 | +0.136 | +2678.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3977 | +0.136 | +2678.82€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4307 | +0.111 | +2680.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4307 | +0.111 | +2680.21€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4510 | +0.205 | +3539.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4510 | +0.205 | +3539.41€ | 0 | 24 |
| ✅ GBM_LATE_5M | 6677 | +0.144 | +3722.94€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6677 | +0.144 | +3722.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1728 | +0.141 | +1097.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1728 | +0.141 | +1097.34€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2101 | +0.147 | +1149.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2101 | +0.147 | +1149.76€ | 0 | 33 |
| ✅ GBM_LATE_5M#SOL | 546 | +0.099 | +178.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 546 | +0.099 | +178.45€ | 0 | 14 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1620 | +0.070 | +706.31€ | 2 | 12 |
| ✅ GBM_LATE_60M#60min | 1620 | +0.070 | +706.31€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 583 | +0.088 | +247.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 583 | +0.088 | +247.13€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 540 | +0.074 | +269.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 540 | +0.074 | +269.93€ | 2 | 18 |
| ✅ GBM_LATE_60M#SOL | 497 | +0.043 | +189.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 497 | +0.043 | +189.25€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 360 | -0.262 | -28.78€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 360 | -0.262 | -28.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 137 | -0.227 | -11.84€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 137 | -0.227 | -11.84€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 119 | -0.269 | -10.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 119 | -0.269 | -10.66€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 104 | -0.292 | -6.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 104 | -0.292 | -6.28€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 668 | +0.063 | +125.93€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 668 | +0.063 | +125.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 264 | +0.053 | +44.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 264 | +0.053 | +44.92€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 190 | +0.031 | -3.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 190 | +0.031 | -3.08€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 214 | +0.102 | +84.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 214 | +0.102 | +84.09€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 92 | +0.245 | +68.60€ | 0 | 9 |
| ✅ LATE_WINDOW_5MIN#5min | 92 | +0.245 | +68.60€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 92 | +0.245 | +68.60€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 92 | +0.245 | +68.60€ | 0 | 9 |
| ✅ LEADLAG_BTC_XRP_15M | 1835 | +0.095 | +486.27€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1835 | +0.095 | +486.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1835 | +0.095 | +486.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1835 | +0.095 | +486.27€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 373 | -0.081 | -34.54€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 373 | -0.081 | -34.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 131 | -0.026 | -4.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 131 | -0.026 | -4.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1898 | +0.006 | +16.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1898 | +0.006 | +16.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 100 | +0.020 | -1.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 100 | +0.020 | -1.02€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 206 | -0.005 | +12.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 206 | -0.005 | +12.83€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 152 | -0.039 | -7.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 152 | -0.039 | -7.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 800 | +0.029 | +24.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 800 | +0.029 | +24.42€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 467 | -0.001 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 467 | -0.001 | -5.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 173 | -0.037 | -7.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 173 | -0.037 | -7.24€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 1045 | -0.049 | -32.44€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1045 | -0.049 | -32.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 300 | -0.043 | -13.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 300 | -0.043 | -13.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 347 | -0.042 | -6.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 347 | -0.042 | -6.83€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 398 | -0.060 | -12.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 398 | -0.060 | -12.55€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 474 | -0.017 | +6.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 226 | -0.009 | +9.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 248 | -0.024 | -2.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 14 | -0.044 | -1.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 8 | +0.040 | +2.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 6 | -0.075 | -3.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 127 | +0.089 | +32.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 59 | +0.074 | +12.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 68 | +0.100 | +19.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 79 | -0.068 | -7.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 39 | -0.061 | -3.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 40 | -0.071 | -4.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 77 | -0.057 | -6.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 36 | -0.053 | -2.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 41 | -0.058 | -4.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 71 | +0.034 | +6.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 39 | +0.012 | +3.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 32 | +0.059 | +2.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 106 | -0.102 | -16.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 45 | -0.074 | -4.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 61 | -0.119 | -12.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 14251 | -0.012 | -207.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14251 | -0.012 | -207.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2968 | -0.021 | -60.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2968 | -0.021 | -60.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 27496 | -0.008 | +1192.32€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 27496 | -0.008 | +1192.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4837 | +0.016 | +594.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4837 | +0.016 | +594.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4290 | -0.028 | -55.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4290 | -0.028 | -55.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4878 | +0.013 | +428.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4878 | +0.013 | +428.05€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4070 | -0.052 | -144.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4070 | -0.052 | -144.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4604 | -0.012 | +176.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4604 | -0.012 | +176.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4817 | +0.006 | +193.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4817 | +0.006 | +193.53€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5681 | -0.056 | -132.82€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5681 | -0.056 | -132.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1348 | -0.075 | -32.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1348 | -0.075 | -32.70€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 597 | -0.119 | -21.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 597 | -0.119 | -21.93€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1643 | -0.076 | -31.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1643 | -0.076 | -31.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 69913 | -0.073 | +1722.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 69913 | -0.073 | +1722.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11808 | -0.079 | +683.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11808 | -0.079 | +683.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10810 | -0.093 | -474.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10810 | -0.093 | -474.54€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11981 | -0.067 | +668.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11981 | -0.067 | +668.89€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10338 | -0.092 | -130.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10338 | -0.092 | -130.95€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12818 | -0.048 | +388.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12818 | -0.048 | +388.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12158 | -0.062 | +586.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12158 | -0.062 | +586.96€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7242 | -0.023 | -105.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7242 | -0.023 | -105.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1640 | -0.025 | -1.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1640 | -0.025 | -1.22€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1839 | -0.016 | -12.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1839 | -0.016 | -12.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1026 | -0.040 | -17.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1026 | -0.040 | -17.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1094 | +0.109 | +371.14€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 958 | +0.116 | +358.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 224 | +0.133 | +107.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 224 | +0.133 | +107.92€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 187 | +0.093 | +43.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 187 | +0.093 | +43.26€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 193 | +0.095 | +62.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 193 | +0.095 | +62.76€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 167 | +0.145 | +84.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 167 | +0.145 | +84.75€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 187 | +0.108 | +59.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 187 | +0.108 | +59.86€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 429 | -0.057 | -47.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 429 | -0.057 | -47.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 95 | -0.015 | +1.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 95 | -0.015 | +1.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 120 | -0.082 | -24.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 120 | -0.082 | -24.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 86 | +0.023 | +5.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 86 | +0.023 | +5.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 74 | -0.105 | -14.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 74 | -0.105 | -14.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 542 | -0.101 | -35.89€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 249 | -0.149 | -53.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 201 | -0.195 | -56.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 188 | -0.084 | -0.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 144 | -0.096 | -9.02€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 105 | -0.014 | +18.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 83 | -0.029 | +11.72€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 428 | -0.130 | -53.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 674 | -0.209 | -32.15€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 277 | -0.199 | -27.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 240 | -0.194 | -27.18€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 235 | -0.226 | -22.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 203 | -0.237 | -26.74€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 162 | -0.195 | +17.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 146 | -0.196 | +12.84€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 589 | -0.211 | -41.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 279 | +0.415 | +215.62€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 73 | +0.380 | +58.19€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 73 | +0.380 | +58.19€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 177 | +0.483 | +161.66€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 177 | +0.483 | +161.66€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#sniper | 279 | +0.415 | +215.62€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 484 | +0.033 | +13.72€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 484 | +0.033 | +13.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 225 | +0.037 | +6.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 225 | +0.037 | +6.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 31 | +0.076 | +0.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 31 | +0.076 | +0.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 52 | -0.018 | -3.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 52 | -0.018 | -3.62€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 176 | +0.034 | +10.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 176 | +0.034 | +10.02€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2695 | -0.022 | -110.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2695 | -0.022 | -110.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 565 | -0.022 | -22.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 565 | -0.022 | -22.81€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1171 | -0.021 | -45.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1171 | -0.021 | -45.79€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 71 | -0.048 | -6.37€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 71 | -0.048 | -6.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 34 | +0.000 | -2.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 34 | +0.000 | -2.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7554 | +0.022 | +105.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7554 | +0.022 | +105.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2126 | +0.021 | +20.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2126 | +0.021 | +20.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1674 | +0.035 | +50.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1674 | +0.035 | +50.90€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2299 | +0.010 | -0.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2299 | +0.010 | -0.77€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1455 | +0.028 | +34.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1455 | +0.028 | +34.66€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7084 | +0.010 | -55.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7084 | +0.010 | -55.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2838 | +0.013 | -14.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2838 | +0.013 | -14.76€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2773 | +0.011 | -20.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2773 | +0.011 | -20.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1473 | +0.002 | -19.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1473 | +0.002 | -19.96€ | 2 | 0 |
| ✅ UPDOWN_GBM | 34962 | +0.031 | +2073.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9429 | +0.065 | +1670.87€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1291 | +0.004 | +6.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 21993 | +0.021 | +374.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2116 | +0.009 | +22.83€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3482 | +0.068 | +370.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 576 | +0.149 | +225.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 29 | -0.016 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2877 | +0.052 | +146.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6480 | +0.035 | +433.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1197 | +0.081 | +258.28€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 352 | +0.020 | +7.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3929 | +0.032 | +149.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 951 | +0.005 | +17.17€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 51 | -0.104 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4080 | +0.040 | +239.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 539 | +0.141 | +195.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 25 | -0.018 | -1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3516 | +0.024 | +45.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7444 | +0.018 | +282.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2450 | +0.045 | +268.39€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 340 | +0.006 | +7.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3888 | +0.006 | +4.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 723 | +0.006 | -1.41€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 43 | -0.144 | +3.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8407 | +0.016 | +221.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2334 | +0.025 | +160.82€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 334 | -0.006 | -3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5260 | +0.015 | +59.47€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 442 | +0.020 | +7.06€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 37 | -0.167 | -2.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5067 | +0.035 | +528.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2333 | +0.079 | +562.98€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 211 | -0.002 | -2.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2523 | -0.003 | -31.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 131 | -0.139 | +1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 529 | +0.336 | +152.47€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 529 | +0.336 | +152.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 297 | +0.340 | +82.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 297 | +0.340 | +82.27€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 232 | +0.329 | +70.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 232 | +0.329 | +70.21€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11366 | -0.042 | +2319.48€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11366 | -0.042 | +2319.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 689 | -0.043 | +328.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 689 | -0.043 | +328.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2126 | -0.124 | +19.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2126 | -0.124 | +19.38€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 332 | +0.177 | +216.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 332 | +0.177 | +216.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1252 | +0.202 | +720.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1252 | +0.202 | +720.50€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3476 | -0.064 | +527.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3476 | -0.064 | +527.36€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3491 | -0.079 | +506.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3491 | -0.079 | +506.96€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 135 | +0.047 | +10.29€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 135 | +0.047 | +10.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 135 | +0.047 | +10.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 135 | +0.047 | +10.29€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 853 | +0.288 | +682.67€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 853 | +0.288 | +682.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 473 | +0.281 | +351.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 473 | +0.281 | +351.93€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 380 | +0.296 | +330.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 380 | +0.296 | +330.74€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 706 | -0.106 | -78.79€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 706 | -0.106 | -78.79€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 198 | -0.065 | -11.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 198 | -0.065 | -11.77€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 61 | -0.198 | -8.66€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 61 | -0.198 | -8.66€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2280 | +0.300 | +1133.71€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 784 | +0.248 | +107.00€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 845 | +0.287 | +348.98€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 651 | +0.376 | +677.73€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.017 n=464 — no justifica filtro, seguir monitorizando
  - _Datos_: n=464 IC=+0.017 PNL=+21.72€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 523 celda(s) pasan gate riguroso completo de 2189 evaluadas (n>=40) y 3184 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.025 < 0.08 — monitorear
  - _Datos_: n=2331 IC=+0.025 PNL=+160.35€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=845/15 IC=+0.287 PNL=+348.98€ | BTC: n=784/15 IC=+0.248 PNL=+107.00€ | SOL: n=651/15 IC=+0.376 PNL=+677.73€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.098 n=274/60 | contraria IC=+0.149 n=274 | gap=-0.051 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=273, boost estimado=+0.005. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=723/40 IC=+0.006 PNL=-1.41€ | BTC#60min: n=951/40 IC=+0.005 PNL=+17.17€ | SOL#60min: n=442/40 IC=+0.020 PNL=+7.06€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.051 n=320201 | tras_1loss IC=+0.077 n=249262 | tras_2loss IC=+0.046 n=105437/40 | gap=+0.005 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=310 PNL=+195.66€
  - _Datos_: n=310 IC=+0.176 PNL=+195.66€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.08 con n=366 PNL=+267.19€
  - _Datos_: n=366 IC=+0.220 PNL=+267.19€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.275 > 0.08 con n=38 PNL=+33.67€
  - _Datos_: n=38 IC=+0.275 PNL=+33.67€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.328 > 0.1 con n=1884 PNL=+1054.79€
  - _Datos_: n=1884 IC=+0.328 PNL=+1054.79€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=264 PNL=+35.29€
  - _Datos_: n=264 IC=+0.086 PNL=+35.29€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=50 IC=+0.192 PNL=+34.21€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=50 IC=+0.192 PNL=+34.21€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

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
  - _Estado_: n=1512 IC=+0.018 PNL=+18.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1512 IC=+0.018 PNL=+18.13€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=604 IC=-0.017 PNL=+4.69€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=604 IC=-0.017 PNL=+4.69€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=464 IC=+0.017 PNL=+21.72€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=464 IC=+0.017 PNL=+21.72€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.1 con n=2017 PNL=+1264.80€
  - _Datos_: n=2017 IC=+0.186 PNL=+1264.80€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1195 IC=+0.081 PNL=+258.24€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1195 IC=+0.081 PNL=+258.24€

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
  - _Estado_: n=495 IC=+0.007 PNL=+31.14€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=495 IC=+0.007 PNL=+31.14€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=46 IC=+0.062 PNL=+2.91€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=46 IC=+0.062 PNL=+2.91€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.245 n=92) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=92 IC=+0.245 PNL=+68.60€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.02 con n=626 PNL=+248.25€
  - _Datos_: n=626 IC=+0.126 PNL=+248.25€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=12127 IC=+0.057 PNL=+1521.68€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=12127 IC=+0.057 PNL=+1521.68€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.161 < -0.1 con n=219 PNL=+18.75€
  - _Datos_: n=219 IC=-0.161 PNL=+18.75€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1792 IC=+0.045 PNL=+183.26€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1792 IC=+0.045 PNL=+183.26€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=71 IC=-0.130 PNL=+3.08€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=71 IC=-0.130 PNL=+3.08€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.1 con n=382 PNL=+105.54€
  - _Datos_: n=382 IC=+0.128 PNL=+105.54€

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
  - _Estado_: n=16988 IC=-0.136 PNL=+1196.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=16988 IC=-0.136 PNL=+1196.48€

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
  - _Estado_: n=1841 IC=+0.138 PNL=+997.88€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1841 IC=+0.138 PNL=+997.88€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3730 IC=+0.021 PNL=+125.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3730 IC=+0.021 PNL=+125.99€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=2001 PNL=+1052.79€
  - _Datos_: n=2001 IC=+0.087 PNL=+1052.79€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1669 PNL=-187.60€
  - _Datos_: n=1669 IC=-0.238 PNL=-187.60€

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

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 35/40 ops en el filtro definido (IC actual=-0.041 PNL=+2.93€)
  - _Datos_: n=35 IC=-0.041 PNL=+2.93€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.084 n=941) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=941 IC=+0.084 PNL=+205.56€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=430) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=430 IC=+0.412 PNL=+606.70€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8447 IC=+0.176 PNL=-984.58€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8447 IC=+0.176 PNL=-984.58€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
