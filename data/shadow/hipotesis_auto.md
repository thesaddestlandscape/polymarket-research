# Hipótesis automáticas — 2026-10-03 17:01 UTC
_Generado por shadow_postmortem.py sobre 731861 resoluciones (PNL=+88211.67€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.222 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.218 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.802` → IC=+0.260 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.802 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.204` → IC=+0.197 (n=209)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.204 (IC base=+0.132)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.723` → IC=+0.133 (n=556)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.723 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.132 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=652)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4916.8647` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4916.8647 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.229 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.197 (n=229)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 67.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.7976` → IC=+0.264 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7976 (IC base=+0.141)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=557)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2876.7023` → IC=+0.141 (n=441)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2876.7023 (IC base=+0.141)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.229 (n=105)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=94)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=113)

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

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.120)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.250 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.120)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `banda_z` > 6.043 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.178 (n=113)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `1207.4096` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1207.4096 (IC base=+0.120)

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
- **FILTRO** `restante_s_al_confirmar` < `144.43` → IC=-0.218 (n=8145)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.43
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=24440)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `132.61` → IC=-0.267 (n=1053)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.61
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3162)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.8` → IC=-0.310 (n=963)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.8
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2890)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.88` → IC=-0.220 (n=2027)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.88
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6084)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.7` → IC=-0.326 (n=1581)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.7
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=4746)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.212 (n=15831)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=3812)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `5445.9162` → IC=+0.171 (n=2472)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5445.9162 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=16845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=12944)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6253)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7661.4913` → IC=+0.169 (n=2392)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7661.4913 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1827)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.222 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=1647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2348)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15960.1808` → IC=+0.209 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15960.1808 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=391)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `4614.6151` → IC=+0.127 (n=247)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4614.6151 (IC base=+0.091)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.095)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=917)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.095)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=3294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.355 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=1476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.364 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.257 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=895)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1316.2002` → IC=+0.145 (n=781)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1316.2002 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.405 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=799)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.225 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=13852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=11806)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.227 (n=5899)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=3096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=3110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=3144)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.246 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.236 (n=1298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.340 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.235)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=3055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=3082)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2570)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.243)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2022)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=2381)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1142)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `11651.323` → IC=+0.457 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11651.323 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.448 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.456 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `14792.1345` → IC=+0.446 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14792.1345 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.446 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.465 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.450 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.422 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.409 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.411)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.417 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.411)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.411)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `4.0` → IC=-0.300 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=41270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=18086)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=7105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=5710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.196 (n=7802)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.267 (n=4199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7515)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=3707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=2513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2699)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=3149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=6320)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=6065)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.136 (n=5843)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.49 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=3180)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.125 (n=2911)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.16 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3021)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=3847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.2` → IC=+0.143 (n=2912)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.2 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.182 (n=3140)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.129 (n=3331)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.133 (n=2954)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.288 (n=1270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4188.4802` → IC=+0.304 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4188.4802 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.349 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `3797.228` → IC=+0.292 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3797.228 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=639)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1716.9381` → IC=+0.309 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1716.9381 (IC base=+0.287)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.441 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.456 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.456 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `1965.9066` → IC=+0.458 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.9066 (IC base=+0.442)

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
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=60)

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
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=60)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4912` → IC=+0.130 (n=9862)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4912 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.244 (n=3288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.981 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.256 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.015` → IC=+0.184 (n=3750)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.015 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.251 (n=2756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6158` → IC=+0.253 (n=2755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6158 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.228 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.4617` → IC=+0.212 (n=6889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4617 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5682` → IC=+0.137 (n=11980)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5682 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5959` → IC=+0.203 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5959 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1508` → IC=+0.176 (n=3983)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1508 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.178 (n=4345)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1942 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.05` → IC=+0.177 (n=1970)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.05 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1665` → IC=+0.221 (n=2092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1665 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.2745` → IC=+0.196 (n=6548)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2745 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.446` → IC=+0.198 (n=7443)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.446 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.212 (n=7239)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 119.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.217 (n=736)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.185 (n=735)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3519` → IC=+0.184 (n=2197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3519 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=1060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.184 (n=1470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.279 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.289 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.222 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.182 (n=2074)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2253)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2040.64` → IC=+0.187 (n=733)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2040.64 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1252` → IC=+0.267 (n=767)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1252 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.285 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.481` → IC=+0.241 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.481 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.381` → IC=+0.238 (n=1821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.381 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0926` → IC=+0.230 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0926 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.261 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.5704` → IC=+0.242 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5704 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1590.9711` → IC=+0.244 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1590.9711 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.240 (n=766)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.246 (n=766)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=1744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9785` → IC=+0.260 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9785 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.349` → IC=+0.219 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.349 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.762` → IC=+0.254 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.762 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2501` → IC=+0.221 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2501 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.220 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.238 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3944` → IC=+0.239 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3944 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `11120.3502` → IC=+0.219 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11120.3502 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.185 (n=588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.167 (n=586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7204` → IC=+0.174 (n=1756)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.7204 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1283` → IC=+0.155 (n=1582)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1283 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.140 (n=281)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.144 (n=1614)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.148 (n=1756)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2035 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8505` → IC=+0.139 (n=1170)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8505 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.174 (n=470)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4453` → IC=+0.148 (n=1645)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4453 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7746` → IC=+0.147 (n=1096)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7746 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14181.4555` → IC=+0.142 (n=1170)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14181.4555 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.172 (n=690)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.200 (n=2214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=2215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.261 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.194 (n=1941)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3472` → IC=+0.203 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3472 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.7627` → IC=+0.200 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7627 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2643)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `1945.272` → IC=+0.193 (n=1004)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 1945.272 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.220 (n=1718)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.1319` → IC=+0.220 (n=651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1319 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.231 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.686` → IC=+0.238 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.686 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3463` → IC=+0.250 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3463 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.72` → IC=+0.216 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.72 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.221 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1936.341` → IC=+0.214 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1936.341 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.211 (n=1751)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=120)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2645)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.152 (n=423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0037 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9556` → IC=+0.218 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9556 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1962` → IC=+0.330 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1962 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.896` → IC=+0.172 (n=873)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.896 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.332 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.326 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.345 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.350 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.8416` → IC=+0.327 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8416 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.330 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1014` → IC=+0.157 (n=692)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1014 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.3255` → IC=+0.198 (n=319)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3255 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.150 (n=718)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8471 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `1.1666` → IC=+0.143 (n=359)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1666 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.197 (n=143)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5175` → IC=+0.163 (n=914)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5175 (IC base=+0.023)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=401)

- **FILTRO** `ibs_20min` < `0.3111` → IC=-0.183 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3111
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=354)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.126 (n=2668)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=1318)

- **FILTRO** `sigma_ewma_delta_pct` > `8.766` → IC=-0.215 (n=419)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.766
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3567)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.205 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `1.695` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.695 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.332` → IC=+0.131 (n=166)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.332 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.289 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.2381` → IC=+0.131 (n=1318)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2381 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7013` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7013 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.272 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.306 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.371` → IC=+0.290 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.371 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6494` → IC=-0.180 (n=691)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6494
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2098)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.205 (n=662)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2127)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.210 (n=1019)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=3117)

- **PATRÓN** `dist_vwap_pct` > `0.4705` → IC=+0.314 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4705 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.21` → IC=+0.316 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.21 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.637` → IC=+0.311 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.637 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.298 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.303 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.300 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8274` → IC=+0.306 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8274 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.555` → IC=+0.280 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.555 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.252 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` > `1.0783` → IC=+0.272 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0783 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.265 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.1378` → IC=+0.257 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1378 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.253 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.42 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.200 (n=4276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4713` → IC=+0.188 (n=11446)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4713 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0075` → IC=+0.288 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0075 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.675` → IC=+0.159 (n=5854)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.675 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1772` → IC=+0.246 (n=4668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1772 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.254 (n=4170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.0802` → IC=+0.241 (n=6915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0802 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2934` → IC=+0.266 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2934 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6371` → IC=+0.257 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6371 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7069)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.167 (n=4144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0091 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5462` → IC=+0.156 (n=10928)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5462 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7008` → IC=+0.251 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7008 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2416` → IC=+0.248 (n=3593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2416 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7068` → IC=+0.249 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7068 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.260 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.305 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5868` → IC=+0.276 (n=2268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5868 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.279 (n=5037)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2593` → IC=-0.159 (n=889)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2593
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2667)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.174 (n=726)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2182)

- **FILTRO** `sigma_ewma_delta_pct` > `4.567` → IC=-0.178 (n=656)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.567
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2252)

- **PATRÓN** `ibs_20min` > `0.9053` → IC=+0.279 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9053 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.851` → IC=+0.210 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.851 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.278 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4393` → IC=+0.201 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4393 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.238 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.234 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.429 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2235` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2235 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4828` → IC=+0.442 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4828 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.432 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8651` → IC=+0.163 (n=858)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.8651 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.2998` → IC=+0.193 (n=463)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2998 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0504` → IC=+0.165 (n=1062)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.0504 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.178 (n=1078)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6754 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.198 (n=395)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4169` → IC=+0.185 (n=395)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4169 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.223 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 231.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.225 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6093` → IC=+0.229 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6093 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0728` → IC=+0.223 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0728 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2683` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2683 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1685` → IC=+0.236 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1685 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.275 (n=1750)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.254 (n=1969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=1753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.778` → IC=+0.284 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.778 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.265 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `1.6205` → IC=+0.259 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6205 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.272 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.324 (n=736)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.300 (n=714)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.318 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.357` → IC=+0.292 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.357 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.0991` → IC=+0.287 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0991 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.682` → IC=+0.293 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.682 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1194` → IC=+0.291 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1194 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.57` → IC=+0.298 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.57 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6513` → IC=+0.294 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6513 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1930.3184` → IC=+0.306 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.3184 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.288 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7715` → IC=-0.187 (n=740)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2223)

- **PATRÓN** `ibs_20min` > `0.9035` → IC=+0.176 (n=665)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.9035 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.398` → IC=+0.234 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.398 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.009` → IC=+0.250 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.009 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0816` → IC=+0.256 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0816 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4078` → IC=+0.268 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4078 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.260 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.131` → IC=+0.232 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.131 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1801` → IC=+0.217 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1801 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8269` → IC=+0.267 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8269 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.254 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 134.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7593` → IC=-0.184 (n=1357)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7593
  - _Potencial_: sin este filtro IC_bueno=+0.284 (n=1358)

- **FILTRO** `ibs_20min` > `0.675` → IC=-0.241 (n=681)

  - _Acción_: SKIP cuando `ibs_20min` > 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2049)

- **FILTRO** `sigma_ewma_delta_pct` > `4.807` → IC=-0.202 (n=582)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.807
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2148)

- **PATRÓN** `ibs_20min` > `0.7593` → IC=+0.284 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7593 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `1.0733` → IC=+0.333 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0733 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.668` → IC=+0.169 (n=430)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.668 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.309 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.302 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.299 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.294 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4182` → IC=+0.322 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4182 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.323 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.131 (n=1805)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.2679` → IC=+0.239 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2679 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.266 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1866` → IC=+0.227 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1866 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0689` → IC=+0.250 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0689 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4055` → IC=+0.248 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4055 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.257 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.020)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.328 (n=1418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.303 (n=744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `0.6454` → IC=+0.316 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6454 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.317 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.309 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `0.6276` → IC=+0.297 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6276 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.328 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.294 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.296 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.315 (n=1120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.1959` → IC=+0.288 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1959 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.289 (n=1597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.3774` → IC=+0.309 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3774 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.5981` → IC=+0.296 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5981 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` < `0.2311` → IC=+0.284 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2311 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.299 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` < `0.6418` → IC=+0.285 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6418 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.316 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.341 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.292 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.280 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2431.0932` → IC=+0.288 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2431.0932 (IC base=+0.284)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.183 (n=3220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0048 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.207 (n=3216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3618` → IC=+0.183 (n=8482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3618 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=10060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5707` → IC=+0.226 (n=9638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5707 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1732` → IC=+0.197 (n=4150)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1732 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.406` → IC=+0.255 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.406 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.167 (n=6417)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2075 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6296` → IC=+0.162 (n=6414)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6296 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.200 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.599` → IC=+0.182 (n=3095)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.599 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1978.1716` → IC=+0.176 (n=8610)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1978.1716 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.189 (n=8549)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 106.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.186 (n=6149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0812` → IC=+0.217 (n=3074)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0812 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=3504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.4877` → IC=+0.229 (n=9220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4877 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1713` → IC=+0.167 (n=6442)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1713 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.308` → IC=+0.196 (n=1548)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.308 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1769` → IC=+0.161 (n=6620)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1769 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.215 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5543` → IC=+0.172 (n=3751)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5543 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.6004` → IC=+0.172 (n=2842)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6004 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.181 (n=8192)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 108.0 (IC base=+0.172)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.241 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.207 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.219 (n=1616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.9136` → IC=+0.287 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9136 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.249` → IC=+0.332 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.249 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.248 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4317` → IC=+0.198 (n=1510)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4317 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2042.27` → IC=+0.202 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.27 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.250 (n=1078)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=1097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.300 (n=538)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=1093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.262 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.202` → IC=+0.248 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.202 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.263 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4169` → IC=+0.265 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4169 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1585.8448` → IC=+0.254 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1585.8448 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.233 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0701` → IC=+0.195 (n=483)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0701 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=1451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.389` → IC=+0.222 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.389 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2011` → IC=+0.205 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2011 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.528` → IC=+0.227 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.528 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6882` → IC=+0.170 (n=638)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6882 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.200 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.179 (n=471)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.4826` → IC=+0.159 (n=470)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4826 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `11975.7404` → IC=+0.157 (n=1294)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11975.7404 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.165 (n=604)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 236.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1529)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2316` → IC=+0.174 (n=1346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2316 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5901` → IC=+0.195 (n=1529)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5901 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1346` → IC=+0.168 (n=1513)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1346 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.882` → IC=+0.196 (n=301)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.882 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.160 (n=1529)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2116 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2261` → IC=+0.144 (n=1567)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2261 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0696` → IC=+0.149 (n=684)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0696 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4573` → IC=+0.150 (n=1417)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4573 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7547` → IC=+0.141 (n=945)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.7547 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.175 (n=447)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.225 (n=729)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2513` → IC=+0.218 (n=1073)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2513 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.488` → IC=+0.286 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.488 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.128` → IC=+0.209 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.128 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.217 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.216 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.237 (n=1215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1015` → IC=+0.262 (n=460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1015 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.246 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.651` → IC=+0.252 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.651 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3506` → IC=+0.256 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3506 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7349` → IC=+0.237 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7349 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.228 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1930.7184` → IC=+0.224 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.7184 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.213 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.185 (n=1365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4227` → IC=+0.166 (n=1550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4227 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3395` → IC=+0.205 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3395 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1453` → IC=+0.186 (n=1010)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1453 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.946` → IC=+0.228 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.946 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.164 (n=1034)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.856 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1014` → IC=+0.177 (n=646)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1014 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4269` → IC=+0.167 (n=506)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4269 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.163 (n=506)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5129.2383` → IC=+0.193 (n=1033)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 5129.2383 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.155 (n=1490)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 154.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=1620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3855` → IC=+0.146 (n=1620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3855 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6652` → IC=+0.179 (n=1620)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6652 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.145 (n=1586)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.853` → IC=+0.166 (n=561)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.853 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8555` → IC=+0.152 (n=1080)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8555 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.180 (n=239)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8074` → IC=+0.138 (n=997)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8074 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4195` → IC=+0.126 (n=1494)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4195 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `4272.1274` → IC=+0.158 (n=1080)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4272.1274 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.125 (n=1268)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 127.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.160 (n=802)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.01 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5846` → IC=+0.125 (n=1762)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.5846 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.211 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0792` → IC=+0.216 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0792 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.866` → IC=+0.262 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.866 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2106` → IC=+0.136 (n=1761)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2106 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6472` → IC=+0.130 (n=1761)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6472 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.132 (n=1772)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.127 (n=729)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.5369` → IC=+0.144 (n=749)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5369 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1841)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2388.4402` → IC=+0.181 (n=1174)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2388.4402 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.144 (n=1400)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 47.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.160 (n=783)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.174 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.217 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5778 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.7711` → IC=+0.121 (n=323)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.7711 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.1986` → IC=+0.148 (n=1641)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1986 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.134 (n=541)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.151 (n=594)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6382 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.227` → IC=+0.159 (n=309)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.227 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.141 (n=542)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4132` → IC=+0.127 (n=542)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4132 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2744.0462` → IC=+0.182 (n=806)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2744.0462 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.127 (n=1578)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.230 (n=1480)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.2928` → IC=+0.214 (n=1105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2928 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.215 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.6` → IC=+0.248 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.6 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1935` → IC=+0.211 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1935 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.217 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6232 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.273 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.47` → IC=+0.213 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.47 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.8052` → IC=+0.218 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8052 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2466.454` → IC=+0.209 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2466.454 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.226 (n=746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.216 (n=1130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.235 (n=565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4305` → IC=+0.243 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4305 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `1.2049` → IC=+0.228 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2049 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.251 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.1733` → IC=+0.212 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1733 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.7028` → IC=+0.221 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7028 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.275 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.1921` → IC=+0.205 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1921 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.212 (n=1549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2404.9954` → IC=+0.219 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.9954 (IC base=+0.212)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.192 (n=1116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0042 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.171 (n=847)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0085 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3457` → IC=+0.178 (n=2231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3457 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=1250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.3437` → IC=+0.197 (n=2535)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3437 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.186 (n=403)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.8089 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.743` → IC=+0.192 (n=1109)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.743 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.189 (n=1504)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8725 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.176 (n=752)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2084 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1629` → IC=+0.177 (n=673)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1629 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.184 (n=820)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.8204` → IC=+0.173 (n=1639)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8204 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=2879)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2685.4936` → IC=+0.170 (n=2264)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2685.4936 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.187 (n=2316)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 143.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.136 (n=1740)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0691` → IC=+0.191 (n=868)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0691 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.123 (n=987)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.143 (n=841)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4404 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2750.9096` → IC=+0.123 (n=2325)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2750.9096 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.126 (n=1099)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 28.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.187 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0029 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3325` → IC=+0.163 (n=675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3325 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.180 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.6376` → IC=+0.206 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6376 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2955` → IC=+0.164 (n=233)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.2955 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.164 (n=293)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.952` → IC=+0.143 (n=707)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.952 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8924` → IC=+0.170 (n=450)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8924 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.145 (n=646)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.144 (n=265)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.223` → IC=+0.152 (n=579)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.223 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5114` → IC=+0.149 (n=587)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5114 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `10893.2461` → IC=+0.151 (n=675)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10893.2461 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.194 (n=286)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 152.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3462` → IC=+0.159 (n=814)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3462 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=825)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6123` → IC=+0.179 (n=717)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6123 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.183` → IC=+0.154 (n=805)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.183 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.074` → IC=+0.145 (n=745)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.074 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2185` → IC=+0.145 (n=814)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2185 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6936` → IC=+0.154 (n=727)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6936 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.196 (n=218)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.156 (n=708)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4106` → IC=+0.146 (n=804)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4106 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12062.2629` → IC=+0.143 (n=727)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 12062.2629 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `294.0` → IC=+0.153 (n=690)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 294.0 (IC base=+0.139)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.252 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4057` → IC=+0.220 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4057 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.3605` → IC=+0.242 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3605 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.1422` → IC=+0.214 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1422 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2147` → IC=+0.210 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2147 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.334` → IC=+0.229 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.334 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8407` → IC=+0.216 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8407 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.230 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.242 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.239 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.4384` → IC=+0.245 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4384 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.122 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.145 (n=249)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.0873 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.139 (n=328)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6872 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `7918.7339` → IC=+0.135 (n=496)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7918.7339 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.170 (n=535)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0058 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.5423` → IC=+0.156 (n=599)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5423 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9739` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9739 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.363` → IC=+0.213 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.363 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.0661` → IC=+0.173 (n=527)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.0661 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6528` → IC=+0.162 (n=599)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6528 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0789` → IC=+0.154 (n=515)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0789 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.165 (n=165)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.17 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.4811` → IC=+0.155 (n=577)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4811 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.167 (n=262)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=635)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3081.1151` → IC=+0.193 (n=200)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3081.1151 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.475` → IC=+0.152 (n=509)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.475 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.5684` → IC=+0.135 (n=242)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5684 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `2884.1245` → IC=+0.151 (n=262)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2884.1245 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.131 (n=350)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 22.0 (IC base=+0.061)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0239` → IC=+0.167 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0239 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2478` → IC=+0.174 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2478 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.192 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.190 (n=169)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.56 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `1.1352` → IC=+0.162 (n=211)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.1352 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.738` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.738 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.179 (n=163)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=189)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2504.6528` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2504.6528 (IC base=+0.153)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.178 (n=4170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0047 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.209 (n=4153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=13041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9921` → IC=+0.310 (n=4153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9921 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.9211` → IC=+0.202 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9211 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.368` → IC=+0.251 (n=3077)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.368 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.171 (n=5573)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8799 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.201 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.5787` → IC=+0.198 (n=4014)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.5787 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1808.4532` → IC=+0.179 (n=12459)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1808.4532 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.203 (n=9762)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.195 (n=4932)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.15` → IC=+0.192 (n=4932)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.15 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4528` → IC=+0.247 (n=9863)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4528 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2461` → IC=+0.163 (n=7002)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2461 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.045` → IC=+0.203 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.045 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.731` → IC=+0.183 (n=10821)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.731 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.162 (n=3349)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7046 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.245 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.8549` → IC=+0.188 (n=6959)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8549 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=6748)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.242 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.227 (n=693)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.3602` → IC=+0.210 (n=2066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3602 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=993)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.669` → IC=+0.357 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.669 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.261 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2327` → IC=+0.219 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2327 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2040.9902` → IC=+0.218 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.9902 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.224 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.262 (n=1123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=1690)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1255` → IC=+0.281 (n=743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1255 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3605` → IC=+0.284 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3605 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.509` → IC=+0.260 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.509 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.291 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.5478` → IC=+0.257 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5478 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6156` → IC=+0.274 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6156 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1587.224` → IC=+0.268 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1587.224 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.207 (n=667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.163 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.2876` → IC=+0.203 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2876 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.182 (n=1131)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.177 (n=435)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.182` → IC=+0.150 (n=1829)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.182 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.7006` → IC=+0.169 (n=880)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7006 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.194 (n=282)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1297` → IC=+0.158 (n=1710)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1297 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5121` → IC=+0.152 (n=1736)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5121 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11444.8195` → IC=+0.153 (n=1787)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 11444.8195 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.173 (n=837)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 278.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3305` → IC=+0.160 (n=1679)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3305 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.2934` → IC=+0.241 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2934 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1321` → IC=+0.164 (n=1532)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1321 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.212` → IC=+0.152 (n=800)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.212 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.304` → IC=+0.147 (n=1527)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.304 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.160 (n=1679)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1894 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1527` → IC=+0.200 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1527 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4213` → IC=+0.156 (n=1580)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4213 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7624` → IC=+0.160 (n=1053)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7624 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `348.0` → IC=+0.147 (n=996)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 348.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.257 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=2036)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=1835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.303 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.2051` → IC=+0.224 (n=2047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2051 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.7674` → IC=+0.232 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7674 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2017.22` → IC=+0.231 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2017.22 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.241 (n=1683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.234 (n=1708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1826` → IC=+0.243 (n=841)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1826 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.300 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.188` → IC=+0.276 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.188 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3408` → IC=+0.291 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3408 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.239 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1472` → IC=+0.237 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1472 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1930.7184` → IC=+0.244 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.7184 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.234 (n=1714)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.203 (n=713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4338` → IC=+0.153 (n=2131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4338 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.2715` → IC=+0.189 (n=2131)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2715 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.3614` → IC=+0.160 (n=821)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3614 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.555` → IC=+0.168 (n=344)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.555 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8732` → IC=+0.163 (n=1421)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8732 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.160 (n=912)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1631` → IC=+0.155 (n=940)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1631 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7527.6821` → IC=+0.230 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7527.6821 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.177 (n=676)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 71.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.166 (n=1145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0051 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4451` → IC=+0.141 (n=1715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4451 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.5979` → IC=+0.195 (n=1509)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5979 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1535` → IC=+0.131 (n=1504)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1535 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.273` → IC=+0.165 (n=258)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.273 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.141 (n=572)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6225 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.219 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.140 (n=1641)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `9305.197` → IC=+0.200 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9305.197 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.128 (n=1647)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 169.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.143 (n=1423)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0081 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.573` → IC=+0.129 (n=2135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.573 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.202 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0653` → IC=+0.212 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0653 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.552` → IC=+0.245 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.552 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8911` → IC=+0.149 (n=1424)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8911 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1602` → IC=+0.128 (n=2199)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1602 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4501` → IC=+0.133 (n=693)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4501 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2171)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2551.935` → IC=+0.233 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2551.935 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.146 (n=1310)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 42.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.182 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0058 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1347` → IC=+0.158 (n=677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1347 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=2098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5065` → IC=+0.233 (n=1786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5065 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2176` → IC=+0.140 (n=1689)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2176 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.463` → IC=+0.128 (n=1957)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.463 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6459` → IC=+0.163 (n=678)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6459 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2194` → IC=+0.188 (n=322)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2194 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.1434` → IC=+0.134 (n=1641)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1434 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2798.604` → IC=+0.192 (n=677)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2798.604 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.134 (n=1622)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.231 (n=1870)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.216 (n=1513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.2117` → IC=+0.234 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2117 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.725` → IC=+0.266 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.725 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.0566` → IC=+0.216 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0566 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.221 (n=2093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.243 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.505` → IC=+0.243 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.505 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2464.3289` → IC=+0.218 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.3289 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.219 (n=732)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.229 (n=993)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.226 (n=1547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.262 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `1.2232` → IC=+0.217 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2232 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2187` → IC=+0.216 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2187 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.857` → IC=+0.257 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.857 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.238 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.283 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `2.1751` → IC=+0.204 (n=1760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1751 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4282` → IC=+0.210 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4282 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2414.1306` → IC=+0.214 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2414.1306 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.202 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.211)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=3690)

- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.199 (n=3232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0089 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.5067` → IC=+0.191 (n=3673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.5067 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=1368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=1674)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.240 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1717` → IC=+0.191 (n=1357)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1717 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.22` → IC=+0.214 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.22 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7106` → IC=+0.186 (n=1108)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7106 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.183 (n=1679)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8944 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.209 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.190 (n=1209)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.8601` → IC=+0.186 (n=2416)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8601 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2734)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `2523.314` → IC=+0.187 (n=3672)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2523.314 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.216 (n=927)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3841` → IC=+0.182 (n=2446)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3841 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.185 (n=1224)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1827 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6648` → IC=+0.181 (n=519)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6648 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` < `0.2382` → IC=+0.153 (n=2467)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2382 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.169 (n=2774)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2566` → IC=+0.165 (n=2615)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2566 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.166 (n=2539)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.162 (n=575)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.169 (n=1208)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.171 (n=1829)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=3690)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `5349.3599` → IC=+0.167 (n=2483)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5349.3599 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.166 (n=1809)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 86.0 (IC base=+0.161)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.228 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.267 (n=170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.220 (n=234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.232 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.516 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.7635` → IC=+0.208 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7635 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.3275` → IC=+0.215 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3275 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.566` → IC=+0.209 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.566 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2189` → IC=+0.214 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2189 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.5931` → IC=+0.218 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5931 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.227 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `12575.9809` → IC=+0.237 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12575.9809 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.227 (n=466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.163 (n=1053)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.180 (n=404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.182 (n=463)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.144 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.151 (n=477)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6084 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6653` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6653 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.167 (n=1035)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.188 (n=702)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8811 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.179 (n=219)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.538` → IC=+0.156 (n=1048)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.538 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8221` → IC=+0.166 (n=699)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8221 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11538.1781` → IC=+0.162 (n=1052)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11538.1781 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `698.0` → IC=+0.159 (n=1006)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 698.0 (IC base=+0.148)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.216 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1517` → IC=+0.211 (n=517)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1517 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.193 (n=536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.5256` → IC=+0.203 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5256 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.8847` → IC=+0.195 (n=391)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8847 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.2066` → IC=+0.201 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2066 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.171` → IC=+0.199 (n=1056)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.171 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.195 (n=1033)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0845 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `1.2457` → IC=+0.192 (n=391)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.2457 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.192 (n=1078)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.202 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.197 (n=1150)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=1181)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.221 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.189 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.174 (n=634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 10.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.7559` → IC=+0.169 (n=944)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7559 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.0908` → IC=+0.170 (n=944)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0908 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6069` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6069 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2152` → IC=+0.165 (n=873)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2152 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.718` → IC=+0.168 (n=966)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.718 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6432` → IC=+0.203 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6432 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.165 (n=843)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7259 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.180 (n=814)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.7855` → IC=+0.166 (n=617)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7855 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `7438.5832` → IC=+0.179 (n=944)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7438.5832 (IC base=+0.164)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.163 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0111 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.162 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 3.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.2206` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.2206 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.097` → IC=+0.227 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.097 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7119 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.282` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.282 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.227 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.4251` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4251 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=439)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2974.6892` → IC=+0.162 (n=371)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2974.6892 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.156 (n=309)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 51.0 (IC base=+0.135)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.165 (n=523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0039 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.123 (n=616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.6473` → IC=+0.178 (n=973)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6473 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1425` → IC=+0.142 (n=591)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1425 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.188 (n=254)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.189 (n=149)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.122 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.2302` → IC=+0.261 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2302 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.201` → IC=+0.136 (n=476)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.201 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.082` → IC=+0.150 (n=361)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.082 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.1401` → IC=+0.205 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1401 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `2.5523` → IC=+0.153 (n=370)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5523 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `1.4507` → IC=+0.146 (n=331)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4507 (IC base=+0.052)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.140 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0058 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.124 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4395` → IC=+0.166 (n=375)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.4395 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.163 (n=200)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.5009` → IC=+0.122 (n=334)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.5009 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.126 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0053 (IC base=+0.090)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.202 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.2737` → IC=+0.268 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2737 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` < `0.0689` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0689 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.802` → IC=+0.180 (n=198)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.802 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `1.151` → IC=+0.136 (n=204)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.151 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `0.8122` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.8122 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `2.412` → IC=+0.167 (n=181)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.412 (IC base=+0.090)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.7146` → IC=-0.123 (n=157)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7146
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=320)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=162)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.139 (n=261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0048 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.7146` → IC=+0.214 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7146 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.172 (n=196)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.652` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.652 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.7834` → IC=+0.146 (n=204)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7834 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `1136.0742` → IC=+0.148 (n=316)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1136.0742 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7058 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.011` → IC=-0.256 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=132)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.261 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=90)

- **PATRÓN** `ibs_20min` > `0.7727` → IC=+0.171 (n=238)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.7727 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.051)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.142 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.011 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.847` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.847 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.84` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.84 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `0.5953` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.5953 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1332` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1332 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.7925` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7925 (IC base=+0.042)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.06 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `591.2821` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 591.2821 (IC base=+0.042)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=183)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=226)

- **FILTRO** `volumen_regimen` < `0.7363` → IC=-0.355 (n=60)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7363
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=181)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.365 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=153)

- **FILTRO** `ibs_20min` > `0.92` → IC=-0.327 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` > 0.92
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=153)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=181)

- **FILTRO** `volumen_pendiente_norm` > `0.0549` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=92)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.238 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=64)

- **FILTRO** `sigma_ewma_delta_pct` > `2.55` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.55
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=55)

- **FILTRO** `volumen_regimen` > `0.8507` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8507
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=64)

- **FILTRO** `libro_liquidez` < `3685.6992` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 3685.6992
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=57)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7738` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.350 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=56)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=54)

- **FILTRO** `libro_liquidez` < `1256.9437` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 1256.9437
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=56)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.179)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.175 (n=158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0058 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.122 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.6472` → IC=+0.140 (n=348)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.6472 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.4919` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4919 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.125 (n=166)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.140 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.182 (n=319)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.156 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.664` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.664 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.132 (n=286)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `4049.9464` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 4049.9464 (IC base=+0.085)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6295` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6295
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=102)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.185 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0024 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.230 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.224 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1414 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1082` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1082 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.611` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 4.611 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.1471` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1471 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.6733` → IC=+0.171 (n=144)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.6733 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.6869` → IC=+0.204 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6869 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.4563` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4563 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `4599.6467` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4599.6467 (IC base=+0.157)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1682` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1682
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=89)

- **FILTRO** `libro_liquidez` < `1549.8575` → IC=-0.173 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 1549.8575
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=98)

- **FILTRO** `ibs_20min` > `0.2038` → IC=-0.127 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2038
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=112)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.148 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.2038` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2038 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` < `0.8316` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 0.8316 (IC base=+0.061)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.1087` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1087
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=28)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.277 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.242 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.216 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9459` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9459 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.1281` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1281 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.265 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.287 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.089` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.089 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.818` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.818 (IC base=-0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.1087` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1087 (IC base=-0.035)

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
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.121 (n=1109)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.495 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2938.7445` → IC=+0.156 (n=318)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2938.7445 (IC base=+0.110)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.121 (n=1109)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.495 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2938.7445` → IC=+0.156 (n=318)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2938.7445 (IC base=+0.110)

### LIQUIDACIONES_15M
- **FILTRO** `py_entrada` < `0.445` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=116)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2489)

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
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=98)

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

- **PATRÓN** `liq_usd_total` > `80505.33` → IC=+0.129 (n=122)

  - _Acción_: Kelly boost +0.65€ cuando `liq_usd_total` > 80505.33 (IC base=+0.059)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.059)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=985)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=939)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=575)

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
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=286)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.495 (IC base=+0.030)

- **PATRÓN** `libro_liquidez` > `4214.4529` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4214.4529 (IC base=+0.030)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=749)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=749)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.131 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=587)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=481)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=481)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=206)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=206)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=168)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.144 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=150)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=119)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=143)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=239)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=115)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=128)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=289)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=289)

- **FILTRO** `libro_liquidez` < `553.2637` → IC=-0.136 (n=105)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.2637
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=173)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.48` → IC=-0.120 (n=1386)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=763)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.122 (n=146)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=56)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.145 (n=74)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=193)

- **PATRÓN** `py_entrada` < `0.56` → IC=+0.123 (n=136)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.56 (IC base=+0.020)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.207 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.043)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `profundidad_ratio` < `30.6` → IC=-0.134 (n=91)

  - _Acción_: SKIP cuando `profundidad_ratio` < 30.6
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=47)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=106)

- **FILTRO** `restante_min` < `3.99` → IC=-0.130 (n=106)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `lag_apertura_s` > `60.75` → IC=-0.134 (n=110)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.75
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=38)

- **PATRÓN** `py_entrada` < `0.49` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.49 (IC base=+0.081)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.155 (n=140)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=47)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.230 (n=61)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=154)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=199)

- **FILTRO** `restante_min` < `3.43` → IC=-0.220 (n=80)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=163)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=187)

- **FILTRO** `lag_apertura_s` > `92.29` → IC=-0.202 (n=82)

  - _Acción_: SKIP cuando `lag_apertura_s` > 92.29
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=161)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.160 (n=154)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=85)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.144 (n=85)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` > 0.5 (IC base=-0.052)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.227 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=216)

- **FILTRO** `lag_apertura_s` > `104.65` → IC=-0.130 (n=98)

  - _Acción_: SKIP cuando `lag_apertura_s` > 104.65
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=193)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.164 (n=4396)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=13312)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=4408)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=13908)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.197 (n=774)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=2360)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.151 (n=775)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=2499)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.125 (n=2141)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.495 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1803.58` → IC=+0.133 (n=1066)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1803.58 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1573.34` → IC=+0.142 (n=1114)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1573.34 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.179 (n=773)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2407)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=768)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2549)

- **PATRÓN** `libro_liquidez` > `1801.3284` → IC=+0.133 (n=1082)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1801.3284 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.163 (n=758)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2365)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2422)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3162)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

- **FILTRO** `libro_liquidez` < `17110.7517` → IC=-0.144 (n=237)

  - _Acción_: SKIP cuando `libro_liquidez` < 17110.7517
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=712)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=282)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1934.3745` → IC=-0.173 (n=325)

  - _Acción_: SKIP cuando `libro_liquidez` < 1934.3745
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=661)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=230)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=12393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=27595)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=9378)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=30610)

- **FILTRO** `ibs_7min` < `0.2614` → IC=-0.233 (n=9995)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2614
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=29993)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=13556)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=26432)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=12351)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=38331)

- **FILTRO** `ibs_7min` > `0.2909` → IC=-0.180 (n=12663)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2909
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=38019)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=2016)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4768)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=1623)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=5161)

- **FILTRO** `ibs_7min` < `0.7083` → IC=-0.249 (n=2238)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7083
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=4546)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.182 (n=1536)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5248)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.264 (n=2155)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6601)

- **FILTRO** `ibs_7min` > `0.7899` → IC=-0.208 (n=2188)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7899
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=6568)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5212)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.248 (n=1680)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5158)

- **FILTRO** `ibs_7min` < `0.7428` → IC=-0.196 (n=1707)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7428
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5131)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.177 (n=1700)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5138)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1629)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5337)

- **FILTRO** `ibs_7min` > `0.2631` → IC=-0.191 (n=1741)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2631
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5225)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.187 (n=1741)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5225)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.160 (n=1834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=4609)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=1529)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4914)

- **FILTRO** `ibs_7min` < `0.7026` → IC=-0.246 (n=2126)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7026
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4317)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.212 (n=1497)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4946)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=2145)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7206)

- **FILTRO** `ibs_7min` > `0.7436` → IC=-0.174 (n=2336)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=7015)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.236 (n=1955)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4619)

- **FILTRO** `ibs_7min` < `0.7397` → IC=-0.188 (n=1643)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7397
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4931)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.177 (n=1606)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4968)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1672)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5092)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.178 (n=1690)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5074)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.182 (n=1663)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5101)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.264 (n=1692)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=5103)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1665)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5130)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2310)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7374)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.272 (n=1544)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=5010)

- **FILTRO** `ibs_7min` < `0.26` → IC=-0.221 (n=1637)

  - _Acción_: SKIP cuando `ibs_7min` < 0.26
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4917)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1637)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=4917)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.210 (n=2134)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=7027)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1200)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.131 (n=155)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=494)

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
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=334)

- **FILTRO** `libro_liquidez` < `3298.5458` → IC=-0.156 (n=161)

  - _Acción_: SKIP cuando `libro_liquidez` < 3298.5458
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=485)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.134 (n=888)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.136 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.120)

- **PATRÓN** `total_vol_5m` < `443.866` → IC=+0.149 (n=297)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 443.866 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.128 (n=755)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 53.0 (IC base=+0.120)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.167 (n=70)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.224 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `307.527` → IC=+0.138 (n=139)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 307.527 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.137 (n=224)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.04 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2602.0106` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2602.0106 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.170 (n=92)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 12.0 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 10.0 (IC base=+0.106)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.183 (n=121)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `390.044` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.044 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 73.0 (IC base=+0.109)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.171 (n=159)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `8082.459` → IC=+0.158 (n=159)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 8082.459 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 28.0 (IC base=+0.139)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.143 (n=155)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.124 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `3602.5746` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3602.5746 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=113)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.234 (n=332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=165)

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
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.196 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `T_h` < `87.1706` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `T_h` < 87.1706
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0087` → IC=-0.178 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=157)

- **FILTRO** `T_h` > `72.5264` → IC=-0.150 (n=344)

  - _Acción_: SKIP cuando `T_h` > 72.5264
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=115)

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
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.267 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=87)

- **FILTRO** `T_h` > `135.9851` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=97)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.167 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=86)

- **FILTRO** `sigma_h` < `0.0073` → IC=-0.200 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

- **FILTRO** `T_h` > `135.1248` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `T_h` > 135.1248
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

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

- **PATRÓN** `edge` > `0.096` → IC=+0.454 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.421)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.433 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.421)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.448 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.421)

- **PATRÓN** `T_h` < `0.608` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.421)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.421)

- **PATRÓN** `dist_50` > `0.4027` → IC=+0.483 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4027 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.421)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1072` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.421)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.406 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.421)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.455 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.421)

- **PATRÓN** `T_h` < `0.9168` → IC=+0.450 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9168 (IC base=+0.421)

- **PATRÓN** `T_h` > `0.5098` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5098 (IC base=+0.421)

- **PATRÓN** `dist_50` > `0.4166` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4166 (IC base=+0.421)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.421)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=235)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=330)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.146 (n=145)

  - _Acción_: Kelly boost +0.73€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.032)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `990711.2` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `volumen_racha` > 990711.2
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=34)

- **FILTRO** `streak_estiramiento` > `0.4382` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4382
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=41)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_racha` < 990711.2 (IC base=-0.007)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.4382 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.122 (n=96)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 48.0 (IC base=+0.062)

- **PATRÓN** `libro_liquidez` > `2492.9344` → IC=+0.124 (n=91)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2492.9344 (IC base=+0.062)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=523)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=746)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=897)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=886)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3297)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1711)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.212 (n=711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.242 (n=711)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.1593` → IC=+0.205 (n=1877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1593 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2202` → IC=+0.212 (n=711)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2202 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.128` → IC=+0.234 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.128 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=1982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=2210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.6176` → IC=+0.281 (n=2133)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6176 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1186` → IC=+0.205 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1186 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.791` → IC=+0.280 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.791 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2953.6818` → IC=+0.209 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2953.6818 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.220 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.202)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=914)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.231 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.278 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2017` → IC=+0.248 (n=204)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2017 (IC base=+0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.272 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.277 (n=450)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.270 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.216)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.104` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.104
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=547)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.195 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0034 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.067` → IC=+0.167 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.067 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2347` → IC=+0.177 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2347 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1204` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1204 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.149 (n=223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5788` → IC=+0.242 (n=486)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5788 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.160 (n=448)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.239 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3422.7688` → IC=+0.165 (n=434)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3422.7688 (IC base=+0.149)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.286 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.208 (n=262)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0615` → IC=+0.200 (n=261)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0615 (IC base=+0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3438` → IC=+0.245 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3438 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.280 (n=261)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5926 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.216 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.362 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3214.9675` → IC=+0.298 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3214.9675 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.216 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.189)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0233` → IC=+0.286 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0233 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.224 (n=237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0429` → IC=+0.213 (n=538)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0429 (IC base=+0.209)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0848` → IC=+0.260 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0848 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.209)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.293 (n=538)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.1345` → IC=+0.221 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1345 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.5623` → IC=+0.210 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5623 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.006` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.006 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.277` → IC=+0.212 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.277 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2935.997` → IC=+0.291 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2935.997 (IC base=+0.209)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.147 (n=601)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` < 0.1154 (IC base=+0.058)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.366 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.364 (n=499)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.360 (n=334)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.383 (n=332)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.391 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.373 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.396 (n=499)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.388 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.366 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.357 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.358)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.375 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.379 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 446.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1128` → IC=+0.369 (n=120)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1128 (IC base=+0.363)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.372 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.365 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0025 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.371 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.363)

- **PATRÓN** `drift_15min` |x|≤ `0.5207` → IC=+0.370 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5207 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1529` → IC=+0.385 (n=181)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1529 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.384 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.395 (n=273)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.3959` → IC=+0.415 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3959 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.018` → IC=+0.367 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.018 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.657` → IC=+0.367 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.657 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.382 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.420 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.353 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.349)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.349)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.364 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.349)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.368 (n=203)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.349)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.376 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.349)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.409 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.349)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.400 (n=227)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.349)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.349)

- **PATRÓN** `dist_vwap_pct` < `0.2966` → IC=+0.351 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2966 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.364 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.352 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.349)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.355 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.349)

- **PATRÓN** `libro_liquidez` > `4242.86` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.86 (IC base=+0.349)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.356 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.349)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.221 (n=801)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=2407)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.203 (n=1145)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2063)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.184 (n=521)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=-0.061)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1363` → IC=+0.253 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1363 (IC base=-0.061)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.282 (n=781)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.424` → IC=+0.202 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.424 (IC base=-0.061)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1242` → IC=+0.252 (n=1615)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1242 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1818` → IC=+0.250 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1818 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.3499` → IC=+0.275 (n=2419)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3499 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.6601` → IC=+0.294 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6601 (IC base=-0.022)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.207 (n=479)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1438)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.219 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1438)

- **FILTRO** `sigma_ewma_delta_pct` > `23.641` → IC=-0.258 (n=271)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.641
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1646)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.170 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0028 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.306 (n=106)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.322 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.124 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 12.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.334 (n=233)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.0996` → IC=+0.290 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0996 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.3564` → IC=+0.287 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3564 (IC base=+0.088)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0841` → IC=+0.176 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0841 (IC base=-0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.501` → IC=+0.306 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.501 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.0553` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0553 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.192)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=487)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.169 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0065 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.173 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0049 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.216 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.162)

- **PATRÓN** `drift_15min` |x|≤ `0.4132` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `drift_15min` |x|≤ 0.4132 (IC base=+0.162)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.165 (n=252)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.162)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.232 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.186 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 11.0 (IC base=+0.162)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.266 (n=379)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.176 (n=350)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.207 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=487)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `9633.3802` → IC=+0.172 (n=172)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 9633.3802 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.247 (n=909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.445` → IC=+0.240 (n=909)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.445 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.774` → IC=+0.251 (n=800)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.774 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2075` → IC=+0.266 (n=412)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2075 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.240 (n=641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.271 (n=909)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.7515` → IC=+0.306 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7515 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.25` → IC=+0.277 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.25 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.457` → IC=+0.241 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.457 (IC base=+0.238)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.233 (n=253)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=496)

- **FILTRO** `drift_15min` |x|> `0.8925` → IC=-0.273 (n=187)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8925
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=562)

- **FILTRO** `sigma_ewma_delta_pct` > `18.255` → IC=-0.145 (n=401)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.255
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.151 (n=41)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.174)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.219 (n=55)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.174)

- **PATRÓN** `dist_vwap_pct` < `0.1248` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1248 (IC base=-0.174)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 44.0 (IC base=-0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0785` → IC=+0.227 (n=353)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0785 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.183` → IC=+0.229 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.183 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.268 (n=395)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.6912` → IC=+0.241 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6912 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1683` → IC=+0.236 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1683 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.19` → IC=-0.212 (n=307)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.19
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=598)

- **FILTRO** `sigma_h` > `0.0196` → IC=-0.260 (n=452)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=453)

- **FILTRO** `drift_60min` |x|> `0.1554` → IC=-0.206 (n=226)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1554
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=679)

- **FILTRO** `drift_15min` |x|> `1.2349` → IC=-0.272 (n=226)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2349
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=679)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1449` → IC=+0.271 (n=278)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1449 (IC base=-0.034)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1081` → IC=+0.320 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1081 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=614)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `0.8592` → IC=+0.355 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8592 (IC base=-0.034)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.035)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.035)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.304 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.330 (n=269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.312 (n=269)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.323 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.328 (n=806)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2727` → IC=+0.330 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2727 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.350 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `12909.8374` → IC=+0.302 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.8374 (IC base=+0.294)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.295 (n=389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.333 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.287 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.312 (n=147)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.304 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.317 (n=441)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.342 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.326 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.321 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.301)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.301 (n=365)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0035 (IC base=+0.301)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.322 (n=161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.301)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.301 (n=244)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.301)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.332 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.319 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.301)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.339 (n=365)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.312 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.338 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.301)

### UPDOWN_OU_5M
- **FILTRO** `sigma_h` > `0.0043` → IC=-0.265 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=197)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=128)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0687` → IC=-0.139 (n=59)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0687
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=132)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

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

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1065` → IC=-0.200 (n=18)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1065
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=23)

- **FILTRO** `sigma_h` > `0.0054` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

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

- **PATRÓN** `T_h` < `115.2222` → IC=+0.293 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 115.2222 (IC base=+0.289)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6176 sube el IC de +0.202 a +0.281 en UPDOWN_GBM#15min (n=2133). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.216 a +0.277 en UPDOWN_GBM#BTC#15min (n=450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5788 sube el IC de +0.149 a +0.242 en UPDOWN_GBM#ETH#15min (n=486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.189 a +0.280 en UPDOWN_GBM#SOL#15min (n=261). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.209 a +0.293 en UPDOWN_GBM#XRP#15min (n=538). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.061 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=781). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3499 sube el IC de -0.022 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=2419). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.088 a +0.334 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.192 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.162 a +0.266 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=379). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.361 sube el IC de +0.238 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=909). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.174 a +0.219 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.040 a +0.268 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=395). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.034 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=614). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.294 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=806). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.286 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=441). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.301 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=365). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.358 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=499). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.363 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=273). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.349 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=227). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1511 | +0.097 | +191.15€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1511 | +0.097 | +191.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1148 | +0.105 | +167.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1148 | +0.105 | +167.05€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 261 | +0.063 | +9.98€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 261 | +0.063 | +9.98€ | 6 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 71 | +0.103 | +14.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 71 | +0.103 | +14.46€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 104 | +0.028 | +17.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 104 | +0.028 | +17.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 83 | +0.041 | +14.06€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 83 | +0.041 | +14.06€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 21 | -0.022 | +3.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 21 | -0.022 | +3.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 32585 | -0.090 | -4322.25€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1672 | -0.020 | -219.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 30913 | -0.093 | -4103.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4215 | -0.114 | -686.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4215 | -0.114 | -686.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1672 | -0.020 | -219.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1672 | -0.020 | -219.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3853 | -0.115 | -866.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3853 | -0.115 | -866.77€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8407 | -0.007 | -764.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8407 | -0.007 | -764.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8111 | -0.105 | -578.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8111 | -0.105 | -578.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6327 | -0.167 | -1206.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6327 | -0.167 | -1206.62€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 24143 | -0.021 | +3684.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6251 | +0.001 | +1740.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 17892 | -0.029 | +1943.64€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 24143 | -0.021 | +3684.62€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6251 | +0.001 | +1740.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 17892 | -0.029 | +1943.64€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 111098 | +0.113 | -5233.50€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15808 | +0.183 | -490.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 468 | -0.055 | -59.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 87860 | +0.102 | -4415.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6962 | +0.105 | -269.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14595 | +0.101 | -1098.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 51 | -0.141 | +9.84€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14529 | +0.102 | -1096.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22122 | +0.130 | -375.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4797 | +0.199 | -125.46€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14568 | +0.115 | -161.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2715 | +0.093 | -66.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14640 | +0.092 | -1238.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 59 | -0.107 | -4.41€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14566 | +0.093 | -1222.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23596 | +0.124 | -446.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6327 | +0.176 | -103.59€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14729 | +0.106 | -274.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2528 | +0.100 | -60.35€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21534 | +0.114 | -1221.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4522 | +0.187 | -276.42€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 371 | -0.017 | -5.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14922 | +0.093 | -796.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1719 | +0.130 | -142.62€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14611 | +0.100 | -853.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14546 | +0.101 | -863.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17710 | +0.195 | -1083.59€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17710 | +0.195 | -1083.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4129 | +0.175 | -380.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4129 | +0.175 | -380.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1822 | +0.203 | -18.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1822 | +0.203 | -18.65€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4073 | +0.181 | -331.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4073 | +0.181 | -331.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3594 | +0.243 | -116.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3594 | +0.243 | -116.79€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4013 | +0.190 | -249.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4013 | +0.190 | -249.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 830 | +0.433 | -18.33€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 830 | +0.433 | -18.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 326 | +0.442 | -0.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 326 | +0.442 | -0.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 315 | +0.434 | -5.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 315 | +0.434 | -5.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 177 | +0.411 | -9.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 177 | +0.411 | -9.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 61449 | +0.199 | -4652.25€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 61449 | +0.199 | -4652.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10575 | +0.181 | -1152.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10575 | +0.181 | -1152.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9859 | +0.224 | -345.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9859 | +0.224 | -345.88€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10593 | +0.174 | -1221.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10593 | +0.174 | -1221.86€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9934 | +0.219 | -377.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9934 | +0.219 | -377.10€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10176 | +0.203 | -665.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10176 | +0.203 | -665.82€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10312 | +0.193 | -889.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10312 | +0.193 | -889.55€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 23367 | +0.115 | +120.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 23367 | +0.115 | +120.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11604 | +0.119 | +121.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11604 | +0.119 | +121.10€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11763 | +0.112 | -0.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11763 | +0.112 | -0.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1687 | +0.288 | -26.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1687 | +0.288 | -26.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 758 | +0.279 | -18.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 758 | +0.279 | -18.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 814 | +0.287 | -12.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 814 | +0.287 | -12.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 750 | +0.439 | +0.27€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 750 | +0.439 | +0.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 360 | +0.436 | -2.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 360 | +0.436 | -2.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 344 | +0.442 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 344 | +0.442 | +2.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1295 | +0.068 | -63.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 461 | +0.055 | -39.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 834 | +0.075 | -24.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1018 | +0.074 | -32.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 184 | +0.070 | -8.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 834 | +0.075 | -24.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 211 | +0.026 | -33.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 211 | +0.026 | -33.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 44509 | +0.099 | -1226.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3620 | +0.091 | +43.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 40889 | +0.099 | -1270.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 24730 | +0.103 | -318.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3620 | +0.091 | +43.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21110 | +0.105 | -362.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8744 | +0.107 | -44.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8744 | +0.107 | -44.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11035 | +0.081 | -863.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11035 | +0.081 | -863.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 863 | +0.207 | -101.67€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 863 | +0.207 | -101.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 863 | +0.207 | -101.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 863 | +0.207 | -101.67€ | 1 | 4 |
| ✅ GBM_LATE_15M | 31299 | +0.087 | +15462.24€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 31299 | +0.087 | +15462.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5252 | +0.203 | +4035.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5252 | +0.203 | +4035.33€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4659 | +0.177 | +3339.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4659 | +0.177 | +3339.63€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 5551 | +0.199 | +4163.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5551 | +0.199 | +4163.02€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4454 | +0.030 | +1112.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4454 | +0.030 | +1112.73€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4458 | -0.031 | +980.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4458 | -0.031 | +980.45€ | 4 | 11 |
| ✅ GBM_LATE_15M#XRP | 6925 | -0.036 | +1831.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6925 | -0.036 | +1831.07€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 33635 | +0.087 | +17906.96€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 33635 | +0.087 | +17906.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6464 | +0.012 | +3344.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6464 | +0.012 | +3344.69€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6987 | +0.015 | +1472.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6987 | +0.015 | +1472.62€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4767 | +0.267 | +4888.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4767 | +0.267 | +4888.37€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5622 | +0.009 | +1239.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5622 | +0.009 | +1239.97€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5445 | +0.035 | +2188.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5445 | +0.035 | +2188.63€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4350 | +0.283 | +4772.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4350 | +0.283 | +4772.68€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 25143 | +0.173 | +19468.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 25143 | +0.173 | +19468.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3783 | +0.217 | +3166.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3783 | +0.217 | +3166.10€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3969 | +0.149 | +2888.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3969 | +0.149 | +2888.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3982 | +0.212 | +3238.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3982 | +0.212 | +3238.91€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4225 | +0.137 | +3123.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4225 | +0.137 | +3123.82€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4717 | +0.122 | +3427.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4717 | +0.122 | +3427.10€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4467 | +0.209 | +3624.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4467 | +0.209 | +3624.12€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6848 | +0.137 | +3215.23€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6848 | +0.137 | +3215.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 338 | +0.141 | +185.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 338 | +0.141 | +185.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1984 | +0.141 | +1050.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1984 | +0.141 | +1050.69€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2050 | +0.153 | +1005.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2050 | +0.153 | +1005.13€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1568 | +0.108 | +566.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1568 | +0.108 | +566.21€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 534 | +0.134 | +230.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 534 | +0.134 | +230.88€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 31551 | +0.179 | +24243.44€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 31551 | +0.179 | +24243.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4999 | +0.230 | +4432.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4999 | +0.230 | +4432.41€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4904 | +0.148 | +3188.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4904 | +0.148 | +3188.73€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5261 | +0.227 | +4556.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5261 | +0.227 | +4556.80€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5126 | +0.135 | +3595.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5126 | +0.135 | +3595.95€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5552 | +0.122 | +3811.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5552 | +0.122 | +3811.74€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5709 | +0.213 | +4657.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5709 | +0.213 | +4657.82€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8601 | +0.172 | +5697.23€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 8601 | +0.172 | +5697.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2080 | +0.167 | +1503.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2080 | +0.167 | +1503.18€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2822 | +0.179 | +1857.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2822 | +0.179 | +1857.72€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 893 | +0.147 | +506.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 893 | +0.147 | +506.36€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2248 | +0.072 | +818.97€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2248 | +0.072 | +818.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 843 | +0.093 | +308.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 843 | +0.093 | +308.12€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 715 | +0.069 | +312.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 715 | +0.069 | +312.86€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 690 | +0.049 | +198.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 690 | +0.049 | +198.00€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 444 | -0.240 | -10.69€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 444 | -0.240 | -10.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 165 | -0.219 | -5.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 165 | -0.219 | -5.48€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 153 | -0.229 | -0.43€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 153 | -0.229 | -0.43€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 126 | -0.273 | -4.79€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 126 | -0.273 | -4.79€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 945 | +0.087 | +238.07€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 945 | +0.087 | +238.07€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 350 | +0.082 | +73.98€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 350 | +0.082 | +73.98€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 314 | +0.054 | +37.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 314 | +0.054 | +37.09€ | 3 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 281 | +0.129 | +127.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 281 | +0.129 | +127.00€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2592 | +0.105 | +704.56€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2592 | +0.105 | +704.56€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2592 | +0.105 | +704.56€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2592 | +0.105 | +704.56€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 415 | -0.073 | -33.23€ | 5 | 0 |
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
| ✅ LIQUIDACIONES_5M | 2690 | +0.023 | +78.14€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2690 | +0.023 | +78.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 134 | +0.029 | -0.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 134 | +0.029 | -0.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 391 | +0.037 | +37.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 391 | +0.037 | +37.07€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1034 | +0.032 | +31.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1034 | +0.032 | +31.04€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 615 | +0.014 | +1.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 615 | +0.014 | +1.53€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 315 | +0.021 | +15.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 315 | +0.021 | +15.22€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1325 | -0.047 | -32.31€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1325 | -0.047 | -32.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 379 | -0.043 | -14.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 379 | -0.043 | -14.04€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 439 | -0.028 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 439 | -0.028 | -1.60€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 507 | -0.066 | -16.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 507 | -0.066 | -16.68€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4088 | -0.022 | +46.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1924 | -0.028 | -9.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2164 | -0.017 | +56.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 111 | +0.004 | +4.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 58 | +0.050 | +8.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 53 | -0.045 | -3.68€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1003 | -0.002 | +44.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 469 | -0.007 | +11.08€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 534 | +0.004 | +33.24€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 462 | -0.024 | +7.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 223 | -0.038 | -2.48€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 239 | -0.010 | +10.42€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 829 | -0.039 | -27.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 378 | -0.055 | -29.01€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 451 | -0.025 | +1.59€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 805 | -0.027 | +8.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 389 | -0.032 | +2.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 416 | -0.021 | +6.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 878 | -0.028 | +8.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 407 | -0.028 | -0.24€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 471 | -0.029 | +8.25€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 36024 | -0.004 | +1706.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 36024 | -0.004 | +1706.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6408 | +0.023 | +836.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6408 | +0.023 | +836.77€ | 2 | 3 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5416 | -0.031 | -73.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5416 | -0.031 | -73.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6497 | +0.019 | +625.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6497 | +0.019 | +625.42€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5207 | -0.053 | -162.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5207 | -0.053 | -162.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6068 | -0.008 | +208.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6068 | -0.008 | +208.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6428 | +0.012 | +272.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6428 | +0.012 | +272.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6105 | -0.060 | -148.06€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6105 | -0.060 | -148.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1484 | -0.080 | -36.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1484 | -0.080 | -36.26€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 702 | -0.126 | -34.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 702 | -0.126 | -34.44€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1803 | -0.077 | -32.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1803 | -0.077 | -32.64€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 90670 | -0.073 | +1845.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 90670 | -0.073 | +1845.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15540 | -0.074 | +933.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15540 | -0.074 | +933.79€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13804 | -0.097 | -754.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13804 | -0.097 | -754.48€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15794 | -0.065 | +904.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15794 | -0.065 | +904.61€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13338 | -0.093 | -332.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13338 | -0.093 | -332.85€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16479 | -0.051 | +352.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16479 | -0.051 | +352.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15715 | -0.063 | +741.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15715 | -0.063 | +741.77€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7957 | -0.030 | -141.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7957 | -0.030 | -141.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1864 | -0.041 | -17.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1864 | -0.041 | -17.31€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1083 | -0.046 | -19.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1083 | -0.046 | -19.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 769 | -0.021 | -24.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 769 | -0.021 | -24.37€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1320 | +0.114 | +475.89€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1184 | +0.120 | +463.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 277 | +0.138 | +139.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 277 | +0.138 | +139.62€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#DOGE | 224 | +0.106 | +61.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 224 | +0.106 | +61.70€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 241 | +0.109 | +90.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 241 | +0.109 | +90.42€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 211 | +0.139 | +103.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 211 | +0.139 | +103.68€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 231 | +0.101 | +67.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 231 | +0.101 | +67.88€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 803 | -0.029 | -38.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 803 | -0.029 | -38.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 158 | -0.006 | +3.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 158 | -0.006 | +3.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 115 | -0.021 | -4.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 115 | -0.021 | -4.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 220 | -0.054 | -23.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 220 | -0.054 | -23.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 175 | +0.003 | +1.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 175 | +0.003 | +1.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 135 | -0.062 | -15.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 135 | -0.062 | -15.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 714 | -0.092 | -64.70€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 326 | -0.146 | -77.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 255 | -0.189 | -72.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 252 | -0.051 | -1.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 183 | -0.057 | -4.31€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 69 | -0.035 | +3.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 136 | -0.036 | +14.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 108 | -0.054 | +8.12€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 546 | -0.119 | -68.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 168 | -0.006 | +4.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 861 | -0.201 | -47.19€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 357 | -0.194 | -31.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 307 | -0.196 | -31.46€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 292 | -0.218 | -29.97€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 251 | -0.227 | -35.81€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 212 | -0.187 | +14.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 194 | -0.184 | +10.42€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 752 | -0.204 | -56.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 354 | +0.402 | +287.59€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 90 | +0.370 | +74.48€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 90 | +0.370 | +74.48€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 224 | +0.460 | +214.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 224 | +0.460 | +214.35€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 354 | +0.402 | +287.59€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 603 | +0.027 | +15.77€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 603 | +0.027 | +15.77€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 295 | +0.022 | +2.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 63 | -0.008 | -1.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 63 | -0.008 | -1.69€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 202 | +0.039 | +14.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 202 | +0.039 | +14.40€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 3039 | -0.024 | -126.75€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3039 | -0.024 | -126.75€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 903 | -0.021 | -32.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 903 | -0.021 | -32.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 577 | -0.025 | -24.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 577 | -0.025 | -24.71€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1403 | -0.022 | -55.45€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1403 | -0.022 | -55.45€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9460 | +0.020 | +109.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9460 | +0.020 | +109.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2620 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2620 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2172 | +0.029 | +49.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2172 | +0.029 | +49.72€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2843 | +0.010 | +1.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2843 | +0.010 | +1.40€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1825 | +0.022 | +30.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1825 | +0.022 | +30.00€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8409 | +0.013 | -42.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8409 | +0.013 | -42.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3316 | +0.017 | -6.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3316 | +0.017 | -6.26€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3348 | +0.012 | -23.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3348 | +0.012 | -23.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1745 | +0.008 | -13.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1745 | +0.008 | -13.14€ | 1 | 0 |
| ✅ UPDOWN_GBM | 51770 | +0.040 | +3738.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13196 | +0.076 | +2714.22€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1753 | +0.006 | +10.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 33576 | +0.032 | +981.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3056 | +0.005 | +36.45€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5276 | +0.076 | +681.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1014 | +0.155 | +445.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4229 | +0.058 | +237.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9940 | +0.049 | +787.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1703 | +0.090 | +392.91€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 470 | +0.013 | +5.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6313 | +0.051 | +354.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1383 | +0.005 | +34.73€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 71 | -0.089 | +0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6104 | +0.046 | +444.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 995 | +0.136 | +351.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5081 | +0.029 | +94.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11412 | +0.031 | +604.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3258 | +0.054 | +445.85€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 463 | +0.007 | +9.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6593 | +0.027 | +149.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1036 | +0.002 | -3.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 62 | -0.125 | +2.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11560 | +0.020 | +390.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3124 | +0.030 | +260.27€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 453 | -0.001 | -0.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7292 | +0.020 | +131.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 637 | +0.007 | +4.72€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 54 | -0.161 | -4.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7476 | +0.045 | +832.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3102 | +0.093 | +818.74€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 306 | +0.006 | -1.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4068 | +0.012 | +14.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 187 | -0.124 | -2.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 665 | +0.358 | +231.97€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 665 | +0.358 | +231.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 363 | +0.363 | +124.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 363 | +0.363 | +124.59€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 302 | +0.349 | +107.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 302 | +0.349 | +107.38€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14832 | -0.030 | +3427.77€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14832 | -0.030 | +3427.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1107 | -0.058 | +371.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1107 | -0.058 | +371.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2658 | -0.114 | +114.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2658 | -0.114 | +114.25€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 613 | +0.201 | +462.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 613 | +0.201 | +462.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1715 | +0.216 | +1121.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1715 | +0.216 | +1121.68€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4370 | -0.063 | +615.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4370 | -0.063 | +615.67€ | 3 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4369 | -0.069 | +741.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4369 | -0.069 | +741.94€ | 4 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1074 | +0.294 | +897.13€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1074 | +0.294 | +897.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 588 | +0.286 | +451.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 588 | +0.286 | +451.48€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 486 | +0.301 | +445.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 486 | +0.301 | +445.65€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 750 | -0.112 | -82.64€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 750 | -0.112 | -82.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 223 | -0.087 | -17.79€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 223 | -0.087 | -17.79€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 78 | -0.175 | -5.47€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 78 | -0.175 | -5.47€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2823 | +0.307 | +1399.95€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 994 | +0.260 | +149.29€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 1079 | +0.299 | +475.76€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 750 | +0.378 | +774.90€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.052) — sin ventaja clara. oversold(IBS<0.3): IC=+0.051 n=18178 | neutral: IC=+0.042 n=19206 | overbought(IBS>0.7): IC=+0.093 n=18464
  - _Datos_: n=57881 IC=+0.062 PNL=+7764.40€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 600 celda(s) pasan gate riguroso completo de 2394 evaluadas (n>=40) y 3390 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.030 < 0.08 — monitorear
  - _Datos_: n=3124 IC=+0.030 PNL=+260.27€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1079/15 IC=+0.299 PNL=+475.76€ | BTC: n=994/15 IC=+0.260 PNL=+149.29€ | SOL: n=750/15 IC=+0.378 PNL=+774.90€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 51708 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.122 n=490/60 | contraria IC=+0.186 n=495 | gap=-0.064 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=358, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 211 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1036/40 IC=+0.002 PNL=-3.00€ | BTC#60min: n=1383/40 IC=+0.005 PNL=+34.73€ | SOL#60min: n=637/40 IC=+0.007 PNL=+4.72€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=413219 | tras_1loss IC=+0.086 n=318347 | tras_2loss IC=+0.055 n=131727/40 | gap=-0.006 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.022 n=6469 | contrario_BTC IC=+0.038 n=5711/40 | gap=+0.016 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=429 PNL=+351.48€
  - _Datos_: n=429 IC=+0.217 PNL=+351.48€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=490 PNL=+371.88€
  - _Datos_: n=490 IC=+0.217 PNL=+371.88€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.08 con n=48 PNL=+32.92€
  - _Datos_: n=48 IC=+0.220 PNL=+32.92€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=2303 PNL=+1267.98€
  - _Datos_: n=2303 IC=+0.333 PNL=+1267.98€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=397 IC=+0.071 PNL=+44.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=397 IC=+0.071 PNL=+44.23€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=62 IC=+0.188 PNL=+41.81€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=62 IC=+0.188 PNL=+41.81€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=49320 IC=+0.040 PNL=+3559.63€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49320 IC=+0.040 PNL=+3559.63€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.067 PNL=+7.14€)
  - _Datos_: n=4 IC=+0.067 PNL=+7.14€

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
  - _Estado_: n=2088 IC=+0.007 PNL=+0.61€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2088 IC=+0.007 PNL=+0.61€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=968 IC=+0.000 PNL=+35.85€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=968 IC=+0.000 PNL=+35.85€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=646 IC=+0.015 PNL=+27.45€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=646 IC=+0.015 PNL=+27.45€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=2843 PNL=+2018.08€
  - _Datos_: n=2843 IC=+0.202 PNL=+2018.08€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1802 IC=+0.067 PNL=+148.93€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1802 IC=+0.067 PNL=+148.93€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1703 IC=+0.090 PNL=+392.91€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1703 IC=+0.090 PNL=+392.91€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=7538 PNL=+2040.16€
  - _Datos_: n=7538 IC=+0.095 PNL=+2040.16€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=201 IC=-0.264 PNL=-12.84€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=201 IC=-0.264 PNL=-12.84€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=321 IC=-0.033 PNL=-5.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=321 IC=-0.033 PNL=-5.99€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=689 IC=+0.022 PNL=+55.52€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=689 IC=+0.022 PNL=+55.52€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=74 IC=+0.053 PNL=+4.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=74 IC=+0.053 PNL=+4.31€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6799 IC=+0.007 PNL=+56.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6799 IC=+0.007 PNL=+56.81€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=74 PNL=+21.75€
  - _Datos_: n=74 IC=+0.184 PNL=+21.75€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.258 n=122) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=122 IC=+0.258 PNL=+105.64€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=9245 IC=+0.041 PNL=+625.68€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=9245 IC=+0.041 PNL=+625.68€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=3121 IC=+0.061 PNL=+420.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3121 IC=+0.061 PNL=+420.49€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=417 PNL=+127.46€
  - _Datos_: n=417 IC=+0.111 PNL=+127.46€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=784 PNL=+208.23€
  - _Datos_: n=784 IC=+0.150 PNL=+208.23€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=603 PNL=+343.99€
  - _Datos_: n=603 IC=+0.113 PNL=+343.99€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64288 IC=+0.118 PNL=+23913.28€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64288 IC=+0.118 PNL=+23913.28€

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
  - _Estado_: n=7720 IC=+0.046 PNL=+665.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7720 IC=+0.046 PNL=+665.29€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.02 con n=756 PNL=+292.24€
  - _Datos_: n=756 IC=+0.120 PNL=+292.24€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=179 IC=-0.064 PNL=+28.99€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=179 IC=-0.064 PNL=+28.99€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=1320 PNL=+1295.87€
  - _Datos_: n=1320 IC=+0.451 PNL=+1295.87€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=19091 IC=+0.065 PNL=+2600.72€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=19091 IC=+0.065 PNL=+2600.72€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=4618 PNL=+2700.52€
  - _Datos_: n=4618 IC=+0.207 PNL=+2700.52€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.155 < -0.1 con n=308 PNL=+27.36€
  - _Datos_: n=308 IC=-0.155 PNL=+27.36€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2385 IC=+0.058 PNL=+253.54€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2385 IC=+0.058 PNL=+253.54€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=101 IC=-0.121 PNL=+1.95€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=101 IC=-0.121 PNL=+1.95€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.1 con n=560 PNL=+147.67€
  - _Datos_: n=560 IC=+0.121 PNL=+147.67€

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
  - _Estado_: n=22745 IC=-0.135 PNL=+1731.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=22745 IC=-0.135 PNL=+1731.96€

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
  - _Estado_: n=2340 IC=+0.138 PNL=+1360.82€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2340 IC=+0.138 PNL=+1360.82€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.08 con n=2804 PNL=+2005.45€
  - _Datos_: n=2804 IC=+0.203 PNL=+2005.45€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=5396 IC=+0.033 PNL=+292.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5396 IC=+0.033 PNL=+292.55€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=2551 PNL=+1381.14€
  - _Datos_: n=2551 IC=+0.090 PNL=+1381.14€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.215 > 0.08 con n=599 PNL=+322.42€
  - _Datos_: n=599 IC=+0.215 PNL=+322.42€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.227 < -0.1 con n=2259 PNL=-176.81€
  - _Datos_: n=2259 IC=-0.227 PNL=-176.81€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6604 IC=+0.182 PNL=+4604.08€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6604 IC=+0.182 PNL=+4604.08€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=91 PNL=+32.89€
  - _Datos_: n=91 IC=+0.102 PNL=+32.89€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2375 IC=+0.070 PNL=+746.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2375 IC=+0.070 PNL=+746.73€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=2174 PNL=+1531.21€
  - _Datos_: n=2174 IC=+0.177 PNL=+1531.21€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3636 IC=-0.031 PNL=+952.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3636 IC=-0.031 PNL=+952.23€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.085 > 0.08 con n=598 PNL=-53.62€
  - _Datos_: n=598 IC=+0.085 PNL=-53.62€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=3831 PNL=-327.49€
  - _Datos_: n=3831 IC=+0.239 PNL=-327.49€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=46 IC=+0.000 PNL=+5.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=46 IC=+0.000 PNL=+5.83€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=1321) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1321 IC=+0.100 PNL=+300.86€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.322 > 0.08 con n=335 PNL=+110.55€
  - _Datos_: n=335 IC=+0.322 PNL=+110.55€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.408 n=487) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=487 IC=+0.408 PNL=+684.31€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=10575 IC=+0.181 PNL=-1152.04€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10575 IC=+0.181 PNL=-1152.04€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.1 con n=168 PNL=+102.14€
  - _Datos_: n=168 IC=+0.206 PNL=+102.14€
