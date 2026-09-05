# Hipótesis automáticas — 2026-09-05 00:34 UTC
_Generado por shadow_postmortem.py sobre 288333 resoluciones (PNL=+28203.96€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.465` → IC=-0.172 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=346)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=297)

- **PATRÓN** `py_entrada` > `0.465` → IC=+0.253 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.465 (IC base=+0.147)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.153 (n=318)

  - _Acción_: Kelly boost +0.77€ cuando `n_ballena_banda` > 19.0 (IC base=+0.147)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.244 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.147)

- **PATRÓN** `banda_hit_calibrado` > `0.6181` → IC=+0.246 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6181 (IC base=+0.147)

- **PATRÓN** `banda_z` > `11.589` → IC=+0.269 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.589 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=360)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3120.8362` → IC=+0.185 (n=157)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3120.8362 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.139 (n=297)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.5 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 124.0 (IC base=+0.024)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.131 (n=82)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.273 (n=249)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=169)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=194)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.273 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=+0.173)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.178 (n=253)

  - _Acción_: Kelly boost +0.89€ cuando `n_ballena_banda` > 18.0 (IC base=+0.173)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.241 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.173)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.274 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.173)

- **PATRÓN** `banda_z` > `11.678` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.678 (IC base=+0.173)

- **PATRÓN** `ballenas_wallet_edge_medio` > `3.339` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `ballenas_wallet_edge_medio` > 3.339 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=280)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2988.1169` → IC=+0.184 (n=166)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2988.1169 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.132 (n=169)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 99.0 (IC base=+0.011)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=93)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.238 (n=82)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=97)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.085)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.085)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.36` → IC=-0.300 (n=3871)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.36
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=11621)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `133.05` → IC=-0.328 (n=514)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.05
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1544)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `626.73` → IC=-0.152 (n=331)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 626.73
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=645)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.55` → IC=-0.404 (n=516)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.55
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=1550)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `144.73` → IC=-0.311 (n=859)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.73
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=2577)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `158.35` → IC=-0.378 (n=931)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.35
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=1895)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=8207)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=2089)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2367.8896` → IC=+0.168 (n=2006)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2367.8896 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.145 (n=5035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=6773)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.255 (n=5116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.182 (n=4000)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `1943.5814` → IC=+0.174 (n=3422)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1943.5814 (IC base=+0.140)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.217 (n=892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.375 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `14488.4893` → IC=+0.222 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14488.4893 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.201 (n=866)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.259 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=1213)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `12559.4301` → IC=+0.209 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12559.4301 (IC base=+0.190)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.121 (n=576)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 15.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` > `0.595` → IC=+0.167 (n=298)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.595 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `4800.0243` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4800.0243 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.181 (n=340)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.41 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4140.4788` → IC=+0.153 (n=324)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4140.4788 (IC base=+0.130)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=98)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1422)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.310 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.263 (n=739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` < `0.2` → IC=+0.404 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.2 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.261 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1944.5824` → IC=+0.265 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1944.5824 (IC base=+0.258)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.139 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=350)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.259 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=475)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `1512.3969` → IC=+0.158 (n=393)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1512.3969 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.164 (n=144)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.216 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.426 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=815)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.348 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `933.731` → IC=+0.206 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 933.731 (IC base=+0.201)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.335 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=172)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `3436.2112` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3436.2112 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.226 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=295)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **FILTRO** `libro_liquidez` < `11360.7096` → IC=-0.266 (n=143)

  - _Acción_: SKIP cuando `libro_liquidez` < 11360.7096
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=6396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=5376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.202 (n=3045)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3332.6237` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3332.6237 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=1390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=1644)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.164)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.317)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.354 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.317)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.176 (n=1543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.178 (n=1355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=1651)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.183 (n=1089)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.72 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=1222)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.313 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.236)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=1327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.191 (n=810)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.7 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.184 (n=669)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.73 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.450 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.442 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.481 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.441 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2032.8407` → IC=+0.449 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2032.8407 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.450 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.942` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.942 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `10987.7492` → IC=+0.463 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10987.7492 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.448 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `2106.7117` → IC=+0.450 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2106.7117 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.426 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` < `0.932` → IC=+0.423 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.932 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `libro_liquidez` < `6196.1698` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 6196.1698
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=6685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.209 (n=18226)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=3545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.152 (n=3147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 15.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.182 (n=2700)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.72 (IC base=+0.151)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=3157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=1160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.272 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.179 (n=1168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=3158)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.164)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=1621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=1182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.237 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=3027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=2364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.206 (n=3064)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=2590)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `4.0` → IC=+0.140 (n=2419)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 4.0 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.159 (n=2424)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.94 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.148 (n=3525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `3.87` → IC=+0.159 (n=2418)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 3.87 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.209 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.136)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.147 (n=1206)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` < 3.95 (IC base=+0.136)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.150 (n=1671)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.160 (n=1739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 8.0 (IC base=+0.136)

- **PATRÓN** `lag_apertura_s` < `6.9` → IC=+0.149 (n=1585)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 6.9 (IC base=+0.136)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=1292)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.125)

- **PATRÓN** `restante_min` < `4.44` → IC=+0.132 (n=1610)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.44 (IC base=+0.125)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.169 (n=1231)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` > 4.95 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=3672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.135 (n=1786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.169 (n=1220)

  - _Acción_: Kelly boost +0.85€ cuando `lag_apertura_s` < 3.28 (IC base=+0.125)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.313 (n=657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.291 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.368 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.291 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1752.2159` → IC=+0.294 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1752.2159 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.298 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.277 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5512.6115` → IC=+0.296 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5512.6115 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.337 (n=243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.377 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1547.5346` → IC=+0.316 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1547.5346 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.327 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.321)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.348 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.321)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.321)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.321)

- **PATRÓN** `libro_liquidez` > `662.0852` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 662.0852 (IC base=+0.321)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.433 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.428 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.434 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.424 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `1987.6172` → IC=+0.436 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1987.6172 (IC base=+0.424)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.432 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.422 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `5459.2656` → IC=+0.460 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5459.2656 (IC base=+0.421)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.436 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.426 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.426 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `1978.9685` → IC=+0.460 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9685 (IC base=+0.429)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `py_entrada` > `0.93` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.365)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.316 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.260)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.412 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.280 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1362.9219` → IC=+0.287 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1362.9219 (IC base=+0.260)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.316 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.260)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.412 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.280 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1362.9219` → IC=+0.287 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1362.9219 (IC base=+0.260)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.3616` → IC=+0.130 (n=3861)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.3616 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.4801` → IC=+0.228 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4801 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.651` → IC=+0.151 (n=1473)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.651 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.6258` → IC=+0.230 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6258 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.0825` → IC=+0.246 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0825 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.171` → IC=+0.181 (n=670)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.171 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `2.8467` → IC=+0.179 (n=2338)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.8467 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `1.4731` → IC=+0.175 (n=2339)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4731 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.4017` → IC=+0.129 (n=3697)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.4017 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.342` → IC=+0.147 (n=1383)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.342 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.6855` → IC=+0.149 (n=582)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6855 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.0462` → IC=+0.144 (n=600)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0462 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3026` → IC=+0.238 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3026 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.8121` → IC=+0.215 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8121 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.209 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.042)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.183 (n=392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.007 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2892` → IC=+0.157 (n=861)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2892 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.193 (n=405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.685` → IC=+0.295 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.685 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.6455` → IC=+0.141 (n=763)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.6455 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.4431` → IC=+0.146 (n=763)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4431 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=709)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.185 (n=510)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 64.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.258 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.271 (n=523)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0819` → IC=+0.318 (n=196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0819 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.260 (n=536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.266 (n=587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4059` → IC=+0.281 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4059 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.485` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.485 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.215` → IC=+0.272 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.215 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0688` → IC=+0.255 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0688 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7975` → IC=+0.312 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7975 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.265 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1713.22` → IC=+0.278 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1713.22 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.256 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=+0.255)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.256 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.219 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.2114` → IC=+0.235 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2114 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9263` → IC=+0.244 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9263 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1834` → IC=+0.219 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1834 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.4864` → IC=+0.221 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4864 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.217` → IC=+0.227 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.217 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.068` → IC=+0.217 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.068 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.6988` → IC=+0.230 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6988 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.231 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.0971` → IC=+0.220 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0971 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4783` → IC=+0.247 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4783 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `11046.4069` → IC=+0.239 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11046.4069 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.148 (n=736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0061 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.146 (n=659)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.003 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1753` → IC=+0.149 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1753 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.145 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6598` → IC=+0.168 (n=736)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6598 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.3411` → IC=+0.159 (n=720)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.3411 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.496` → IC=+0.222 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.496 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.613` → IC=+0.169 (n=246)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.613 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0641` → IC=+0.212 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0641 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.725` → IC=+0.158 (n=419)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.725 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.3961` → IC=+0.157 (n=628)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.3961 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `12653.1063` → IC=+0.153 (n=491)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 12653.1063 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.176 (n=183)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 214.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.202 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.195 (n=392)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.338` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.338 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.1342` → IC=+0.160 (n=701)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1342 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.8668` → IC=+0.159 (n=731)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 3.8668 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.6803` → IC=+0.174 (n=731)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.6803 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.188 (n=854)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.192 (n=501)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 47.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.245 (n=665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.3852` → IC=+0.237 (n=584)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3852 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0315` → IC=+0.295 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0315 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.771` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.771 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3749` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3749 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.6995` → IC=+0.243 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6995 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `3.1205` → IC=+0.225 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1205 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.230 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.235)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.137 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=565)

- **FILTRO** `ibs_20min` > `0.8223` → IC=-0.179 (n=300)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8223
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=901)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1129)

- **PATRÓN** `dist_vwap_pct` < `0.1402` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1402 (IC base=-0.029)

- **PATRÓN** `volumen_regimen` < `0.6119` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6119 (IC base=-0.029)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1153` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1153 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2279` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2279 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4376` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4376 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.9125` → IC=+0.286 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9125 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 177.0 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.2895` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2895 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0689` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0689 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` > `1.8023` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8023 (IC base=-0.038)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=150)

- **FILTRO** `ibs_20min` < `0.28` → IC=-0.172 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=128)

- **FILTRO** `sigma_ewma_delta_pct` > `8.345` → IC=-0.191 (n=208)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.345
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1611)

- **FILTRO** `volumen_pendiente_norm` < `0.1097` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1097
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=26)

- **FILTRO** `volumen_spike_ratio` > `1.4181` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4181
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=16)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.180 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.047)

- **PATRÓN** `ibs_20min` > `0.28` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.28 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.6372` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6372 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.7744` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7744 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.6091` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6091 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `2.1624` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1624 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4181` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4181 (IC base=-0.059)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5168` → IC=-0.163 (n=366)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5168
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=712)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.202 (n=129)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=949)

- **FILTRO** `ibs_20min` > `0.7882` → IC=-0.193 (n=431)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7882
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1295)

- **FILTRO** `sigma_ewma_delta_pct` > `9.004` → IC=-0.138 (n=197)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.004
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1529)

- **PATRÓN** `dist_vwap_pct` > `0.5913` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5913 (IC base=-0.099)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=-0.099)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.066` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.066 (IC base=-0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.4974` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4974 (IC base=-0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.099)

- **PATRÓN** `dist_vwap_pct` < `0.2538` → IC=+0.219 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2538 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` > `1.295` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.295 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2503` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2503 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.3188` → IC=+0.198 (n=117)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.3188 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` > `1.8998` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8998 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 21.0 (IC base=-0.048)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.174 (n=1587)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0094 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.3007` → IC=+0.146 (n=4758)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.3007 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `1.2307` → IC=+0.294 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2307 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.476` → IC=+0.123 (n=2519)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.476 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `0.6792` → IC=+0.221 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6792 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.251` → IC=+0.243 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.251 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.4852` → IC=+0.233 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4852 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.293 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.5848` → IC=+0.131 (n=4594)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5848 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.7976` → IC=+0.247 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7976 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.2281` → IC=+0.221 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2281 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2233` → IC=+0.251 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2233 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2567` → IC=+0.338 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2567 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.8088` → IC=+0.280 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8088 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.268 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.053)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.149 (n=397)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=808)

- **FILTRO** `sigma_ewma_delta_pct` > `2.449` → IC=-0.157 (n=351)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.449
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=769)

- **PATRÓN** `ibs_20min` > `0.8378` → IC=+0.224 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8378 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.112` → IC=+0.128 (n=452)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.112 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.9049` → IC=+0.233 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9049 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.4735` → IC=+0.229 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4735 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.330 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8608` → IC=-0.158 (n=396)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8608
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1192)

- **PATRÓN** `volumen_spike_ratio` < `2.0452` → IC=+0.125 (n=310)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.0452 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `261.0` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 261.0 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.123` → IC=+0.167 (n=184)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.123 (IC base=-0.024)

- **PATRÓN** `volumen_regimen` < `0.8238` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8238 (IC base=-0.024)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1078 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.0635` → IC=+0.149 (n=146)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0635 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.0752` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0752 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.0225` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.0225 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.3934` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.3934 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 263.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.270 (n=515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1252` → IC=+0.233 (n=339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1252 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.252 (n=365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.7083` → IC=+0.261 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7083 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.351` → IC=+0.297 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.351 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.1095` → IC=+0.238 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1095 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4356` → IC=+0.228 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4356 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.727` → IC=+0.233 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.727 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.323 (n=545)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.305)

- **PATRÓN** `drift_60min` |x|≤ `0.5361` → IC=+0.304 (n=545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5361 (IC base=+0.305)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.329 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.305)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.315 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.68` → IC=+0.341 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.68 (IC base=+0.305)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` < `3.4433` → IC=+0.298 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.4433 (IC base=+0.305)

- **PATRÓN** `volumen_spike_ratio` > `2.3431` → IC=+0.316 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3431 (IC base=+0.305)

- **PATRÓN** `libro_liquidez` > `1665.1432` → IC=+0.308 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1665.1432 (IC base=+0.305)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.301 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.305)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.147 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=535)

- **FILTRO** `ibs_20min` < `0.5702` → IC=-0.167 (n=385)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5702
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=386)

- **FILTRO** `ibs_20min` > `0.7357` → IC=-0.143 (n=424)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7357
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=826)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.135 (n=83)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1167)

- **PATRÓN** `dist_vwap_pct` > `1.5591` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.5591 (IC base=-0.052)

- **PATRÓN** `volumen_regimen` < `0.9328` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.9328 (IC base=-0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=-0.052)

- **PATRÓN** `volumen_spike_ratio` < `2.0972` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0972 (IC base=-0.052)

- **PATRÓN** `volumen_spike_ratio` > `1.3689` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3689 (IC base=-0.052)

- **PATRÓN** `ballena_activa_n` < `189.0` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 189.0 (IC base=-0.052)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.825` → IC=-0.137 (n=678)

  - _Acción_: SKIP cuando `ibs_20min` < 0.825
  - _Potencial_: sin este filtro IC_bueno=+0.295 (n=350)

- **FILTRO** `ibs_20min` > `0.7571` → IC=-0.233 (n=294)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7571
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=885)

- **FILTRO** `sigma_ewma_delta_pct` > `4.704` → IC=-0.149 (n=297)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.704
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=882)

- **PATRÓN** `ibs_20min` > `0.825` → IC=+0.295 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.825 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` > `0.5651` → IC=+0.325 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5651 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.266 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `1.1512` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1512 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` < `0.1143` → IC=+0.260 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1143 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4502` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4502 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.305 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.121 (n=138)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.4351 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7154 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2973` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2973 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5013` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5013 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.337 (n=508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.263 (n=361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` > `0.9016` → IC=+0.328 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9016 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.1627` → IC=+0.315 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1627 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.289 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.255)

- **PATRÓN** `volumen_regimen` > `0.839` → IC=+0.294 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.839 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.296 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `2.5673` → IC=+0.264 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5673 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `1.8308` → IC=+0.259 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8308 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.258 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `2468.3035` → IC=+0.260 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2468.3035 (IC base=+0.255)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.283 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.298 (n=275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.3181` → IC=+0.275 (n=549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3181 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.284 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.275)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.275 (n=878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.275)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.315 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.5441` → IC=+0.280 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5441 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` < `0.2083` → IC=+0.278 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2083 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.408` → IC=+0.299 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.408 (IC base=+0.275)

- **PATRÓN** `volumen_regimen` > `1.2604` → IC=+0.309 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2604 (IC base=+0.275)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.380 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.275)

- **PATRÓN** `volumen_spike_ratio` > `2.1862` → IC=+0.290 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1862 (IC base=+0.275)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.205 (n=1337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3415` → IC=+0.171 (n=3526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3415 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=1471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.798` → IC=+0.233 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.798 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.726` → IC=+0.236 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.726 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.6283` → IC=+0.163 (n=2708)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6283 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1053` → IC=+0.185 (n=1506)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1053 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `2.3173` → IC=+0.165 (n=3290)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.3173 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.165 (n=4100)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3951.4039` → IC=+0.174 (n=1336)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3951.4039 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.182 (n=2576)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 90.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.187 (n=3283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0084 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.211 (n=1246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=1810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.181 (n=1702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 7.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.4387` → IC=+0.227 (n=3730)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4387 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` < `0.2271` → IC=+0.170 (n=2836)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.2271 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.024` → IC=+0.211 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.024 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1693` → IC=+0.163 (n=2814)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1693 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.159 (n=2814)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6211 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.246 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6536` → IC=+0.202 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6536 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.176 (n=2691)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 157.0 (IC base=+0.176)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.179 (n=297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0057 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.207 (n=305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.2941` → IC=+0.199 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.2941 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.231 (n=251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.749` → IC=+0.306 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.749 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.254 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.6366` → IC=+0.167 (n=589)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.6366 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.4596` → IC=+0.168 (n=588)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4596 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.207 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.195 (n=267)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 44.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.266 (n=379)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1635` → IC=+0.307 (n=283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1635 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.261 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.2708` → IC=+0.268 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2708 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.692` → IC=+0.253 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.692 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0672` → IC=+0.230 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0672 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.299` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.299 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.9129` → IC=+0.237 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9129 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.7651` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7651 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.252 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1701.1448` → IC=+0.279 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1701.1448 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.244 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.225 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4072` → IC=+0.172 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4072 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4744` → IC=+0.209 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4744 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2039` → IC=+0.220 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2039 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.9` → IC=+0.235 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.9 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.190 (n=198)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6381 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.8957` → IC=+0.168 (n=395)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8957 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.191 (n=124)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4774` → IC=+0.204 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4774 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `11364.2884` → IC=+0.190 (n=530)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 11364.2884 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.180 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0061 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.0616` → IC=+0.213 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0616 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.4893` → IC=+0.191 (n=683)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.4893 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.1998` → IC=+0.172 (n=691)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1998 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.3` → IC=+0.238 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.3 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.220 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.223 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.7233` → IC=+0.155 (n=384)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7233 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.3943` → IC=+0.164 (n=575)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.3943 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `15740.8566` → IC=+0.157 (n=228)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 15740.8566 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 239.0 (IC base=+0.155)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.212 (n=210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1777` → IC=+0.198 (n=419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1777 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.185 (n=284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 7.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.316 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1321` → IC=+0.184 (n=232)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1321 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `3.1497` → IC=+0.167 (n=497)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 3.1497 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `1.7083` → IC=+0.167 (n=565)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7083 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=644)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1901.2255` → IC=+0.174 (n=210)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1901.2255 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.247 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.227` → IC=+0.246 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.227 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.250 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.266 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.838` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.838 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.3671` → IC=+0.271 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3671 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.9277` → IC=+0.226 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9277 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `3.0915` → IC=+0.224 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0915 (IC base=+0.230)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.208 (n=402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.3646` → IC=+0.167 (n=530)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3646 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.4362` → IC=+0.202 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4362 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1549` → IC=+0.184 (n=416)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1549 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.391` → IC=+0.269 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.391 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.2091` → IC=+0.214 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2091 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.3003` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3003 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.155 (n=195)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.6117` → IC=+0.201 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6117 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=674)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.190 (n=401)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.148 (n=362)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 136.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.217 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3796` → IC=+0.149 (n=668)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3796 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.174 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.146 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.5424` → IC=+0.181 (n=668)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5424 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.609` → IC=+0.143 (n=782)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.609 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.339` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.339 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1531` → IC=+0.137 (n=668)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1531 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.6121` → IC=+0.136 (n=668)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6121 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.170 (n=225)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.5407` → IC=+0.149 (n=246)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5407 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.5177` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5177 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `11624.4939` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 11624.4939 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `181.0` → IC=+0.124 (n=424)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 181.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.186 (n=342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0104 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.192 (n=754)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5357 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.9321` → IC=+0.249 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9321 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.123 (n=754)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6285 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1686` → IC=+0.131 (n=755)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1686 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=572)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3204.0646` → IC=+0.216 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3204.0646 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.146 (n=312)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0094 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0982` → IC=+0.149 (n=229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0982 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.4688` → IC=+0.220 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4688 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.2472` → IC=+0.141 (n=656)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2472 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.287` → IC=+0.154 (n=273)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.287 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1635` → IC=+0.144 (n=686)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1635 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.8537` → IC=+0.141 (n=457)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8537 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.3625` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.3625 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `1483.926` → IC=+0.150 (n=613)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1483.926 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0173` → IC=+0.217 (n=507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0173 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1678` → IC=+0.216 (n=336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1678 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.8851` → IC=+0.272 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8851 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.2568` → IC=+0.229 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2568 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.238 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `0.6862` → IC=+0.209 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6862 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.0834` → IC=+0.250 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0834 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.5204` → IC=+0.209 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5204 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.5152` → IC=+0.197 (n=644)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.5152 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=865)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.267 (n=260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0909` → IC=+0.233 (n=260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0909 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.207 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.414` → IC=+0.253 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.414 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.5192` → IC=+0.211 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5192 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.931` → IC=+0.258 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.931 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6905` → IC=+0.235 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6905 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2777` → IC=+0.335 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2777 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.6536` → IC=+0.229 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6536 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2528.706` → IC=+0.206 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2528.706 (IC base=+0.206)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.172 (n=394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.008 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.147 (n=290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.169 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.171 (n=870)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4444 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.9747` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9747 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.176 (n=399)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8601` → IC=+0.160 (n=466)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8601 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.1634` → IC=+0.147 (n=233)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1634 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1712` → IC=+0.174 (n=240)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1712 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.2604` → IC=+0.149 (n=717)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.2604 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.823` → IC=+0.144 (n=543)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.823 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=905)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `9423.6963` → IC=+0.192 (n=290)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 9423.6963 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.174 (n=222)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 14.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.3074` → IC=+0.127 (n=591)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.3074 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.97` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 7.97 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.1737` → IC=+0.167 (n=217)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1737 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.153 (n=327)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 22.0 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.142 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0036 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.178 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 10.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6089` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6089 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.9582` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9582 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.475` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.475 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.573` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.573 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `11295.2956` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11295.2956 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.6256` → IC=+0.145 (n=257)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6256 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.02` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.02 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.240 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.073)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.281 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.261)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.321 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.296 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` > `0.3963` → IC=+0.287 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3963 (IC base=+0.261)

- **PATRÓN** `dist_vwap_pct` > `0.1787` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1787 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.247` → IC=+0.306 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.247 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` < `0.8223` → IC=+0.274 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8223 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` > `1.1387` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1387 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.2472` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2472 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.368` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.368 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.0363` → IC=+0.327 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0363 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.1304` → IC=+0.146 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1304 (IC base=+0.047)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.8462` → IC=-0.123 (n=120)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8462
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=123)

- **FILTRO** `ibs_20min` > `0.4375` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4375
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=105)

- **FILTRO** `dist_vwap_pct` > `0.2325` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2325
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=137)

- **FILTRO** `volumen_pendiente_norm` > `0.2176` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2176
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=119)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 14.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` > `0.8462` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8462 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.6872` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6872 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.165` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.165 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 20.0 (IC base=-0.037)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0226` → IC=+0.146 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0226 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.31` → IC=+0.161 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.31 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.2912` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2912 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.434` → IC=+0.140 (n=159)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.434 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.9833` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9833 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6571 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.1036` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1036 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.899` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.899 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.213 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.141 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.0588 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.9736` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9736 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.507` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.507 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6197 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.5677` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5677 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2567.2585` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2567.2585 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 16.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.200 (n=2199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=4880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.488` → IC=+0.209 (n=4845)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.488 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.7662` → IC=+0.213 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7662 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.635` → IC=+0.223 (n=2694)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.635 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8816` → IC=+0.159 (n=2231)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8816 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1677` → IC=+0.194 (n=1315)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1677 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8748` → IC=+0.170 (n=3011)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8748 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=4579)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3867.8176` → IC=+0.185 (n=1615)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3867.8176 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.209 (n=2323)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.195 (n=4453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0109 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4818` → IC=+0.194 (n=4452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4818 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=2181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=1985)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.240 (n=4452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.4489` → IC=+0.170 (n=3167)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.4489 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.698` → IC=+0.216 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.698 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.613` → IC=+0.188 (n=4354)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.613 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6208` → IC=+0.166 (n=1053)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6208 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `1.1947` → IC=+0.165 (n=1053)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1947 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2366` → IC=+0.244 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2366 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2973` → IC=+0.200 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2973 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.181 (n=3325)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 143.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.185 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0052 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.236 (n=362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.073` → IC=+0.298 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.073 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2215` → IC=+0.262 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2215 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5922` → IC=+0.188 (n=315)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.5922 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.8897` → IC=+0.173 (n=475)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8897 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.236 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.275 (n=526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.274 (n=594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1847` → IC=+0.297 (n=397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1847 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.274 (n=543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.276 (n=601)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.4087` → IC=+0.302 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4087 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.577` → IC=+0.282 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.577 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2963` → IC=+0.318 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2963 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `1.511` → IC=+0.281 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.511 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.271 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1483.9192` → IC=+0.277 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1483.9192 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.264 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.168 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.006 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0956` → IC=+0.168 (n=266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0956 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3271` → IC=+0.204 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3271 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2359` → IC=+0.217 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2359 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.807` → IC=+0.182 (n=190)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.807 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.384` → IC=+0.168 (n=696)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 4.384 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.261` → IC=+0.168 (n=795)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.261 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0941` → IC=+0.161 (n=361)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0941 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.0707` → IC=+0.170 (n=671)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0707 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1464` → IC=+0.193 (n=216)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1464 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.3899` → IC=+0.177 (n=745)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.3899 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.7228` → IC=+0.173 (n=497)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.7228 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `10774.9458` → IC=+0.184 (n=710)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 10774.9458 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `470.0` → IC=+0.177 (n=592)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 470.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.172 (n=721)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0062 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.169 (n=645)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0029 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3506` → IC=+0.176 (n=721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3506 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.165 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.166 (n=747)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 18.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.6191` → IC=+0.204 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6191 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.1479` → IC=+0.180 (n=627)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1479 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.691` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.691 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6166` → IC=+0.228 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6166 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1414` → IC=+0.237 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1414 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.3983` → IC=+0.195 (n=208)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.3983 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.0527` → IC=+0.191 (n=283)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.0527 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 290.0 (IC base=+0.164)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.221 (n=704)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.242 (n=331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.253 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.68 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.652` → IC=+0.337 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.652 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.2199` → IC=+0.211 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2199 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `3.9028` → IC=+0.204 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.9028 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.4544` → IC=+0.204 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4544 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `1456.9184` → IC=+0.210 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1456.9184 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.253 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.289 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.247 (n=318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.4838` → IC=+0.241 (n=700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4838 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.272 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.290 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.453` → IC=+0.289 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.453 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3568` → IC=+0.279 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3568 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `3.0387` → IC=+0.243 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0387 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.3262` → IC=+0.223 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3262 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.223 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.160 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.007 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.158 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.7347` → IC=+0.239 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7347 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.383` → IC=+0.187 (n=314)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.383 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.082` → IC=+0.183 (n=140)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 12.082 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8905` → IC=+0.167 (n=536)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8905 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.1984` → IC=+0.148 (n=268)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1984 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.230 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.5054` → IC=+0.200 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5054 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=879)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `9596.597` → IC=+0.235 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9596.597 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.151 (n=560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4454` → IC=+0.151 (n=637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4454 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.166 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 8.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6809` → IC=+0.176 (n=637)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6809 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.4125` → IC=+0.132 (n=644)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4125 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.305` → IC=+0.217 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.305 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.194` → IC=+0.132 (n=598)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.194 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.1278` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1278 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2771` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2771 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.512` → IC=+0.165 (n=192)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.512 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `9578.0604` → IC=+0.177 (n=289)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 9578.0604 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `193.0` → IC=+0.144 (n=492)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 193.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.148 (n=560)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0083 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.138 (n=570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 12.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.177 (n=844)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4706 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.8895` → IC=+0.194 (n=207)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8895 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.355` → IC=+0.217 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.355 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=583)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2968.0736` → IC=+0.248 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.0736 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 33.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.175 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0059 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1302` → IC=+0.175 (n=266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1302 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.199 (n=798)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5909 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.5134` → IC=+0.138 (n=774)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.5134 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.222` → IC=+0.136 (n=783)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.222 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0614` → IC=+0.132 (n=702)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0614 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.168 (n=269)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5571` → IC=+0.141 (n=285)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5571 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.139 (n=294)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2665.5883` → IC=+0.159 (n=362)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2665.5883 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0279` → IC=+0.246 (n=305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0279 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9321` → IC=+0.293 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9321 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.1714` → IC=+0.249 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1714 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.169` → IC=+0.249 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.169 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2203` → IC=+0.232 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2203 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1687` → IC=+0.251 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1687 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.8201` → IC=+0.208 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8201 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.209 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.273 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.227 (n=335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.215 (n=1058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.260 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2662` → IC=+0.215 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2662 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.357` → IC=+0.282 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.357 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.7028` → IC=+0.222 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7028 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.309 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4571` → IC=+0.199 (n=831)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4571 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.186 (n=733)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 35.0 (IC base=+0.208)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=1783)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.137 (n=1381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.01 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.2793` → IC=+0.139 (n=1046)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2793 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.191 (n=523)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.9275 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.47` → IC=+0.140 (n=248)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 10.47 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.783` → IC=+0.122 (n=1431)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 3.783 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.175` → IC=+0.153 (n=428)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.175 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.142 (n=518)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.8939` → IC=+0.143 (n=1035)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8939 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `8938.0512` → IC=+0.137 (n=711)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 8938.0512 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.168 (n=456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.5037` → IC=+0.148 (n=1349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.5037 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.146 (n=520)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.153 (n=594)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.2 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `1.0112` → IC=+0.131 (n=177)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 1.0112 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.329` → IC=+0.139 (n=1348)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.329 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1015` → IC=+0.138 (n=1139)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1015 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1484` → IC=+0.128 (n=1349)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1484 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.146 (n=636)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.4927` → IC=+0.137 (n=1335)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4927 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.7981` → IC=+0.135 (n=890)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.7981 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=1783)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7933.3228` → IC=+0.133 (n=1205)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7933.3228 (IC base=+0.127)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.554` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.554
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.136 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.2159` → IC=+0.125 (n=102)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.2159 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.147 (n=182)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `0.7903` → IC=+0.123 (n=104)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.7903 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.2086` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.2086 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `12617.0993` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 12617.0993 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.170 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0035 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.143 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.1703` → IC=+0.159 (n=274)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1703 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.6448` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6448 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.138 (n=620)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.8701` → IC=+0.147 (n=415)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8701 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.0635` → IC=+0.151 (n=293)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0635 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.143 (n=208)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.112)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.212 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.182 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0104 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4227` → IC=+0.153 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4227 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.9743` → IC=+0.228 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9743 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.295` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.295 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.167 (n=151)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `3.5716` → IC=+0.150 (n=367)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 3.5716 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.4093` → IC=+0.159 (n=244)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4093 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `1761.2152` → IC=+0.151 (n=368)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1761.2152 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.278 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.308 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.315 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.5806` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5806 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.158` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.158 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `1.861` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.861 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2488.6766` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2488.6766 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.280)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.163 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0052 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3932` → IC=+0.141 (n=500)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3932 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.144 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.185` → IC=+0.147 (n=568)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.185 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `1.0394` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 1.0394 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.4266` → IC=+0.144 (n=537)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4266 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.989` → IC=+0.146 (n=571)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.989 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1165` → IC=+0.147 (n=500)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1165 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1749` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1749 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8023` → IC=+0.137 (n=373)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.8023 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=493)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8385.7236` → IC=+0.146 (n=568)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8385.7236 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.168 (n=422)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0088 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4079` → IC=+0.208 (n=371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4079 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.159 (n=288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 10.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.1076` → IC=+0.160 (n=422)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.1076 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.7273` → IC=+0.157 (n=468)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.7273 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.927` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.927 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2231` → IC=+0.168 (n=422)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2231 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.7338` → IC=+0.149 (n=377)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.7338 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1472` → IC=+0.155 (n=430)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1472 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.0698` → IC=+0.163 (n=185)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0698 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1713` → IC=+0.172 (n=364)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1713 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.169 (n=370)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `8204.9591` → IC=+0.165 (n=422)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8204.9591 (IC base=+0.149)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `ibs_20min` < `0.425` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.425
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=79)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.247` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.247 (IC base=-0.014)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.008)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0104` → IC=-0.297 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=189)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.215 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=137)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.197 (n=249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0058 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.6383` → IC=+0.217 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6383 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.8747` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8747 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.047` → IC=+0.244 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.047 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `0.8208` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8208 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2652` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2652 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.9975` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.9975 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `1.4867` → IC=+0.183 (n=162)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4867 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.165 (n=231)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `1205.3517` → IC=+0.177 (n=230)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1205.3517 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0875 (IC base=-0.124)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7788` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7788
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=94)

- **FILTRO** `sigma_h` > `0.0058` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.223 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.7788` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7788 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.3562` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3562 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.35` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.35 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.8996` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8996 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` < `0.0651` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0651 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.1124` → IC=+0.200 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1124 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=92)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.687` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.687 (IC base=-0.036)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.364 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=61)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.238 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **FILTRO** `ibs_20min` > `0.6442` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6442
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=35)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.200 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.5424` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5424 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.1738` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1738 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.205` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.205 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.7864` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.7864 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `1.0184` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.0184 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1359` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1359 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `1136.0742` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1136.0742 (IC base=+0.122)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0159` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0159
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=67)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.273 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=46)

- **FILTRO** `volumen_regimen` > `0.8518` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8518
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=24)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.204 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6842 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.9623` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9623 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.817` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.817 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `0.9891` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.9891 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.308` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.308 (IC base=+0.051)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.07 (IC base=+0.051)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1312` → IC=-0.368 (n=36)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1312
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=70)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.463 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=83)

- **FILTRO** `volumen_pendiente_norm` < `0.137` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.137
  - _Potencial_: sin este filtro IC_bueno=-0.333 (n=10)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0038` → IC=-0.250 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `ibs_20min` < `0.6047` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6047
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `volumen_regimen` > `1.0011` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0011
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7335` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7335
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `volumen_regimen` > `0.5614` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5614
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0086` → IC=-0.231 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `volumen_regimen` < `1.0152` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0152
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0084` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `dist_vwap_pct` < `0.2118` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2118
  - _Potencial_: sin este filtro IC_bueno=-0.312 (n=14)

- **FILTRO** `volumen_regimen` < `1.1255` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1255
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6331` → IC=-0.246 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6331
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=171)

- **PATRÓN** `ibs_20min` > `0.6331` → IC=+0.124 (n=171)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.6331 (IC base=+0.030)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.251 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.672` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.672 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0662` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0662 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `2923.7123` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2923.7123 (IC base=+0.051)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=60)

- **FILTRO** `volumen_regimen` < `0.7102` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.258 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1622 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.501` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 14.501 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.5658` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5658 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3671.9914` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3671.9914 (IC base=+0.109)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=39)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.2013` → IC=+0.134 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2013 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.8029 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1039` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1039 (IC base=+0.057)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2339.7005` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2339.7005 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 19.0 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2418.7992` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2418.7992 (IC base=+0.038)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_spike_ratio` > `1.5494` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5494
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **FILTRO** `dist_vwap_pct` > `0.1588` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1588
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

- **FILTRO** `volumen_regimen` < `1.0195` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0195
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.140 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0047 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.791 (IC base=+0.076)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.076)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2776.7577` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2776.7577 (IC base=+0.099)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.122 (n=154)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2352.3194` → IC=+0.126 (n=252)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2352.3194 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2776.7577` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2776.7577 (IC base=+0.099)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.122 (n=154)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2352.3194` → IC=+0.126 (n=252)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2352.3194 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=64)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=109)

- **FILTRO** `libro_liquidez` < `2306.3177` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 2306.3177
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=94)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=171)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=157)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1064)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=79)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=47)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35093.65` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `liq_usd_total` < 35093.65
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=78)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **PATRÓN** `liq_usd_total` > `58893.21` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 58893.21 (IC base=+0.004)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.004)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9534` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9534
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=76)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=366)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=404)

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
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.7365` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.7365
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=161)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=161)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=133)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=121)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=121)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=90)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=42)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=49)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.3878` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.3878
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=127)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=371)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=744)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=810)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.177 (n=1539)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=4641)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.186 (n=1561)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=4860)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.224 (n=237)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=729)

- **FILTRO** `ibs_20min` < `0.737` → IC=-0.204 (n=241)

  - _Acción_: SKIP cuando `ibs_20min` < 0.737
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=725)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.167 (n=277)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=847)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.187 (n=247)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=763)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.146 (n=252)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=758)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=975)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.197 (n=331)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=692)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.213 (n=252)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=843)

- **FILTRO** `ibs_20min` > `0.7143` → IC=-0.197 (n=272)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=823)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.179 (n=241)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=792)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.167 (n=253)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=773)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.178 (n=253)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=773)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=276)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=765)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.162 (n=264)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=812)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.195 (n=234)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=732)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=951)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.195 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=830)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.340 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=167)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=186)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=514)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=520)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.242 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=59)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.0752` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0752
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `py_entrada` > `0.665` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.665
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=98)

- **FILTRO** `ibs_20min` > `0.9863` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9863
  - _Potencial_: sin este filtro IC_bueno=-0.126 (n=97)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.136 (n=3193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=11832)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=3661)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=11364)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.241 (n=3739)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=11286)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.170 (n=5084)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=9941)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.221 (n=4642)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=14333)

- **FILTRO** `ibs_7min` > `0.7143` → IC=-0.173 (n=4729)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=14246)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=537)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=1665)

- **FILTRO** `ibs_7min` < `0.7018` → IC=-0.256 (n=726)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7018
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1476)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=539)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=1663)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.238 (n=820)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2478)

- **FILTRO** `drift_7min_pct` |x|> `0.1136` → IC=-0.130 (n=1121)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1136
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=2177)

- **FILTRO** `ibs_7min` > `0.837` → IC=-0.196 (n=824)

  - _Acción_: SKIP cuando `ibs_7min` > 0.837
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2474)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.134 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=2179)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.262 (n=673)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2111)

- **FILTRO** `ibs_7min` < `0.7711` → IC=-0.195 (n=696)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7711
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=2088)

- **FILTRO** `ballena_activa_n` > `168.0` → IC=-0.178 (n=691)

  - _Acción_: SKIP cuando `ballena_activa_n` > 168.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=2093)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.242 (n=665)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2137)

- **FILTRO** `ballena_activa_n` > `108.0` → IC=-0.172 (n=950)

  - _Acción_: SKIP cuando `ballena_activa_n` > 108.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1852)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.186 (n=696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=1522)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.310 (n=699)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1519)

- **FILTRO** `ibs_7min` < `0.2174` → IC=-0.295 (n=553)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2174
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1665)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.238 (n=537)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=1681)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.225 (n=801)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2620)

- **FILTRO** `ibs_7min` > `0.7964` → IC=-0.170 (n=855)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7964
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2566)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=1775)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=610)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=1928)

- **FILTRO** `ibs_7min` < `0.754` → IC=-0.193 (n=634)

  - _Acción_: SKIP cuando `ibs_7min` < 0.754
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=1904)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.178 (n=836)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1702)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.234 (n=844)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1718)

- **FILTRO** `ibs_7min` > `0.277` → IC=-0.176 (n=640)

  - _Acción_: SKIP cuando `ibs_7min` > 0.277
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=1922)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.187 (n=627)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1935)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.245 (n=676)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2133)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.205 (n=697)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2112)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.185 (n=687)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2122)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.176 (n=848)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2720)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.125 (n=587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1887)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.291 (n=602)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1872)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.235 (n=618)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1856)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.226 (n=607)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1867)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.210 (n=820)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2504)

- **FILTRO** `ibs_7min` > `0.7647` → IC=-0.162 (n=830)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7647
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2494)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=38)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=480)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.146 (n=526)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 453.526 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3338.8044` → IC=+0.159 (n=206)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3338.8044 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.132 (n=370)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 64.0 (IC base=+0.132)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.268 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.121)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.413` → IC=+0.212 (n=57)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.413 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.127 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 10.0 (IC base=+0.112)

- **PATRÓN** `total_vol_5m` < `498.822` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 498.822 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `7409.4986` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7409.4986 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 136.0 (IC base=+0.112)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4038` → IC=+0.216 (n=79)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4038 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.257 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.192)

- **PATRÓN** `total_vol_5m` < `6013.826` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 6013.826 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3096.9147` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3096.9147 (IC base=+0.192)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.163 (n=81)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.156 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `374733.9` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 374733.9 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3424.0673` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3424.0673 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 43.0 (IC base=+0.131)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `3.488` → IC=-0.389 (n=61)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.488
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=120)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.363 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=25)

- **FILTRO** `T_h` > `39.9952` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `T_h` > 39.9952
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.132)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.214 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `135.9952` → IC=-0.167 (n=49)

  - _Acción_: SKIP cuando `T_h` > 135.9952
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=151)

- **FILTRO** `pct_vs_K` |x|> `5.2323` → IC=-0.245 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.2323
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=151)

- **FILTRO** `T_h` > `145.6762` → IC=-0.360 (n=55)

  - _Acción_: SKIP cuando `T_h` > 145.6762
  - _Potencial_: sin este filtro IC_bueno=-0.307 (n=112)

- **FILTRO** `pct_vs_K` |x|> `4.4208` → IC=-0.448 (n=56)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4208
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=111)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.9866` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `pct_vs_K` |x|> `3.6199` → IC=-0.444 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6199
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=59)

- **FILTRO** `T_h` > `144.6172` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=41)

- **FILTRO** `pct_vs_K` |x|> `2.3742` → IC=-0.435 (n=29)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3742
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=31)

- **PATRÓN** `pct_vs_K` |x|≤ `1.2308` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.2308 (IC base=-0.058)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0037` → IC=-0.256 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `T_h` > `111.9956` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 111.9956
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=36)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=39)

- **FILTRO** `T_h` > `145.5703` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `T_h` > 145.5703
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.395 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

- **FILTRO** `T_h` > `135.2296` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `T_h` > 135.2296
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2412` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2412 (IC base=+0.383)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.383)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.419 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.383)

- **PATRÓN** `dist_50` > `0.4092` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4092 (IC base=+0.383)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.383)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.447 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.479)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `7.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=67)

- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=74)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=131)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.038)

- **PATRÓN** `streak_estiramiento` < `0.4411` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4411 (IC base=+0.032)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=77)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.144 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=159)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=179)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=181)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=191)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=286)

- **PATRÓN** `streak_estiramiento` < `0.3587` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.3587 (IC base=+0.036)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=564)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=293)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=372)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1626)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=903)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=911)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.165 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0036 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.170 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0073 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1668` → IC=+0.139 (n=505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.1668 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0597` → IC=+0.137 (n=574)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.0597 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.138 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 4.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.168 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5909` → IC=+0.221 (n=574)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5909 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.4417` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.4417 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.5751` → IC=+0.136 (n=613)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.5751 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.55` → IC=+0.231 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.55 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=585)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.180 (n=192)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.136)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_ewma_delta_pct` > `7.827` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.827
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1029)

### UPDOWN_GBM#60min
- **FILTRO** `ibs_15` < `0.2038` → IC=-0.147 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2038
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=96)

- **FILTRO** `sigma_ewma_delta_pct` > `15.947` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.947
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=88)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.130 (n=71)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=145)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.200 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.201 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.173)

- **PATRÓN** `drift_15min` |x|≤ `0.6` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.6 (IC base=+0.173)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.196 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 4.0 (IC base=+0.173)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.293 (n=109)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.306` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.306 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1221` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1221 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.598` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 18.598 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `14955.5892` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14955.5892 (IC base=+0.173)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` > `0.0048` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

- **FILTRO** `ibs_15` < `0.1693` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1693
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

- **FILTRO** `libro_liquidez` < `13463.8087` → IC=-0.130 (n=52)

  - _Acción_: SKIP cuando `libro_liquidez` < 13463.8087
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=27)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.6724` → IC=-0.196 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6724
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=133)

- **FILTRO** `ibs_15` < `0.2299` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2299
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=42)

- **FILTRO** `sigma_ewma_delta_pct` > `12.292` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.292
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=44)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.331` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 20.331 (IC base=+0.010)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6414` → IC=-0.194 (n=47)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6414
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=142)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.140 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0031 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2632` → IC=+0.180 (n=48)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.2632 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1616` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1616 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.6414` → IC=+0.194 (n=142)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.97€ cuando `ibs_15` > 0.6414 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1511 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.097)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=74)

- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

- **FILTRO** `libro_liquidez` < `8064.8076` → IC=-0.123 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 8064.8076
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=51)

- **FILTRO** `drift_15min` |x|> `0.5012` → IC=-0.158 (n=144)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5012
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=435)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=166)

- **FILTRO** `drift_15min` |x|> `0.3805` → IC=-0.182 (n=20)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3805
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `ibs_15` > `0.2345` → IC=-0.147 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=64)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.269 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.139 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.121)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2244` → IC=+0.147 (n=32)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.2244 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 20.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.258 (n=64)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.1491` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1491 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.576` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.576 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3083.8765` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3083.8765 (IC base=+0.121)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0264` → IC=-0.200 (n=38)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0264
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=115)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=113)

- **FILTRO** `ibs_15` < `0.4118` → IC=-0.218 (n=37)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4118
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=116)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=69)

- **FILTRO** `sigma_ewma_delta_pct` < `10.065` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 10.065
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **PATRÓN** `dist_vwap_pct` < `0.3849` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3849 (IC base=+0.011)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0501` → IC=+0.158 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0501 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.176 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.119)

- **PATRÓN** `ibs_15` > `0.4894` → IC=+0.197 (n=153)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.4894 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.2672` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2672 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.957` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.957 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2496.2216` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2496.2216 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 18.0 (IC base=+0.119)

- **PATRÓN** `ibs_15` < `0.1171` → IC=+0.180 (n=179)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` < 0.1171 (IC base=+0.031)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.329 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.323)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.387 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.323)

- **PATRÓN** `drift_60min` |x|≤ `0.1149` → IC=+0.350 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1149 (IC base=+0.323)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.329 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.323)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.341 (n=224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.323)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.388 (n=185)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.323)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.323)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.464` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.464 (IC base=+0.323)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.331 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.323)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.329 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.323)

- **PATRÓN** `libro_liquidez` > `8508.8052` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8508.8052 (IC base=+0.323)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.368 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.323)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.324 (n=106)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.315)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.315 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.333 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.315)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.333 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.315)

- **PATRÓN** `drift_15min` |x|≤ `0.411` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.411 (IC base=+0.315)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.317 (n=80)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.315)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.344 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.315)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.352 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2747` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2747 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `11439.5159` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11439.5159 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `626.0` → IC=+0.419 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 626.0 (IC base=+0.315)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.325 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.329)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.367 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.343 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2105` → IC=+0.333 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2105 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.333 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.329)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.329 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.399 (n=87)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.144` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.144 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.994` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.994 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `2809.1248` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2809.1248 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 166.0 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0109` → IC=-0.206 (n=355)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1066)

- **FILTRO** `ibs_15` < `0.5789` → IC=-0.189 (n=162)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5789
  - _Potencial_: sin este filtro IC_bueno=+0.229 (n=330)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=363)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1058)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.297` → IC=+0.174 (n=182)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.297 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.5789` → IC=+0.229 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5789 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.1779` → IC=+0.130 (n=225)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1779 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1246` → IC=+0.227 (n=335)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1246 (IC base=-0.062)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.246 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=-0.062)

- **PATRÓN** `ibs_15` < `0.3707` → IC=+0.271 (n=501)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3707 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` < `0.46` → IC=+0.223 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.46 (IC base=-0.062)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.227 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=-0.062)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.233 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=704)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.230 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=629)

- **FILTRO** `sigma_ewma_delta_pct` > `19.454` → IC=-0.248 (n=169)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.454
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=769)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.148 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0029 (IC base=+0.027)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.192 (n=24)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.027)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1355` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1355 (IC base=+0.027)

- **PATRÓN** `ibs_15` > `0.6026` → IC=+0.292 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6026 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1823` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1823 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 308.0 (IC base=+0.027)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6395` → IC=-0.247 (n=77)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6395
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=157)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=217)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.212 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.089)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.255 (n=157)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.1779` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1779 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `10832.5702` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 10832.5702 (IC base=+0.089)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.248 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.211 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.220 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0913` → IC=+0.224 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0913 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.226 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.288 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` < `0.2963` → IC=+0.297 (n=215)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2963 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1753` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1753 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4127` → IC=+0.213 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4127 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.178` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.178 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.415` → IC=+0.230 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.415 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `3638.7885` → IC=+0.211 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3638.7885 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.212)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1627` → IC=-0.180 (n=120)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1627
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=233)

- **FILTRO** `drift_15min` |x|> `0.8505` → IC=-0.256 (n=88)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8505
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=265)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=123)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=230)

- **PATRÓN** `ibs_15` > `0.8214` → IC=+0.300 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8214 (IC base=-0.128)

- **PATRÓN** `delta_ratio_macro` |x|> `0.124` → IC=+0.176 (n=72)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.124 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.189` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.189 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3926` → IC=+0.230 (n=109)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3926 (IC base=-0.046)

- **PATRÓN** `ibs_15` > `0.0714` → IC=+0.170 (n=98)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` > 0.0714 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` < `0.5028` → IC=+0.198 (n=114)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5028 (IC base=-0.046)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.264 (n=53)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=336)

- **FILTRO** `libro_liquidez` < `2497.8056` → IC=-0.215 (n=128)

  - _Acción_: SKIP cuando `libro_liquidez` < 2497.8056
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=261)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0927` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0927 (IC base=-0.059)

- **PATRÓN** `ibs_15` < `0.1385` → IC=+0.295 (n=86)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1385 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5629` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5629 (IC base=-0.059)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.4465` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4465 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.2576` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2576 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `12949.2689` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12949.2689 (IC base=+0.100)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.4465` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4465 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.2576` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2576 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `12949.2689` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12949.2689 (IC base=+0.100)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.290 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.287 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.340 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.305 (n=234)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8343` → IC=+0.321 (n=350)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8343 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.306` → IC=+0.325 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.306 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.732` → IC=+0.288 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.732 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.066` → IC=+0.287 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.066 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `13914.1536` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13914.1536 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.307 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.285 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.311 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.283)

- **PATRÓN** `drift_15min` |x|≤ `0.7272` → IC=+0.281 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7272 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.128` → IC=+0.322 (n=133)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.128 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8246` → IC=+0.306 (n=199)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8246 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.3186` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3186 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.666` → IC=+0.284 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.666 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `11875.3868` → IC=+0.322 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11875.3868 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.291 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.288 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0682` → IC=+0.341 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0682 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1882` → IC=+0.317 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1882 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.324 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.846` → IC=+0.324 (n=151)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.846 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` < `0.4822` → IC=+0.290 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4822 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.547` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.547 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.173` → IC=+0.297 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.173 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.303 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `10755.3155` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10755.3155 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `190.0` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 190.0 (IC base=+0.288)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0902` → IC=-0.268 (n=54)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0902
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.233 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=144)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.174` → IC=-0.129 (n=60)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.174
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=61)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
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
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.1352` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1352
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9922` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.115)

- **PATRÓN** `T_h` > `145.965` → IC=+0.419 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.965 (IC base=+0.343)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.343)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.973` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.096)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.282)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `59.2591` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 59.2591 (IC base=+0.163)

- **PATRÓN** `ratio` < `0.9624` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9624 (IC base=+0.163)

- **PATRÓN** `T_h` > `87.996` → IC=+0.329 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.996 (IC base=+0.315)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.315)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `127.3918` → IC=+0.425 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.3918 (IC base=+0.409)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5909 sube el IC de +0.136 a +0.221 en UPDOWN_GBM#15min (n=574). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.173 a +0.293 en UPDOWN_GBM#BTC#15min (n=109). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6414 sube el IC de +0.097 a +0.194 en UPDOWN_GBM#ETH#15min (n=142). Ya aplicado como kelly_boost=+0.97€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.121 a +0.258 en UPDOWN_GBM#SOL#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4894 sube el IC de +0.119 a +0.197 en UPDOWN_GBM#XRP#15min (n=153). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1171 sube el IC de +0.031 a +0.180 en UPDOWN_GBM#XRP#15min (n=179). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5789 sube el IC de -0.067 a +0.229 en UPDOWN_GBM_15M_TARDIO (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3707 sube el IC de -0.062 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=501). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.6026 sube el IC de +0.027 a +0.292 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6395 sube el IC de +0.089 a +0.255 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=157). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2963 sube el IC de +0.212 a +0.297 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=215). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8214 sube el IC de -0.128 a +0.300 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=18). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3926 sube el IC de -0.046 a +0.230 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=109). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS > 0.0714 sube el IC de -0.046 a +0.170 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=98). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1385 sube el IC de -0.059 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8343 sube el IC de +0.286 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=350). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8246 sube el IC de +0.283 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=199). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.846 sube el IC de +0.288 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=151). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.323 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=185). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.315 a +0.352 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.329 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=87). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.365 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.365 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 838 | +0.092 | +60.37€ | 2 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 838 | +0.092 | +60.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 24 | +0.077 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 24 | +0.077 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 552 | +0.108 | +44.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 552 | +0.108 | +44.47€ | 3 | 12 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 5 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 40 | +0.167 | +15.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 40 | +0.167 | +15.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 15492 | -0.116 | -2617.11€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 976 | -0.013 | -143.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 14516 | -0.123 | -2473.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2058 | -0.104 | -473.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2058 | -0.104 | -473.25€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 976 | -0.013 | -143.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 976 | -0.013 | -143.30€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2066 | -0.174 | -571.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2066 | -0.174 | -571.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 4130 | -0.054 | -396.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 4130 | -0.054 | -396.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3436 | -0.129 | -276.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3436 | -0.129 | -276.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2826 | -0.193 | -756.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2826 | -0.193 | -756.05€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 4626 | -0.078 | +1865.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 1321 | -0.013 | +970.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 3305 | -0.104 | +895.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 4626 | -0.078 | +1865.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 1321 | -0.013 | +970.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 3305 | -0.104 | +895.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 99 | -0.035 | -9.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 99 | -0.035 | -9.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 99 | -0.035 | -9.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 99 | -0.035 | -9.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 49734 | +0.114 | -3013.94€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 8284 | +0.183 | -274.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 174 | -0.108 | -55.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 37455 | +0.099 | -2603.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3821 | +0.116 | -80.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 6287 | +0.086 | -792.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 28 | -0.100 | +6.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 6244 | +0.087 | -787.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 9949 | +0.132 | -221.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2441 | +0.198 | -112.71€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 6187 | +0.109 | -132.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1279 | +0.124 | +46.35€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 6307 | +0.084 | -759.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 31 | +0.015 | +3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#240min | 13 | -0.195 | -9.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 6263 | +0.086 | -753.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 10751 | +0.127 | -161.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 3090 | +0.171 | -19.00€ | 1 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 6231 | +0.112 | -88.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1418 | +0.095 | -45.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 10154 | +0.123 | -661.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2671 | +0.190 | -154.22€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 85 | -0.017 | -4.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 6274 | +0.095 | -421.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1124 | +0.131 | -81.80€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 6286 | +0.106 | -417.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 23 | -0.020 | +1.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 7 | +0.019 | +0.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 6256 | +0.106 | -420.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 8195 | +0.178 | -634.42€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 8195 | +0.178 | -634.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2093 | +0.164 | -236.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2093 | +0.164 | -236.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2044 | +0.171 | -212.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2044 | +0.171 | -212.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1832 | +0.236 | -44.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1832 | +0.236 | -44.14€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1998 | +0.184 | -154.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1998 | +0.184 | -154.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 411 | +0.442 | -0.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 411 | +0.442 | -0.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 155 | +0.443 | +1.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 155 | +0.443 | +1.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 157 | +0.437 | -0.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 157 | +0.437 | -0.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 95 | +0.428 | -1.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 95 | +0.428 | -1.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 26592 | +0.189 | -2452.77€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 26592 | +0.189 | -2452.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4724 | +0.151 | -726.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4724 | +0.151 | -726.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 4152 | +0.225 | -143.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 4152 | +0.225 | -143.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 4600 | +0.164 | -617.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 4600 | +0.164 | -617.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 4239 | +0.219 | -173.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 4239 | +0.219 | -173.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 4399 | +0.199 | -325.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 4399 | +0.199 | -325.38€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 4478 | +0.184 | -465.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 4478 | +0.184 | -465.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 9671 | +0.131 | +325.08€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 9671 | +0.131 | +325.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 4797 | +0.136 | +205.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 4797 | +0.136 | +205.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 4874 | +0.125 | +119.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 4874 | +0.125 | +119.22€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 974 | +0.291 | -12.82€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 974 | +0.291 | -12.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 421 | +0.278 | -11.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 421 | +0.278 | -11.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 460 | +0.294 | +2.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 460 | +0.294 | +2.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 93 | +0.321 | -3.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 93 | +0.321 | -3.00€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 418 | +0.424 | -10.54€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 418 | +0.424 | -10.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 189 | +0.421 | -5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 189 | +0.421 | -5.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 194 | +0.429 | -4.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 194 | +0.429 | -4.13€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 35 | +0.365 | -0.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 35 | +0.365 | -0.68€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 501 | +0.094 | -4.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 172 | +0.086 | -6.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 329 | +0.098 | +1.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 32 | +0.088 | +0.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 32 | +0.088 | +0.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 393 | +0.105 | +6.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 64 | +0.136 | +4.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 329 | +0.098 | +1.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 76 | +0.038 | -11.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 76 | +0.038 | -11.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 14843 | +0.094 | -558.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1323 | +0.074 | -27.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 13520 | +0.096 | -530.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 8881 | +0.097 | -201.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1323 | +0.074 | -27.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 7558 | +0.101 | -173.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 1934 | +0.115 | +26.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 1934 | +0.115 | +26.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 4028 | +0.078 | -383.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 4028 | +0.078 | -383.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 578 | +0.260 | -70.14€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 578 | +0.260 | -70.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 578 | +0.260 | -70.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 578 | +0.260 | -70.14€ | 0 | 4 |
| ✅ GBM_LATE_15M | 12538 | +0.059 | +5380.29€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 12538 | +0.059 | +5380.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1926 | +0.196 | +1408.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1926 | +0.196 | +1408.49€ | 0 | 24 |
| ✅ GBM_LATE_15M#BTC | 1882 | +0.177 | +1288.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1882 | +0.177 | +1288.12€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 1971 | +0.196 | +1442.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1971 | +0.196 | +1442.40€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1946 | -0.034 | +128.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1946 | -0.034 | +128.37€ | 3 | 11 |
| ✅ GBM_LATE_15M#SOL | 2009 | -0.049 | +491.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2009 | -0.049 | +491.61€ | 5 | 8 |
| ✅ GBM_LATE_15M#XRP | 2804 | -0.067 | +621.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2804 | -0.067 | +621.30€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 13304 | +0.064 | +6948.09€ | 0 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 13304 | +0.064 | +6948.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 2325 | -0.001 | +1718.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 2325 | -0.001 | +1718.62€ | 2 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2888 | -0.017 | +442.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2888 | -0.017 | +442.01€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1751 | +0.259 | +1742.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1751 | +0.259 | +1742.41€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2021 | -0.044 | +76.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2021 | -0.044 | +76.76€ | 7 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2207 | -0.010 | +803.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2207 | -0.010 | +803.22€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2112 | +0.266 | +2165.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2112 | +0.266 | +2165.07€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 10315 | +0.169 | +7339.90€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 10315 | +0.169 | +7339.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1460 | +0.200 | +1123.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1460 | +0.200 | +1123.71€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1700 | +0.160 | +1232.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1700 | +0.160 | +1232.83€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1494 | +0.199 | +1136.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1494 | +0.199 | +1136.97€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1692 | +0.142 | +1036.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1692 | +0.142 | +1036.97€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1919 | +0.122 | +1210.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1919 | +0.122 | +1210.84€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2050 | +0.199 | +1598.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2050 | +0.199 | +1598.58€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 2338 | +0.107 | +782.22€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 2338 | +0.107 | +782.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 91 | +0.113 | +37.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 91 | +0.113 | +37.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 584 | +0.084 | +173.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 584 | +0.084 | +173.70€ | 0 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 339 | +0.142 | +160.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 339 | +0.142 | +160.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 536 | +0.169 | +236.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 536 | +0.169 | +236.65€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 401 | +0.001 | +21.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 401 | +0.001 | +21.94€ | 4 | 5 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 12394 | +0.175 | +8961.52€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#15min | 12394 | +0.175 | +8961.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1852 | +0.221 | +1562.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1852 | +0.221 | +1562.12€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2019 | +0.162 | +1442.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2019 | +0.162 | +1442.14€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1870 | +0.224 | +1598.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1870 | +0.224 | +1598.24€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1918 | +0.136 | +1151.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1918 | +0.136 | +1151.43€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2182 | +0.106 | +1209.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2182 | +0.106 | +1209.38€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2553 | +0.204 | +1998.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2553 | +0.204 | +1998.21€ | 0 | 21 |
| ✅ GBM_LATE_5M | 3889 | +0.124 | +1813.59€ | 1 | 24 |
| ✅ GBM_LATE_5M#5min | 3889 | +0.124 | +1813.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 235 | +0.171 | +149.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 235 | +0.171 | +149.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1036 | +0.109 | +498.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1036 | +0.109 | +498.21€ | 1 | 16 |
| ✅ GBM_LATE_5M#DOGE | 538 | +0.159 | +314.67€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 538 | +0.159 | +314.67€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 1319 | +0.141 | +659.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1319 | +0.141 | +659.73€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 168 | -0.006 | +6.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 168 | -0.006 | +6.17€ | 2 | 2 |
| ✅ GBM_LATE_5M#XRP | 593 | +0.097 | +184.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 593 | +0.097 | +184.83€ | 0 | 0 |
| ✅ GBM_LATE_60M | 747 | +0.023 | +201.84€ | 3 | 12 |
| ✅ GBM_LATE_60M#60min | 747 | +0.023 | +201.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 248 | +0.060 | +55.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 248 | +0.060 | +55.57€ | 3 | 10 |
| ✅ GBM_LATE_60M#ETH | 275 | +0.049 | +102.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 275 | +0.049 | +102.89€ | 3 | 13 |
| ✅ GBM_LATE_60M#SOL | 224 | -0.049 | +43.37€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 224 | -0.049 | +43.37€ | 3 | 8 |
| 🚫 GBM_LATE_60M_FADE | 220 | -0.297 | -34.35€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 220 | -0.297 | -34.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 86 | -0.250 | -8.73€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 86 | -0.250 | -8.73€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 72 | -0.351 | -21.15€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 72 | -0.351 | -21.15€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 62 | -0.281 | -4.47€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 62 | -0.281 | -4.47€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 453 | +0.041 | +44.95€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 453 | +0.041 | +44.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 187 | +0.045 | +25.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 187 | +0.045 | +25.52€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 122 | +0.048 | -3.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 122 | +0.048 | -3.59€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 144 | +0.027 | +23.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 144 | +0.027 | +23.02€ | 3 | 3 |
| ✅ LATE_WINDOW_5MIN | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 616 | +0.100 | +152.19€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 616 | +0.100 | +152.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 616 | +0.100 | +152.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 616 | +0.100 | +152.19€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 317 | -0.099 | -37.91€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 317 | -0.099 | -37.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 73 | -0.113 | -10.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 73 | -0.113 | -10.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 97 | -0.025 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 97 | -0.025 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1260 | -0.009 | -18.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1260 | -0.009 | -18.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 70 | -0.014 | -3.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 70 | -0.014 | -3.67€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 148 | -0.033 | -4.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 148 | -0.033 | -4.86€ | 2 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 96 | -0.061 | -6.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 96 | -0.061 | -6.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 412 | +0.019 | +10.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 412 | +0.019 | +10.58€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 444 | -0.004 | -7.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 444 | -0.004 | -7.56€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 90 | -0.065 | -5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 90 | -0.065 | -5.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 650 | -0.020 | -4.11€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 650 | -0.020 | -4.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 193 | -0.038 | -9.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 193 | -0.038 | -9.74€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 198 | +0.005 | +4.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 198 | +0.005 | +4.37€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 259 | -0.025 | +1.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 259 | -0.025 | +1.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 7711 | -0.003 | -98.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 7711 | -0.003 | -98.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 549 | -0.004 | +2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 549 | -0.004 | +2.89€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 793 | -0.016 | -15.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 793 | -0.016 | -15.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1795 | +0.007 | -16.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1795 | +0.007 | -16.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1585 | +0.001 | +1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1585 | +0.001 | +1.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 1511 | -0.011 | -39.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 1511 | -0.011 | -39.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1478 | -0.005 | -30.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1478 | -0.005 | -30.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 12601 | -0.031 | +604.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 12601 | -0.031 | +604.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 2090 | -0.020 | +315.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 2090 | -0.020 | +315.76€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2161 | -0.031 | -12.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2161 | -0.031 | -12.14€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 2118 | -0.030 | +188.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 2118 | -0.030 | +188.65€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2059 | -0.045 | -44.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2059 | -0.045 | -44.91€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 2117 | -0.036 | +72.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 2117 | -0.036 | +72.69€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 2056 | -0.025 | +84.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 2056 | -0.025 | +84.84€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 750 | -0.089 | -49.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 750 | -0.089 | -49.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 110 | -0.045 | -6.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 110 | -0.045 | -6.25€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 117 | -0.147 | -13.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 117 | -0.147 | -13.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 160 | -0.167 | -18.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 160 | -0.167 | -18.00€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 213 | -0.053 | -1.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 213 | -0.053 | -1.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 114 | -0.017 | -5.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 114 | -0.017 | -5.55€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 34000 | -0.077 | +607.54€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 34000 | -0.077 | +607.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 5500 | -0.086 | +454.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 5500 | -0.086 | +454.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 5586 | -0.080 | -139.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 5586 | -0.080 | -139.92€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 5639 | -0.083 | +162.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 5639 | -0.083 | +162.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 5100 | -0.100 | -277.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 5100 | -0.100 | -277.61€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 6377 | -0.053 | +120.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 6377 | -0.053 | +120.41€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 5798 | -0.065 | +287.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 5798 | -0.065 | +287.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6256 | -0.013 | -109.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6256 | -0.013 | -109.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 994 | -0.018 | -21.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 994 | -0.018 | -21.35€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1318 | -0.008 | -11.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1318 | -0.008 | -11.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1359 | -0.004 | -8.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1359 | -0.004 | -8.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 847 | -0.018 | -12.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 847 | -0.018 | -12.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 739 | +0.115 | +254.62€ | 1 | 6 |
| ✅ ORDER_FLOW_5M#5min | 603 | +0.128 | +242.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 143 | +0.121 | +60.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 143 | +0.121 | +60.42€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 121 | +0.085 | +23.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 121 | +0.085 | +23.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 114 | +0.112 | +42.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 114 | +0.112 | +42.19€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 105 | +0.192 | +70.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 105 | +0.192 | +70.55€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 120 | +0.131 | +45.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 120 | +0.131 | +45.45€ | 0 | 6 |
| ✅ PRICE_TARGET_GBM | 346 | -0.129 | -14.35€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 152 | -0.201 | -37.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 122 | -0.258 | -39.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 30 | +0.031 | +1.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 130 | -0.106 | +2.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 93 | -0.132 | -5.01€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 37 | -0.038 | +7.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 64 | +0.000 | +20.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 47 | -0.031 | +13.70€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 17 | +0.067 | +7.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 262 | -0.174 | -30.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 84 | +0.012 | +15.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 367 | -0.213 | -12.47€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 159 | -0.177 | -12.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 135 | -0.164 | -11.63€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 133 | -0.263 | -18.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 111 | -0.279 | -22.51€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 22 | -0.167 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 75 | -0.188 | +18.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 62 | -0.188 | +14.99€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 13 | -0.108 | +3.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 308 | -0.213 | -19.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 59 | -0.205 | +6.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 107 | +0.362 | +44.37€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#BTC | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 62 | +0.484 | +42.77€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 62 | +0.484 | +42.77€ | 0 | 1 |
| ✅ RESOLUTION_SNIPER#sniper | 107 | +0.362 | +44.37€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 243 | +0.035 | +1.73€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 243 | +0.035 | +1.73€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 109 | +0.050 | +1.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 109 | +0.050 | +1.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 90 | +0.022 | +0.56€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 90 | +0.022 | +0.56€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1920 | -0.022 | -82.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1920 | -0.022 | -82.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 800 | -0.018 | -25.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 800 | -0.018 | -25.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 141 | -0.038 | -12.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 141 | -0.038 | -12.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 426 | -0.021 | -18.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 426 | -0.021 | -18.96€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 4011 | +0.020 | +54.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 4011 | +0.020 | +54.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1309 | +0.021 | +11.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1309 | +0.021 | +11.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 813 | +0.040 | +34.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 813 | +0.040 | +34.46€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1182 | +0.009 | -3.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1182 | +0.009 | -3.97€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 707 | +0.015 | +12.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 707 | +0.015 | +12.49€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 4280 | +0.012 | -24.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 4280 | +0.012 | -24.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1645 | +0.011 | -12.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1645 | +0.011 | -12.26€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1700 | +0.022 | +6.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1700 | +0.022 | +6.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 935 | -0.005 | -18.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 935 | -0.005 | -18.85€ | 2 | 0 |
| ✅ UPDOWN_GBM | 10624 | +0.011 | +341.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3692 | +0.041 | +387.85€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 451 | +0.010 | +6.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 5757 | -0.004 | -46.35€ | 1 | 0 |
| ✅ UPDOWN_GBM#60min | 672 | -0.006 | -5.92€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 469 | +0.071 | +53.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 186 | +0.117 | +44.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 11 | -0.021 | -0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 272 | +0.044 | +9.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1994 | +0.016 | +109.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 431 | +0.070 | +83.44€ | 1 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 135 | +0.047 | +8.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1150 | -0.003 | +17.80€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 258 | +0.004 | -1.26€ | 3 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 20 | -0.136 | +1.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 1216 | +0.002 | +1.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 129 | +0.088 | +27.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 10 | +0.042 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 1077 | -0.010 | -26.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 2167 | +0.002 | +22.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1067 | +0.030 | +48.99€ | 1 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 127 | +0.027 | +7.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 681 | -0.036 | -30.07€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 275 | -0.016 | -4.59€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 17 | -0.157 | +0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 3049 | +0.005 | +21.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 961 | +0.010 | +22.26€ | 1 | 10 |
| ✅ UPDOWN_GBM#SOL#240min | 121 | -0.004 | -3.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1815 | +0.006 | +2.78€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 139 | -0.004 | -0.06€ | 2 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 13 | -0.152 | -0.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1727 | +0.019 | +134.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 918 | +0.051 | +160.24€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 47 | -0.112 | -6.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 762 | -0.011 | -19.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 50 | -0.192 | +0.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 275 | +0.323 | +64.10€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 275 | +0.323 | +64.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 160 | +0.315 | +30.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 160 | +0.315 | +30.10€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 115 | +0.329 | +34.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 115 | +0.329 | +34.00€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 5883 | -0.063 | +1321.60€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 5883 | -0.063 | +1321.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 310 | -0.051 | +340.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 310 | -0.051 | +340.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1211 | -0.148 | -55.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1211 | -0.148 | -55.52€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 559 | +0.161 | +275.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 559 | +0.161 | +275.05€ | 2 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1911 | -0.061 | +386.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1911 | -0.061 | +386.57€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1811 | -0.085 | +366.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1811 | -0.085 | +366.31€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 57 | +0.059 | +3.08€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 57 | +0.059 | +3.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 57 | +0.059 | +3.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 57 | +0.059 | +3.08€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 466 | +0.286 | +369.30€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 466 | +0.286 | +369.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 265 | +0.283 | +206.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 265 | +0.283 | +206.97€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 201 | +0.288 | +162.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 201 | +0.288 | +162.33€ | 0 | 14 |
| ✅ UPDOWN_OU_5M | 643 | -0.100 | -74.24€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 643 | -0.100 | -74.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 310 | -0.077 | -35.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 310 | -0.077 | -35.00€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 159 | -0.047 | -8.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 159 | -0.047 | -8.23€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 56 | -0.172 | -9.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 56 | -0.172 | -9.06€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 51 | -0.179 | -7.91€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 51 | -0.179 | -7.91€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1424 | +0.294 | +625.49€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 458 | +0.226 | +22.35€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 472 | +0.276 | +139.65€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 494 | +0.373 | +463.49€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.085) — sin ventaja clara. oversold(IBS<0.3): IC=+0.029 n=3781 | neutral: IC=+0.005 n=4133 | overbought(IBS>0.7): IC=+0.090 n=4141
  - _Datos_: n=12519 IC=+0.043 PNL=+1326.45€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 209 celda(s) pasan gate riguroso completo de 1399 evaluadas (n>=40) y 2504 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.010 < 0.08 — monitorear
  - _Datos_: n=961 IC=+0.010 PNL=+22.26€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=472/15 IC=+0.276 PNL=+139.65€ | BTC: n=458/15 IC=+0.226 PNL=+22.35€ | SOL: n=494/15 IC=+0.373 PNL=+463.49€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 23 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 10562 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.043 n=68/60 | contraria IC=+0.138 n=45 | gap=-0.095 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=153, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 105 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=275/40 IC=-0.016 PNL=-4.59€ | BTC#60min: n=258/40 IC=+0.004 PNL=-1.26€ | SOL#60min: n=139/40 IC=-0.004 PNL=-0.06€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.065 n=161137 | tras_1loss IC=+0.052 n=126928 | tras_2loss IC=+0.017 n=56779/40 | gap=+0.048 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.001 n=965 | contrario_BTC IC=-0.006 n=856/40 | gap=-0.005 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.08 con n=107 PNL=+67.05€
  - _Datos_: n=107 IC=+0.188 PNL=+67.05€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=140 PNL=+57.56€
  - _Datos_: n=140 IC=+0.162 PNL=+57.56€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 24/25 ops en el filtro definido (IC actual=+0.269 PNL=+19.70€)
  - _Datos_: n=24 IC=+0.269 PNL=+19.70€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.1 con n=1202 PNL=+626.80€
  - _Datos_: n=1202 IC=+0.336 PNL=+626.80€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=87 IC=+0.039 PNL=+13.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=87 IC=+0.039 PNL=+13.95€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=30 IC=+0.219 PNL=+23.04€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=30 IC=+0.219 PNL=+23.04€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=10326 IC=+0.009 PNL=+284.50€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=10326 IC=+0.009 PNL=+284.50€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 2/15 ops en el filtro definido (IC actual=+0.025 PNL=+3.18€)
  - _Datos_: n=2 IC=+0.025 PNL=+3.18€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=530 IC=+0.004 PNL=-1.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=530 IC=+0.004 PNL=-1.58€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=142 IC=-0.042 PNL=-4.34€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=142 IC=-0.042 PNL=-4.34€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=185 IC=-0.035 PNL=+2.91€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=185 IC=-0.035 PNL=+2.91€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.1 con n=765 PNL=+261.01€
  - _Datos_: n=765 IC=+0.136 PNL=+261.01€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=204 IC=+0.073 PNL=+41.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=204 IC=+0.073 PNL=+41.48€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=431 IC=+0.070 PNL=+83.44€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=431 IC=+0.070 PNL=+83.44€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=2149 IC=+0.037 PNL=+225.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2149 IC=+0.037 PNL=+225.02€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=54 IC=-0.268 PNL=-10.60€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=54 IC=-0.268 PNL=-10.60€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=113 IC=-0.013 PNL=+8.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=113 IC=-0.013 PNL=+8.43€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=155 IC=+0.029 PNL=+9.66€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=155 IC=+0.029 PNL=+9.66€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 11/15 ops en el filtro definido (IC actual=+0.064 PNL=+1.63€)
  - _Datos_: n=11 IC=+0.064 PNL=+1.63€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2659 IC=-0.016 PNL=-42.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2659 IC=-0.016 PNL=-42.97€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=38 PNL=+9.28€
  - _Datos_: n=38 IC=+0.175 PNL=+9.28€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.217 n=44) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=44 IC=+0.217 PNL=+18.24€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2721 IC=+0.016 PNL=+120.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2721 IC=+0.016 PNL=+120.09€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=768 IC=+0.033 PNL=+23.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=768 IC=+0.033 PNL=+23.24€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=217 PNL=+62.59€
  - _Datos_: n=217 IC=+0.112 PNL=+62.59€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.08 con n=197 PNL=+20.42€
  - _Datos_: n=197 IC=+0.118 PNL=+20.42€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.08 con n=169 PNL=+57.77€
  - _Datos_: n=169 IC=+0.132 PNL=+57.77€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=27110 IC=+0.102 PNL=+8520.42€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27110 IC=+0.102 PNL=+8520.42€

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
  - _Estado_: n=1467 IC=+0.031 PNL=+81.07€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1467 IC=+0.031 PNL=+81.07€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.02 con n=412 PNL=+156.94€
  - _Datos_: n=412 IC=+0.130 PNL=+156.94€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=127 IC=-0.043 PNL=+34.76€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=127 IC=-0.043 PNL=+34.76€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=740 PNL=+659.46€
  - _Datos_: n=740 IC=+0.445 PNL=+659.46€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=2675 IC=+0.035 PNL=+234.27€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2675 IC=+0.035 PNL=+234.27€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.169 > 0.1 con n=1148 PNL=+456.11€
  - _Datos_: n=1148 IC=+0.169 PNL=+456.11€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.186 < -0.1 con n=68 PNL=+0.76€
  - _Datos_: n=68 IC=-0.186 PNL=+0.76€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=715 IC=+0.031 PNL=+76.29€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=715 IC=+0.031 PNL=+76.29€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=32 IC=-0.147 PNL=+4.20€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=32 IC=-0.147 PNL=+4.20€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=140 PNL=+33.32€
  - _Datos_: n=140 IC=+0.113 PNL=+33.32€

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
  - _Estado_: n=8153 IC=-0.140 PNL=+450.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8153 IC=-0.140 PNL=+450.08€

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
  - _Estado_: n=981 IC=+0.141 PNL=+524.24€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=981 IC=+0.141 PNL=+524.24€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.138 > 0.08 con n=727 PNL=+246.64€
  - _Datos_: n=727 IC=+0.138 PNL=+246.64€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=1038 IC=+0.004 PNL=+12.21€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1038 IC=+0.004 PNL=+12.21€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=975 PNL=+588.11€
  - _Datos_: n=975 IC=+0.086 PNL=+588.11€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=214 PNL=+83.53€
  - _Datos_: n=214 IC=+0.171 PNL=+83.53€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.237 < -0.1 con n=892 PNL=-112.10€
  - _Datos_: n=892 IC=-0.237 PNL=-112.10€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=2323 IC=+0.141 PNL=+1368.56€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=2323 IC=+0.141 PNL=+1368.56€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=48 PNL=+14.93€
  - _Datos_: n=48 IC=+0.100 PNL=+14.93€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=986 IC=+0.001 PNL=+117.54€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=986 IC=+0.001 PNL=+117.54€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=897 PNL=+608.87€
  - _Datos_: n=897 IC=+0.184 PNL=+608.87€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1477 IC=-0.058 PNL=+322.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1477 IC=-0.058 PNL=+322.48€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=324 PNL=-36.98€
  - _Datos_: n=324 IC=+0.110 PNL=-36.98€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=2084 PNL=-217.33€
  - _Datos_: n=2084 IC=+0.227 PNL=-217.33€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 19/40 ops en el filtro definido (IC actual=-0.068 PNL=+3.27€)
  - _Datos_: n=19 IC=-0.068 PNL=+3.27€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=336) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=336 IC=+0.101 PNL=+85.24€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.316 > 0.08 con n=112 PNL=+57.45€
  - _Datos_: n=112 IC=+0.316 PNL=+57.45€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.422 n=292) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=292 IC=+0.422 PNL=+403.70€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=4724 IC=+0.151 PNL=-726.63€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4724 IC=+0.151 PNL=-726.63€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.258 > 0.1 con n=64 PNL=+47.91€
  - _Datos_: n=64 IC=+0.258 PNL=+47.91€
