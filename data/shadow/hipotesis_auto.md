# Hipótesis automáticas — 2026-08-22 16:02 UTC
_Generado por shadow_postmortem.py sobre 115053 resoluciones (PNL=+9000.06€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.178 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=179)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=177)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=215)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.262 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.120)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.136 (n=185)

  - _Acción_: Kelly boost +0.68€ cuando `n_ballena_banda` > 20.0 (IC base=+0.120)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.120)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.260 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.120)

- **PATRÓN** `banda_z` > `9.861` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.861 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.142 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.135 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 4.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=206)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2524.0354` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2524.0354 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=+0.120)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.018)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.725` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.151)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `n_ballena_banda` > 26.0 (IC base=+0.151)

- **PATRÓN** `n_total_lado` > `55.0` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 55.0 (IC base=+0.151)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 9.958 (IC base=+0.151)

- **PATRÓN** `ballenas_wallet_edge_medio` > `1.284` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `ballenas_wallet_edge_medio` > 1.284 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 4.0 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4546.1989` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4546.1989 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=86)

- **FILTRO** `banda_hit_calibrado` < `0.6284` → IC=-0.218 (n=37)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6284
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=90)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.078)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 8.174 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `156.97` → IC=-0.261 (n=1615)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.97
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4848)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.126 (n=404)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=233)

- **FILTRO** `restante_s_al_confirmar` < `169.33` → IC=-0.259 (n=210)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 169.33
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=427)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `n_ballenas` < `5.0` → IC=-0.190 (n=140)

  - _Acción_: SKIP cuando `n_ballenas` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=445)

- **FILTRO** `restante_s_al_confirmar` < `344.88` → IC=-0.311 (n=146)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 344.88
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=439)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `88.27` → IC=-0.435 (n=168)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 88.27
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=505)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `144.69` → IC=-0.256 (n=395)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.69
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1187)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `253.99` → IC=-0.243 (n=945)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 253.99
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=316)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.192 (n=3836)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.7 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=1336)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.170 (n=1290)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=2444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=3031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.263 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.182 (n=2440)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4312.8986` → IC=+0.171 (n=1014)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4312.8986 (IC base=+0.132)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.383 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.191 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.180 (n=489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.284 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=612)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.152 (n=400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 15.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.142 (n=473)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.555 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.39` → IC=+0.201 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.39 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4514.6378` → IC=+0.154 (n=258)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4514.6378 (IC base=+0.135)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.141 (n=606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.305 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.296 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.411 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.287 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `3311.8953` → IC=+0.315 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3311.8953 (IC base=+0.287)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.165 (n=261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.248 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=363)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2100.1274` → IC=+0.164 (n=293)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2100.1274 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.162 (n=140)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4420.281 (IC base=+0.086)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.206 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.434 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.298 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `762.1544` → IC=+0.225 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 762.1544 (IC base=+0.204)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.263 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.198 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 8.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.236 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.120 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.220 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=266)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.101)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=77)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=3505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=3093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.200 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3258.7888` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.7888 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=794)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.191 (n=893)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.74 (IC base=+0.170)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=46)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=782)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.188 (n=309)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.7 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.167 (n=485)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.73 (IC base=+0.163)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.310 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.227)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.201 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.71 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.444 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3939.3842` → IC=+0.451 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3939.3842 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.429 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `9836.4076` → IC=+0.467 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9836.4076 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.430 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.419 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.412)

- **PATRÓN** `libro_liquidez` > `2106.7117` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2106.7117 (IC base=+0.412)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.450 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.932` → IC=+0.425 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.932 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.92` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.92 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.432)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=2843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.201 (n=5392)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.228 (n=5827)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.148 (n=998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.169 (n=1072)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.71 (IC base=+0.126)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.270 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.285 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.240)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.173 (n=542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.191 (n=972)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.72 (IC base=+0.160)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.240 (n=852)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.301 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.238)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.251 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.231)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.199 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.130)

- **PATRÓN** `restante_min` < `3.9` → IC=+0.157 (n=960)

  - _Acción_: Kelly boost +0.78€ cuando `restante_min` < 3.9 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.92` → IC=+0.147 (n=993)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.92 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=1283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `6.89` → IC=+0.142 (n=1259)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 6.89 (IC base=+0.130)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.221 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.142)

- **PATRÓN** `restante_min` < `3.81` → IC=+0.172 (n=477)

  - _Acción_: Kelly boost +0.86€ cuando `restante_min` < 3.81 (IC base=+0.142)

- **PATRÓN** `restante_min` > `4.89` → IC=+0.158 (n=525)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.89 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.153 (n=1281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `lag_apertura_s` < `6.49` → IC=+0.163 (n=476)

  - _Acción_: Kelly boost +0.82€ cuando `lag_apertura_s` < 6.49 (IC base=+0.142)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.178 (n=535)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.37 (IC base=+0.117)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.147 (n=482)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 3.95 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.146 (n=538)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.125 (n=1465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 17.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.153 (n=480)

  - _Acción_: Kelly boost +0.77€ cuando `lag_apertura_s` < 3.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.312 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.308 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.388 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.283 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.273)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.273)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `5730.9756` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5730.9756 (IC base=+0.273)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.312 (n=237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.308 (n=233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `2570.3258` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2570.3258 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.377 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.380)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.423 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.380)

- **PATRÓN** `py_entrada` > `0.88` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.88 (IC base=+0.380)

- **PATRÓN** `libro_liquidez` > `791.5739` → IC=+0.395 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 791.5739 (IC base=+0.380)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.416 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.423 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.408)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.421 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.408)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.420 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.408)

- **PATRÓN** `libro_liquidez` > `1854.0504` → IC=+0.422 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1854.0504 (IC base=+0.408)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.413 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.436 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.420 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.419 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `5428.3063` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5428.3063 (IC base=+0.409)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.414 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.428 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.404 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.403)

- **PATRÓN** `libro_liquidez` > `1933.7222` → IC=+0.441 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.7222 (IC base=+0.403)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.332 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.423 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.298 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `785.9437` → IC=+0.291 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 785.9437 (IC base=+0.277)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.332 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.423 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.298 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `785.9437` → IC=+0.291 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 785.9437 (IC base=+0.277)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9609` → IC=+0.249 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9609 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1697` → IC=+0.232 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1697 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `1.0541` → IC=+0.229 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.0541 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.929` → IC=+0.213 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.929 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `1.0855` → IC=+0.261 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0855 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.123 (n=854)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.3158` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.3158 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `1.4913` → IC=+0.128 (n=899)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4913 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.4058` → IC=+0.124 (n=1832)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.4058 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.145 (n=601)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.6283` → IC=+0.141 (n=207)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6283 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.2477` → IC=+0.149 (n=206)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.2477 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.3085` → IC=+0.270 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3085 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.6349` → IC=+0.209 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6349 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `3.0486` → IC=+0.224 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0486 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.041)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.170 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0071 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.343 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.154 (n=325)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.06 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.319 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.329 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.329 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.297 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.330 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0645` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0645 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7987` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7987 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.334 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1982.2745` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.2745 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.287)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.276 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.237 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.237 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.236 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `1.1167` → IC=+0.233 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.1167 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.802` → IC=+0.331 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.802 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `1.1094` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1094 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.1033` → IC=+0.227 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1033 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.3533` → IC=+0.235 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3533 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.0135` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0135 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `13198.9616` → IC=+0.267 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13198.9616 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.155 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.004 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.2388` → IC=+0.151 (n=305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.2388 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.142 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.143 (n=357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 18.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.3939` → IC=+0.162 (n=306)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3939 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1822` → IC=+0.167 (n=307)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1822 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.937` → IC=+0.233 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.937 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6279 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0017` → IC=+0.144 (n=158)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0017 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0771` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0771 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.7604` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.7604 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.183` → IC=+0.155 (n=111)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.183 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=447)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `13633.3694` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 13633.3694 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 231.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0071 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.136 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.147 (n=432)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `1917.67` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1917.67 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 23.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.328 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.305 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.289 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.5027` → IC=+0.312 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5027 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.013` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.013 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.3362` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3362 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `4.5585` → IC=+0.267 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.5585 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.9495` → IC=+0.286 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9495 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.287 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.285)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `sigma_h` > `0.0045` → IC=-0.124 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=404)

- **FILTRO** `ibs_20min` > `0.8814` → IC=-0.188 (n=152)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8814
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=460)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=563)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.865` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.865 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.1367` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1367 (IC base=-0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.0669` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0669 (IC base=-0.062)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `2.933` → IC=-0.128 (n=307)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.933
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=733)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.081)

- **PATRÓN** `drift_60min` |x|≤ `0.3497` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3497 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.3333` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3333 (IC base=+0.081)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.4378` → IC=-0.120 (n=235)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4378
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=236)

- **FILTRO** `ibs_20min` > `0.7634` → IC=-0.152 (n=234)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7634
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=706)

- **FILTRO** `sigma_ewma_delta_pct` > `8.034` → IC=-0.170 (n=113)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.034
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=827)

- **PATRÓN** `dist_vwap_pct` > `0.2288` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2288 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1542` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1542 (IC base=-0.045)

- **PATRÓN** `volumen_regimen` < `0.8221` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8221 (IC base=-0.045)

- **PATRÓN** `volumen_regimen` > `0.9364` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9364 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` < `0.3361` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3361 (IC base=-0.012)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6961 (IC base=-0.012)

- **PATRÓN** `volumen_regimen` > `1.0971` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0971 (IC base=-0.012)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.158 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0076 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.247 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.6964` → IC=+0.272 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6964 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.306` → IC=+0.132 (n=1233)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.306 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.1809` → IC=+0.180 (n=223)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.1809 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.117` → IC=+0.151 (n=878)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.117 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.3201` → IC=+0.208 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3201 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `1.6679` → IC=+0.159 (n=817)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.6679 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.287 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.1024` → IC=+0.165 (n=999)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1024 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `0.7476` → IC=+0.207 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7476 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `1.0538` → IC=+0.207 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0538 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2632` → IC=+0.346 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2632 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `3.0884` → IC=+0.288 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0884 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.251 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.037)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.936` → IC=-0.214 (n=110)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.936
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=552)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.418` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.418 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0542` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0542 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.317` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.317 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `volumen_regimen` < `0.5591` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.5591 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` > `0.9983` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.9983 (IC base=-0.035)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.292 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0614` → IC=+0.222 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0614 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.303 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1444` → IC=+0.187 (n=266)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1444 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.0881` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.0881 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.198 (n=405)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.06 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1914.9184` → IC=+0.206 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9184 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.402 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.372)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.378 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.372)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.397 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.372)

- **PATRÓN** `ibs_20min` < `0.3009` → IC=+0.389 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3009 (IC base=+0.372)

- **PATRÓN** `ibs_20min` > `0.0514` → IC=+0.369 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0514 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` < `0.3211` → IC=+0.402 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3211 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.372)

- **PATRÓN** `volumen_spike_ratio` < `2.9764` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9764 (IC base=+0.372)

- **PATRÓN** `libro_liquidez` > `1874.461` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.461 (IC base=+0.372)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `dist_vwap_pct` < `0.58` → IC=-0.221 (n=41)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=16)

- **FILTRO** `volumen_regimen` > `0.9213` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9213
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `libro_liquidez` < `8670.81` → IC=-0.186 (n=84)

  - _Acción_: SKIP cuando `libro_liquidez` < 8670.81
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=252)

- **FILTRO** `dist_vwap_pct` < `0.1085` → IC=-0.143 (n=54)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1085
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `volumen_regimen` > `0.8819` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8819
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `volumen_regimen` < `0.6808` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6808
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=48)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.148 (n=52)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=808)

- **PATRÓN** `dist_vwap_pct` > `0.58` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.58 (IC base=-0.065)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.5` → IC=-0.154 (n=218)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=221)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=46)

- **FILTRO** `volumen_regimen` > `1.2342` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2342
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=41)

- **FILTRO** `volumen_pendiente_norm` < `0.1045` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1045
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.159 (n=221)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` > `0.1881` → IC=+0.240 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1881 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `1.1512` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1512 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2555` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2555 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.2948` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.2948 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.339 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.238 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.5623` → IC=+0.327 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5623 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.097` → IC=+0.259 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.097 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `0.8361` → IC=+0.238 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8361 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0802` → IC=+0.197 (n=345)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0802 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2479` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2479 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.36` → IC=+0.216 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.36 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2654.5546` → IC=+0.226 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.5546 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.352 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.278 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.3422` → IC=+0.272 (n=371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3422 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.319 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.316 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` < `0.6136` → IC=+0.268 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6136 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.486` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.486 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `1.2535` → IC=+0.304 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2535 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.7624` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7624 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.262)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.222 (n=598)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.907` → IC=+0.258 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.907 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.6468` → IC=+0.253 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6468 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.06` → IC=+0.270 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.06 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.177 (n=1022)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.7026 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1047` → IC=+0.189 (n=628)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1047 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.4067` → IC=+0.150 (n=1363)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4067 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.467` → IC=+0.148 (n=1549)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.467 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=1358)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3322.554` → IC=+0.202 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.554 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.196 (n=616)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 121.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.207 (n=1585)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3252` → IC=+0.198 (n=1585)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3252 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.230 (n=814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.3945` → IC=+0.249 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3945 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.5066` → IC=+0.173 (n=1458)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.5066 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.657` → IC=+0.201 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.657 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.382` → IC=+0.191 (n=1594)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 5.382 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.164 (n=1285)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1777 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `0.6808` → IC=+0.170 (n=1148)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6808 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2511` → IC=+0.246 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2511 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.6125` → IC=+0.186 (n=431)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.6125 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.8143` → IC=+0.223 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8143 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.199 (n=363)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 58.0 (IC base=+0.189)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.210 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.377` → IC=+0.359 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.377 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1402` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1402 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4192` → IC=+0.134 (n=260)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4192 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.186 (n=269)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.302 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.332 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.315 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.4177` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4177 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.0686` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0686 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.8747` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8747 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.374 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1966.1335` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.1335 (IC base=+0.291)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.250 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.210 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `0.6555` → IC=+0.249 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6555 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.17` → IC=+0.243 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.17 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.604` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.604 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `0.9279` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9279 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2852` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2852 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.4249` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4249 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.721` → IC=+0.200 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.721 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `11170.0615` → IC=+0.238 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11170.0615 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.200 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.2038` → IC=+0.200 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2038 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.3584` → IC=+0.201 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3584 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.1407` → IC=+0.189 (n=319)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1407 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.578` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.578 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6331` → IC=+0.241 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6331 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.1729` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1729 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.218 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.7551` → IC=+0.190 (n=140)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.7551 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.4382` → IC=+0.159 (n=209)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4382 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `238.0` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 238.0 (IC base=+0.157)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.198 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0076 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.157 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.3507` → IC=+0.134 (n=282)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.3507 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.0183` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0183 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `3.9092` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 3.9092 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.175 (n=244)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.04 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `1970.8484` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1970.8484 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.339 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.302)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.304 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.2366` → IC=+0.326 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2366 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.329 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.3486` → IC=+0.323 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3486 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.578` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.578 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3308` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3308 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `4.3528` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.3528 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.302)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.251 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1373` → IC=+0.277 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1373 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.4687` → IC=+0.286 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4687 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1385` → IC=+0.236 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1385 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.3995` → IC=+0.218 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3995 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.711` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.711 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6382` → IC=+0.243 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6382 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1047` → IC=+0.288 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1047 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4661` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4661 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.5456` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5456 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `9491.6866` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9491.6866 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.205 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 236.0 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.211 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2651` → IC=+0.177 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2651 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.2823` → IC=+0.225 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2823 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.4512` → IC=+0.169 (n=366)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.4512 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.649` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.649 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.849` → IC=+0.167 (n=208)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.849 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6094` → IC=+0.152 (n=311)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6094 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2376` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2376 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.9018` → IC=+0.200 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9018 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.4642` → IC=-0.214 (n=103)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4642
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=310)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.230 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.222 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.8908` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8908 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` > `0.6164` → IC=+0.125 (n=339)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6164 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.0962` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0962 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2717.1791` → IC=+0.186 (n=154)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2717.1791 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.110)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.207 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.209 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.4642` → IC=+0.211 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4642 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.145` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 7.145 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.8537` → IC=+0.151 (n=207)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.8537 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `2.3994` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.3994 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2407.6604` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2407.6604 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 32.0 (IC base=+0.105)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.214 (n=337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.174 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 7.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.8077` → IC=+0.218 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8077 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.2985` → IC=+0.246 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2985 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.278` → IC=+0.239 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.278 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6122` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6122 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.8467` → IC=+0.188 (n=251)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.8467 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2437` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2437 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `2.6244` → IC=+0.181 (n=340)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.6244 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=407)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2451.018` → IC=+0.168 (n=377)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2451.018 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.271 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.281 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.246 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.1094` → IC=+0.338 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1094 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` < `0.7761` → IC=+0.241 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7761 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.824` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.824 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` > `0.6867` → IC=+0.267 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6867 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2516` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2516 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.9873` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9873 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 34.0 (IC base=+0.234)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.205 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.077)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` > `0.5258` → IC=+0.138 (n=277)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.5258 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.5918` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5918 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.914` → IC=+0.268 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.914 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 124.0 (IC base=+0.077)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.300 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.2308` → IC=+0.148 (n=163)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2308 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.625` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.625 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.7501` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.7501 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.5764` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5764 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 12.0 (IC base=+0.060)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

- **FILTRO** `ibs_20min` < `0.233` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.233
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=-0.044)

- **PATRÓN** `ibs_20min` > `0.6089` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.6089 (IC base=-0.044)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.218 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1162` → IC=+0.288 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1162 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 4.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.243 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.412` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.412 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1967` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1967 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.2318` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2318 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.287` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.287 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2185 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.5322` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5322 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 175.0 (IC base=+0.177)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0045` → IC=-0.154 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=50)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.231 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.225 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.208` → IC=+0.250 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.208 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.321 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.5593` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5593 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1417` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1417 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.984` → IC=+0.389 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.984 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `0.7406` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7406 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `1.1182` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1182 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.1824` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1824 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.9173` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9173 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2800.762` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2800.762 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.092)

- **PATRÓN** `drift_60min` |x|≤ `0.2707` → IC=+0.186 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.2707 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.232 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.529` → IC=+0.121 (n=56)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.529 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.121` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.121 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `9493.103` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9493.103 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `hora_utc` < `4.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=70)

- **FILTRO** `volumen_regimen` > `1.1865` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.1865
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `volumen_pendiente_norm` > `0.1169` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1169
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=51)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.144 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 1.0 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.4414` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4414 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.98` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 7.98 (IC base=+0.044)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.781` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.781 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.2226` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2226 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.029)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.240 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.153 (n=778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 6.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.96` → IC=+0.288 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.96 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.8943` → IC=+0.251 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8943 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.396` → IC=+0.238 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.396 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8962` → IC=+0.141 (n=886)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8962 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0941` → IC=+0.153 (n=603)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0941 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1687` → IC=+0.174 (n=498)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1687 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.8379` → IC=+0.138 (n=1741)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.8379 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.9412` → IC=+0.151 (n=1160)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.9412 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=1562)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3272.5153` → IC=+0.182 (n=684)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3272.5153 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.214 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.217 (n=1652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3668` → IC=+0.199 (n=1876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3668 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5385` → IC=+0.247 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5385 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.5928` → IC=+0.176 (n=1456)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.5928 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.225` → IC=+0.221 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.225 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.193 (n=1757)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6119` → IC=+0.183 (n=465)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6119 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` > `1.1856` → IC=+0.185 (n=465)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1856 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.235 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.286` → IC=+0.207 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.286 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.145 (n=333)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 35.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.210 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.158 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.289 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.154` → IC=+0.356 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.154 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2113` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2113 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.159 (n=297)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.312 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.287 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.329 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.300 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5819` → IC=+0.339 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5819 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.316 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1989.2275` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.2275 (IC base=+0.287)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.172 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.192 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0054 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3307` → IC=+0.218 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3307 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2176` → IC=+0.233 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2176 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.229` → IC=+0.261 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.229 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9134` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.9134 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1445` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1445 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.6131` → IC=+0.199 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6131 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.3478` → IC=+0.199 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3478 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10679.1014` → IC=+0.190 (n=188)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 10679.1014 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.207 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3105` → IC=+0.172 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3105 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.164 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.169 (n=351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 18.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.3342` → IC=+0.204 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3342 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` < `0.2947` → IC=+0.185 (n=328)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2947 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.674` → IC=+0.233 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.674 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6208` → IC=+0.215 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6208 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.2004` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.2004 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1576` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1576 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.7314` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.7314 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.5054` → IC=+0.188 (n=219)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.5054 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=438)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `12510.8748` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 12510.8748 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `318.0` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 318.0 (IC base=+0.159)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.245 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.717` → IC=+0.247 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.717 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.864` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.864 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.2327` → IC=+0.168 (n=251)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.2327 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1733` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1733 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `4.0128` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 4.0128 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.190 (n=349)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.06 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1854.4986` → IC=+0.185 (n=214)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1854.4986 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.332 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.273 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.282 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.5575` → IC=+0.340 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5575 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.4009` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4009 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.5357` → IC=+0.276 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5357 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.153 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0023 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.174 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.008 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.174 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.3665` → IC=+0.204 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3665 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1732` → IC=+0.198 (n=160)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1732 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.544` → IC=+0.202 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.544 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.7406` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.7406 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1192` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1192 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2367` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2367 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4124` → IC=+0.226 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4124 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `8486.8458` → IC=+0.234 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8486.8458 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 235.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.250 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3993` → IC=+0.148 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3993 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.161 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.2541` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2541 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1518` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1518 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.5685` → IC=+0.150 (n=241)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.5685 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.785` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.785 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.9419` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.9419 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2596` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2596 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.0946` → IC=+0.173 (n=157)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.0946 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4547` → IC=+0.172 (n=178)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.4547 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `4060.7684` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4060.7684 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.217 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.9434` → IC=+0.265 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9434 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.7862` → IC=+0.260 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7862 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.935` → IC=+0.261 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.935 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `2643.3921` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2643.3921 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.076)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.198 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0049 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.179 (n=341)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5789 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.4028` → IC=+0.128 (n=294)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4028 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.655` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 6.655 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.1689` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.1689 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1454` → IC=+0.128 (n=205)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1454 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.5236` → IC=+0.159 (n=174)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.5236 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1300.037` → IC=+0.138 (n=227)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1300.037 (IC base=+0.096)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.255 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0932` → IC=+0.182 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0932 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.171 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.3323` → IC=+0.266 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3323 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.825` → IC=+0.249 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.825 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.6079` → IC=+0.196 (n=146)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6079 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2439` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.2439 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2479` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2479 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.8196` → IC=+0.177 (n=388)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.8196 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.9308` → IC=+0.163 (n=259)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.9308 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=470)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `3104.3643` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3104.3643 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.278 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4486` → IC=+0.219 (n=482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4486 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.268 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.466` → IC=+0.283 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.466 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.8572` → IC=+0.228 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8572 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.973` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.973 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.839` → IC=+0.220 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.839 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8799` → IC=+0.240 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8799 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7303` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7303 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.134 (n=173)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 35.0 (IC base=+0.213)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=354)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.211 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.2745` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2745 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.1342` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1342 (IC base=+0.072)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=131)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.072)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.201 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1887` → IC=+0.168 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1887 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.250 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5876` → IC=+0.179 (n=244)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5876 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.2889` → IC=+0.151 (n=259)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2889 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.35` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.35 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1762` → IC=+0.167 (n=244)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1762 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6432` → IC=+0.145 (n=277)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6432 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0752` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0752 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.6543` → IC=+0.170 (n=274)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.6543 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4141` → IC=+0.149 (n=274)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4141 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=354)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7402.2744` → IC=+0.180 (n=248)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7402.2744 (IC base=+0.141)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **FILTRO** `dist_vwap_pct` < `0.5259` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.5259
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.164 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0038 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.220 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.288 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.0542` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0542 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.3593` → IC=+0.146 (n=156)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3593 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.225` → IC=+0.155 (n=137)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.225 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.2758` → IC=+0.151 (n=144)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2758 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `0.7193` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7193 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.827` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.827 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.4122` → IC=+0.144 (n=144)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4122 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `11764.4738` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 11764.4738 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `722.0` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 722.0 (IC base=+0.132)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.237 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.2274` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2274 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.131` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 5.131 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` < `0.1138` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1138 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `2.397` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.397 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `7271.563` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7271.563 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.312 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.4286` → IC=+0.254 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4286 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.265 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.649` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.649 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.1288` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1288 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.5729` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5729 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.688` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.688 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2693` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2693 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.1261` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1261 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.6912` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6912 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `7230.0627` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7230.0627 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.222)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `sigma_ewma_delta_pct` < `2.985` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.985
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.037)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.149 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=112)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `volumen_spike_ratio` < `2.7298` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.7298
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.180 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0054 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.1151` → IC=+0.151 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1151 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.213 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.0949` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0949 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.0847` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0847 (IC base=+0.057)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=111)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2013.1835` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2013.1835 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=42)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7342 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.062)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=43)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.242 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2012` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2012 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.41` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.41 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.8241` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8241 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2340.5972` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2340.5972 (IC base=+0.100)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `volumen_regimen` > `0.903` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.903
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=-0.020)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=-0.020)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `libro_liquidez` < `2167.8726` → IC=-0.337 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2167.8726
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=48)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.380 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=75)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `libro_liquidez` < `1468.1795` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 1468.1795
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=74)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `libro_liquidez` < `4361.6218` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4361.6218
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.5333` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5333
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=101)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6429 (IC base=+0.059)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.125 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=39)

- **PATRÓN** `ibs_20min` > `0.7184` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7184 (IC base=-0.067)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.3803` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.3803 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.085)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.991` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.991 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2399.5952` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.5952 (IC base=+0.159)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.03 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.197 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 14.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.485 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2598.9726` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.9726 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2545.8374` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2545.8374 (IC base=+0.087)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.197 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 14.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.485 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2598.9726` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.9726 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2545.8374` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2545.8374 (IC base=+0.087)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=93)

- **FILTRO** `libro_liquidez` < `2012.8653` → IC=-0.397 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 2012.8653
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=82)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `libro_liquidez` < `2892.3985` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2892.3985
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M
- **FILTRO** `hora_utc` < `6.0` → IC=-0.173 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=157)

- **FILTRO** `libro_liquidez` < `3732.639` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_liquidez` < 3732.639
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=139)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.285 (n=63)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35898.38` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `liq_usd_total` < 35898.38
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=51)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_usd_total` < `6190.71` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 6190.71
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

### LIQUIDACIONES_60M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=62)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.136 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=43)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_usd_total` < `433.59` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_usd_total` < 433.59
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=66)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=66)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2166.2663` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 2166.2663
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=72)

- **FILTRO** `drift_20min_pct` |x|> `0.1387` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1387
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=83)

- **PATRÓN** `libro_liquidez` > `2221.671` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2221.671 (IC base=+0.015)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0647` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `drift_20min_pct` |x|≤ 0.0647 (IC base=+0.032)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `ibs_20min` > `0.9506` → IC=-0.214 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9506
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=121)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=200)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.45` → IC=-0.168 (n=429)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1322)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.255 (n=418)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1313)

- **FILTRO** `ibs_20min` > `0.2782` → IC=-0.237 (n=432)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2782
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1299)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.124 (n=588)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1143)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=198)

- **FILTRO** `ibs_20min` < `0.8359` → IC=-0.129 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8359
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=130)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=218)

- **FILTRO** `ibs_20min` > `0.7602` → IC=-0.226 (n=71)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7602
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=215)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.131 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=165)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.276 (n=74)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=230)

- **FILTRO** `ibs_20min` > `0.2136` → IC=-0.250 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2136
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=230)

- **FILTRO** `ballena_activa_n` > `82.0` → IC=-0.197 (n=74)

  - _Acción_: SKIP cuando `ballena_activa_n` > 82.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=230)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=147)

- **FILTRO** `ibs_20min` < `0.7235` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7235
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=196)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.253 (n=71)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=220)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.230 (n=98)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=193)

- **PATRÓN** `ibs_20min` > `0.9507` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.9507 (IC base=-0.021)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.171 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=239)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.212 (n=71)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=244)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.197 (n=74)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=241)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.309 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=201)

- **FILTRO** `drift_20min_pct` |x|> `0.3233` → IC=-0.250 (n=66)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.3233
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=201)

- **FILTRO** `ibs_20min` > `0.2692` → IC=-0.250 (n=66)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2692
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=201)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.198 (n=160)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=107)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.237 (n=74)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=227)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=286)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=204)

- **FILTRO** `drift_20min_pct` |x|> `0.2236` → IC=-0.159 (n=133)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=135)

- **FILTRO** `ibs_20min` > `0.2949` → IC=-0.382 (n=66)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2949
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=202)

- **PATRÓN** `py_entrada` > `0.47` → IC=+0.120 (n=227)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.47 (IC base=+0.031)

- **PATRÓN** `libro_liquidez` > `2461.1674` → IC=+0.148 (n=103)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2461.1674 (IC base=+0.031)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=373)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=379)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `drift_20min_pct` |x|> `0.1906` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1906
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `ibs_20min` > `0.8837` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8837
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.033)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **PATRÓN** `libro_liquidez` > `9438.7586` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 9438.7586 (IC base=+0.064)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=1217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=3037)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=1020)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=3234)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.228 (n=1059)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3195)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.169 (n=1441)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2813)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.230 (n=1213)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=3822)

- **FILTRO** `ibs_7min` > `0.7122` → IC=-0.171 (n=1258)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7122
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3777)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.162 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=420)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.336 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=460)

- **FILTRO** `ibs_7min` < `0.8305` → IC=-0.230 (n=305)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8305
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=305)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.243 (n=150)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=460)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.137 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=617)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.242 (n=215)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=568)

- **FILTRO** `drift_7min_pct` |x|> `0.1413` → IC=-0.179 (n=266)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1413
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=517)

- **FILTRO** `ibs_7min` > `0.828` → IC=-0.206 (n=195)

  - _Acción_: SKIP cuando `ibs_7min` > 0.828
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=588)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.153 (n=188)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=595)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.252 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=655)

- **FILTRO** `ibs_7min` < `0.7988` → IC=-0.164 (n=215)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7988
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=648)

- **FILTRO** `ballena_activa_n` > `143.0` → IC=-0.157 (n=214)

  - _Acción_: SKIP cuando `ballena_activa_n` > 143.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=649)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.220 (n=216)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=655)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.208 (n=169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=411)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.354 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=438)

- **FILTRO** `ibs_7min` < `0.7106` → IC=-0.262 (n=191)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7106
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=389)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.274 (n=144)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=436)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.270 (n=198)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=670)

- **FILTRO** `ibs_7min` > `0.8333` → IC=-0.179 (n=216)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8333
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=652)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.150 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=568)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.242 (n=184)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=559)

- **FILTRO** `ibs_7min` < `0.7802` → IC=-0.174 (n=185)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7802
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=558)

- **FILTRO** `ballena_activa_n` > `45.0` → IC=-0.227 (n=185)

  - _Acción_: SKIP cuando `ballena_activa_n` > 45.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=558)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.273 (n=183)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=551)

- **FILTRO** `ibs_7min` > `0.1692` → IC=-0.160 (n=248)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1692
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=486)

- **FILTRO** `ballena_activa_n` > `36.0` → IC=-0.194 (n=181)

  - _Acción_: SKIP cuando `ballena_activa_n` > 36.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=553)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.203 (n=197)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=591)

- **FILTRO** `ibs_7min` < `0.7778` → IC=-0.178 (n=197)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7778
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=591)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.208 (n=193)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=595)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.187 (n=228)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=703)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.268 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=508)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.233 (n=163)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=507)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.218 (n=161)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=509)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.301 (n=199)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=649)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.172 (n=288)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=560)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.143 (n=275)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=573)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=149)

- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

- **FILTRO** `ibs_7min` > `0.0606` → IC=-0.133 (n=58)

  - _Acción_: SKIP cuando `ibs_7min` > 0.0606
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=371)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=248)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3996` → IC=+0.143 (n=211)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.3996 (IC base=+0.108)

- **PATRÓN** `total_vol_5m` < `389.535` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 389.535 (IC base=+0.108)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.100)

- **PATRÓN** `total_vol_5m` < `340.581` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 340.581 (IC base=+0.100)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.048)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=66)

- **FILTRO** `T_h` > `87.9756` → IC=-0.365 (n=72)

  - _Acción_: SKIP cuando `T_h` > 87.9756
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=36)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.147 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0039 (IC base=-0.169)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **FILTRO** `T_h` > `111.9936` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `T_h` > 111.9936
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=-0.161)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.173 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

- **FILTRO** `T_h` > `135.9709` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `T_h` > 135.9709
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=37)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.333 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=51)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0029` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0029
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `95.1632` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `streak_estiramiento` > `0.4086` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4086
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `62.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 62.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

### STREAK_FADE_5M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=149)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 3.0 (IC base=+0.006)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=37)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **FILTRO** `libro_liquidez` < `3627.5123` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 3627.5123
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=40)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **PATRÓN** `libro_liquidez` > `3988.6558` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3988.6558 (IC base=+0.008)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=56)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=57)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=94)

- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=59)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.127 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.030)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=62)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=125)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.147 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 19.0 (IC base=-0.017)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 16.0 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 29.0 (IC base=+0.085)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=950)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=543)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=551)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.145 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0036 (IC base=+0.109)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.135 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0048 (IC base=+0.109)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0663` → IC=+0.129 (n=346)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio_macro` |x|> 0.0663 (IC base=+0.109)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.190 (n=356)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.5 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.359` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.359 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.503` → IC=+0.246 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.503 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3848.1598` → IC=+0.141 (n=157)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3848.1598 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 58.0 (IC base=+0.109)

### UPDOWN_GBM#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1929` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1929
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.241 (n=83)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=249)

- **FILTRO** `sigma_ewma_delta_pct` > `8.526` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.526
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=295)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=71)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=183)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.220 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `dist_vwap_pct` < `0.2283` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2283
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=3)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.134 (n=129)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.030)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.004` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=41)

- **FILTRO** `dist_vwap_pct` < `0.2426` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2426
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=35)

- **FILTRO** `libro_liquidez` < `14339.8207` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 14339.8207
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=28)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.159 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0035 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.170 (n=89)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.142)

- **PATRÓN** `drift_15min` |x|≤ `0.4599` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.4599 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2917` → IC=+0.188 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.2917 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.170 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 3.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.159 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 13.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.9453` → IC=+0.291 (n=41)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9453 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1104` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1104 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.029` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.029 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `11026.1015` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 11026.1015 (IC base=+0.142)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2056` → IC=-0.204 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2056
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.138 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0028 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.755` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.755 (IC base=+0.027)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=58)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1006` → IC=+0.180 (n=23)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.90€ cuando `pct_spot_vs_ref` |x|≤ 0.1006 (IC base=+0.011)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5659` → IC=-0.250 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5659
  - _Potencial_: sin este filtro IC_bueno=+0.267 (n=71)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.122 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.098)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.142 (n=79)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.5659` → IC=+0.267 (n=71)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5659 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `8758.263` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 8758.263 (IC base=+0.098)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=52)

- **FILTRO** `ibs_15` < `0.005` → IC=-0.222 (n=16)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=51)

- **FILTRO** `dist_vwap_pct` > `0.1689` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1689
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=52)

- **FILTRO** `sigma_ewma_delta_pct` > `5.225` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.225
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1911` → IC=+0.140 (n=23)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.1911 (IC base=-0.080)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=56)

- **PATRÓN** `delta_ratio_macro` |x|> `0.222` → IC=+0.167 (n=28)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.222 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.049` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 14.049 (IC base=+0.053)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.03 (IC base=+0.053)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=30)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.250 (n=30)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.764` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.764 (IC base=+0.041)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `ibs_15` < `0.1667` → IC=-0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `dist_vwap_pct` < `0.3215` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3215
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=4)

- **FILTRO** `sigma_ewma_delta_pct` < `2.288` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.288
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.133 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=15)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.011)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.167 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.005 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.130 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 15.0 (IC base=+0.088)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.5354` → IC=+0.185 (n=87)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.5354 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.4287` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4287 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.277` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.277 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.140 (n=87)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.088)

- **PATRÓN** `ibs_15` < `0.1667` → IC=+0.161 (n=107)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1667 (IC base=+0.044)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.300 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.316 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1971` → IC=+0.291 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1971 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.291 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.283 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.7117` → IC=+0.345 (n=108)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7117 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.4655` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4655 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.84` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.84 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `3288.4647` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3288.4647 (IC base=+0.286)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.297 (n=57)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.259)

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.162` → IC=+0.263 (n=57)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.162 (IC base=+0.259)

- **PATRÓN** `drift_15min` |x|≤ `0.4136` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4136 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.262 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.259)

- **PATRÓN** `ibs_15` < `0.9942` → IC=+0.258 (n=64)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9942 (IC base=+0.259)

- **PATRÓN** `ibs_15` > `0.7363` → IC=+0.288 (n=64)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7363 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.3665` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3665 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.744` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.744 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `7219.8643` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7219.8643 (IC base=+0.259)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.312 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.317)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.317)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.382 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.317)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1549` → IC=+0.403 (n=29)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1549 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.342 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.317)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.317)

- **PATRÓN** `ibs_15` > `0.7853` → IC=+0.427 (n=39)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7853 (IC base=+0.317)

- **PATRÓN** `dist_vwap_pct` > `0.1175` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1175 (IC base=+0.317)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.414` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.414 (IC base=+0.317)

- **PATRÓN** `libro_liquidez` > `2646.1898` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2646.1898 (IC base=+0.317)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.375` → IC=-0.333 (n=76)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=231)

- **FILTRO** `sigma_h` > `0.0079` → IC=-0.175 (n=644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1251)

- **FILTRO** `ibs_15` > `0.531` → IC=-0.289 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.531
  - _Potencial_: sin este filtro IC_bueno=+0.272 (n=55)

- **FILTRO** `sigma_ewma_delta_pct` > `13.453` → IC=-0.187 (n=340)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.453
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=1555)

- **PATRÓN** `ibs_15` > `0.375` → IC=+0.140 (n=231)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.70€ cuando `ibs_15` > 0.375 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.531` → IC=+0.272 (n=55)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.531 (IC base=-0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1453` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1453 (IC base=-0.097)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_15` < `0.9205` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.9205
  - _Potencial_: sin este filtro IC_bueno=+0.423 (n=11)

- **FILTRO** `sigma_h` > `0.0067` → IC=-0.225 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=325)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.235 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=332)

- **FILTRO** `sigma_ewma_delta_pct` > `20.169` → IC=-0.253 (n=87)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.169
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=345)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.127 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0029 (IC base=+0.030)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6371` → IC=-0.314 (n=57)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6371
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=58)

- **PATRÓN** `ibs_15` > `0.6371` → IC=+0.233 (n=58)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6371 (IC base=-0.038)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1041` → IC=+0.224 (n=27)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1041 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.184 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.004 (IC base=+0.154)

- **PATRÓN** `drift_15min` |x|≤ `0.6513` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `drift_15min` |x|≤ 0.6513 (IC base=+0.154)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1155` → IC=+0.158 (n=36)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1155 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.235 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.167 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 14.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` < `0.3879` → IC=+0.311 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3879 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.294` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 7.294 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.166` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 8.166 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3807.5396` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3807.5396 (IC base=+0.154)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0078` → IC=-0.211 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=131)

- **FILTRO** `sigma_h` > `0.0085` → IC=-0.153 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=441)

- **FILTRO** `sigma_ewma_delta_pct` > `12.101` → IC=-0.191 (n=108)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.101
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=559)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.666` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.666 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.005` → IC=-0.146 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=139)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.153 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=63)

- **FILTRO** `libro_liquidez` < `2506.382` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 2506.382
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=139)

- **FILTRO** `sigma_h` > `0.0093` → IC=-0.181 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0093
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=405)

- **FILTRO** `drift_60min` |x|> `0.398` → IC=-0.167 (n=208)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.398
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=405)

- **FILTRO** `drift_15min` |x|> `1.0686` → IC=-0.177 (n=153)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0686
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=460)

- **FILTRO** `sigma_ewma_delta_pct` > `14.673` → IC=-0.201 (n=75)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.673
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=538)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.354 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.301 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.340 (n=73)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1069` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1069 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.9678` → IC=+0.378 (n=72)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9678 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.5461` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5461 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` < `0.0966` → IC=+0.298 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0966 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.106` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.106 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.772` → IC=+0.293 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.772 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `9700.4747` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9700.4747 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `354.0` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 354.0 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2` → IC=+0.266 (n=92)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2 (IC base=+0.258)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.255 (n=92)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.262 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0026 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.308 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.258)

- **PATRÓN** `drift_15min` |x|≤ `0.625` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.625 (IC base=+0.258)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1333` → IC=+0.278 (n=61)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1333 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.259 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.258)

- **PATRÓN** `ibs_15` > `0.9353` → IC=+0.341 (n=61)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9353 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.4105` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4105 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.018` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.018 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.495` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.495 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `11686.9744` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11686.9744 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `428.0` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 428.0 (IC base=+0.258)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` > `0.004` → IC=+0.326 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.004 (IC base=+0.311)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1843` → IC=+0.406 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1843 (IC base=+0.311)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.372 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.311)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.314 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.311)

- **PATRÓN** `ibs_15` > `0.8606` → IC=+0.338 (n=66)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8606 (IC base=+0.311)

- **PATRÓN** `dist_vwap_pct` > `0.6017` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6017 (IC base=+0.311)

- **PATRÓN** `dist_vwap_pct` < `0.0769` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0769 (IC base=+0.311)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.469` → IC=+0.333 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.469 (IC base=+0.311)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.311)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.311)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0492` → IC=-0.167 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0492
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `drift_60min` |x|> `0.1447` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1447
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `drift_15min` |x|> `0.3418` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3418
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.147 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=251)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.278 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0045` → IC=-0.289 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9936` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9936 (IC base=+0.062)

- **PATRÓN** `ratio` < `0.9702` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9702 (IC base=+0.062)

- **PATRÓN** `T_h` > `146.1118` → IC=+0.452 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.348)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.348)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `87.9997` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9997 (IC base=+0.266)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.266)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `82.5234` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 82.5234 (IC base=+0.092)

- **PATRÓN** `T_h` < `124.962` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 124.962 (IC base=+0.309)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.311 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.309)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.422)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0058 (IC=+0.265 n=15). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.109 a +0.190 en UPDOWN_GBM#15min (n=356). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9453 sube el IC de +0.142 a +0.291 en UPDOWN_GBM#BTC#15min (n=41). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5659 sube el IC de +0.098 a +0.267 en UPDOWN_GBM#ETH#15min (n=71). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.041 a +0.250 en UPDOWN_GBM#SOL#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5354 sube el IC de +0.088 a +0.185 en UPDOWN_GBM#XRP#15min (n=87). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1667 sube el IC de +0.044 a +0.161 en UPDOWN_GBM#XRP#15min (n=107). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.531 sube el IC de -0.097 a +0.272 en UPDOWN_GBM_15M_TARDIO (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6371 sube el IC de -0.038 a +0.233 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3879 sube el IC de +0.154 a +0.311 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=35). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9678 sube el IC de +0.283 a +0.378 en UPDOWN_GBM_IBS_ALTO (n=72). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9353 sube el IC de +0.258 a +0.341 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=61). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8606 sube el IC de +0.311 a +0.338 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=66). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7117 sube el IC de +0.286 a +0.345 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=108). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9942 sube el IC de +0.259 a +0.258 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7363 sube el IC de +0.259 a +0.288 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7853 sube el IC de +0.317 a +0.427 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=39). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#DOGE#5min` — IC=+0.118 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#DOGE` — IC=+0.118 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL#5min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 542 | +0.068 | +40.77€ | 3 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 542 | +0.068 | +40.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 298 | +0.083 | +29.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 298 | +0.083 | +29.77€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 5149 | -0.104 | -549.90€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 585 | -0.084 | -109.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 4564 | -0.107 | -440.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 637 | -0.101 | -85.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 637 | -0.101 | -85.60€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 585 | -0.084 | -109.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 585 | -0.084 | -109.26€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 359 | -0.137 | -154.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 359 | -0.137 | -154.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 1582 | -0.023 | +34.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 1582 | -0.023 | +34.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1261 | -0.189 | -195.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1261 | -0.189 | -195.60€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 22389 | +0.113 | -1566.39€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 4527 | +0.184 | -182.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 106 | -0.102 | -48.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 14881 | +0.091 | -1314.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2875 | +0.125 | -20.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 2505 | +0.061 | -448.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 17 | -0.067 | -0.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 2483 | +0.063 | -442.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 4782 | +0.134 | -107.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1255 | +0.191 | -84.73€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 2475 | +0.109 | -64.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1010 | +0.135 | +63.43€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 2508 | +0.068 | -387.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 16 | +0.044 | -1.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 2491 | +0.068 | -384.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 5156 | +0.129 | -68.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1660 | +0.169 | -5.97€ | 0 | 8 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 2475 | +0.112 | -39.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1009 | +0.107 | -14.94€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 4934 | +0.125 | -408.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1565 | +0.199 | -90.05€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 45 | +0.011 | -8.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 2468 | +0.077 | -240.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 856 | +0.133 | -69.18€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 2504 | +0.115 | -144.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 14 | +0.000 | -0.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 2489 | +0.116 | -142.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4592 | +0.174 | -346.95€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 4592 | +0.174 | -346.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1151 | +0.170 | -121.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1151 | +0.170 | -121.88€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 97 | -0.106 | +2.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 97 | -0.106 | +2.41€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1146 | +0.163 | -134.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1146 | +0.163 | -134.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1027 | +0.227 | -34.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1027 | +0.227 | -34.41€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1092 | +0.194 | -72.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1092 | +0.194 | -72.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 230 | +0.431 | -4.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 230 | +0.431 | -4.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 81 | +0.428 | -1.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 81 | +0.428 | -1.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 89 | +0.412 | -4.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 89 | +0.412 | -4.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 57 | +0.432 | +0.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 57 | +0.432 | +0.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 10630 | +0.197 | -906.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 10630 | +0.197 | -906.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1965 | +0.126 | -368.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1965 | +0.126 | -368.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1643 | +0.240 | -32.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1643 | +0.240 | -32.94€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1844 | +0.160 | -251.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1844 | +0.160 | -251.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1686 | +0.238 | -37.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1686 | +0.238 | -37.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1699 | +0.231 | -60.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1699 | +0.231 | -60.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1793 | +0.198 | -154.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1793 | +0.198 | -154.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3813 | +0.130 | +66.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 3813 | +0.130 | +66.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1896 | +0.142 | +76.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1896 | +0.142 | +76.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1917 | +0.117 | -9.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1917 | +0.117 | -9.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 651 | +0.298 | +2.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 651 | +0.298 | +2.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 276 | +0.273 | -9.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 276 | +0.273 | -9.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 302 | +0.296 | +3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 302 | +0.296 | +3.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 73 | +0.380 | +9.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 73 | +0.380 | +9.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 270 | +0.408 | -14.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 270 | +0.408 | -14.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 119 | +0.409 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 119 | +0.409 | -5.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 122 | +0.403 | -9.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 122 | +0.403 | -9.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 29 | +0.371 | +0.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 29 | +0.371 | +0.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 92 | +0.117 | +1.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 28 | +0.167 | +3.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 64 | +0.091 | -1.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 5 | +0.054 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 5 | +0.054 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 74 | +0.105 | +0.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 10 | +0.083 | +1.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 64 | +0.091 | -1.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 13 | +0.065 | -0.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 13 | +0.065 | -0.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 2578 | +0.101 | -102.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 267 | +0.028 | -29.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 2311 | +0.110 | -72.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 1771 | +0.094 | -71.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 267 | +0.028 | -29.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 1504 | +0.106 | -41.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 807 | +0.117 | -31.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 807 | +0.117 | -31.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 335 | +0.277 | -25.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 335 | +0.277 | -25.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 335 | +0.277 | -25.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 335 | +0.277 | -25.22€ | 0 | 4 |
| ✅ GBM_LATE_15M | 5857 | +0.057 | +1912.95€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 5857 | +0.057 | +1912.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 843 | +0.176 | +534.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 843 | +0.176 | +534.73€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 757 | +0.168 | +406.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 757 | +0.168 | +406.64€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 853 | +0.191 | +587.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 853 | +0.191 | +587.35€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 881 | -0.048 | +4.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 881 | -0.048 | +4.96€ | 3 | 3 |
| ✅ GBM_LATE_15M#SOL | 1112 | -0.030 | +155.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1112 | -0.030 | +155.84€ | 3 | 4 |
| ✅ GBM_LATE_15M#XRP | 1411 | -0.023 | +223.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1411 | -0.023 | +223.42€ | 3 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 6815 | +0.045 | +2594.16€ | 0 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 6815 | +0.045 | +2594.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1126 | -0.028 | +510.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1126 | -0.028 | +510.46€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1431 | -0.034 | +150.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1431 | -0.034 | +150.42€ | 0 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 717 | +0.241 | +658.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 717 | +0.241 | +658.57€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1196 | -0.038 | +25.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1196 | -0.038 | +25.97€ | 7 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1225 | -0.002 | +262.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1225 | -0.002 | +262.46€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1120 | +0.230 | +986.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1120 | +0.230 | +986.29€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 4501 | +0.172 | +3092.82€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 4501 | +0.172 | +3092.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 634 | +0.193 | +466.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 634 | +0.193 | +466.11€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 715 | +0.170 | +467.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 715 | +0.170 | +467.49€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 630 | +0.201 | +486.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 630 | +0.201 | +486.64€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 691 | +0.174 | +460.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 691 | +0.174 | +460.23€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 865 | +0.108 | +460.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 865 | +0.108 | +460.62€ | 1 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 966 | +0.197 | +751.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 966 | +0.197 | +751.72€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 694 | +0.069 | +103.61€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 694 | +0.069 | +103.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 146 | +0.095 | +36.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 146 | +0.095 | +36.92€ | 2 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 149 | +0.162 | +44.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 149 | +0.162 | +44.92€ | 1 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 250 | +0.004 | +8.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 250 | +0.004 | +8.20€ | 4 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 5235 | +0.163 | +3359.77€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#15min | 5235 | +0.163 | +3359.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 807 | +0.182 | +553.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 807 | +0.182 | +553.90€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 828 | +0.155 | +499.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 828 | +0.155 | +499.10€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 798 | +0.216 | +655.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 798 | +0.216 | +655.60€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 681 | +0.134 | +352.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 681 | +0.134 | +352.61€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 897 | +0.086 | +403.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 897 | +0.086 | +403.22€ | 0 | 16 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1224 | +0.192 | +895.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1224 | +0.192 | +895.33€ | 0 | 25 |
| ✅ GBM_LATE_5M | 568 | +0.117 | +233.65€ | 1 | 19 |
| ✅ GBM_LATE_5M#5min | 568 | +0.117 | +233.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 217 | +0.116 | +105.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 217 | +0.116 | +105.17€ | 2 | 13 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 135 | +0.179 | +69.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 135 | +0.179 | +69.23€ | 0 | 18 |
| ✅ GBM_LATE_5M#SOL | 82 | -0.012 | +5.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 82 | -0.012 | +5.72€ | 1 | 1 |
| ✅ GBM_LATE_5M#XRP | 121 | +0.167 | +57.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 121 | +0.167 | +57.95€ | 0 | 0 |
| ✅ GBM_LATE_60M | 501 | -0.045 | +74.00€ | 4 | 8 |
| ✅ GBM_LATE_60M#60min | 501 | -0.045 | +74.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 173 | -0.003 | +5.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 173 | -0.003 | +5.67€ | 3 | 3 |
| ✅ GBM_LATE_60M#ETH | 177 | -0.020 | +44.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 177 | -0.020 | +44.02€ | 2 | 8 |
| ✅ GBM_LATE_60M#SOL | 151 | -0.121 | +24.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 151 | -0.121 | +24.30€ | 3 | 2 |
| 🚫 GBM_LATE_60M_FADE | 193 | -0.305 | -34.48€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 193 | -0.305 | -34.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 311 | +0.040 | +5.51€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 311 | +0.040 | +5.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 121 | +0.012 | +3.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 121 | +0.012 | +3.09€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 74 | +0.092 | +5.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 74 | +0.092 | +5.73€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 177 | +0.103 | +37.75€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 177 | +0.103 | +37.75€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 177 | +0.103 | +37.75€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 177 | +0.103 | +37.75€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M | 211 | -0.106 | -28.10€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 211 | -0.106 | -28.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 51 | -0.104 | -7.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 51 | -0.104 | -7.11€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 43 | -0.011 | -1.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 43 | -0.011 | -1.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 316 | -0.104 | -39.22€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 316 | -0.104 | -39.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 10 | -0.083 | -2.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 10 | -0.083 | -2.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 67 | -0.138 | -10.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 67 | -0.138 | -10.52€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 29 | -0.048 | -1.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 29 | -0.048 | -1.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 96 | -0.061 | -9.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 96 | -0.061 | -9.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 73 | -0.087 | -7.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 73 | -0.087 | -7.27€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 41 | -0.174 | -8.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 41 | -0.174 | -8.01€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 350 | +0.000 | -4.26€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 350 | +0.000 | -4.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 110 | -0.018 | -8.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 110 | -0.018 | -8.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 115 | -0.021 | -2.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 115 | -0.021 | -2.26€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 125 | +0.035 | +6.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 125 | +0.035 | +6.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 2368 | +0.008 | -19.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 2368 | +0.008 | -19.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 219 | +0.025 | +15.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 219 | +0.025 | +15.34€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M#BTC | 436 | +0.027 | +2.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 436 | +0.027 | +2.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 351 | -0.001 | -16.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 351 | -0.001 | -16.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 461 | +0.008 | +13.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 461 | +0.008 | +13.74€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 439 | +0.006 | -16.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 439 | +0.006 | -16.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 462 | -0.009 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 462 | -0.009 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 3482 | -0.032 | +103.07€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 3482 | -0.032 | +103.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 546 | -0.038 | +61.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 546 | -0.038 | +61.57€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 630 | -0.025 | -14.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 630 | -0.025 | -14.54€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 552 | -0.033 | +71.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 552 | -0.033 | +71.57€ | 4 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 625 | -0.021 | -7.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 625 | -0.021 | -7.78€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 560 | -0.050 | +4.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 560 | -0.050 | +4.79€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 569 | -0.025 | -12.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 569 | -0.025 | -12.55€ | 5 | 2 |
| ✅ MOMENTUM_IBS_15M_FADE | 553 | -0.059 | -40.99€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 553 | -0.059 | -40.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 66 | -0.059 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 66 | -0.059 | -4.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 34 | -0.083 | -3.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 34 | -0.083 | -3.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 1500 | +0.011 | +15.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 1500 | +0.011 | +15.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 295 | +0.042 | +19.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 295 | +0.042 | +19.78€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#SOL | 580 | +0.015 | +6.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 580 | +0.015 | +6.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 9289 | -0.071 | +184.77€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 9289 | -0.071 | +184.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 1393 | -0.106 | +94.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 1393 | -0.106 | +94.99€ | 9 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 1734 | -0.056 | +61.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 1734 | -0.056 | +61.58€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 1448 | -0.077 | +44.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 1448 | -0.077 | +44.95€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 1477 | -0.090 | -100.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 1477 | -0.090 | -100.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 1719 | -0.047 | +26.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 1719 | -0.047 | +26.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 1518 | -0.058 | +57.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 1518 | -0.058 | +57.06€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 5866 | -0.008 | -103.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 5866 | -0.008 | -103.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1059 | +0.014 | +0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1059 | +0.014 | +0.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1000 | -0.019 | -29.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1000 | -0.019 | -29.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 319 | +0.073 | +50.95€ | 1 | 2 |
| ✅ ORDER_FLOW_5M#5min | 183 | +0.084 | +38.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 53 | +0.100 | +17.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 53 | +0.100 | +17.67€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 32 | +0.118 | +10.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 32 | +0.118 | +10.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 21 | +0.022 | +1.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 21 | +0.022 | +1.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 37 | +0.090 | +5.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 37 | +0.090 | +5.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 40 | +0.048 | +3.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 40 | +0.048 | +3.29€ | 0 | 1 |
| ✅ PRICE_TARGET_GBM | 233 | -0.155 | -17.39€ | 2 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 99 | -0.213 | -27.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 86 | -0.227 | -24.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 92 | -0.149 | -4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 76 | -0.154 | -5.11€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 16 | -0.089 | +0.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 199 | -0.157 | -13.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 34 | -0.139 | -3.50€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 139 | -0.216 | -3.07€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 59 | -0.156 | +2.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 57 | -0.144 | +3.58€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 60 | -0.242 | -9.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 57 | -0.229 | -6.57€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 20 | -0.273 | +3.48€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 19 | -0.249 | +3.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 133 | -0.204 | +1.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 6 | -0.113 | -4.08€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 49 | +0.245 | +6.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 17 | +0.380 | +8.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 17 | +0.380 | +8.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 49 | +0.245 | +6.70€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 107 | -0.060 | -16.51€ | 6 | 0 |
| ✅ STREAK_FADE_15M#15min | 107 | -0.060 | -16.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 46 | -0.021 | -6.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 46 | -0.021 | -6.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 7 | -0.019 | -0.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 7 | -0.019 | -0.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 9 | +0.021 | -0.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 9 | +0.021 | -0.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 45 | -0.117 | -9.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 45 | -0.117 | -9.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 645 | -0.001 | -18.87€ | 1 | 1 |
| ✅ STREAK_FADE_5M#5min | 645 | -0.001 | -18.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 218 | +0.018 | +0.69€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 218 | +0.018 | +0.69€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 211 | +0.007 | -4.14€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 211 | +0.007 | -4.14€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 84 | -0.023 | -7.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 84 | -0.023 | -7.19€ | 3 | 1 |
| ✅ STREAK_FADE_5M#XRP | 132 | -0.030 | -8.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 132 | -0.030 | -8.23€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 22 | -0.083 | -2.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 22 | -0.083 | -2.34€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 8 | +0.040 | +0.87€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 8 | +0.040 | +0.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 1189 | +0.016 | +5.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 1189 | +0.016 | +5.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 407 | +0.016 | -0.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 407 | +0.016 | -0.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 199 | +0.003 | -1.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 199 | +0.003 | -1.03€ | 2 | 1 |
| ✅ STREAK_MOM_5M#SOL | 354 | +0.006 | -4.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 354 | +0.006 | -4.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 229 | +0.045 | +10.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 229 | +0.045 | +10.49€ | 2 | 3 |
| ✅ STRUCT_NO_15M | 2500 | +0.003 | -35.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 2500 | +0.003 | -35.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 969 | +0.002 | -16.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 969 | +0.002 | -16.09€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 956 | +0.009 | -7.87€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 956 | +0.009 | -7.87€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 575 | -0.004 | -11.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 575 | -0.004 | -11.49€ | 2 | 0 |
| ✅ UPDOWN_GBM | 3939 | +0.013 | +150.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1623 | +0.051 | +171.73€ | 0 | 8 |
| ✅ UPDOWN_GBM#240min | 176 | +0.028 | +4.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 1788 | -0.016 | -31.30€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 305 | +0.005 | +5.60€ | 4 | 1 |
| ✅ UPDOWN_GBM#BNB | 162 | +0.073 | +25.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 150 | +0.099 | +28.56€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 794 | +0.025 | +55.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 174 | +0.080 | +20.41€ | 4 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 52 | +0.111 | +8.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 449 | +0.012 | +27.03€ | 1 | 2 |
| ✅ UPDOWN_GBM#BTC#60min | 101 | -0.024 | -2.91€ | 1 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 474 | +0.015 | +9.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 90 | +0.098 | +21.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 381 | -0.006 | -12.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 879 | +0.027 | +37.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 412 | +0.051 | +33.21€ | 1 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 53 | +0.082 | +4.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 271 | -0.013 | -7.65€ | 4 | 1 |
| ✅ UPDOWN_GBM#ETH#60min | 128 | +0.038 | +8.50€ | 1 | 3 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 882 | -0.014 | -18.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 352 | -0.006 | -9.03€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 40 | -0.048 | -4.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 402 | -0.010 | -5.33€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 76 | -0.013 | +0.01€ | 1 | 1 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 746 | +0.000 | +42.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 445 | +0.057 | +76.75€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 25 | -0.130 | -4.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 276 | -0.079 | -30.11€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 143 | +0.286 | +11.17€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 143 | +0.286 | +11.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 85 | +0.259 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 85 | +0.259 | -0.87€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 58 | +0.317 | +12.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 58 | +0.317 | +12.05€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 2622 | -0.082 | +410.59€ | 4 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 2622 | -0.082 | +410.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 209 | -0.088 | +115.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 209 | -0.088 | +115.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 545 | -0.151 | -36.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 545 | -0.151 | -36.86€ | 4 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 61 | +0.024 | +4.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 61 | +0.024 | +4.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 168 | +0.024 | +32.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 168 | +0.024 | +32.41€ | 1 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 841 | -0.062 | +190.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 841 | -0.062 | +190.21€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 798 | -0.083 | +104.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 798 | -0.083 | +104.80€ | 7 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 17 | -0.067 | -2.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 17 | -0.067 | -2.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 17 | -0.067 | -2.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 17 | -0.067 | -2.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 210 | +0.283 | +144.44€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 210 | +0.283 | +144.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 122 | +0.258 | +69.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 122 | +0.258 | +69.99€ | 0 | 15 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 88 | +0.311 | +74.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 88 | +0.311 | +74.45€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 368 | -0.062 | -28.63€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 368 | -0.062 | -28.63€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 233 | -0.006 | -11.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 233 | -0.006 | -11.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 23 | +0.020 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 23 | +0.020 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 26 | -0.179 | -5.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 26 | -0.179 | -5.17€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 993 | +0.287 | +396.85€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 295 | +0.200 | +2.11€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 312 | +0.258 | +69.34€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 386 | +0.374 | +325.39€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.101) — sin ventaja clara. oversold(IBS<0.3): IC=-0.009 n=1341 | neutral: IC=+0.012 n=1415 | overbought(IBS>0.7): IC=+0.093 n=1623
  - _Datos_: n=4626 IC=+0.035 PNL=+350.77€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 3 celda(s) pasan gate riguroso completo de 124 evaluadas (n>=40) y 445 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.006 < 0.08 — monitorear
  - _Datos_: n=352 IC=-0.006 PNL=-9.03€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=312/15 IC=+0.258 PNL=+69.34€ | BTC: n=295/15 IC=+0.200 PNL=+2.11€ | SOL: n=386/15 IC=+0.374 PNL=+325.39€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.086 n=65226 | tras_1loss IC=+0.046 n=49522 | tras_2loss IC=+0.008 n=22451/40 | gap=+0.077 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 17 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 3877 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.155 n=27/60 | contraria IC=-0.022 n=15 | gap=+0.177 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=36, boost estimado=+0.004. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 37/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=128/40 IC=+0.038 PNL=+8.50€ | BTC#60min: n=101/40 IC=-0.024 PNL=-2.91€ | SOL#60min: n=76/40 IC=-0.013 PNL=+0.01€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.007 n=351 | contrario_BTC IC=+0.014 n=278/40 | gap=+0.021 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.08 con n=65 PNL=+32.96€
  - _Datos_: n=65 IC=+0.172 PNL=+32.96€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.08 con n=79 PNL=+17.43€
  - _Datos_: n=79 IC=+0.117 PNL=+17.43€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 8/25 ops en el filtro definido (IC actual=+0.160 PNL=+9.98€)
  - _Datos_: n=8 IC=+0.160 PNL=+9.98€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.337 > 0.1 con n=843 PNL=+402.22€
  - _Datos_: n=843 IC=+0.337 PNL=+402.22€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=31 IC=+0.015 PNL=+8.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=31 IC=+0.015 PNL=+8.66€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 12/30 ops en el filtro definido (IC actual=+0.043 PNL=+0.77€)
  - _Datos_: n=12 IC=+0.043 PNL=+0.77€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=3702 IC=+0.007 PNL=+97.25€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=3702 IC=+0.007 PNL=+97.25€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 1/15 ops en el filtro definido (IC actual=+0.008 PNL=+1.22€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.22€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=245 IC=+0.030 PNL=+12.47€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=245 IC=+0.030 PNL=+12.47€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=60 IC=-0.097 PNL=-6.87€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=60 IC=-0.097 PNL=-6.87€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=66 IC=+0.015 PNL=+2.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=66 IC=+0.015 PNL=+2.31€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.1 con n=461 PNL=+89.43€
  - _Datos_: n=461 IC=+0.109 PNL=+89.43€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=167 IC=+0.092 PNL=+43.27€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=167 IC=+0.092 PNL=+43.27€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=174 IC=+0.080 PNL=+20.41€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=174 IC=+0.080 PNL=+20.41€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=981 IC=+0.042 PNL=+71.63€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=981 IC=+0.042 PNL=+71.63€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 16/30 ops en el filtro definido (IC actual=-0.178 PNL=-2.92€)
  - _Datos_: n=16 IC=-0.178 PNL=-2.92€

**🟡 H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=43 PNL=+15.07€
  - _Datos_: n=43 IC=+0.100 PNL=+15.07€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=50 IC=+0.077 PNL=+8.77€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=50 IC=+0.077 PNL=+8.77€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.000 PNL=-0.05€)
  - _Datos_: n=4 IC=+0.000 PNL=-0.05€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=1009 IC=-0.029 PNL=-44.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1009 IC=-0.029 PNL=-44.35€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=33 PNL=+9.78€
  - _Datos_: n=33 IC=+0.214 PNL=+9.78€

**⏳ H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: 30
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: 4/30 ops en el filtro definido (IC actual=+0.067 PNL=+2.07€)
  - _Datos_: n=4 IC=+0.067 PNL=+2.07€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1051 IC=+0.030 PNL=+78.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1051 IC=+0.030 PNL=+78.48€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=382 IC=+0.026 PNL=-4.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=382 IC=+0.026 PNL=-4.01€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.08 con n=54 PNL=+16.29€
  - _Datos_: n=54 IC=+0.125 PNL=+16.29€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.144 > 0.08 con n=99 PNL=-3.22€
  - _Datos_: n=99 IC=+0.144 PNL=-3.22€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=98 PNL=+24.62€
  - _Datos_: n=98 IC=+0.110 PNL=+24.62€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=571 IC=+0.144 PNL=+1.44€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=571 IC=+0.144 PNL=+1.44€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=547 IC=+0.025 PNL=+34.69€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=547 IC=+0.025 PNL=+34.69€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.02 con n=164 PNL=+50.59€
  - _Datos_: n=164 IC=+0.139 PNL=+50.59€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=87 IC=-0.129 PNL=+13.53€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=87 IC=-0.129 PNL=+13.53€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.442 > 0.1 con n=551 PNL=+447.31€
  - _Datos_: n=551 IC=+0.442 PNL=+447.31€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1185 IC=+0.032 PNL=+73.48€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1185 IC=+0.032 PNL=+73.48€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.1 con n=668 PNL=+232.01€
  - _Datos_: n=668 IC=+0.157 PNL=+232.01€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 14/40 ops en el filtro definido (IC actual=-0.219 PNL=-4.47€)
  - _Datos_: n=14 IC=-0.219 PNL=-4.47€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=316 IC=+0.044 PNL=+41.00€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=316 IC=+0.044 PNL=+41.00€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**⏳ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: 50
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: 49/50 ops en el filtro definido (IC actual=+0.069 PNL=-0.23€)
  - _Datos_: n=49 IC=+0.069 PNL=-0.23€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=2712 IC=-0.114 PNL=+393.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2712 IC=-0.114 PNL=+393.11€

**⏳ H-CUSTOM-LATE15-PHOTO-FINISH** — GBM_LATE_15M photo finish — entrar pegado al strike es moneda al aire cobrada como favorito
  - _Hipótesis_: Detectado 2026-07-05 validando contra nuestros datos la única idea aprovechable de un artículo-anuncio de copy-bot: GBM_LATE_15M con |drift_ventana_pct|<0.02 tenía IC=-0.145 n=181 (win 35%, -9.70€), estable en ambas mitades temporales (-0.163/-0.127), monótono con la distancia (0.02-0.05: IC=+0.061; ≥0.05: IC=+0.14..0.19) y consistente en crudo y normalizado por sigma (|d_gbm|<0.1 IC=-0.081 n=244). BTC (IC=-0.163 n=90) y ETH (-0.130 n=79) concentraban el daño; SOL/XRP apenas entran en esa zona. Mecanismo: sin distancia real al strike el resultado es ~50/50 pero py_entrada ya cobra favorito. Filtro GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict el 2026-07-05. Esta hipótesis trackea la zona filtrada: si vuelven a aparecer ops aquí, el filtro se ha roto.
  - _Umbral_: 200
  - _Acción_: Si aparecen ops nuevas en la zona → el filtro está roto, revisar shadow_predict. Si el buffer [0.02,0.05) se vuelve negativo con n≥60 forward → subir el corte a 0.05.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=462 IC=+0.134 PNL=+167.19€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=462 IC=+0.134 PNL=+167.19€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.08 con n=461 PNL=+89.43€
  - _Datos_: n=461 IC=+0.109 PNL=+89.43€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=398 IC=+0.000 PNL=+3.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=398 IC=+0.000 PNL=+3.19€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=487 PNL=+293.14€
  - _Datos_: n=487 IC=+0.099 PNL=+293.14€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.142 > 0.08 con n=118 PNL=+23.93€
  - _Datos_: n=118 IC=+0.142 PNL=+23.93€

**⏳ H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: 289
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: 233/289 ops en el filtro definido (IC actual=-0.223 PNL=-14.05€)
  - _Datos_: n=233 IC=-0.223 PNL=-14.05€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=854 IC=+0.158 PNL=+480.31€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=854 IC=+0.158 PNL=+480.31€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 17/40 ops en el filtro definido (IC actual=+0.022 PNL=-1.83€)
  - _Datos_: n=17 IC=+0.022 PNL=-1.83€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=469 IC=-0.035 PNL=+13.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=469 IC=-0.035 PNL=+13.06€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=414 PNL=+227.01€
  - _Datos_: n=414 IC=+0.180 PNL=+227.01€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=754 IC=-0.015 PNL=+138.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=754 IC=-0.015 PNL=+138.58€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=199 PNL=-24.97€
  - _Datos_: n=199 IC=+0.122 PNL=-24.97€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.244 > 0.08 con n=1000 PNL=-95.47€
  - _Datos_: n=1000 IC=+0.244 PNL=-95.47€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 7/40 ops en el filtro definido (IC actual=+0.019 PNL=+3.02€)
  - _Datos_: n=7 IC=+0.019 PNL=+3.02€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.087 n=90) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=90 IC=+0.087 PNL=+10.93€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.08 con n=59 PNL=+45.57€
  - _Datos_: n=59 IC=+0.336 PNL=+45.57€

**⏳ H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: 200
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: 198/200 ops en el filtro definido (IC actual=+0.440 PNL=+265.93€)
  - _Datos_: n=198 IC=+0.440 PNL=+265.93€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=1965 IC=+0.126 PNL=-368.22€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=1965 IC=+0.126 PNL=-368.22€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 23/40 ops en el filtro definido (IC actual=+0.260 PNL=+18.39€)
  - _Datos_: n=23 IC=+0.260 PNL=+18.39€
