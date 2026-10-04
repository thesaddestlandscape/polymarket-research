# Hipótesis automáticas — 2026-10-04 13:20 UTC
_Generado por shadow_postmortem.py sobre 744530 resoluciones (PNL=+89957.74€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.222 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.133)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.133)

- **PATRÓN** `banda_hit_calibrado` > `0.8014` → IC=+0.263 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8014 (IC base=+0.133)

- **PATRÓN** `banda_z` > `9.189` → IC=+0.198 (n=210)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.189 (IC base=+0.133)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.716` → IC=+0.132 (n=561)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.716 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.135 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 11.0 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=663)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3816.3674` → IC=+0.145 (n=285)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3816.3674 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.228 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `42.0` → IC=+0.168 (n=468)

  - _Acción_: Kelly boost +0.84€ cuando `n_total_lado` > 42.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.6206` → IC=+0.261 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6206 (IC base=+0.141)

- **PATRÓN** `banda_z` > `9.932` → IC=+0.212 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.932 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.141 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 12.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=565)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4510.9366` → IC=+0.142 (n=227)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4510.9366 (IC base=+0.141)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=107)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=96)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1207.4096` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1207.4096 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.004)

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
- **FILTRO** `restante_s_al_confirmar` < `144.16` → IC=-0.216 (n=8252)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.16
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=24757)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `131.91` → IC=-0.269 (n=1065)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.91
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3195)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.35` → IC=-0.303 (n=971)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2915)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.79` → IC=-0.223 (n=2066)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.79
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6199)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.53` → IC=-0.324 (n=1601)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.53
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=4805)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.213 (n=16011)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=3847)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5409.9744` → IC=+0.170 (n=2497)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5409.9744 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=14005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=17151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=13129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6309)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7637.2914` → IC=+0.169 (n=2415)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7637.2914 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=1836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `16028.7692` → IC=+0.222 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16028.7692 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2357)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15958.35` → IC=+0.210 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15958.35 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.123 (n=1024)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.555 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.126 (n=249)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.091)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.092)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.135 (n=930)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.44 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `5732.4723` → IC=+0.151 (n=233)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 5732.4723 (IC base=+0.092)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.355 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.230 (n=1500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.362 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=716)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.257 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=910)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2166.1457` → IC=+0.155 (n=360)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2166.1457 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.212 (n=1468)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.407 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=649)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=801)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `1192.3838` → IC=+0.151 (n=236)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1192.3838 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.225 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=14079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=13472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.234 (n=4454)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=3328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3196)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.174)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.238 (n=1340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.236 (n=1345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.337 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.234)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=3272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.192 (n=1275)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.73 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.242)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=3196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=2749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=2419)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.195 (n=1160)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3895.4216` → IC=+0.443 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3895.4216 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.442 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `14878.5401` → IC=+0.441 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14878.5401 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.446 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.466 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.451 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3366.033 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.405 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.410 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.418 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.418 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.406)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=41879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=18467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=7217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=5821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.197 (n=7941)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.268 (n=4280)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=7620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7630)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=3763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.271 (n=2579)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2762)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=3207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=6433)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=5974)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.19 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6174)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.137 (n=5940)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.49 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=3226)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.127 (n=2963)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3074)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=3918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.19` → IC=+0.144 (n=2954)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.19 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.185 (n=3207)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.130 (n=3391)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=2997)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.289 (n=1286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4177.6236` → IC=+0.305 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4177.6236 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.279 (n=586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.333 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `4309.4335` → IC=+0.296 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4309.4335 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1423.7966` → IC=+0.300 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1423.7966 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.354 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.346)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.364 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.346)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.388 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.346)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.375 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.346)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.438 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.457 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.441 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `2152.0985` → IC=+0.456 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2152.0985 (IC base=+0.441)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=62)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.735` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=62)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4859` → IC=+0.130 (n=10034)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4859 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9841` → IC=+0.242 (n=3346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9841 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.3783` → IC=+0.254 (n=2616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3783 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.009` → IC=+0.183 (n=3816)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 6.009 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.250 (n=2808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2117 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.254 (n=2809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.226 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.4655` → IC=+0.211 (n=7017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4655 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.137 (n=12179)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5676 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5841` → IC=+0.202 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5841 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.177 (n=4027)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.1948` → IC=+0.178 (n=4430)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1948 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1674` → IC=+0.218 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1674 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.8742` → IC=+0.196 (n=5065)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.8742 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4488` → IC=+0.198 (n=7598)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4488 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.213 (n=7399)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.217 (n=751)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=747)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3503` → IC=+0.184 (n=2237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3503 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=1081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.185 (n=1499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.209` → IC=+0.287 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.209 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.224 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4344` → IC=+0.181 (n=2114)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4344 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2294)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2042.27` → IC=+0.189 (n=746)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2042.27 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.242 (n=1590)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1252` → IC=+0.263 (n=783)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1252 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0605` → IC=+0.283 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0605 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.481` → IC=+0.244 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.481 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.236 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.231 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.261 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.6113` → IC=+0.247 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6113 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=1949)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1595.2` → IC=+0.244 (n=1779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1595.2 (IC base=+0.232)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.238 (n=778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.351` → IC=+0.229 (n=1766)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.351 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=1768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.979` → IC=+0.258 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.979 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.218 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.3442` → IC=+0.221 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3442 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.772` → IC=+0.256 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.772 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2505` → IC=+0.222 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2505 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.221 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.4169` → IC=+0.241 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4169 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.183 (n=595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0741` → IC=+0.165 (n=592)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0741 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7206` → IC=+0.174 (n=1774)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.7206 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1267` → IC=+0.153 (n=1591)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1267 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.323` → IC=+0.139 (n=283)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 11.323 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.143 (n=1630)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.147 (n=1774)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2035 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.137 (n=1775)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6206 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.172 (n=477)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.149 (n=1663)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.144 (n=1110)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.171 (n=700)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 231.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.200 (n=2254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=2373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2028)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.344` → IC=+0.256 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.344 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.193 (n=1971)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.202 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.1684` → IC=+0.205 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1684 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2691)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `1948.2131` → IC=+0.195 (n=1021)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1948.2131 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.220 (n=1748)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.1762` → IC=+0.218 (n=874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1762 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=930)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.233 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.240 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.348` → IC=+0.253 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.348 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.217 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7571` → IC=+0.222 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7571 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1939.1684` → IC=+0.212 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1939.1684 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.211 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=120)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2684)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.155 (n=430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0036 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9604` → IC=+0.221 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9604 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.5234` → IC=+0.324 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5234 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.909` → IC=+0.174 (n=889)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.909 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.333 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.324 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1119` → IC=+0.333 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1119 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.353 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.8429` → IC=+0.323 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8429 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.326 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1014` → IC=+0.158 (n=702)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1014 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.314` → IC=+0.196 (n=324)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.314 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8486` → IC=+0.151 (n=735)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8486 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.198 (n=147)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.163 (n=936)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5239 (IC base=+0.025)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.189 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=411)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.194 (n=119)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=364)

- **FILTRO** `ibs_20min` > `0.2368` → IC=-0.126 (n=2715)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=1339)

- **FILTRO** `sigma_ewma_delta_pct` > `8.793` → IC=-0.218 (n=427)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.793
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3627)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.333` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.333 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.266 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8803 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.6436` → IC=+0.277 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6436 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1482` → IC=+0.285 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1482 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.5444` → IC=+0.281 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5444 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.279 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.2368` → IC=+0.132 (n=1339)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2368 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.1732` → IC=+0.258 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1732 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.276 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1602` → IC=+0.309 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1602 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.4196` → IC=+0.291 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4196 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.641` → IC=-0.175 (n=711)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.641
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2136)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.201 (n=687)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2160)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.208 (n=1037)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=3171)

- **PATRÓN** `dist_vwap_pct` > `0.783` → IC=+0.320 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.783 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.1984` → IC=+0.316 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1984 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9872` → IC=+0.293 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9872 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.309 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.300 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4628` → IC=+0.296 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4628 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8487` → IC=+0.301 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8487 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8565` → IC=+0.286 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8565 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.7206` → IC=+0.249 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7206 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.0722` → IC=+0.271 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0722 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0997` → IC=+0.264 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0997 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.1456` → IC=+0.254 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1456 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.252 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.42 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.199 (n=4361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0095 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.188 (n=11680)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4706 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.9917` → IC=+0.285 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9917 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.681` → IC=+0.157 (n=5952)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.681 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1766` → IC=+0.247 (n=4760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1766 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6147` → IC=+0.253 (n=4759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6147 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.0805` → IC=+0.242 (n=7039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0805 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.262 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6437` → IC=+0.255 (n=2561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6437 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7230)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.165 (n=4223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.009 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5462` → IC=+0.156 (n=11129)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5462 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.6888` → IC=+0.248 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6888 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2369` → IC=+0.247 (n=3640)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2369 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7073` → IC=+0.248 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7073 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.1951` → IC=+0.258 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1951 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2954` → IC=+0.303 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2954 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5911` → IC=+0.277 (n=2318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5911 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.279 (n=5164)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.159 (n=906)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2723)

- **FILTRO** `ibs_20min` > `0.761` → IC=-0.174 (n=741)

  - _Acción_: SKIP cuando `ibs_20min` > 0.761
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2229)

- **FILTRO** `sigma_ewma_delta_pct` > `4.574` → IC=-0.174 (n=667)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.574
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2303)

- **PATRÓN** `ibs_20min` > `0.9069` → IC=+0.278 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9069 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.223` → IC=+0.199 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.223 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2273` → IC=+0.272 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2273 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.208 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1956` → IC=+0.232 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1956 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.230 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0804` → IC=+0.419 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0804 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2235` → IC=+0.429 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2235 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.5483` → IC=+0.430 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5483 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.5399` → IC=+0.427 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5399 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.429 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.159 (n=877)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8641 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1111` → IC=+0.189 (n=673)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1111 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6758` → IC=+0.179 (n=1099)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6758 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0741` → IC=+0.168 (n=1133)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0741 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.220 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.196 (n=403)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4378` → IC=+0.184 (n=403)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.4378 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.224 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 229.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.225 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `0.6127` → IC=+0.226 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6127 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.221 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.287 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.4405` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4405 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1719` → IC=+0.233 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1719 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.271 (n=1988)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.255 (n=1784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=1781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.778` → IC=+0.280 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.778 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.265 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `1.6236` → IC=+0.258 (n=1900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6236 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `2009.8728` → IC=+0.271 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.8728 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.301 (n=1653)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.299 (n=728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.321 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.292 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.287 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.692` → IC=+0.294 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.692 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.1948` → IC=+0.281 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1948 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1197` → IC=+0.290 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1197 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.7245` → IC=+0.298 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7245 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.297 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1933.4584` → IC=+0.306 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.4584 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.287 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7715` → IC=-0.185 (n=754)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2269)

- **PATRÓN** `ibs_20min` > `0.9033` → IC=+0.172 (n=682)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.9033 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.3814` → IC=+0.232 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3814 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0072` → IC=+0.251 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0072 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.1683` → IC=+0.237 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1683 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.0821` → IC=+0.250 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0821 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4092` → IC=+0.264 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4092 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.262 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 140.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1259` → IC=+0.234 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1259 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1801` → IC=+0.218 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1801 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.1699` → IC=+0.271 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1699 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8338` → IC=+0.268 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8338 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.253 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.76` → IC=-0.184 (n=1388)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.284 (n=1390)

- **FILTRO** `ibs_20min` > `0.675` → IC=-0.242 (n=695)

  - _Acción_: SKIP cuando `ibs_20min` > 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2093)

- **FILTRO** `sigma_ewma_delta_pct` > `4.818` → IC=-0.204 (n=592)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.818
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2196)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.284 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.2146` → IC=+0.319 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2146 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.69` → IC=+0.171 (n=438)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.69 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8598` → IC=+0.311 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8598 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.304 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.302 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.313 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4244` → IC=+0.320 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4244 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.323 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.132 (n=1841)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.2679` → IC=+0.240 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2679 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.273 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1866` → IC=+0.230 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1866 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.257 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.251 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.260 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.020)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.329 (n=1434)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.305 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.317 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2135` → IC=+0.319 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2135 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.755` → IC=+0.310 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.755 (IC base=+0.285)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.299 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.331 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.296 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2473.4216` → IC=+0.297 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2473.4216 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.323 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.315 (n=1131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.286 (n=747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.289 (n=1614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.308 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.3099` → IC=+0.295 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3099 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.513` → IC=+0.298 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.513 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.285 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.315 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.329 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.293 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.282 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2430.3904` → IC=+0.288 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2430.3904 (IC base=+0.283)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.187 (n=3268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.205 (n=3268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3566` → IC=+0.184 (n=8624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3566 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=10216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5707` → IC=+0.225 (n=9799)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5707 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1715` → IC=+0.197 (n=4240)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1715 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.412` → IC=+0.252 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.412 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.167 (n=6518)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2075 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.163 (n=6519)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6297 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.197 (n=1455)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5628` → IC=+0.172 (n=4155)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5628 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6089` → IC=+0.183 (n=3148)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6089 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1979.3384` → IC=+0.177 (n=8754)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1979.3384 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.189 (n=8709)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 105.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.187 (n=6240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0066 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.0801` → IC=+0.219 (n=3116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0801 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=3570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.4865` → IC=+0.229 (n=9345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4865 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1689` → IC=+0.167 (n=6483)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1689 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.307` → IC=+0.196 (n=1569)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.307 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.161 (n=6700)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1777 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.214 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5582` → IC=+0.172 (n=3807)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5582 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6164` → IC=+0.175 (n=2883)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6164 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.181 (n=8312)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 107.0 (IC base=+0.173)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.243 (n=551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.204 (n=549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3413` → IC=+0.220 (n=1646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3413 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=1104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9141` → IC=+0.287 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9141 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.239` → IC=+0.331 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.239 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.245 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.197 (n=1539)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2043.0977` → IC=+0.202 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2043.0977 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.248 (n=1097)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.247 (n=1246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.102` → IC=+0.294 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.102 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=1112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.262 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.39` → IC=+0.244 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.39 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.221` → IC=+0.247 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.221 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.262 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.238 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1593.12` → IC=+0.255 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1593.12 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.227 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0689` → IC=+0.196 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0689 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=1471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3933` → IC=+0.223 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3933 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1978` → IC=+0.208 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1978 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.528` → IC=+0.232 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.528 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6891` → IC=+0.167 (n=647)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6891 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.195 (n=231)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4139` → IC=+0.183 (n=478)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4139 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `11907.94` → IC=+0.160 (n=1314)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11907.94 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `435.0` → IC=+0.159 (n=1393)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 435.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.160 (n=1540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2943` → IC=+0.164 (n=1540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2943 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=725)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.195 (n=1540)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5915 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1334` → IC=+0.168 (n=1520)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1334 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.196 (n=304)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.160 (n=1540)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2116 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.2271` → IC=+0.143 (n=1581)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2271 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0699` → IC=+0.147 (n=689)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0699 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.151 (n=1429)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=451)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.232 (n=546)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2452` → IC=+0.221 (n=1093)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2452 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.5` → IC=+0.279 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.5 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1276` → IC=+0.208 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1276 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.217 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `1940.595` → IC=+0.213 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1940.595 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.239 (n=1234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1427` → IC=+0.258 (n=617)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1427 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.246 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.254 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.259 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.7484` → IC=+0.236 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7484 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.7483` → IC=+0.229 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7483 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1933.4584` → IC=+0.226 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.4584 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.215 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.182 (n=1387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0065 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4204` → IC=+0.165 (n=1573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4204 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.339` → IC=+0.204 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.339 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1409` → IC=+0.186 (n=1030)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1409 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.220 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.164 (n=1049)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8561 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1017` → IC=+0.172 (n=657)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1017 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.169 (n=514)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.161 (n=514)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5109.0415` → IC=+0.192 (n=1049)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 5109.0415 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.154 (n=1511)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 152.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=1640)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0071 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.383` → IC=+0.146 (n=1638)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.383 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6652` → IC=+0.180 (n=1638)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6652 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1489` → IC=+0.149 (n=1598)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1489 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.878` → IC=+0.166 (n=570)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.878 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.154 (n=1092)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8548 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.182 (n=243)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8136` → IC=+0.139 (n=1009)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8136 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5391` → IC=+0.132 (n=504)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5391 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `4266.2624` → IC=+0.159 (n=1092)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4266.2624 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.123 (n=1453)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 151.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.158 (n=814)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.01 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4512` → IC=+0.128 (n=1577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4512 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.214 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `1.064` → IC=+0.216 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.064 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.874` → IC=+0.259 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.874 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2054` → IC=+0.137 (n=1792)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2054 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.6492` → IC=+0.131 (n=1792)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6492 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.133 (n=1803)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0708` → IC=+0.127 (n=744)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0708 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5413` → IC=+0.144 (n=762)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5413 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=1873)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2388.4402` → IC=+0.182 (n=1195)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2388.4402 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.145 (n=1433)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 47.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.160 (n=792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0061 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1027` → IC=+0.178 (n=600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1027 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.217 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5789 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.1985` → IC=+0.147 (n=1648)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1985 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.338` → IC=+0.132 (n=549)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 5.338 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.153 (n=601)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6382 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2274` → IC=+0.158 (n=314)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2274 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4487` → IC=+0.139 (n=549)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4487 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.126 (n=549)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3065.2583` → IC=+0.191 (n=600)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3065.2583 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.128 (n=1601)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.229 (n=1681)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.2885` → IC=+0.216 (n=1121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2885 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.215 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.245 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.212 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1937 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6239` → IC=+0.219 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6239 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.269 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.4722` → IC=+0.213 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4722 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.8094` → IC=+0.220 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8094 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2466.2754` → IC=+0.209 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2466.2754 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.228 (n=760)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.216 (n=781)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0909` → IC=+0.240 (n=575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0909 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4267` → IC=+0.244 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4267 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.232 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.252 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.7031` → IC=+0.222 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7031 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.273 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.212 (n=1578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2408.5954` → IC=+0.218 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2408.5954 (IC base=+0.212)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.192 (n=1132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0042 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.171 (n=860)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0084 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3417` → IC=+0.178 (n=2263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3417 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=1264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.3438` → IC=+0.196 (n=2571)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3438 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.7932` → IC=+0.189 (n=410)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.7932 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.756` → IC=+0.194 (n=1123)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.756 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.190 (n=1529)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8725 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2092` → IC=+0.175 (n=764)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.2092 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.175 (n=685)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.183 (n=832)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.823` → IC=+0.173 (n=1663)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.823 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2923)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2688.5612` → IC=+0.169 (n=2297)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2688.5612 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.186 (n=2349)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 143.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.156 (n=881)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0037 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=2486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.192 (n=881)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0714 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.145 (n=855)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2751.2995` → IC=+0.126 (n=2359)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2751.2995 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.123 (n=1108)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 28.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.199 (n=304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.3296` → IC=+0.165 (n=690)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3296 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.203 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.2873` → IC=+0.167 (n=241)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2873 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.170 (n=298)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.892` → IC=+0.175 (n=460)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.892 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.1571` → IC=+0.149 (n=718)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1571 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.147 (n=273)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.2382` → IC=+0.153 (n=592)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.2382 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.5183` → IC=+0.153 (n=601)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5183 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `10658.416` → IC=+0.155 (n=690)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10658.416 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.197 (n=292)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 152.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.160 (n=825)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=832)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.611` → IC=+0.181 (n=726)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.611 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1811` → IC=+0.156 (n=811)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1811 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.074` → IC=+0.146 (n=753)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.074 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.146 (n=825)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2185 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6939` → IC=+0.154 (n=737)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6939 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.194 (n=220)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.159 (n=717)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.412` → IC=+0.146 (n=815)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.412 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=1068)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11929.6805` → IC=+0.143 (n=737)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11929.6805 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `356.0` → IC=+0.152 (n=793)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 356.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.259 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2091` → IC=+0.222 (n=538)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2091 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.6723` → IC=+0.251 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6723 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.3636` → IC=+0.219 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3636 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2076` → IC=+0.207 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2076 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.333` → IC=+0.229 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.333 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.8432` → IC=+0.217 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8432 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.220 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.182 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.235 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.239 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.1092` → IC=+0.227 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1092 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.121 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.125 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 11.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.148 (n=254)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.0873 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.144 (n=335)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6872 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.134 (n=121)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3957.4133` → IC=+0.123 (n=679)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3957.4133 (IC base=+0.097)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4762` → IC=-0.122 (n=265)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4762
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=519)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.158 (n=407)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0071 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.172 (n=610)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0051 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.159 (n=608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.9532` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9532 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.363` → IC=+0.218 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.363 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.176 (n=535)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0671 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.6528` → IC=+0.166 (n=608)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6528 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.175 (n=266)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=643)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3079.1777` → IC=+0.193 (n=203)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3079.1777 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.4762` → IC=+0.145 (n=519)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.4762 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.5687` → IC=+0.122 (n=247)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.5687 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `2865.6878` → IC=+0.151 (n=267)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2865.6878 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.124 (n=360)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 23.0 (IC base=+0.055)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.172 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0238 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.188 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.007 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.169 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.188 (n=171)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5556 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2434` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.2434 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.164 (n=212)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.737` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.737 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.177 (n=190)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6182 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.2526` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2526 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `2503.9142` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2503.9142 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.160 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0119 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.126 (n=212)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6515 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2293` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2293 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.8124` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.8124 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.177 (n=4228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0046 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.211 (n=4223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=13242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9938` → IC=+0.308 (n=4222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9938 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.9062` → IC=+0.200 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9062 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.904` → IC=+0.240 (n=4559)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.904 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2317` → IC=+0.165 (n=8488)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2317 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.200 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.5937` → IC=+0.197 (n=4081)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5937 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1812.5048` → IC=+0.180 (n=12661)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1812.5048 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.203 (n=9965)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.191 (n=7593)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1473` → IC=+0.192 (n=5009)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1473 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=4278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4528` → IC=+0.246 (n=10018)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4528 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2434` → IC=+0.163 (n=7068)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2434 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.053` → IC=+0.203 (n=1599)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.053 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.731` → IC=+0.183 (n=10988)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.731 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.162 (n=3398)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.705 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.247 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.188 (n=7075)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8611 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1745.6284` → IC=+0.183 (n=11382)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1745.6284 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=6909)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.249 (n=706)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.228 (n=703)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.210 (n=2104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=1013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.669` → IC=+0.353 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.669 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.267 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.5691` → IC=+0.216 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5691 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2042.3486` → IC=+0.219 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.3486 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.222 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.262 (n=1147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1721)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1255` → IC=+0.280 (n=758)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1255 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3605` → IC=+0.283 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3605 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.509` → IC=+0.263 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.509 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.291 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.255 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6242` → IC=+0.276 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6242 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1595.0002` → IC=+0.269 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1595.0002 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.209 (n=686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1809` → IC=+0.162 (n=1354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1809 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2865` → IC=+0.204 (n=2030)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2865 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.186 (n=1159)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.761` → IC=+0.180 (n=342)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.761 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.2` → IC=+0.150 (n=1856)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.2 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.7033` → IC=+0.167 (n=893)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7033 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.193 (n=291)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1425` → IC=+0.158 (n=1736)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1425 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5157` → IC=+0.153 (n=1763)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5157 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `277.0` → IC=+0.174 (n=842)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 277.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.3284` → IC=+0.157 (n=1696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3284 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.2934` → IC=+0.240 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2934 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.164 (n=1541)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.156 (n=286)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.315` → IC=+0.146 (n=1540)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.315 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.158 (n=1696)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1913 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1532` → IC=+0.200 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1532 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.432` → IC=+0.155 (n=1597)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.432 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.158 (n=1064)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `414.0` → IC=+0.144 (n=1320)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 414.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.253 (n=691)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=1866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.846` → IC=+0.294 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.846 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.2061` → IC=+0.224 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2061 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.7674` → IC=+0.232 (n=1779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7674 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1947.8684` → IC=+0.232 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1947.8684 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.241 (n=1711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.245 (n=857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.301 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.177` → IC=+0.276 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.177 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.296 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.235 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.241 (n=1213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1933.8384` → IC=+0.245 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.8384 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.234 (n=1759)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=954)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.153 (n=2166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2719` → IC=+0.189 (n=2165)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2719 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.553` → IC=+0.162 (n=599)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.553 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.591` → IC=+0.160 (n=348)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.591 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8735` → IC=+0.164 (n=1444)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8735 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2367` → IC=+0.185 (n=392)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2367 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.161 (n=927)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.154 (n=955)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7393.0386` → IC=+0.234 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7393.0386 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.180 (n=691)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 71.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.166 (n=1161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0051 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4436` → IC=+0.142 (n=1741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4436 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.5985` → IC=+0.195 (n=1533)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5985 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1494` → IC=+0.134 (n=1521)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1494 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.298` → IC=+0.165 (n=264)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.298 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6226` → IC=+0.143 (n=581)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6226 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2974` → IC=+0.226 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2974 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.2491` → IC=+0.132 (n=1466)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2491 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4439` → IC=+0.140 (n=1666)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4439 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `8971.7775` → IC=+0.199 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8971.7775 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.131 (n=1666)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 168.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.143 (n=1450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.008 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5637` → IC=+0.130 (n=2174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.5637 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.463` → IC=+0.201 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.463 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0494` → IC=+0.212 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0494 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.574` → IC=+0.245 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.574 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2303` → IC=+0.137 (n=2174)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2303 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1608` → IC=+0.129 (n=2241)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1608 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.5712` → IC=+0.125 (n=931)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.5712 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4578` → IC=+0.128 (n=2116)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4578 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2212)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2549.0292` → IC=+0.235 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2549.0292 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.145 (n=1349)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 42.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.180 (n=689)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.164 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5128` → IC=+0.234 (n=1817)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5128 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2176` → IC=+0.139 (n=1700)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2176 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.469` → IC=+0.130 (n=1989)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.469 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.645` → IC=+0.166 (n=689)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.645 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.185 (n=331)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.151` → IC=+0.136 (n=1670)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.151 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2799.1755` → IC=+0.197 (n=688)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2799.1755 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.135 (n=1656)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.119)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.231 (n=2120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.218 (n=1539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.2089` → IC=+0.236 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2089 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.744` → IC=+0.261 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.744 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.2351` → IC=+0.218 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2351 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.222 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.243 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.5092` → IC=+0.248 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5092 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2463.6549` → IC=+0.219 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2463.6549 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.220 (n=743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.229 (n=1009)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.226 (n=1572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.261 (n=1961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `1.2051` → IC=+0.217 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2051 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.212` → IC=+0.215 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.212 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.252 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.2299` → IC=+0.238 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2299 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.280 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4305` → IC=+0.210 (n=2034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4305 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2414.7926` → IC=+0.214 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2414.7926 (IC base=+0.211)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=3725)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.223 (n=1242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.5036` → IC=+0.194 (n=3712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.5036 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.241 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.191 (n=1389)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.223` → IC=+0.214 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.223 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7118` → IC=+0.188 (n=1125)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.7118 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8955` → IC=+0.184 (n=1705)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8955 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1688` → IC=+0.210 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1688 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.192 (n=1221)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.187 (n=2442)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8611 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=2770)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2918.8634` → IC=+0.189 (n=3316)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2918.8634 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.219 (n=939)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.4861` → IC=+0.179 (n=2806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.4861 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.186 (n=1235)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1827 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.6568` → IC=+0.181 (n=524)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6568 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.214` → IC=+0.171 (n=2799)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.214 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2581` → IC=+0.168 (n=2641)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2581 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.168 (n=2560)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.164 (n=581)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5361` → IC=+0.170 (n=1219)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5361 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.827` → IC=+0.173 (n=1847)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.827 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=3725)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `12371.7726` → IC=+0.168 (n=935)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 12371.7726 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.171 (n=2404)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 207.0 (IC base=+0.163)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.236 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0805` → IC=+0.266 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0805 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.215 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.231 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.516 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.7635` → IC=+0.213 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7635 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.3179` → IC=+0.217 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3179 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.529` → IC=+0.212 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.529 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.219 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.596` → IC=+0.219 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.596 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.231 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `12550.0528` → IC=+0.235 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12550.0528 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.229 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.366` → IC=+0.165 (n=1056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.366 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.181 (n=465)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1485 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.153 (n=479)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6084 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.2114` → IC=+0.151 (n=1071)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2114 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.168 (n=1038)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.188 (n=704)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8812 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2218` → IC=+0.180 (n=220)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2218 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.5397` → IC=+0.157 (n=1052)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5397 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.167 (n=701)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11518.9437` → IC=+0.162 (n=1056)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11518.9437 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `696.0` → IC=+0.160 (n=1010)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 696.0 (IC base=+0.149)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.188 (n=213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.180 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.01 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.173 (n=637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.242 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.56` → IC=+0.231 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.56 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.204 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.6711` → IC=+0.173 (n=212)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.6711 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8234` → IC=+0.171 (n=567)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8234 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2429.8516` → IC=+0.204 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2429.8516 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1988` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1988 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.220 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1515` → IC=+0.211 (n=518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1515 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.204 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5305 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.196 (n=393)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.8854 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.2041` → IC=+0.202 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2041 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.199 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `1.0851` → IC=+0.196 (n=1036)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.0851 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.2457` → IC=+0.194 (n=393)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.2457 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.205 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.4777` → IC=+0.197 (n=1154)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.4777 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=1184)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.226 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.190 (n=945)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.174 (n=634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 10.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.7559` → IC=+0.170 (n=945)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7559 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.0897` → IC=+0.171 (n=945)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0897 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.6046` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6046 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.3831` → IC=+0.167 (n=973)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3831 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.153` → IC=+0.168 (n=1052)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 9.153 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6432` → IC=+0.203 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6432 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.166 (n=844)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7259 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.180 (n=815)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.167 (n=617)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `7437.397` → IC=+0.179 (n=945)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7437.397 (IC base=+0.165)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.160 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.011 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.162 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 3.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.134 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.5833` → IC=+0.189 (n=332)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5833 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.5213` → IC=+0.210 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5213 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7119 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.282` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.282 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.220 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.4285` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4285 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=440)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2958.069` → IC=+0.160 (n=372)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2958.069 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.147 (n=355)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 60.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.192 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0067 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.6689` → IC=+0.179 (n=300)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.6689 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.164 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 16.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.2667` → IC=+0.224 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2667 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.631` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.631 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.164 (n=290)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.3839` → IC=+0.169 (n=300)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.3839 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.219 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.6095` → IC=+0.179 (n=129)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.6095 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3170.0512` → IC=+0.195 (n=300)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3170.0512 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.216 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.161)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.161 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.4702` → IC=+0.159 (n=1115)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.4702 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.147 (n=615)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.192 (n=258)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.188 (n=152)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `1366.0299` → IC=+0.120 (n=727)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1366.0299 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.2295` → IC=+0.256 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2295 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.1082` → IC=+0.140 (n=456)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1082 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.931` → IC=+0.139 (n=380)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.931 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.1432` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1432 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.6041` → IC=+0.151 (n=391)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.6041 (IC base=+0.051)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.141 (n=413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0057 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4395` → IC=+0.172 (n=382)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4395 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1188` → IC=+0.165 (n=207)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1188 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.0809` → IC=+0.136 (n=300)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.0809 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.121 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0052 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.304 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.132 (n=237)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.802` → IC=+0.162 (n=208)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.802 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` < `1.1357` → IC=+0.125 (n=214)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.1357 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `0.802` → IC=+0.141 (n=143)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.802 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.155 (n=192)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.083)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=151)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.152 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.7051` → IC=+0.218 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7051 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.281 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.807` → IC=+0.132 (n=245)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.807 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.7849` → IC=+0.141 (n=210)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7849 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.156 (n=324)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7058 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.011` → IC=-0.245 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=139)

- **FILTRO** `ibs_20min` > `0.2051` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2051
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=108)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.171 (n=244)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.7778 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.7456` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.7456 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.631` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.631 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.053)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.161 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0088 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.264 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2051 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` < `0.1772` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1772 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.6637` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6637 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.9805` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.9805 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.6676` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6676 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` > `1.8779` → IC=+0.200 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8779 (IC base=+0.048)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.06 (IC base=+0.048)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.241 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=83)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=228)

- **FILTRO** `volumen_regimen` < `0.7363` → IC=-0.355 (n=60)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7363
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=183)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.368 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=158)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.251 (n=175)

- **FILTRO** `sigma_ewma_delta_pct` > `10.458` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.458
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=184)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=98)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.238 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=65)

- **FILTRO** `ibs_20min` > `0.92` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.92
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=65)

- **FILTRO** `sigma_ewma_delta_pct` > `2.482` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.482
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

- **FILTRO** `volumen_regimen` > `0.8507` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8507
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=65)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7738` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=57)

- **FILTRO** `ibs_20min` > `0.5972` → IC=-0.350 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5972
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

- **FILTRO** `libro_liquidez` < `1289.9986` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 1289.9986
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=53)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.179)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=68)

- **FILTRO** `ibs_20min` < `0.2444` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2444
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=57)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.177 (n=165)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0058 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6466` → IC=+0.145 (n=364)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6466 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.4822` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4822 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6625` → IC=+0.132 (n=123)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6625 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.8223` → IC=+0.140 (n=176)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8223 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.127 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 12.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.180 (n=326)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.156 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.682` → IC=+0.201 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.682 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.6713` → IC=+0.126 (n=295)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.6713 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.182 (n=168)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.082)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6361` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6361
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=108)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.187 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0024 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.223 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1524 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1082` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1082 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.0797` → IC=+0.151 (n=170)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.0797 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.611` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 4.611 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1471` → IC=+0.155 (n=166)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1471 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.6733` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6733 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1891` → IC=+0.204 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1891 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.6869` → IC=+0.191 (n=134)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.6869 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.176 (n=134)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.149)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1654` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1654
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=92)

- **FILTRO** `libro_liquidez` < `1457.1387` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 1457.1387
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=114)

- **PATRÓN** `volumen_spike_ratio` < `1.8267` → IC=+0.123 (n=59)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8267 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `1457.1387` → IC=+0.121 (n=114)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1457.1387 (IC base=+0.045)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.152 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 12.0 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.1906` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1906 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.489` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.489 (IC base=+0.063)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0941` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0941
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=31)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.273 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.250 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.92` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.92 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.025` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.025 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.1205` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1205 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.662` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.662 (IC base=-0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0941` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0941 (IC base=-0.034)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `193.1` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.1 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.360 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.281)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.226)

- **PATRÓN** `elapsed_s` > `177.0` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 177.0 (IC base=+0.226)

- **PATRÓN** `elapsed_s` < `177.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 177.0 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.318 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `1457.0` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1457.0 (IC base=+0.226)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `193.1` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.1 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.8028` → IC=+0.360 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8028 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.281)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.226)

- **PATRÓN** `elapsed_s` > `177.0` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 177.0 (IC base=+0.226)

- **PATRÓN** `elapsed_s` < `177.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 177.0 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.318 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `1457.0` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1457.0 (IC base=+0.226)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=951)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2927.8455` → IC=+0.153 (n=327)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2927.8455 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=951)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2927.8455` → IC=+0.153 (n=327)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2927.8455 (IC base=+0.107)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=147)

- **FILTRO** `libro_liquidez` < `9493.103` → IC=-0.179 (n=107)

  - _Acción_: SKIP cuando `libro_liquidez` < 9493.103
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=231)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=217)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=50)

- **FILTRO** `liq_n` < `5.0` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `liq_n` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=23)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=96)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2516)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=52)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=84)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=95)

- **FILTRO** `ballena_activa_n` > `555.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 555.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=99)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.124 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 15.0 (IC base=+0.050)

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

- **PATRÓN** `liq_usd_total` > `128179.75` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 128179.75 (IC base=+0.059)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.161 (n=160)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.495 (IC base=+0.059)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=991)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=945)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9855` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9855
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `142.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 142.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=583)

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
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=293)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.495 (IC base=+0.030)

- **PATRÓN** `libro_liquidez` > `3914.0347` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3914.0347 (IC base=+0.030)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=754)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=754)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.131 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=592)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=491)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=491)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=207)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=207)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=169)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=134)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=121)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=145)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=118)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=131)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=290)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=290)

- **FILTRO** `libro_liquidez` < `553.2637` → IC=-0.136 (n=105)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.2637
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=215)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=178)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.48` → IC=-0.120 (n=1399)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=780)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.125 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=57)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=202)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.45 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.042)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.125 (n=86)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=56)

- **FILTRO** `restante_min` < `10.05` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 10.05
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=96)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=98)

- **PATRÓN** `py_entrada` < `0.53` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.53 (IC base=+0.017)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=106)

- **FILTRO** `restante_min` < `3.99` → IC=-0.133 (n=107)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `lag_apertura_s` > `60.75` → IC=-0.137 (n=111)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.75
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=38)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.5 (IC base=+0.085)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.150 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=50)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.208 (n=63)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=128)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=160)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.146 (n=156)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=92)

- **FILTRO** `restante_min` < `3.44` → IC=-0.211 (n=81)

  - _Acción_: SKIP cuando `restante_min` < 3.44
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=167)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=192)

- **FILTRO** `lag_apertura_s` > `88.83` → IC=-0.209 (n=84)

  - _Acción_: SKIP cuando `lag_apertura_s` > 88.83
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=164)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `lag_apertura_s` < `90.78` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 90.78 (IC base=-0.019)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.156 (n=155)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=86)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.5 (IC base=-0.047)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.222 (n=77)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=217)

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

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.475` → IC=-0.162 (n=4473)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=13581)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=4498)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=14179)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.192 (n=791)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2406)

- **PATRÓN** `libro_liquidez` > `1806.8572` → IC=+0.132 (n=1087)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1806.8572 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1583.845` → IC=+0.144 (n=1135)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1583.845 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.180 (n=785)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=2458)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.199 (n=789)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2598)

- **PATRÓN** `libro_liquidez` > `1805.3584` → IC=+0.129 (n=1103)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1805.3584 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.164 (n=768)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=2422)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2441)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3181)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=284)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1948.8168` → IC=-0.174 (n=326)

  - _Acción_: SKIP cuando `libro_liquidez` < 1948.8168
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=664)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=231)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.037)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=12655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=28045)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=9554)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=31146)

- **FILTRO** `ibs_7min` < `0.2619` → IC=-0.234 (n=10175)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2619
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=30525)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=13753)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=26947)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.236 (n=12565)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=39059)

- **FILTRO** `ibs_7min` > `0.2903` → IC=-0.181 (n=12898)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=38726)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=2060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4849)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1651)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=5258)

- **FILTRO** `ibs_7min` < `0.7089` → IC=-0.250 (n=2278)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7089
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4631)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.183 (n=1544)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5365)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.265 (n=2193)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6730)

- **FILTRO** `ibs_7min` > `0.788` → IC=-0.210 (n=2230)

  - _Acción_: SKIP cuando `ibs_7min` > 0.788
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6693)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5299)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1708)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5252)

- **FILTRO** `ibs_7min` < `0.7429` → IC=-0.198 (n=1740)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5220)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.179 (n=1722)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=5238)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.267 (n=1667)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5422)

- **FILTRO** `ibs_7min` > `0.2646` → IC=-0.195 (n=1772)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2646
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5317)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.190 (n=1764)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5325)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.161 (n=1871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4687)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=1558)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5000)

- **FILTRO** `ibs_7min` < `0.7032` → IC=-0.246 (n=2163)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7032
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4395)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.214 (n=1514)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5044)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2179)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7351)

- **FILTRO** `ibs_7min` > `0.741` → IC=-0.173 (n=2381)

  - _Acción_: SKIP cuando `ibs_7min` > 0.741
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=7149)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=2171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4522)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.238 (n=1993)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4700)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.187 (n=1673)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5020)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.179 (n=1625)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5068)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1706)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5181)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.180 (n=1720)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5167)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.184 (n=1687)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5200)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1725)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=5188)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1692)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5221)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2347)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=7495)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.274 (n=1575)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=5092)

- **FILTRO** `ibs_7min` < `0.2571` → IC=-0.222 (n=1666)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2571
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=5001)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1656)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5011)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.211 (n=2163)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=7190)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1216)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=611)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7920.2009` → IC=-0.129 (n=346)

  - _Acción_: SKIP cuando `libro_liquidez` < 7920.2009
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=703)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=341)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.138 (n=150)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=293)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.159 (n=162)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=488)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.135 (n=903)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.139 (n=411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `442.2457` → IC=+0.147 (n=301)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 442.2457 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.129 (n=769)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 53.0 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.438` → IC=+0.171 (n=71)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.438 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.224 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.137 (n=224)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.04 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2596.4012` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2596.4012 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.170 (n=95)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 12.0 (IC base=+0.137)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 10.0 (IC base=+0.110)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.188 (n=123)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 73.0 (IC base=+0.115)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.173 (n=163)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.144)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 8043.774 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 28.0 (IC base=+0.144)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.139 (n=156)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.098)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.120 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `3602.5746` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3602.5746 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=114)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.234 (n=333)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=165)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0052` → IC=-0.262 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=50)

- **FILTRO** `T_h` > `88.6528` → IC=-0.397 (n=37)

  - _Acción_: SKIP cuando `T_h` > 88.6528
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=112)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.269 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=-0.083)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.083)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `pct_vs_K` |x|> `8.662` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.662
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.196 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.7615` → IC=-0.250 (n=114)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7615
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=345)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.304 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=302)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.314 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=302)

- **FILTRO** `T_h` > `58.2176` → IC=-0.315 (n=301)

  - _Acción_: SKIP cuando `T_h` > 58.2176
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=101)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `68.7654` → IC=-0.145 (n=119)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=41)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=121)

- **FILTRO** `sigma_h` > `0.0056` → IC=-0.327 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=74)

- **FILTRO** `T_h` > `143.6315` → IC=-0.304 (n=49)

  - _Acción_: SKIP cuando `T_h` > 143.6315
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=98)

- **FILTRO** `T_h` < `96.6729` → IC=-0.340 (n=48)

  - _Acción_: SKIP cuando `T_h` < 96.6729
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=99)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9851` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=97)

- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=98)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `135.1248` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `T_h` > 135.1248
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

- **FILTRO** `pct_vs_K` |x|> `3.7818` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7818
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=76)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.352 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

- **FILTRO** `T_h` > `49.3573` → IC=-0.385 (n=59)

  - _Acción_: SKIP cuando `T_h` > 49.3573
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.469 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.349)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.398 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.349)

- **PATRÓN** `T_h` > `1.2173` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2173 (IC base=+0.349)

- **PATRÓN** `dist_50` > `0.4086` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4086 (IC base=+0.349)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.369 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.349)

- **PATRÓN** `edge` > `0.096` → IC=+0.454 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.421)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.434 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.421)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.449 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.421)

- **PATRÓN** `T_h` < `0.608` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.421)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.450 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.421)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.483 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.475 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.421)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1078` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1078 (IC base=+0.422)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.409 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.422)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.455 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.422)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.4166` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4166 (IC base=+0.422)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.422)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.436)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.469 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.436)

- **PATRÓN** `T_h` > `0.801` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.801 (IC base=+0.436)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.436)

- **PATRÓN** `edge` > `0.1155` → IC=+0.471 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.487 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.464)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.465 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4578` → IC=+0.491 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4578 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.469 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=239)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=331)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.149 (n=146)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.034)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=24)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=50)

- **FILTRO** `volumen_racha` > `2314731.8` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_racha` > 2314731.8
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

- **FILTRO** `streak_estiramiento` > `0.4315` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4315
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=43)

- **PATRÓN** `streak_estiramiento` < `0.4315` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4315 (IC base=-0.014)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 48.0 (IC base=+0.065)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=88)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=535)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `3.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `libro_liquidez` < `2775.6672` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2775.6672
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=759)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=907)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=901)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3354)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1746)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.211 (n=734)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.243 (n=733)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.1592` → IC=+0.207 (n=1936)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1592 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2217` → IC=+0.216 (n=733)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2217 (IC base=+0.203)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1289` → IC=+0.232 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1289 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=2037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=2280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.6197` → IC=+0.283 (n=2199)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6197 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.205 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.817` → IC=+0.276 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.817 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2943.5682` → IC=+0.209 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2943.5682 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.224 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.203)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=940)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.230 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.281 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.217)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2017` → IC=+0.248 (n=208)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2017 (IC base=+0.217)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.265 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.278 (n=458)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.269 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.607` → IC=+0.285 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.607 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.255 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.217)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.834` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.834
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=561)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.201 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.067` → IC=+0.164 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.067 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2358` → IC=+0.183 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.2358 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1204` → IC=+0.165 (n=186)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1204 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5797` → IC=+0.238 (n=495)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5797 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.2769` → IC=+0.158 (n=457)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2769 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.56` → IC=+0.233 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.56 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3426.0142` → IC=+0.162 (n=442)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3426.0142 (IC base=+0.147)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.300 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1521` → IC=+0.211 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1521 (IC base=+0.185)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0716` → IC=+0.196 (n=248)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.0716 (IC base=+0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3519` → IC=+0.237 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3519 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_15` > `0.587` → IC=+0.274 (n=277)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.587 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.201 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.3257` → IC=+0.185 (n=268)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.3257 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.359 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=294)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `3077.8574` → IC=+0.289 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3077.8574 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.225 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.185)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.255 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0807` → IC=+0.224 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0807 (IC base=+0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0432` → IC=+0.218 (n=555)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0432 (IC base=+0.213)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0888` → IC=+0.268 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0888 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.213)

- **PATRÓN** `ibs_15` > `0.5854` → IC=+0.295 (n=555)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5854 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.223 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.303` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.303 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.318` → IC=+0.216 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.318 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2924.6824` → IC=+0.286 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2924.6824 (IC base=+0.213)

- **PATRÓN** `ibs_15` < `0.1145` → IC=+0.145 (n=607)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` < 0.1145 (IC base=+0.060)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.371 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.364 (n=507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.360 (n=341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.385 (n=338)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.388 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.396 (n=507)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.389 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.369 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.358)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.375 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `444.0` → IC=+0.379 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 444.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.112` → IC=+0.364 (n=123)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.112 (IC base=+0.363)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.370 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.364 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.374 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.363)

- **PATRÓN** `drift_15min` |x|≤ `0.5146` → IC=+0.367 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5146 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1537` → IC=+0.382 (n=185)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1537 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.382 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.393 (n=278)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.405 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.106` → IC=+0.371 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.106 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.384 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.417 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.354 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.351)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.369 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.351)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.365 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.351)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.370 (n=206)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.351)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.377 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.351)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.411 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.351)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.401 (n=230)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` < `0.2948` → IC=+0.352 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2948 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.366 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.354 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.357 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.351)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.359 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.351)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.220 (n=820)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=2462)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.201 (n=1180)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2102)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1416` → IC=+0.182 (n=530)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.1416 (IC base=-0.062)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.245 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.062)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.279 (n=795)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.197 (n=456)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1051 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` < `0.2631` → IC=+0.202 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2631 (IC base=-0.062)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.251 (n=824)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1831` → IC=+0.248 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1831 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.273 (n=2478)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.649` → IC=+0.291 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.649 (IC base=-0.022)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.208 (n=481)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1446)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.225 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1446)

- **FILTRO** `sigma_ewma_delta_pct` > `23.695` → IC=-0.260 (n=273)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.695
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1654)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.175 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0027 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.300 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.314 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.124 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 12.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.333 (n=237)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.289 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2377` → IC=+0.278 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2377 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0841` → IC=+0.176 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0841 (IC base=-0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.193)

- **PATRÓN** `ibs_15` < `0.501` → IC=+0.306 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.501 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.0553` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0553 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.193)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.169 (n=497)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.165 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0064 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.172 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0038 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0735` → IC=+0.215 (n=170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0735 (IC base=+0.159)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.160 (n=386)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.159)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.221 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.185 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 11.0 (IC base=+0.159)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.261 (n=387)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` < `0.2726` → IC=+0.171 (n=357)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2726 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=497)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3758.6556` → IC=+0.163 (n=345)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3758.6556 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.241 (n=920)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4431` → IC=+0.235 (n=920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4431 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.245 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.208` → IC=+0.259 (n=417)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.208 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.235 (n=652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.234 (n=629)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.266 (n=920)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.7436` → IC=+0.309 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7436 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.287` → IC=+0.268 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.287 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.489` → IC=+0.236 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.489 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.201 (n=577)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=193)

- **FILTRO** `drift_60min` |x|> `0.1672` → IC=-0.241 (n=261)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1672
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=509)

- **FILTRO** `drift_15min` |x|> `0.8849` → IC=-0.273 (n=192)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8849
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=578)

- **FILTRO** `sigma_ewma_delta_pct` > `18.27` → IC=-0.143 (n=407)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.27
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3271)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.159 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.175)

- **PATRÓN** `ibs_15` > `0.6071` → IC=+0.224 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6071 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1248` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1248 (IC base=-0.175)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 44.0 (IC base=-0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0785` → IC=+0.228 (n=362)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0785 (IC base=-0.041)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1866` → IC=+0.228 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1866 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.270 (n=407)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.667` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.667 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.171` → IC=+0.230 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.171 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0194` → IC=-0.260 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=466)

- **FILTRO** `drift_60min` |x|> `0.1549` → IC=-0.204 (n=231)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1549
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=699)

- **FILTRO** `drift_15min` |x|> `1.2211` → IC=-0.274 (n=232)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2211
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=698)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.200)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.147` → IC=+0.270 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.147 (IC base=-0.033)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1698` → IC=+0.303 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1698 (IC base=-0.033)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.292 (n=628)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` > `0.8316` → IC=+0.351 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8316 (IC base=-0.033)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.031)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.031)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.305 (n=546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.329 (n=273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2408` → IC=+0.307 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2408 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.221` → IC=+0.316 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.221 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.327 (n=819)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.436` → IC=+0.337 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.436 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.343 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12848.0159` → IC=+0.304 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12848.0159 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.298 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.336 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2575` → IC=+0.308 (n=149)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2575 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.304 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.317 (n=447)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4139` → IC=+0.352 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4139 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.328 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.308 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.299 (n=332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.004 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1077` → IC=+0.312 (n=248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1077 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.322 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.326 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8732` → IC=+0.350 (n=332)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8732 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.308 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.324 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0878` → IC=-0.263 (n=74)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0878
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=226)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=131)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0682` → IC=-0.145 (n=60)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0682
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=133)

- **FILTRO** `drift_15min` |x|> `0.3691` → IC=-0.265 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3691
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1819` → IC=-0.260 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1819
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=24)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2557` → IC=-0.145 (n=29)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2557
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.214 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1195` → IC=-0.206 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1195
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3593` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3593
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3119` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3119
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `80.0063` → IC=+0.231 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.215)

- **PATRÓN** `ratio` < `0.9752` → IC=+0.471 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9752 (IC base=+0.215)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.320 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.6969` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.6969 (IC base=+0.196)

- **PATRÓN** `ratio` < `0.972` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.196)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.296 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.289)

- **PATRÓN** `ratio` > `1.0057` → IC=+0.273 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0057 (IC base=+0.289)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `82.5234` → IC=+0.271 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.249)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.431 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.249)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.343 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.354 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6197 sube el IC de +0.203 a +0.283 en UPDOWN_GBM#15min (n=2199). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.217 a +0.278 en UPDOWN_GBM#BTC#15min (n=458). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5797 sube el IC de +0.147 a +0.238 en UPDOWN_GBM#ETH#15min (n=495). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.587 sube el IC de +0.185 a +0.274 en UPDOWN_GBM#SOL#15min (n=277). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5854 sube el IC de +0.213 a +0.295 en UPDOWN_GBM#XRP#15min (n=555). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.062 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=795). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.022 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=2478). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.088 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=237). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.193 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.159 a +0.261 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=387). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.234 a +0.266 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=920). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.6071 sube el IC de -0.175 a +0.224 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.270 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=407). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.200 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.033 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=628). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.292 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=819). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.288 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=447). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8732 sube el IC de +0.297 a +0.350 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=332). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.358 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=507). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.363 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=278). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.351 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=230). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1522 | +0.098 | +196.84€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1522 | +0.098 | +196.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1156 | +0.105 | +169.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1156 | +0.105 | +169.93€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 263 | +0.066 | +11.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 263 | +0.066 | +11.20€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 130 | +0.023 | +24.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 130 | +0.023 | +24.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 106 | +0.028 | +20.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 106 | +0.028 | +20.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 33009 | -0.089 | -4342.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1689 | -0.018 | -217.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 31320 | -0.093 | -4125.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4260 | -0.117 | -719.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4260 | -0.117 | -719.41€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1689 | -0.018 | -217.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1689 | -0.018 | -217.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3886 | -0.112 | -868.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3886 | -0.112 | -868.57€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8503 | -0.004 | -767.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8503 | -0.004 | -767.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8265 | -0.107 | -554.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8265 | -0.107 | -554.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6406 | -0.164 | -1214.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6406 | -0.164 | -1214.24€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 24704 | -0.021 | +3651.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6393 | +0.001 | +1730.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 18311 | -0.028 | +1921.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 24704 | -0.021 | +3651.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6393 | +0.001 | +1730.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 18311 | -0.028 | +1921.05€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 112850 | +0.113 | -5136.96€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15968 | +0.183 | -486.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 477 | -0.053 | -60.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 89352 | +0.102 | -4318.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7053 | +0.104 | -272.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14840 | +0.102 | -1089.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 52 | -0.130 | +12.55€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14773 | +0.103 | -1089.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22435 | +0.131 | -337.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4820 | +0.199 | -121.17€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14816 | +0.116 | -129.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2757 | +0.091 | -64.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14887 | +0.093 | -1233.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 60 | -0.113 | -5.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14812 | +0.094 | -1216.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23973 | +0.124 | -434.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6419 | +0.176 | -103.21€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14981 | +0.106 | -261.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2561 | +0.099 | -60.69€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21857 | +0.114 | -1202.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4563 | +0.187 | -278.99€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 380 | -0.016 | -6.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15179 | +0.094 | -770.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1735 | +0.130 | -147.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14858 | +0.101 | -840.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 54 | -0.036 | +10.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14791 | +0.102 | -850.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 18014 | +0.194 | -1121.25€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 18014 | +0.194 | -1121.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4195 | +0.174 | -392.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4195 | +0.174 | -392.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1887 | +0.203 | -22.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1887 | +0.203 | -22.72€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4132 | +0.181 | -339.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4132 | +0.181 | -339.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3645 | +0.242 | -120.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3645 | +0.242 | -120.82€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4076 | +0.190 | -259.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4076 | +0.190 | -259.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 844 | +0.430 | -23.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 844 | +0.430 | -23.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 334 | +0.438 | -3.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 334 | +0.438 | -3.75€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 319 | +0.435 | -5.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 319 | +0.435 | -5.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 179 | +0.406 | -11.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 179 | +0.406 | -11.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 62447 | +0.199 | -4672.48€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 62447 | +0.199 | -4672.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10750 | +0.182 | -1153.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10750 | +0.182 | -1153.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10030 | +0.224 | -349.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10030 | +0.224 | -349.59€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10748 | +0.176 | -1217.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10748 | +0.176 | -1217.85€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10098 | +0.220 | -381.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10098 | +0.220 | -381.63€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10343 | +0.203 | -670.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10343 | +0.203 | -670.36€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10478 | +0.193 | -899.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10478 | +0.193 | -899.06€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 23743 | +0.116 | +149.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 23743 | +0.116 | +149.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11787 | +0.120 | +142.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11787 | +0.120 | +142.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11956 | +0.112 | +7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11956 | +0.112 | +7.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1709 | +0.288 | -26.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1709 | +0.288 | -26.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 769 | +0.280 | -17.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 769 | +0.280 | -17.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 825 | +0.286 | -12.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 825 | +0.286 | -12.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 764 | +0.439 | -0.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 764 | +0.439 | -0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 366 | +0.438 | -1.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 366 | +0.438 | -1.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 352 | +0.441 | +0.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 352 | +0.441 | +0.91€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1308 | +0.071 | -57.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 469 | +0.058 | -37.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 839 | +0.078 | -20.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1026 | +0.077 | -27.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 187 | +0.071 | -7.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 839 | +0.078 | -20.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 216 | +0.032 | -31.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 216 | +0.032 | -31.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 45319 | +0.100 | -1189.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3681 | +0.092 | +46.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 41638 | +0.100 | -1236.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 25165 | +0.104 | -300.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3681 | +0.092 | +46.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21484 | +0.106 | -347.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8920 | +0.109 | -25.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8920 | +0.109 | -25.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11234 | +0.082 | -863.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11234 | +0.082 | -863.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 865 | +0.206 | -102.69€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 865 | +0.206 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 865 | +0.206 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 865 | +0.206 | -102.69€ | 1 | 4 |
| ✅ GBM_LATE_15M | 31828 | +0.088 | +15741.57€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 31828 | +0.088 | +15741.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5353 | +0.202 | +4108.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5353 | +0.202 | +4108.33€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4719 | +0.177 | +3368.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4719 | +0.177 | +3368.89€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 5649 | +0.199 | +4238.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5649 | +0.199 | +4238.79€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4515 | +0.032 | +1147.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4515 | +0.032 | +1147.94€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4537 | -0.032 | +992.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4537 | -0.032 | +992.57€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7055 | -0.036 | +1885.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7055 | -0.036 | +1885.06€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 34282 | +0.087 | +18273.46€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 34282 | +0.087 | +18273.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6599 | +0.012 | +3427.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6599 | +0.012 | +3427.33€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7117 | +0.014 | +1511.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7117 | +0.014 | +1511.79€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4853 | +0.267 | +4972.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4853 | +0.267 | +4972.62€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5749 | +0.010 | +1280.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5749 | +0.010 | +1280.37€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5566 | +0.035 | +2242.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5566 | +0.035 | +2242.48€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4398 | +0.284 | +4838.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4398 | +0.284 | +4838.88€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 25524 | +0.173 | +19761.92€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 25524 | +0.173 | +19761.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3853 | +0.217 | +3226.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3853 | +0.217 | +3226.80€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4013 | +0.149 | +2900.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4013 | +0.149 | +2900.85€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4053 | +0.213 | +3301.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4053 | +0.213 | +3301.79€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4280 | +0.137 | +3151.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4280 | +0.137 | +3151.28€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4787 | +0.123 | +3489.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4787 | +0.123 | +3489.69€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4538 | +0.210 | +3691.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4538 | +0.210 | +3691.51€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6948 | +0.137 | +3267.61€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6948 | +0.137 | +3267.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2018 | +0.143 | +1077.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2018 | +0.143 | +1077.71€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2087 | +0.152 | +1016.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2087 | +0.152 | +1016.44€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1594 | +0.107 | +571.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1594 | +0.107 | +571.86€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 535 | +0.135 | +236.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 535 | +0.135 | +236.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 32057 | +0.179 | +24627.33€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 32057 | +0.179 | +24627.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5094 | +0.230 | +4513.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5094 | +0.230 | +4513.64€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4966 | +0.147 | +3213.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4966 | +0.147 | +3213.96€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5352 | +0.227 | +4638.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5352 | +0.227 | +4638.84€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5206 | +0.135 | +3630.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5206 | +0.135 | +3630.26€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5648 | +0.122 | +3900.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5648 | +0.122 | +3900.04€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5791 | +0.213 | +4730.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5791 | +0.213 | +4730.58€ | 0 | 23 |
| ✅ GBM_LATE_5M | 8688 | +0.174 | +5798.03€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8688 | +0.174 | +5798.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2097 | +0.169 | +1525.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2097 | +0.169 | +1525.17€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2828 | +0.179 | +1866.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2828 | +0.179 | +1866.92€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 894 | +0.146 | +504.32€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 894 | +0.146 | +504.32€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2310 | +0.074 | +849.31€ | 0 | 12 |
| ✅ GBM_LATE_60M#60min | 2310 | +0.074 | +849.31€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 867 | +0.093 | +317.24€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 867 | +0.093 | +317.24€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 731 | +0.073 | +332.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 731 | +0.073 | +332.13€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 712 | +0.052 | +199.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 712 | +0.052 | +199.94€ | 2 | 14 |
| 🚫 GBM_LATE_60M_FADE | 452 | -0.240 | -11.08€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 452 | -0.240 | -11.08€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 166 | -0.220 | -5.99€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 166 | -0.220 | -5.99€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 157 | -0.230 | -0.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 157 | -0.230 | -0.38€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 129 | -0.271 | -4.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 129 | -0.271 | -4.71€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 978 | +0.089 | +257.35€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 978 | +0.089 | +257.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 363 | +0.081 | +79.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 363 | +0.081 | +79.86€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 324 | +0.055 | +39.89€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 324 | +0.055 | +39.89€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 291 | +0.135 | +137.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 291 | +0.135 | +137.61€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2655 | +0.103 | +702.23€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2655 | +0.103 | +702.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2655 | +0.103 | +702.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2655 | +0.103 | +702.23€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 415 | -0.073 | -33.23€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 415 | -0.073 | -33.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 111 | -0.040 | -2.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 111 | -0.040 | -2.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 155 | -0.029 | -5.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 155 | -0.029 | -5.55€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2717 | +0.024 | +78.85€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2717 | +0.024 | +78.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 135 | +0.033 | -0.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 135 | +0.033 | -0.10€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 396 | +0.038 | +35.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 396 | +0.038 | +35.91€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1040 | +0.032 | +31.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1040 | +0.032 | +31.06€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 623 | +0.015 | +2.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 623 | +0.015 | +2.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 322 | +0.022 | +15.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 322 | +0.022 | +15.64€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1340 | -0.045 | -30.03€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1340 | -0.045 | -30.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 382 | -0.042 | -13.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 382 | -0.042 | -13.37€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 445 | -0.026 | -0.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 445 | -0.026 | -0.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 513 | -0.065 | -16.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 513 | -0.065 | -16.31€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4183 | -0.019 | +69.17€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1978 | -0.023 | +12.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2205 | -0.017 | +57.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 118 | -0.008 | +2.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 61 | +0.040 | +8.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 57 | -0.059 | -5.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1026 | -0.003 | +41.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 485 | -0.009 | +8.99€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 541 | +0.003 | +32.24€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 472 | -0.017 | +13.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 231 | -0.024 | +2.72€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 241 | -0.010 | +10.51€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 850 | -0.032 | -15.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 388 | -0.046 | -21.10€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 462 | -0.019 | +6.08€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 823 | -0.025 | +10.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 399 | -0.029 | +4.55€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 424 | -0.021 | +5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 894 | -0.025 | +17.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 414 | -0.019 | +8.97€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 480 | -0.029 | +8.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 36731 | -0.004 | +1739.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 36731 | -0.004 | +1739.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6534 | +0.024 | +867.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6534 | +0.024 | +867.94€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5515 | -0.032 | -80.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5515 | -0.032 | -80.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6630 | +0.018 | +641.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6630 | +0.018 | +641.38€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5302 | -0.053 | -168.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5302 | -0.053 | -168.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6186 | -0.008 | +208.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6186 | -0.008 | +208.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6564 | +0.012 | +270.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6564 | +0.012 | +270.35€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6124 | -0.059 | -145.46€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6124 | -0.059 | -145.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1496 | -0.079 | -34.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1496 | -0.079 | -34.50€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 704 | -0.126 | -34.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 704 | -0.126 | -34.31€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1807 | -0.076 | -31.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1807 | -0.076 | -31.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 855 | -0.016 | -25.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 855 | -0.016 | -25.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3348 | +0.004 | -2.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3348 | +0.004 | -2.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 190 | +0.016 | +0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 190 | +0.016 | +0.21€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1317 | +0.006 | +6.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1317 | +0.006 | +6.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 92324 | -0.073 | +1658.61€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 92324 | -0.073 | +1658.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15832 | -0.074 | +921.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15832 | -0.074 | +921.87€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14049 | -0.098 | -805.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14049 | -0.098 | -805.23€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 16088 | -0.066 | +878.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 16088 | -0.066 | +878.60€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13580 | -0.094 | -375.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13580 | -0.094 | -375.45€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16755 | -0.052 | +337.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16755 | -0.052 | +337.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 16020 | -0.063 | +701.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 16020 | -0.063 | +701.75€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7994 | -0.030 | -144.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7994 | -0.030 | -144.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1889 | -0.043 | -18.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1889 | -0.043 | -18.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1094 | -0.047 | -21.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1094 | -0.047 | -21.11€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 770 | -0.022 | -24.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 770 | -0.022 | -24.88€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1338 | +0.116 | +494.85€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1202 | +0.122 | +482.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 282 | +0.137 | +141.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 282 | +0.137 | +141.30€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 226 | +0.110 | +65.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 226 | +0.110 | +65.51€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 245 | +0.115 | +98.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 245 | +0.115 | +98.12€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 217 | +0.144 | +111.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 217 | +0.144 | +111.48€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 232 | +0.098 | +65.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 232 | +0.098 | +65.84€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 850 | -0.016 | -20.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 850 | -0.016 | -20.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 166 | +0.000 | +6.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 166 | +0.000 | +6.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 119 | -0.012 | -2.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 119 | -0.012 | -2.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 232 | -0.034 | -15.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 232 | -0.034 | -15.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 189 | +0.013 | +4.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 189 | +0.013 | +4.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 144 | -0.048 | -12.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 144 | -0.048 | -12.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 716 | -0.092 | -65.10€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 326 | -0.146 | -77.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 255 | -0.189 | -72.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 254 | -0.051 | -1.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 183 | -0.057 | -4.31€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 71 | -0.034 | +2.83€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 136 | -0.036 | +14.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 108 | -0.054 | +8.12€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 546 | -0.119 | -68.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 170 | -0.006 | +3.87€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 861 | -0.201 | -47.19€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 357 | -0.194 | -31.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 307 | -0.196 | -31.46€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 292 | -0.218 | -29.97€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 251 | -0.227 | -35.81€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 212 | -0.187 | +14.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 194 | -0.184 | +10.42€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 752 | -0.204 | -56.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 355 | +0.402 | +289.03€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 91 | +0.371 | +75.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 91 | +0.371 | +75.92€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 224 | +0.460 | +214.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 224 | +0.460 | +214.35€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 355 | +0.402 | +289.03€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 608 | +0.026 | +15.17€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 608 | +0.026 | +15.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 64 | -0.015 | -2.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 64 | -0.015 | -2.20€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 206 | +0.038 | +14.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 206 | +0.038 | +14.31€ | 3 | 3 |
| ✅ STREAK_FADE_5M | 3053 | -0.023 | -125.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3053 | -0.023 | -125.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 904 | -0.022 | -32.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 904 | -0.022 | -32.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 578 | -0.026 | -25.22€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 578 | -0.026 | -25.22€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1415 | -0.020 | -53.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1415 | -0.020 | -53.65€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9543 | +0.019 | +107.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9543 | +0.019 | +107.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2623 | +0.021 | +27.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2623 | +0.021 | +27.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2210 | +0.029 | +50.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2210 | +0.029 | +50.33€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2860 | +0.010 | -0.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2860 | +0.010 | -0.30€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1850 | +0.021 | +29.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1850 | +0.021 | +29.19€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8557 | +0.013 | -45.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8557 | +0.013 | -45.34€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3373 | +0.016 | -8.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3373 | +0.016 | -8.97€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3404 | +0.012 | -21.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3404 | +0.012 | -21.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1780 | +0.007 | -15.15€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1780 | +0.007 | -15.15€ | 1 | 0 |
| ✅ UPDOWN_GBM | 53530 | +0.042 | +3973.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13464 | +0.077 | +2806.30€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1788 | +0.006 | +9.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 34959 | +0.035 | +1124.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3130 | +0.005 | +37.62€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5440 | +0.079 | +723.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1050 | +0.157 | +467.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4357 | +0.060 | +257.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 10304 | +0.049 | +812.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1726 | +0.090 | +398.20€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 480 | +0.012 | +4.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6609 | +0.051 | +373.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1418 | +0.006 | +35.32€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 71 | -0.089 | +0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6338 | +0.052 | +501.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1020 | +0.138 | +368.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5290 | +0.036 | +133.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11771 | +0.032 | +630.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3302 | +0.054 | +447.54€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 473 | +0.007 | +8.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6873 | +0.029 | +171.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1061 | +0.004 | -0.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 62 | -0.125 | +2.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11940 | +0.021 | +415.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3200 | +0.030 | +270.18€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 463 | -0.001 | -0.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7572 | +0.021 | +148.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 651 | +0.005 | +2.89€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 54 | -0.161 | -4.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7735 | +0.049 | +891.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3166 | +0.096 | +854.08€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 311 | +0.005 | -1.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4258 | +0.017 | +39.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 187 | -0.124 | -2.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 676 | +0.358 | +237.55€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 676 | +0.358 | +237.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 370 | +0.363 | +128.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 370 | +0.363 | +128.15€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 306 | +0.351 | +109.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 306 | +0.351 | +109.40€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 15090 | -0.031 | +3438.52€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 15090 | -0.031 | +3438.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1141 | -0.059 | +378.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1141 | -0.059 | +378.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2680 | -0.114 | +108.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2680 | -0.114 | +108.37€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 628 | +0.200 | +470.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 628 | +0.200 | +470.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1740 | +0.212 | +1111.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1740 | +0.212 | +1111.86€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4448 | -0.064 | +608.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4448 | -0.064 | +608.25€ | 4 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4453 | -0.068 | +760.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4453 | -0.068 | +760.81€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 173 | +0.026 | +6.12€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 173 | +0.026 | +6.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 173 | +0.026 | +6.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 173 | +0.026 | +6.12€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1091 | +0.292 | +903.53€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1091 | +0.292 | +903.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 596 | +0.288 | +458.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 596 | +0.288 | +458.87€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 495 | +0.297 | +444.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 495 | +0.297 | +444.65€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 756 | -0.114 | -84.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 756 | -0.114 | -84.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 72 | -0.162 | -9.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 72 | -0.162 | -9.27€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 81 | -0.187 | -7.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 81 | -0.187 | -7.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2823 | +0.307 | +1399.95€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 994 | +0.260 | +149.29€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1079 | +0.299 | +475.76€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 750 | +0.378 | +774.90€ | 0 | 1 |