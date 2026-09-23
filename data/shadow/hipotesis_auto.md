# Hipótesis automáticas — 2026-09-23 08:59 UTC
_Generado por shadow_postmortem.py sobre 570931 resoluciones (PNL=+63959.63€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.254 (n=510)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=462)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.254 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.207 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8038` → IC=+0.252 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8038 (IC base=+0.139)

- **PATRÓN** `banda_z` > `4.204` → IC=+0.168 (n=534)

  - _Acción_: Kelly boost +0.84€ cuando `banda_z` > 4.204 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=570)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4804.7376` → IC=+0.161 (n=178)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4804.7376 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 96.0 (IC base=+0.043)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=404)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=335)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.261 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.208 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.8012` → IC=+0.265 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8012 (IC base=+0.148)

- **PATRÓN** `banda_z` > `10.822` → IC=+0.229 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.822 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=481)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 96.0 (IC base=+0.045)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=101)

- **FILTRO** `banda_hit_calibrado` < `0.6297` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6297
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=107)

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

- **PATRÓN** `py_entrada` > `0.35` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.35 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1195.1095` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1195.1095 (IC base=+0.110)

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
- **FILTRO** `restante_s_al_confirmar` < `146.2` → IC=-0.231 (n=6845)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.2
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=20541)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.44` → IC=-0.236 (n=892)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.44
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2678)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `496.69` → IC=-0.149 (n=357)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 496.69
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1074)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `131.87` → IC=-0.288 (n=847)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.87
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2544)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `163.92` → IC=-0.228 (n=1626)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 163.92
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4879)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `125.17` → IC=-0.357 (n=1368)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.17
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=4104)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.202 (n=13518)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=3394)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5600.4068` → IC=+0.175 (n=2164)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5600.4068 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=10974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=13472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.232 (n=10555)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5521)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7716.0988` → IC=+0.173 (n=2077)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7716.0988 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.352 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2056)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15840.683` → IC=+0.232 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15840.683 (IC base=+0.204)

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

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.108)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.147 (n=800)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.108)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=2330)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.333 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.357 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=1448)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.432 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.203)

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
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.206 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.112)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=107)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=11046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=10590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3718)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2559)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.184 (n=1870)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.253 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.355 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.249)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=2527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2185)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.319 (n=830)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=2562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=2472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=1891)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.195)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.432 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `2069.2076` → IC=+0.439 (n=502)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.453 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.438 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `3364.1944` → IC=+0.445 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3364.1944 (IC base=+0.437)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=32699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.232 (n=17807)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=6672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=5654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6116)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=5867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=5868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=2107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=5958)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6017)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=2947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=5412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=2207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=6469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=5476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5039)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.126 (n=4621)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.15 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=4958)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=6145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.94` → IC=+0.142 (n=4599)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.94 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=2540)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.1` → IC=+0.131 (n=2284)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.1 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2456)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=3033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.43` → IC=+0.145 (n=2283)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.43 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=2499)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=2329)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=2505)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.31` → IC=+0.140 (n=2321)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.286 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.256)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.286 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.256)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4792` → IC=+0.122 (n=7730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.4792 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.982` → IC=+0.243 (n=2578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.982 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.8312` → IC=+0.246 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8312 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.6263` → IC=+0.248 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6263 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.932` → IC=+0.177 (n=2974)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.932 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `1.0481` → IC=+0.259 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0481 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.3051` → IC=+0.218 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3051 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.9086` → IC=+0.207 (n=3517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9086 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.5707` → IC=+0.132 (n=9314)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5707 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.5912` → IC=+0.194 (n=719)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5912 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.1494` → IC=+0.172 (n=2886)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1494 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` < `0.6997` → IC=+0.179 (n=1423)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6997 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `0.8691` → IC=+0.174 (n=2155)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8691 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.168` → IC=+0.222 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.168 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `1.5756` → IC=+0.201 (n=4830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5756 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.211 (n=5189)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.063)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.181 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.172 (n=586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.166 (n=1750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=1176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.105` → IC=+0.271 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.105 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.214 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.164 (n=1635)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.250 (n=1163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.287 (n=434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0603` → IC=+0.296 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0603 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.405` → IC=+0.248 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.405 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.092` → IC=+0.231 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.092 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6317` → IC=+0.247 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6317 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1793.28` → IC=+0.239 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1793.28 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.230 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.234 (n=588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.251 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=1394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.215 (n=1355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9042` → IC=+0.258 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9042 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.222 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.735` → IC=+0.218 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.735 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.851` → IC=+0.250 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.851 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.218 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.8746` → IC=+0.226 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8746 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.228 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.223 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.223 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `12308.655` → IC=+0.219 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12308.655 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.177 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.162 (n=462)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6928` → IC=+0.170 (n=1384)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6928 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1319` → IC=+0.157 (n=1221)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1319 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.202` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.202 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.236` → IC=+0.141 (n=1258)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.236 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.149 (n=1384)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2035 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8505` → IC=+0.139 (n=922)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8505 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.176 (n=372)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.150 (n=1273)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7671` → IC=+0.146 (n=849)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7671 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `13974.5212` → IC=+0.145 (n=922)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 13974.5212 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.147 (n=1194)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 411.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.218 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=1797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.253 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.2114` → IC=+0.188 (n=1704)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2114 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3629` → IC=+0.200 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3629 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.8557` → IC=+0.207 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8557 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.195 (n=1207)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.224 (n=1456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.5843` → IC=+0.216 (n=1456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5843 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.242 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.591` → IC=+0.242 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.591 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3589` → IC=+0.272 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3589 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.221` → IC=+0.222 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.221 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1871.1464` → IC=+0.233 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1871.1464 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.216 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=96)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2141)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.211 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.3632` → IC=+0.326 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3632 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.7698` → IC=+0.328 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7698 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.666` → IC=+0.154 (n=686)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.666 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.6017` → IC=+0.330 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6017 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1961 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1818` → IC=+0.317 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1818 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.3097` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3097 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4057` → IC=+0.335 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4057 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.326 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.331 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.3305` → IC=+0.186 (n=259)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3305 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.160 (n=530)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8509 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.214 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` > `1.5204` → IC=+0.176 (n=662)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5204 (IC base=+0.014)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.161 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=313)

- **FILTRO** `ibs_20min` < `0.2692` → IC=-0.202 (n=92)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=278)

- **FILTRO** `ibs_20min` > `0.2581` → IC=-0.125 (n=2112)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2581
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=1043)

- **FILTRO** `sigma_ewma_delta_pct` > `8.651` → IC=-0.204 (n=339)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.651
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2816)

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

- **PATRÓN** `ibs_20min` < `0.2581` → IC=+0.125 (n=1043)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2581 (IC base=-0.043)

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
- **FILTRO** `drift_60min` |x|> `0.6492` → IC=-0.184 (n=540)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6492
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1623)

- **FILTRO** `ibs_20min` < `0.705` → IC=-0.159 (n=1425)

  - _Acción_: SKIP cuando `ibs_20min` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=738)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.200 (n=401)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1762)

- **FILTRO** `ibs_20min` > `0.7733` → IC=-0.204 (n=800)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7733
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2402)

- **PATRÓN** `dist_vwap_pct` > `0.7564` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7564 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2654` → IC=+0.322 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2654 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9865` → IC=+0.292 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9865 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.307 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.0956` → IC=+0.294 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0956 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.308 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4256` → IC=+0.299 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4256 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.7951` → IC=+0.296 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7951 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8119` → IC=+0.273 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8119 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7389` → IC=+0.249 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7389 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.0828` → IC=+0.283 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0828 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1689` → IC=+0.277 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1689 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.1732` → IC=+0.250 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1732 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4431` → IC=+0.249 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4431 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4731` → IC=+0.188 (n=8641)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4731 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.7452` → IC=+0.287 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7452 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.569` → IC=+0.156 (n=4572)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.569 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6887` → IC=+0.247 (n=3064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6887 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2972` → IC=+0.265 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2972 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.241 (n=1857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6833` → IC=+0.237 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6833 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.268 (n=5089)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.149 (n=3224)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.009 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.5488` → IC=+0.151 (n=8508)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5488 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.2434` → IC=+0.238 (n=2639)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2434 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.237 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.247 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2461` → IC=+0.303 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2461 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` < `1.6115` → IC=+0.255 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6115 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `2.3302` → IC=+0.257 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3302 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.262 (n=3566)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.072)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.5` → IC=-0.165 (n=509)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.5
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1716)

- **PATRÓN** `ibs_20min` > `0.8893` → IC=+0.267 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8893 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.746` → IC=+0.202 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.746 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.274 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.177 (n=280)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.189 (n=380)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.176 (n=372)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 15.0 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.3867` → IC=+0.443 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3867 (IC base=-0.019)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=-0.019)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8632` → IC=+0.157 (n=646)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8632 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.173 (n=503)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6718` → IC=+0.163 (n=792)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6718 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.214 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.198 (n=289)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `247.0` → IC=+0.193 (n=376)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 247.0 (IC base=+0.025)

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
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.285 (n=695)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.725` → IC=+0.280 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.725 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1382` → IC=+0.257 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1382 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `3.4412` → IC=+0.260 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4412 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.256 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1944.9586` → IC=+0.256 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1944.9586 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.306 (n=808)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.597` → IC=+0.284 (n=1210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.597 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.329 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.2252` → IC=+0.287 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2252 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.812` → IC=+0.300 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.812 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3435` → IC=+0.306 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3435 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.6079` → IC=+0.283 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6079 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.7825` → IC=+0.285 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7825 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.291 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1863.9984` → IC=+0.298 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1863.9984 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.286 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2821` → IC=-0.191 (n=470)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1411)

- **FILTRO** `ibs_20min` > `0.7758` → IC=-0.185 (n=572)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7758
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1721)

- **PATRÓN** `ibs_20min` > `0.8153` → IC=+0.160 (n=640)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8153 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.4511` → IC=+0.225 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4511 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `0.9969` → IC=+0.237 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9969 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.5846` → IC=+0.209 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5846 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.0773` → IC=+0.254 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0773 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `2.1113` → IC=+0.246 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1113 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.260 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.636` → IC=+0.193 (n=448)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.636 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1607` → IC=+0.206 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1607 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.269 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8289` → IC=+0.252 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8289 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1743` → IC=+0.248 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1743 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.248 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7188` → IC=-0.201 (n=1024)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7188
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=1027)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.231 (n=537)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1615)

- **FILTRO** `sigma_ewma_delta_pct` > `4.678` → IC=-0.179 (n=468)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.678
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=1684)

- **PATRÓN** `ibs_20min` > `0.7188` → IC=+0.278 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7188 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8423` → IC=+0.337 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8423 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.155 (n=326)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.300 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.289 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.292 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.294 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.321 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.312 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.211 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.2117` → IC=+0.222 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2117 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.250 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.207 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.202 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.5036` → IC=+0.219 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5036 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.237 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.320 (n=841)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.301 (n=595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.6316` → IC=+0.314 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6316 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2012` → IC=+0.319 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2012 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.504` → IC=+0.307 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.504 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8627` → IC=+0.305 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8627 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.323 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.292 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2618.726` → IC=+0.296 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2618.726 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.296 (n=909)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.279 (n=477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3976` → IC=+0.304 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3976 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.2901` → IC=+0.279 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2901 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.9381` → IC=+0.271 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9381 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.006` → IC=+0.297 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.006 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.2419` → IC=+0.312 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2419 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.338 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `1.4342` → IC=+0.268 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4342 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1632` → IC=+0.276 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1632 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2607.8903` → IC=+0.277 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2607.8903 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.171 (n=2532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.203 (n=2530)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.09` → IC=+0.185 (n=2529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.09 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=7892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.5789` → IC=+0.217 (n=7584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5789 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1749` → IC=+0.196 (n=3365)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1749 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.275` → IC=+0.259 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.275 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2161` → IC=+0.161 (n=5016)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2161 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.161 (n=5016)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6285 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.197 (n=1132)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5628` → IC=+0.172 (n=3197)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5628 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6278` → IC=+0.176 (n=2422)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6278 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2399.8931` → IC=+0.169 (n=5055)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2399.8931 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.182 (n=6493)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 116.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.182 (n=4796)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.08` → IC=+0.209 (n=2398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.08 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=2786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.226 (n=7190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.2282` → IC=+0.159 (n=5186)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2282 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.258` → IC=+0.193 (n=1224)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.258 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.151 (n=5224)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1748 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.222 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.567` → IC=+0.164 (n=2867)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.567 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.2601` → IC=+0.171 (n=2953)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.2601 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.173 (n=6151)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 118.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.223 (n=434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.187 (n=589)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3421` → IC=+0.205 (n=1297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3421 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.107` → IC=+0.313 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.107 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.237 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.181 (n=1197)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.239 (n=819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.252 (n=830)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.294 (n=619)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.262 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.137` → IC=+0.253 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.137 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.1574` → IC=+0.235 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1574 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.252 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.507` → IC=+0.259 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.507 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1961.4408` → IC=+0.260 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.4408 (IC base=+0.238)

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

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.156 (n=1232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0057 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.204 (n=413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.175 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5646` → IC=+0.184 (n=1231)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5646 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.161 (n=1209)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.77` → IC=+0.205 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.77 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2113` → IC=+0.154 (n=1231)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2113 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.156 (n=376)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4266` → IC=+0.143 (n=1119)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4266 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7504` → IC=+0.134 (n=746)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.7504 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.170 (n=349)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 216.0 (IC base=+0.135)

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

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.236 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0946` → IC=+0.259 (n=346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0946 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.281 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.2405` → IC=+0.256 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2405 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.729` → IC=+0.271 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.729 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.221` → IC=+0.229 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.221 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1874.7032` → IC=+0.229 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.7032 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.221 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.208 (n=405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4314` → IC=+0.159 (n=1210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4314 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3812` → IC=+0.196 (n=1209)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3812 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1604` → IC=+0.180 (n=818)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1604 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.868` → IC=+0.229 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.868 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0445` → IC=+0.146 (n=1064)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0445 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.150 (n=1209)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6307 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2462` → IC=+0.199 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2462 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5368` → IC=+0.150 (n=521)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5368 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5292` → IC=+0.172 (n=395)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5292 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `6941.7258` → IC=+0.186 (n=806)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6941.7258 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.144 (n=1151)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 166.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=1269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.383` → IC=+0.143 (n=1269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.383 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6263` → IC=+0.169 (n=1269)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6263 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.5687` → IC=+0.134 (n=1458)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.5687 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.869` → IC=+0.173 (n=447)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.869 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.849` → IC=+0.146 (n=846)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.849 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.201 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7891` → IC=+0.131 (n=767)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7891 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4865` → IC=+0.135 (n=384)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4865 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9950.2818` → IC=+0.160 (n=575)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9950.2818 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.121 (n=1081)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 165.0 (IC base=+0.123)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1031` → IC=+0.152 (n=461)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1031 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=1393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.208 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.7314` → IC=+0.136 (n=278)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7314 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.1956` → IC=+0.137 (n=1257)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1956 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.438` → IC=+0.145 (n=285)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 7.438 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.1863` → IC=+0.121 (n=1381)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.1863 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.4294` → IC=+0.130 (n=411)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4294 (IC base=+0.112)

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

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.247 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1423` → IC=+0.231 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1423 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.8635` → IC=+0.204 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8635 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.243 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6303` → IC=+0.217 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6303 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.289 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2231` → IC=+0.193 (n=1060)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2231 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4431` → IC=+0.200 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4431 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2575.6814` → IC=+0.210 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2575.6814 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.164 (n=593)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0038 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.178 (n=595)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0089 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.155 (n=592)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.5522` → IC=+0.188 (n=1586)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5522 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.3876` → IC=+0.181 (n=553)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3876 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.707` → IC=+0.177 (n=819)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.707 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.164 (n=1034)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8753 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `1.2111` → IC=+0.155 (n=517)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2111 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.177 (n=494)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.168 (n=570)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5495` → IC=+0.157 (n=570)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5495 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=2008)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `12252.2426` → IC=+0.151 (n=592)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12252.2426 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.166 (n=1553)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 164.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.131 (n=1239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0057 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.5219` → IC=+0.141 (n=1634)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5219 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `1.4583` → IC=+0.132 (n=596)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4583 (IC base=+0.102)

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
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.263 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.203 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0977` → IC=+0.216 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0977 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.7033` → IC=+0.249 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7033 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.3883` → IC=+0.208 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3883 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.052` → IC=+0.228 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.052 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.8419` → IC=+0.205 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8419 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.214 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2572` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2572 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.3892` → IC=+0.239 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3892 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.405` → IC=+0.228 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.405 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `12317.9636` → IC=+0.203 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12317.9636 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.0811` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.0811 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.080)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4167` → IC=-0.125 (n=166)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4167
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=326)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=456)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.187 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0089 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.1107` → IC=+0.129 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1107 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.163 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.239 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.6239` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6239 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.127` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.127 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.0712` → IC=+0.145 (n=342)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0712 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.7306` → IC=+0.151 (n=348)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7306 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4844` → IC=+0.143 (n=124)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4844 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.2214` → IC=+0.165 (n=168)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.2214 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=424)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3060.3888` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3060.3888 (IC base=+0.129)

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
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.207 (n=3221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=10066)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4708` → IC=+0.216 (n=9660)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4708 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.948` → IC=+0.207 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.948 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.81` → IC=+0.236 (n=3565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.81 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8818` → IC=+0.165 (n=4306)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8818 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2398` → IC=+0.202 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2398 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6065` → IC=+0.189 (n=3091)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6065 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2342.0046` → IC=+0.172 (n=6440)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2342.0046 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.196 (n=7293)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 87.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.187 (n=7697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0092 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1464` → IC=+0.189 (n=3847)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1464 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.237 (n=8745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5667 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2435` → IC=+0.160 (n=5369)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2435 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.949` → IC=+0.200 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.949 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.72` → IC=+0.182 (n=8470)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.72 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.159 (n=2654)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7054 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.2031` → IC=+0.153 (n=2010)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2031 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.241 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.193 (n=2664)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.191 (n=5087)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 48.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.209 (n=548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.219 (n=550)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3514` → IC=+0.190 (n=1642)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3514 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.977` → IC=+0.312 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.977 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.251 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.5813` → IC=+0.205 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5813 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=968)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.259 (n=1270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.263 (n=1134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1282` → IC=+0.290 (n=559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1282 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3505` → IC=+0.290 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3505 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.537` → IC=+0.265 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.537 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.289 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `1.86` → IC=+0.274 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.86 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1961.8977` → IC=+0.274 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.8977 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0842` → IC=+0.162 (n=516)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0842 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3136` → IC=+0.201 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3136 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1309` → IC=+0.186 (n=894)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1309 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.173 (n=353)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.227` → IC=+0.151 (n=1389)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.227 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.178 (n=516)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.629 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2686` → IC=+0.201 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2686 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1158` → IC=+0.161 (n=1312)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1158 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.156 (n=994)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `15634.6383` → IC=+0.153 (n=701)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 15634.6383 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `476.0` → IC=+0.157 (n=1421)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 476.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3183` → IC=+0.160 (n=1336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3183 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.175 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.6545` → IC=+0.192 (n=1336)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6545 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.166 (n=1193)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.398` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.398 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.186` → IC=+0.161 (n=1336)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.186 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.196 (n=363)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.159 (n=1237)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.0873` → IC=+0.164 (n=561)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.0873 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.156 (n=1004)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 423.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.247 (n=520)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6717` → IC=+0.256 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6717 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.809` → IC=+0.295 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.809 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2117` → IC=+0.220 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2117 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8451` → IC=+0.245 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8451 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1952.96` → IC=+0.218 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.96 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.232 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.240 (n=1444)
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

- **PATRÓN** `ibs_20min` < `0.3617` → IC=+0.268 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3617 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.741` → IC=+0.281 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.741 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.295 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7653` → IC=+0.234 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7653 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1985` → IC=+0.238 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1985 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1872.8576` → IC=+0.253 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1872.8576 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.232 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.235)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.184 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.436` → IC=+0.144 (n=1645)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.436 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=1718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.261 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.877 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5705` → IC=+0.174 (n=482)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.5705 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.148` → IC=+0.159 (n=684)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.148 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8769` → IC=+0.157 (n=1097)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8769 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.219 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5207` → IC=+0.150 (n=700)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5207 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7664` → IC=+0.147 (n=1060)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7664 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8150.9116` → IC=+0.230 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8150.9116 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.156 (n=513)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 80.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.154 (n=1344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4451` → IC=+0.153 (n=1343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4451 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6975` → IC=+0.183 (n=1343)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6975 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.7869` → IC=+0.142 (n=1552)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.7869 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.175 (n=198)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.145 (n=896)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8616 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.142 (n=448)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1852 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.245 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.151 (n=1272)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10929.1174` → IC=+0.204 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10929.1174 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.143 (n=1264)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 179.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.136 (n=1090)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0081 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.190 (n=1632)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4717 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0684` → IC=+0.204 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0684 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.453` → IC=+0.234 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.453 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8911` → IC=+0.134 (n=1089)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8911 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1648)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2913.9614` → IC=+0.249 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2913.9614 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.129 (n=1252)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 54.0 (IC base=+0.111)

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
- **PATRÓN** `sigma_h` > `0.0193` → IC=+0.220 (n=1091)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0193 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1462)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.5146` → IC=+0.251 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5146 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.234 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.156` → IC=+0.271 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.156 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.0716` → IC=+0.211 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0716 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.6367` → IC=+0.218 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6367 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2342` → IC=+0.251 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2342 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.5104` → IC=+0.237 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5104 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2616.3022` → IC=+0.225 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2616.3022 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.224 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.218 (n=584)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.208 (n=1230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.255 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5207 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.204 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.8771` → IC=+0.203 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8771 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.738` → IC=+0.263 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.738 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.237 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.263 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2066` → IC=+0.193 (n=1379)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2066 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4346` → IC=+0.197 (n=1566)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4346 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=2927)

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

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.156 (n=2208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.166 (n=972)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1827 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6828` → IC=+0.153 (n=433)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6828 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.429` → IC=+0.131 (n=2172)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.429 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.22` → IC=+0.146 (n=2199)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.22 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2459` → IC=+0.143 (n=2105)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2459 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.146 (n=1024)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.144 (n=959)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8143` → IC=+0.144 (n=1453)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8143 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=2927)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6949.6369` → IC=+0.150 (n=1972)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6949.6369 (IC base=+0.137)

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

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.212 (n=408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1125` → IC=+0.172 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1125 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.175 (n=407)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1382 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.141 (n=419)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6084 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.6984` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6984 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2186` → IC=+0.137 (n=946)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2186 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.106` → IC=+0.151 (n=1011)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.106 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.183 (n=617)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8817 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.173 (n=200)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4237` → IC=+0.142 (n=308)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4237 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.148 (n=614)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `11389.4654` → IC=+0.148 (n=924)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11389.4654 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `706.0` → IC=+0.144 (n=879)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 706.0 (IC base=+0.136)

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

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.156 (n=722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0084 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3917` → IC=+0.172 (n=633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3917 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.148 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.7363` → IC=+0.143 (n=720)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.7363 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.154 (n=720)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.1001 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1663` → IC=+0.158 (n=360)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1663 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.3831` → IC=+0.144 (n=720)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3831 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.716` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.716 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.281` → IC=+0.143 (n=654)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.281 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.0958` → IC=+0.153 (n=633)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0958 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.7262` → IC=+0.145 (n=643)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7262 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.171 (n=305)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.152 (n=622)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7774` → IC=+0.158 (n=471)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7774 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7593.5796` → IC=+0.166 (n=720)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7593.5796 (IC base=+0.141)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.0677` → IC=+0.139 (n=200)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.0677 (IC base=+0.107)

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
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **FILTRO** `volumen_regimen` > `0.8808` → IC=-0.235 (n=32)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=33)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=665)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2902.7974` → IC=+0.173 (n=224)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2902.7974 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=665)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2902.7974` → IC=+0.173 (n=224)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2902.7974 (IC base=+0.105)

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
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=206)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=192)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1704)

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
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=145)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=86)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=617)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=617)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=489)

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
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

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

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.246 (n=57)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=137)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.160 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=146)

- **PATRÓN** `py_entrada` < `0.56` → IC=+0.122 (n=154)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.56 (IC base=+0.032)

- **PATRÓN** `profundidad_ratio` > `107.3` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `profundidad_ratio` > 107.3 (IC base=+0.032)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.56 (IC base=+0.147)

- **PATRÓN** `restante_min` > `3.97` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 3.97 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.147)

- **PATRÓN** `lag_apertura_s` < `60.77` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 60.77 (IC base=+0.147)

- **PATRÓN** `profundidad_ratio` > `256.5` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio` > 256.5 (IC base=+0.147)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `restante_min` < `3.77` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `restante_min` < 3.77
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `lag_apertura_s` > `80.05` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `lag_apertura_s` > 80.05
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7391)

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
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=10329)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.170 (n=3476)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=10511)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.211 (n=569)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1769)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.154 (n=623)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=1882)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.203 (n=583)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1805)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=612)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1884)

- **FILTRO** `ibs_20min` > `0.2819` → IC=-0.164 (n=623)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2819
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1873)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.174 (n=556)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1769)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.184 (n=616)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1882)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2707)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2875)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2881)

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
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=657)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=9688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=21423)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=7564)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=23547)

- **FILTRO** `ibs_7min` < `0.2879` → IC=-0.234 (n=7777)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2879
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=23334)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=10547)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=20564)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9606)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=29283)

- **FILTRO** `ibs_7min` > `0.2941` → IC=-0.180 (n=9697)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=29192)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.305 (n=1222)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3909)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.249 (n=1690)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3441)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.183 (n=1186)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3945)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.259 (n=1657)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=5036)

- **FILTRO** `drift_7min_pct` |x|> `0.1117` → IC=-0.124 (n=2269)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1117
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4424)

- **FILTRO** `ibs_7min` > `0.7937` → IC=-0.206 (n=1673)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7937
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=5020)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4113)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1290)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4088)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.191 (n=1344)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4034)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.170 (n=1338)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4040)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.254 (n=1350)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4094)

- **FILTRO** `ibs_7min` > `0.2607` → IC=-0.177 (n=1360)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2607
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4084)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.186 (n=1360)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4084)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.166 (n=1394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=3464)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.304 (n=1190)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=3668)

- **FILTRO** `ibs_7min` < `0.1935` → IC=-0.257 (n=1209)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3649)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.215 (n=1139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3719)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.239 (n=1648)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=5491)

- **FILTRO** `ibs_7min` > `0.7534` → IC=-0.179 (n=1784)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7534
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=5355)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1516)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3618)

- **FILTRO** `ibs_7min` < `0.7422` → IC=-0.179 (n=1283)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7422
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3851)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.168 (n=1256)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3878)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=1157)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4060)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.174 (n=1304)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3913)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.190 (n=1285)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3932)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.262 (n=1304)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=4137)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.240 (n=1348)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4093)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1779)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5615)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1223)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3946)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.227 (n=1292)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3877)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1244)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3925)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.203 (n=1701)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=5301)

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
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=526)

- **FILTRO** `libro_liquidez` < `10661.2861` → IC=-0.141 (n=143)

  - _Acción_: SKIP cuando `libro_liquidez` < 10661.2861
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=429)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=878)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=548)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.148 (n=481)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.153 (n=240)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 459.6089 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.144 (n=57)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.142 (n=149)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 445.688 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 13.0 (IC base=+0.134)

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
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=163)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=284)

- **PATRÓN** `streak_estiramiento` < `0.4117` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.4117 (IC base=+0.033)

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
- **FILTRO** `streak_estiramiento` > `0.4152` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4152
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=24)

- **FILTRO** `ballena_activa_n` > `52.0` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 52.0
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=33)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=571)

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

- **PATRÓN** `drift_60min` |x|≤ `0.0514` → IC=+0.205 (n=506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0514 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2136` → IC=+0.192 (n=505)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2136 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1263` → IC=+0.232 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1263 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=1411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.186 (n=1528)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 16.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6077` → IC=+0.263 (n=1515)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6077 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.2989` → IC=+0.191 (n=545)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2989 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.921` → IC=+0.275 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.921 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2979.0729` → IC=+0.194 (n=1010)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2979.0729 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.206 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=553)

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
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=346)

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
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=84)

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
- **FILTRO** `dist_vwap_pct` > `0.6927` → IC=-0.150 (n=101)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6927
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=849)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.662` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 15.662 (IC base=+0.009)

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
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1905)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.187 (n=848)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1691)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.254 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.060)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.268 (n=614)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `0.5693` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5693 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.2752` → IC=+0.178 (n=480)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2752 (IC base=-0.060)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1178` → IC=+0.239 (n=1083)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1178 (IC base=-0.037)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1772` → IC=+0.234 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1772 (IC base=-0.037)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.274 (n=1628)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.6604` → IC=+0.280 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6604 (IC base=-0.037)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.217 (n=387)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1164)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.228 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1164)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.207 (n=978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=573)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.250 (n=278)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1273)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.225)

- **PATRÓN** `drift_15min` |x|≤ `0.7826` → IC=+0.231 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7826 (IC base=+0.225)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2005` → IC=+0.253 (n=294)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2005 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.225)

- **PATRÓN** `ibs_15` < `0.2693` → IC=+0.278 (n=570)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2693 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.7312` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7312 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.823` → IC=+0.252 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.823 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.189` → IC=+0.230 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.189 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3551.8492` → IC=+0.225 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.8492 (IC base=+0.225)

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
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.259 (n=376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=377)

- **FILTRO** `drift_15min` |x|> `1.2315` → IC=-0.258 (n=188)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2315
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=565)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=185)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=568)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1536` → IC=+0.277 (n=146)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1536 (IC base=-0.047)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1028` → IC=+0.349 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1028 (IC base=-0.047)

- **PATRÓN** `ibs_15` < `0.3457` → IC=+0.305 (n=439)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3457 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `0.8637` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8637 (IC base=-0.047)

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
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.054)

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
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.054)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6077 sube el IC de +0.186 a +0.263 en UPDOWN_GBM#15min (n=1515). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.199 a +0.265 en UPDOWN_GBM#BTC#15min (n=351). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.665 sube el IC de +0.138 a +0.240 en UPDOWN_GBM#ETH#15min (n=317). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6122 sube el IC de +0.175 a +0.257 en UPDOWN_GBM#SOL#15min (n=183). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.188 a +0.284 en UPDOWN_GBM#XRP#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.046 a +0.159 en UPDOWN_GBM#XRP#15min (n=452). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.060 a +0.268 en UPDOWN_GBM_15M_TARDIO (n=614). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.037 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=1628). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7466 sube el IC de +0.076 a +0.320 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=165). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.148 a +0.263 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=293). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2693 sube el IC de +0.225 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=570). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.162 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.044 a +0.258 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=295). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3457 sube el IC de -0.047 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=439). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.288 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=640). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.281 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=355). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.296 a +0.336 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=285). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.336 a +0.380 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=397). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.340 a +0.376 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=223). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7403 sube el IC de +0.329 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=174). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1286 | +0.096 | +182.18€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1286 | +0.096 | +182.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 953 | +0.106 | +157.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 953 | +0.106 | +157.12€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 247 | +0.050 | +6.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 247 | +0.050 | +6.40€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 24369 | -0.090 | -3069.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1431 | -0.047 | -221.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 22938 | -0.093 | -2848.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3570 | -0.084 | -577.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3570 | -0.084 | -577.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1431 | -0.047 | -221.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1431 | -0.047 | -221.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7017 | -0.022 | -616.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7017 | -0.022 | -616.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6505 | -0.096 | -426.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6505 | -0.096 | -426.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5472 | -0.183 | -1066.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5472 | -0.183 | -1066.52€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 17124 | -0.029 | +4083.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4484 | -0.000 | +1826.03€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 12640 | -0.040 | +2257.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 17124 | -0.029 | +4083.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4484 | -0.000 | +1826.03€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 12640 | -0.040 | +2257.93€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 89544 | +0.113 | -4555.86€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13629 | +0.184 | -436.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 359 | -0.093 | -50.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 69686 | +0.100 | -3856.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5870 | +0.108 | -212.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11594 | +0.098 | -990.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11535 | +0.100 | -975.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 18112 | +0.132 | -367.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4273 | +0.202 | -144.92€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11550 | +0.112 | -173.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2247 | +0.106 | -26.60€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11634 | +0.089 | -1083.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11568 | +0.091 | -1066.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 19074 | +0.123 | -406.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5268 | +0.175 | -80.13€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11671 | +0.104 | -264.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2123 | +0.098 | -53.18€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17520 | +0.114 | -1026.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3948 | +0.188 | -209.55€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 262 | -0.053 | +3.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11810 | +0.092 | -686.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1500 | +0.126 | -132.63€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11610 | +0.101 | -682.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 45 | -0.032 | +7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11552 | +0.102 | -689.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14211 | +0.192 | -918.99€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14211 | +0.192 | -918.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3399 | +0.168 | -358.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3399 | +0.168 | -358.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1122 | +0.196 | -6.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1122 | +0.196 | -6.21€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3342 | +0.181 | -281.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3342 | +0.181 | -281.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2988 | +0.238 | -97.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2988 | +0.238 | -97.60€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3281 | +0.195 | -189.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3281 | +0.195 | -189.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 669 | +0.430 | -18.52€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 669 | +0.430 | -18.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 256 | +0.434 | -4.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 256 | +0.434 | -4.38€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 252 | +0.437 | -2.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 252 | +0.437 | -2.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 153 | +0.403 | -10.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 153 | +0.403 | -10.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 48835 | +0.198 | -3814.50€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 48835 | +0.198 | -3814.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8464 | +0.176 | -990.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8464 | +0.176 | -990.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7793 | +0.224 | -281.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7793 | +0.224 | -281.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8429 | +0.174 | -1001.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8429 | +0.174 | -1001.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7888 | +0.219 | -303.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7888 | +0.219 | -303.30€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8063 | +0.203 | -530.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8063 | +0.203 | -530.45€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8198 | +0.194 | -708.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8198 | +0.194 | -708.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 18392 | +0.117 | +129.13€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 18392 | +0.117 | +129.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9128 | +0.122 | +128.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9128 | +0.122 | +128.45€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9264 | +0.113 | +0.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9264 | +0.113 | +0.68€ | 0 | 4 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1068 | +0.079 | -35.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 371 | +0.068 | -24.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 697 | +0.084 | -11.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 841 | +0.085 | -12.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 144 | +0.089 | -1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 697 | +0.084 | -11.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 166 | +0.030 | -26.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 166 | +0.030 | -26.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 33832 | +0.097 | -1068.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2803 | +0.089 | +16.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 31029 | +0.098 | -1085.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 19044 | +0.101 | -319.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2803 | +0.089 | +16.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 16241 | +0.104 | -335.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6293 | +0.106 | -54.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6293 | +0.106 | -54.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8495 | +0.081 | -695.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8495 | +0.081 | -695.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 785 | +0.213 | -98.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 785 | +0.213 | -98.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 785 | +0.213 | -98.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 785 | +0.213 | -98.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 24418 | +0.081 | +11493.76€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 24418 | +0.081 | +11493.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4067 | +0.193 | +2949.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4067 | +0.193 | +2949.26€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 3618 | +0.176 | +2501.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3618 | +0.176 | +2501.95€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 4219 | +0.200 | +3171.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4219 | +0.200 | +3171.94€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 3624 | +0.017 | +727.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3624 | +0.017 | +727.67€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3525 | -0.033 | +807.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3525 | -0.033 | +807.47€ | 4 | 16 |
| ✅ GBM_LATE_15M#XRP | 5365 | -0.043 | +1335.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5365 | -0.043 | +1335.47€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 25786 | +0.085 | +13445.23€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 25786 | +0.085 | +13445.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4888 | +0.016 | +2613.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4888 | +0.016 | +2613.41€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5371 | +0.013 | +1090.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5371 | +0.013 | +1090.99€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3653 | +0.262 | +3677.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3653 | +0.262 | +3677.95€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4174 | +0.000 | +767.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4174 | +0.000 | +767.88€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4203 | +0.026 | +1571.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4203 | +0.026 | +1571.93€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3497 | +0.275 | +3723.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3497 | +0.275 | +3723.08€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 19695 | +0.168 | +14648.08€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 19695 | +0.168 | +14648.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2965 | +0.206 | +2344.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2965 | +0.206 | +2344.49€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3142 | +0.147 | +2262.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3142 | +0.147 | +2262.09€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3078 | +0.209 | +2458.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3078 | +0.209 | +2458.40€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3303 | +0.134 | +2290.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3303 | +0.134 | +2290.42€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3664 | +0.115 | +2486.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3664 | +0.115 | +2486.99€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3543 | +0.204 | +2805.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3543 | +0.204 | +2805.69€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4842 | +0.124 | +1973.35€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4842 | +0.124 | +1973.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1382 | +0.119 | +604.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1382 | +0.119 | +604.39€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1390 | +0.140 | +595.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1390 | +0.140 | +595.97€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1010 | +0.097 | +301.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1010 | +0.097 | +301.37€ | 2 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 24532 | +0.174 | +18146.37€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 24532 | +0.174 | +18146.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3880 | +0.220 | +3255.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3880 | +0.220 | +3255.30€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3840 | +0.149 | +2518.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3840 | +0.149 | +2518.61€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4005 | +0.226 | +3461.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4005 | +0.226 | +3461.96€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3983 | +0.136 | +2682.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3983 | +0.136 | +2682.42€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4310 | +0.111 | +2680.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4310 | +0.111 | +2680.87€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4514 | +0.205 | +3547.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4514 | +0.205 | +3547.21€ | 0 | 24 |
| ✅ GBM_LATE_5M | 6680 | +0.144 | +3724.74€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6680 | +0.144 | +3724.74€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1729 | +0.140 | +1095.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1729 | +0.140 | +1095.30€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2103 | +0.147 | +1153.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2103 | +0.147 | +1153.60€ | 0 | 33 |
| ✅ GBM_LATE_5M#SOL | 546 | +0.099 | +178.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 546 | +0.099 | +178.45€ | 0 | 14 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1620 | +0.070 | +706.31€ | 2 | 12 |
| ✅ GBM_LATE_60M#60min | 1620 | +0.070 | +706.31€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 583 | +0.088 | +247.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 583 | +0.088 | +247.13€ | 0 | 15 |
| ✅ GBM_LATE_60M#ETH | 540 | +0.074 | +269.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 540 | +0.074 | +269.93€ | 2 | 18 |
| ✅ GBM_LATE_60M#SOL | 497 | +0.043 | +189.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 497 | +0.043 | +189.25€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 360 | -0.262 | -28.78€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 360 | -0.262 | -28.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 137 | -0.227 | -11.84€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 137 | -0.227 | -11.84€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 119 | -0.269 | -10.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 119 | -0.269 | -10.66€ | 4 | 0 |
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
| ✅ LEADLAG_BTC_XRP_15M | 1837 | +0.095 | +486.11€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1837 | +0.095 | +486.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1837 | +0.095 | +486.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1837 | +0.095 | +486.11€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 374 | -0.082 | -35.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 374 | -0.082 | -35.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 132 | -0.030 | -5.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 132 | -0.030 | -5.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1902 | +0.005 | +15.01€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1902 | +0.005 | +15.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 101 | +0.015 | -1.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 101 | +0.015 | -1.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 206 | -0.005 | +12.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 206 | -0.005 | +12.83€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 154 | -0.038 | -7.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 154 | -0.038 | -7.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 800 | +0.029 | +24.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 800 | +0.029 | +24.42€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 467 | -0.001 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 467 | -0.001 | -5.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 174 | -0.040 | -7.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 174 | -0.040 | -7.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 1046 | -0.050 | -32.95€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1046 | -0.050 | -32.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 301 | -0.045 | -13.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 301 | -0.045 | -13.58€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 347 | -0.042 | -6.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 347 | -0.042 | -6.83€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 398 | -0.060 | -12.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 398 | -0.060 | -12.55€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 493 | -0.003 | +23.85€ | 2 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 236 | +0.004 | +15.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 257 | -0.010 | +8.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 14 | -0.044 | -1.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 8 | +0.040 | +2.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 6 | -0.075 | -3.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 131 | +0.102 | +37.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 61 | +0.087 | +14.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 70 | +0.111 | +22.69€ | 0 | 6 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 82 | -0.048 | -4.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 41 | -0.035 | -1.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 41 | -0.058 | -2.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 78 | -0.050 | -5.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 37 | -0.038 | -1.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 41 | -0.058 | -4.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 76 | +0.038 | +8.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 41 | +0.012 | +3.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 35 | +0.068 | +4.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 112 | -0.079 | -10.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 48 | -0.060 | -2.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 64 | -0.091 | -7.91€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14255 | -0.012 | -207.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14255 | -0.012 | -207.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2972 | -0.021 | -60.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2972 | -0.021 | -60.78€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 27526 | -0.008 | +1199.55€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 27526 | -0.008 | +1199.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4843 | +0.016 | +594.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4843 | +0.016 | +594.63€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4294 | -0.028 | -53.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4294 | -0.028 | -53.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4884 | +0.013 | +429.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4884 | +0.013 | +429.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4074 | -0.052 | -144.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4074 | -0.052 | -144.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4608 | -0.012 | +178.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4608 | -0.012 | +178.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4823 | +0.006 | +195.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4823 | +0.006 | +195.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5683 | -0.056 | -129.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5683 | -0.056 | -129.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1349 | -0.074 | -28.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1349 | -0.074 | -28.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 597 | -0.119 | -21.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 597 | -0.119 | -21.93€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1644 | -0.076 | -32.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1644 | -0.076 | -32.01€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 70000 | -0.073 | +1720.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 70000 | -0.073 | +1720.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11824 | -0.079 | +692.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11824 | -0.079 | +692.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10822 | -0.093 | -477.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10822 | -0.093 | -477.17€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11997 | -0.067 | +669.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11997 | -0.067 | +669.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10351 | -0.092 | -133.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10351 | -0.092 | -133.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12835 | -0.048 | +384.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12835 | -0.048 | +384.39€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12171 | -0.062 | +583.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12171 | -0.062 | +583.22€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7260 | -0.023 | -106.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7260 | -0.023 | -106.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1641 | -0.025 | -1.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1641 | -0.025 | -1.73€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1854 | -0.016 | -13.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1854 | -0.016 | -13.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1028 | -0.040 | -17.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1028 | -0.040 | -17.02€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1095 | +0.109 | +373.14€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 959 | +0.116 | +360.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 225 | +0.134 | +109.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 225 | +0.134 | +109.92€ | 0 | 4 |
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
| ✅ STREAK_FADE_15M | 485 | +0.034 | +14.26€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 485 | +0.034 | +14.26€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 226 | +0.040 | +6.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 226 | +0.040 | +6.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 31 | +0.076 | +0.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 31 | +0.076 | +0.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 52 | -0.018 | -3.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 52 | -0.018 | -3.62€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 176 | +0.034 | +10.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 176 | +0.034 | +10.02€ | 2 | 3 |
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
| ✅ STREAK_MOM_5M | 7557 | +0.022 | +103.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7557 | +0.022 | +103.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2127 | +0.020 | +19.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2127 | +0.020 | +19.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1676 | +0.035 | +49.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1676 | +0.035 | +49.88€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2299 | +0.010 | -0.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2299 | +0.010 | -0.77€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1455 | +0.028 | +34.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1455 | +0.028 | +34.66€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7085 | +0.010 | -54.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7085 | +0.010 | -54.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2838 | +0.013 | -14.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2838 | +0.013 | -14.76€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2774 | +0.011 | -20.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2774 | +0.011 | -20.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1473 | +0.002 | -19.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1473 | +0.002 | -19.96€ | 2 | 0 |
| ✅ UPDOWN_GBM | 35044 | +0.030 | +2070.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9443 | +0.065 | +1671.10€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1299 | +0.004 | +5.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 22048 | +0.020 | +370.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2121 | +0.009 | +23.20€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3493 | +0.067 | +369.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 578 | +0.148 | +224.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 29 | -0.016 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2886 | +0.052 | +145.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6497 | +0.035 | +433.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1199 | +0.081 | +259.28€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 354 | +0.020 | +7.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3940 | +0.032 | +149.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 953 | +0.005 | +17.16€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 51 | -0.104 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4087 | +0.039 | +237.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 540 | +0.140 | +194.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 25 | -0.018 | -1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3522 | +0.024 | +44.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7462 | +0.017 | +279.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2453 | +0.045 | +267.87€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 342 | +0.006 | +7.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3900 | +0.005 | +1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 724 | +0.007 | -0.91€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 43 | -0.144 | +3.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8427 | +0.016 | +222.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2337 | +0.025 | +161.34€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 336 | -0.006 | -3.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5273 | +0.015 | +59.89€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 444 | +0.020 | +6.94€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 37 | -0.167 | -2.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5076 | +0.035 | +529.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2336 | +0.079 | +563.41€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 213 | -0.002 | -2.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2527 | -0.002 | -30.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 131 | -0.139 | +1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 529 | +0.336 | +152.47€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 529 | +0.336 | +152.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 297 | +0.340 | +82.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 297 | +0.340 | +82.27€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 232 | +0.329 | +70.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 232 | +0.329 | +70.21€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11378 | -0.042 | +2322.69€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11378 | -0.042 | +2322.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 691 | -0.043 | +329.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 691 | -0.043 | +329.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2127 | -0.123 | +22.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2127 | -0.123 | +22.88€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 333 | +0.175 | +214.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 333 | +0.175 | +214.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1253 | +0.201 | +718.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1253 | +0.201 | +718.76€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3479 | -0.064 | +530.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3479 | -0.064 | +530.17€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3495 | -0.079 | +507.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3495 | -0.079 | +507.16€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 137 | +0.040 | +8.30€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 137 | +0.040 | +8.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 137 | +0.040 | +8.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 137 | +0.040 | +8.30€ | 2 | 2 |
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
  - _Estado_: 523 celda(s) pasan gate riguroso completo de 2189 evaluadas (n>=40) y 3186 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.025 < 0.08 — monitorear
  - _Datos_: n=2335 IC=+0.025 PNL=+161.31€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.097 n=276/60 | contraria IC=+0.149 n=274 | gap=-0.051 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

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
  - _Estado_: ETH#60min: n=724/40 IC=+0.007 PNL=-0.91€ | BTC#60min: n=953/40 IC=+0.005 PNL=+17.16€ | SOL#60min: n=444/40 IC=+0.020 PNL=+6.94€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.051 n=320685 | tras_1loss IC=+0.077 n=249620 | tras_2loss IC=+0.046 n=105577/40 | gap=+0.005 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.08 con n=311 PNL=+193.62€
  - _Datos_: n=311 IC=+0.174 PNL=+193.62€

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
  - _Estado_: n=1514 IC=+0.018 PNL=+17.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1514 IC=+0.018 PNL=+17.11€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=607 IC=-0.014 PNL=+6.08€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=607 IC=-0.014 PNL=+6.08€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.1 con n=2018 PNL=+1262.76€
  - _Datos_: n=2018 IC=+0.186 PNL=+1262.76€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1197 IC=+0.081 PNL=+258.28€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1197 IC=+0.081 PNL=+258.28€

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
  - _Estado_: n=12155 IC=+0.056 PNL=+1511.53€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=12155 IC=+0.056 PNL=+1511.53€

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
  - _Estado_: n=1795 IC=+0.046 PNL=+185.49€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1795 IC=+0.046 PNL=+185.49€

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
  - _Estado_: n=17024 IC=-0.136 PNL=+1196.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=17024 IC=-0.136 PNL=+1196.13€

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
  - _Estado_: n=1843 IC=+0.138 PNL=+996.20€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1843 IC=+0.138 PNL=+996.20€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.085 n=942) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=942 IC=+0.085 PNL=+206.37€

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
  - _Estado_: n=8460 IC=+0.176 PNL=-988.79€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8460 IC=+0.176 PNL=-988.79€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
