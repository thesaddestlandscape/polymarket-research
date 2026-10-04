# Hipótesis automáticas — 2026-10-04 18:42 UTC
_Generado por shadow_postmortem.py sobre 748040 resoluciones (PNL=+90631.47€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.221 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.8012` → IC=+0.263 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8012 (IC base=+0.132)

- **PATRÓN** `banda_z` > `9.189` → IC=+0.198 (n=210)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.189 (IC base=+0.132)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.71` → IC=+0.132 (n=563)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.71 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.135 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 11.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=666)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2353.6258` → IC=+0.137 (n=563)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2353.6258 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.225 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.197 (n=229)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 67.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.254 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.139)

- **PATRÓN** `banda_z` > `9.932` → IC=+0.212 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.932 (IC base=+0.139)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.903` → IC=+0.139 (n=411)

  - _Acción_: Kelly boost +0.70€ cuando `ballenas_wallet_edge_medio` > 0.903 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.141 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 12.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=568)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4546.1989` → IC=+0.143 (n=228)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4546.1989 (IC base=+0.139)

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
- **FILTRO** `restante_s_al_confirmar` < `144.08` → IC=-0.215 (n=8285)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.08
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=24860)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `131.73` → IC=-0.270 (n=1070)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.73
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3212)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.29` → IC=-0.303 (n=973)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.29
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2921)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.74` → IC=-0.223 (n=2077)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.74
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6231)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.58` → IC=-0.322 (n=1607)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.58
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=4821)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.213 (n=16051)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=3852)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `5397.7239` → IC=+0.170 (n=2501)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5397.7239 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=14070)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=17151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=13174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6324)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7631.7113` → IC=+0.169 (n=2421)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7631.7113 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=1838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `16028.7692` → IC=+0.222 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16028.7692 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1842)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2361)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15958.35` → IC=+0.209 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15958.35 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.122 (n=1027)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.555 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.126 (n=249)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.091)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.135 (n=931)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.44 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `5732.4723` → IC=+0.151 (n=233)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 5732.4723 (IC base=+0.091)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.153 (n=2861)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.356 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=1505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.362 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.257 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=646)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2161.1743` → IC=+0.154 (n=362)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2161.1743 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.407 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=649)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=805)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.225 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=14163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=12046)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.234 (n=4476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=3158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3208)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=1359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.235 (n=1362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.337 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.233)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.192 (n=1282)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.73 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=988)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=3213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=2426)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.194 (n=1166)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3895.4216` → IC=+0.444 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3895.4216 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.442 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `14878.5401` → IC=+0.441 (n=168)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=42148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=18543)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=7260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=5821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.197 (n=7979)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=3761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.268 (n=4298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=7669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7663)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=3790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.271 (n=2590)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=6991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.204 (n=5583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2769)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=3218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=6462)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.125 (n=5996)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=6207)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.137 (n=5972)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.49 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=3237)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.127 (n=2972)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3095)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=3918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.18` → IC=+0.144 (n=2966)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.18 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.185 (n=3225)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.130 (n=3406)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=3008)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.311 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.289 (n=1292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4177.6236` → IC=+0.303 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4177.6236 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.336 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4309.4335` → IC=+0.294 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4309.4335 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.294 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1429.9411` → IC=+0.301 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1429.9411 (IC base=+0.287)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.442 (n=290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.437 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.457 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.441 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `2142.5668` → IC=+0.456 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2142.5668 (IC base=+0.441)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4852` → IC=+0.130 (n=10085)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4852 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.242 (n=3362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2156` → IC=+0.256 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2156 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.01` → IC=+0.183 (n=3831)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.01 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2103` → IC=+0.251 (n=2821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2103 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.255 (n=2822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.225 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `1.4655` → IC=+0.211 (n=7058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4655 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5672` → IC=+0.138 (n=12231)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5672 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5804` → IC=+0.204 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5804 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1474` → IC=+0.176 (n=4038)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1474 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.178 (n=4455)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1954 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.2949` → IC=+0.222 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2949 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4504` → IC=+0.198 (n=7637)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4504 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.213 (n=7441)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.221 (n=750)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=751)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3497` → IC=+0.184 (n=2248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3497 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=1091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.185 (n=1499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.22` → IC=+0.285 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.22 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.225 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.180 (n=2125)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2309)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2041.6724` → IC=+0.186 (n=750)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2041.6724 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.242 (n=1600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1251` → IC=+0.263 (n=787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1251 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0605` → IC=+0.282 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0605 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.49` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.49 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.236 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.232 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.261 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.6087` → IC=+0.246 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6087 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1596.72` → IC=+0.245 (n=1787)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1596.72 (IC base=+0.232)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.238 (n=782)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.3506` → IC=+0.230 (n=1774)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3506 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=1778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.218 (n=1816)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9796` → IC=+0.259 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9796 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1887` → IC=+0.219 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1887 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.3434` → IC=+0.222 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3434 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.772` → IC=+0.256 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.772 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.2499` → IC=+0.222 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2499 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6169` → IC=+0.223 (n=1773)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6169 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.238 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.4118` → IC=+0.243 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4118 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.183 (n=595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.164 (n=594)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7224` → IC=+0.176 (n=1780)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7224 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1267` → IC=+0.153 (n=1593)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1267 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.294` → IC=+0.139 (n=283)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 11.294 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.143 (n=1634)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.146 (n=1780)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2025 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6207` → IC=+0.136 (n=1780)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6207 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0954` → IC=+0.168 (n=643)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0954 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.148 (n=1669)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.144 (n=1115)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.171 (n=700)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 231.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.199 (n=2269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=2270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=2039)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.260 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.345` → IC=+0.255 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.345 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.194 (n=1985)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.196 (n=301)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.1719` → IC=+0.204 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1719 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2711)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `1952.3598` → IC=+0.195 (n=1028)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1952.3598 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.220 (n=1758)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.1763` → IC=+0.219 (n=878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1763 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=930)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0649` → IC=+0.230 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0649 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.717` → IC=+0.240 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.717 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.256 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7339` → IC=+0.215 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7339 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7571` → IC=+0.221 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7571 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1940.5976` → IC=+0.211 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1940.5976 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.211 (n=1805)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=121)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2697)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.156 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0036 (IC base=+0.043)

- **PATRÓN** `ibs_20min` > `0.9624` → IC=+0.224 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9624 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.5192` → IC=+0.323 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5192 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.913` → IC=+0.175 (n=894)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 4.913 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.335 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.326 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.1123` → IC=+0.332 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1123 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4257` → IC=+0.354 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4257 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.8701` → IC=+0.322 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8701 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.326 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.1007` → IC=+0.158 (n=705)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1007 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.309` → IC=+0.193 (n=327)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.309 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8486` → IC=+0.153 (n=741)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8486 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.198 (n=147)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.163 (n=945)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.025)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=414)

- **FILTRO** `ibs_20min` < `0.314` → IC=-0.177 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` < 0.314
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=366)

- **FILTRO** `ibs_20min` > `0.2368` → IC=-0.126 (n=2725)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=1346)

- **FILTRO** `sigma_ewma_delta_pct` > `8.797` → IC=-0.216 (n=428)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.797
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=3643)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.202 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7913 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.359` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.359 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.268 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8803 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1494` → IC=+0.286 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1494 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.5444` → IC=+0.282 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5444 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.281 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.2368` → IC=+0.134 (n=1346)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2368 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.1755` → IC=+0.264 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1755 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.277 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.306 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4205` → IC=+0.290 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4205 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.638` → IC=-0.173 (n=714)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.638
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2145)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.203 (n=694)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2165)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.207 (n=1040)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=3188)

- **PATRÓN** `dist_vwap_pct` > `0.7824` → IC=+0.320 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7824 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2747` → IC=+0.314 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2747 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9872` → IC=+0.293 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9872 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.310 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.301 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.297 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8546` → IC=+0.301 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8546 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.851` → IC=+0.287 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.851 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.7204` → IC=+0.251 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7204 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.0723` → IC=+0.272 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0723 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.266 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.144` → IC=+0.256 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.144 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.4215` → IC=+0.252 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4215 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.199 (n=4378)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4711` → IC=+0.188 (n=11734)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4711 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.9853` → IC=+0.286 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9853 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.685` → IC=+0.158 (n=5978)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.685 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1766` → IC=+0.247 (n=4787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1766 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6148` → IC=+0.253 (n=4785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6148 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.0807` → IC=+0.242 (n=7081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0807 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.261 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.4668` → IC=+0.241 (n=2577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4668 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6436` → IC=+0.255 (n=2576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6436 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.276 (n=7262)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.165 (n=4239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.009 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5462` → IC=+0.156 (n=11182)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5462 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.6863` → IC=+0.249 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6863 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2364` → IC=+0.247 (n=3649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2364 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7073` → IC=+0.249 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7073 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.1953` → IC=+0.259 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1953 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.303 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5918` → IC=+0.277 (n=2329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5918 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.280 (n=5196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.259` → IC=-0.160 (n=912)

  - _Acción_: SKIP cuando `ibs_20min` < 0.259
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2736)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.176 (n=747)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2243)

- **FILTRO** `sigma_ewma_delta_pct` > `4.579` → IC=-0.173 (n=671)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.579
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2319)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.277 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.22` → IC=+0.201 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.22 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.272 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.208 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1956` → IC=+0.228 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1956 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.229 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.420 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2235` → IC=+0.429 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2235 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.5483` → IC=+0.431 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5483 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.5399` → IC=+0.428 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5399 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.428 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.161 (n=882)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8641 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.112` → IC=+0.190 (n=682)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.112 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.167 (n=1237)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2036 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6758` → IC=+0.180 (n=1105)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6758 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0744` → IC=+0.169 (n=1139)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0744 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.217 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.200 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4271` → IC=+0.185 (n=405)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4271 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.226 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 229.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1453` → IC=+0.224 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1453 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `0.6127` → IC=+0.226 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6127 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.0728` → IC=+0.220 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0728 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.289 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.4405` → IC=+0.234 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4405 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1719` → IC=+0.234 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1719 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.272 (n=2001)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.256 (n=1800)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=1791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.772` → IC=+0.280 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.772 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.266 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `1.626` → IC=+0.259 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.626 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `2012.1448` → IC=+0.273 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2012.1448 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.301 (n=1663)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.299 (n=731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.321 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.292 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.0997` → IC=+0.287 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0997 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.689` → IC=+0.295 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.689 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.1953` → IC=+0.281 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1953 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.3399` → IC=+0.292 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3399 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.7255` → IC=+0.296 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7255 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.296 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1934.7584` → IC=+0.304 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.7584 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.287 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7715` → IC=-0.182 (n=760)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=2282)

- **PATRÓN** `ibs_20min` > `0.9034` → IC=+0.170 (n=686)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.9034 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.2239` → IC=+0.233 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2239 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0078` → IC=+0.249 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0078 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.1688` → IC=+0.236 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1688 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.0821` → IC=+0.248 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0821 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.263 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.261 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1237` → IC=+0.236 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1237 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1801` → IC=+0.220 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1801 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.284 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8338` → IC=+0.270 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8338 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.255 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.184 (n=1396)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.285 (n=1396)

- **FILTRO** `ibs_20min` > `0.675` → IC=-0.242 (n=699)

  - _Acción_: SKIP cuando `ibs_20min` > 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2105)

- **FILTRO** `sigma_ewma_delta_pct` > `4.839` → IC=-0.203 (n=598)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.839
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2206)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.285 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.318 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.69` → IC=+0.171 (n=439)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.69 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.8598` → IC=+0.312 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8598 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.303 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.301 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.316 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `1.4306` → IC=+0.321 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4306 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.322 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.132 (n=1853)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.2679` → IC=+0.239 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2679 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.275 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.229 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1883 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.260 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4284` → IC=+0.249 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4284 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.259 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.020)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.329 (n=1436)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.305 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.317 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.319 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.310 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.285)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.299 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.332 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.296 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2473.4216` → IC=+0.297 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2473.4216 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.315 (n=1135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.1892` → IC=+0.286 (n=749)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1892 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=1702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.308 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.3068` → IC=+0.295 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3068 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.516` → IC=+0.298 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.516 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` < `0.7171` → IC=+0.284 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7171 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.314 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.2342` → IC=+0.330 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2342 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.293 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.1375` → IC=+0.280 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1375 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2428.9954` → IC=+0.289 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2428.9954 (IC base=+0.284)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.188 (n=3285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.205 (n=3284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3557` → IC=+0.185 (n=8668)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3557 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=10284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.226 (n=9851)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1718` → IC=+0.197 (n=4269)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1718 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.415` → IC=+0.252 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.415 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.207` → IC=+0.167 (n=6544)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.207 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.163 (n=6546)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6297 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.197 (n=1464)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4506` → IC=+0.173 (n=3167)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4506 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.182 (n=3165)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1979.9172` → IC=+0.177 (n=8800)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1979.9172 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.189 (n=8758)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 104.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.187 (n=6253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.220 (n=3129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=3583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.229 (n=9380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4872 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1687` → IC=+0.167 (n=6496)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1687 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.308` → IC=+0.196 (n=1575)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.308 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.161 (n=6726)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1776 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.215 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5583` → IC=+0.172 (n=3820)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5583 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.6165` → IC=+0.175 (n=2894)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6165 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.181 (n=8346)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 107.0 (IC base=+0.173)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.240 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.205 (n=554)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.3411` → IC=+0.220 (n=1655)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3411 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=1104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.9157` → IC=+0.285 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9157 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.239` → IC=+0.330 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.239 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.245 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.196 (n=1548)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2042.94` → IC=+0.202 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.94 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.248 (n=1101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.247 (n=1251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1013` → IC=+0.293 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1013 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=1119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.1055` → IC=+0.276 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1055 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.39` → IC=+0.245 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.39 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.223` → IC=+0.246 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.223 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.238 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.265 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.263 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.621` → IC=+0.240 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.621 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1595.38` → IC=+0.256 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1595.38 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.226 (n=495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0688` → IC=+0.197 (n=493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0688 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=1479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.394` → IC=+0.224 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.394 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.209 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.234 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6889` → IC=+0.169 (n=650)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6889 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.197 (n=232)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4139` → IC=+0.185 (n=480)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4139 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `11907.096` → IC=+0.161 (n=1319)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11907.096 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `434.0` → IC=+0.159 (n=1398)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 434.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.160 (n=1547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2943` → IC=+0.165 (n=1546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2943 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=725)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5923` → IC=+0.196 (n=1546)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5923 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.169 (n=1523)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.883` → IC=+0.196 (n=304)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.883 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.160 (n=1546)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2116 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.2276` → IC=+0.144 (n=1588)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2276 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0697` → IC=+0.147 (n=693)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0697 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4713` → IC=+0.151 (n=1434)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4713 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=451)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.227 (n=551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2456` → IC=+0.221 (n=1102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2456 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.512` → IC=+0.278 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.512 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.203 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1277` → IC=+0.207 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1277 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.214 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `1943.8205` → IC=+0.215 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1943.8205 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.240 (n=1235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1428` → IC=+0.258 (n=618)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1428 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.247 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.254 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.259 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.7484` → IC=+0.236 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7484 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1707` → IC=+0.226 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1707 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1933.7358` → IC=+0.226 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.7358 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.215 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.185 (n=1390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0064 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.201 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3395` → IC=+0.204 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3395 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1389` → IC=+0.185 (n=1035)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1389 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.217 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.165 (n=1053)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8561 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.171 (n=661)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4305` → IC=+0.168 (n=516)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4305 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.160 (n=516)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5129.2383` → IC=+0.194 (n=1053)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 5129.2383 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.154 (n=1519)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 152.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.156 (n=1645)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3811` → IC=+0.147 (n=1645)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3811 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6652` → IC=+0.179 (n=1645)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6652 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.149 (n=1606)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.896` → IC=+0.165 (n=574)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.896 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.154 (n=1097)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8548 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.181 (n=246)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8146` → IC=+0.138 (n=1014)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8146 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5407` → IC=+0.131 (n=507)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5407 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `4262.9422` → IC=+0.159 (n=1097)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4262.9422 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.123 (n=1462)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 151.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.158 (n=817)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.01 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4494` → IC=+0.128 (n=1584)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4494 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.215 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `1.0636` → IC=+0.217 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0636 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.898` → IC=+0.260 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.898 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.2058` → IC=+0.138 (n=1800)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2058 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.6472` → IC=+0.132 (n=1800)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6472 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.134 (n=1811)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0708` → IC=+0.129 (n=748)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.0708 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.5419` → IC=+0.144 (n=765)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5419 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=1879)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2388.4402` → IC=+0.184 (n=1200)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2388.4402 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.148 (n=1409)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 46.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.160 (n=795)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0061 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.178 (n=603)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.217 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5789 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.9924` → IC=+0.122 (n=236)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.9924 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.1986` → IC=+0.147 (n=1651)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1986 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.439` → IC=+0.127 (n=743)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.439 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.153 (n=604)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6382 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2289` → IC=+0.153 (n=315)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2289 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4516` → IC=+0.137 (n=552)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4516 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4388` → IC=+0.124 (n=552)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.4388 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3058.8778` → IC=+0.190 (n=602)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3058.8778 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.127 (n=1608)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.229 (n=1689)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.287` → IC=+0.214 (n=1127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.287 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.244 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2034` → IC=+0.214 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2034 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.244 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.1949` → IC=+0.212 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1949 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.218 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.624 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.268 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.212 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.213 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2466.454` → IC=+0.209 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2466.454 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.227 (n=761)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.218 (n=786)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.239 (n=577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.287 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `1.1683` → IC=+0.233 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1683 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.252 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6364` → IC=+0.224 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6364 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.274 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4369` → IC=+0.213 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4369 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2407.4896` → IC=+0.220 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.4896 (IC base=+0.213)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.195 (n=1137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0042 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.171 (n=860)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0084 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.179 (n=2270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=1270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.3438` → IC=+0.196 (n=2579)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3438 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.7903` → IC=+0.188 (n=411)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7903 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.75` → IC=+0.194 (n=1126)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.75 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8717` → IC=+0.191 (n=1534)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8717 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.177 (n=768)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2084 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.170 (n=2286)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1032` → IC=+0.173 (n=930)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1032 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.183 (n=835)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `1.823` → IC=+0.173 (n=1668)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.823 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=2933)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2693.0092` → IC=+0.170 (n=2304)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2693.0092 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.187 (n=2356)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 143.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.157 (n=886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0037 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=2496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.193 (n=885)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0714 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.145 (n=858)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2755.5763` → IC=+0.126 (n=2366)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2755.5763 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.123 (n=1108)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 28.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.3292` → IC=+0.166 (n=693)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3292 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.6376` → IC=+0.205 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6376 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.2868` → IC=+0.169 (n=243)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2868 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.181` → IC=+0.170 (n=301)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.181 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.922` → IC=+0.147 (n=729)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.922 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8863` → IC=+0.177 (n=462)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8863 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0931` → IC=+0.149 (n=661)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0931 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.147 (n=276)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.2382` → IC=+0.155 (n=595)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.2382 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.5207` → IC=+0.156 (n=603)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5207 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `10604.8706` → IC=+0.156 (n=693)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 10604.8706 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.199 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.209 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.160 (n=828)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.611` → IC=+0.182 (n=728)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.611 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1811` → IC=+0.156 (n=812)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1811 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.074` → IC=+0.146 (n=755)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.074 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.145 (n=827)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.218 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6954` → IC=+0.154 (n=739)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6954 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.192 (n=222)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1178` → IC=+0.159 (n=719)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1178 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4106` → IC=+0.147 (n=817)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4106 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=1071)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11929.6805` → IC=+0.142 (n=739)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11929.6805 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `294.0` → IC=+0.156 (n=701)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 294.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.243 (n=540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.3973` → IC=+0.213 (n=810)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3973 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.220 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.6714` → IC=+0.251 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6714 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.361` → IC=+0.216 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.361 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.208 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.334` → IC=+0.229 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.334 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.8422` → IC=+0.216 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8422 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.182` → IC=+0.221 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.182 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.229 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.240 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.1087` → IC=+0.226 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1087 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.127 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 11.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.0868` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.0868 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.143 (n=337)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6876 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.134 (n=121)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `3948.9234` → IC=+0.125 (n=683)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3948.9234 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4762` → IC=-0.122 (n=265)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4762
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=520)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.172 (n=610)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0051 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.5405` → IC=+0.160 (n=609)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5405 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.9532` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9532 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.339` → IC=+0.215 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.339 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.177 (n=536)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0671 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.6526` → IC=+0.165 (n=609)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6526 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` < `0.0789` → IC=+0.158 (n=522)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0789 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.175 (n=266)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=644)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3079.1777` → IC=+0.193 (n=203)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3079.1777 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.4762` → IC=+0.144 (n=520)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.4762 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.5687` → IC=+0.122 (n=247)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.5687 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2865.6878` → IC=+0.151 (n=267)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2865.6878 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.124 (n=360)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 23.0 (IC base=+0.054)

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
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.178 (n=4256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0046 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.210 (n=4239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=13316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9937` → IC=+0.308 (n=4240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9937 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1655` → IC=+0.185 (n=4855)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1655 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.249 (n=3134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2316` → IC=+0.165 (n=8518)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2316 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.200 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.5941` → IC=+0.196 (n=4100)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5941 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1813.5204` → IC=+0.180 (n=12717)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1813.5204 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.203 (n=10026)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.195 (n=5049)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1467` → IC=+0.192 (n=5031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1467 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=4301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4528` → IC=+0.247 (n=10062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4528 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2426` → IC=+0.162 (n=7087)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2426 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.061` → IC=+0.202 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.061 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.735` → IC=+0.184 (n=11031)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.735 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.163 (n=3414)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7051 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.246 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.8621` → IC=+0.188 (n=7109)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8621 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1747.428` → IC=+0.183 (n=11433)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1747.428 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=6948)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.250 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.226 (n=705)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.3555` → IC=+0.210 (n=2116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3555 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=1023)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.356 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.264 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.5626` → IC=+0.214 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5626 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2042.27` → IC=+0.217 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.27 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.264 (n=1153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1726)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1254` → IC=+0.281 (n=760)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1254 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3605` → IC=+0.283 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3605 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.509` → IC=+0.264 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.509 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.292 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.278 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1892)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1596.68` → IC=+0.270 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1596.68 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.211 (n=679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.164 (n=1359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2876` → IC=+0.205 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2876 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.188 (n=1167)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.754` → IC=+0.180 (n=342)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.754 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.2` → IC=+0.151 (n=1863)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.2 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.7032` → IC=+0.168 (n=896)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7032 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.193 (n=291)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1425` → IC=+0.159 (n=1742)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1425 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5162` → IC=+0.154 (n=1769)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5162 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `277.0` → IC=+0.176 (n=846)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 277.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1703)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.3282` → IC=+0.157 (n=1702)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3282 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6835` → IC=+0.194 (n=1702)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.6835 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.6505` → IC=+0.145 (n=263)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.6505 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.164 (n=1543)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.156 (n=286)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.315` → IC=+0.146 (n=1544)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.315 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1895` → IC=+0.159 (n=1702)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1895 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1533` → IC=+0.199 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1533 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.432` → IC=+0.154 (n=1603)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.432 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.158 (n=1068)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `415.0` → IC=+0.143 (n=1326)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 415.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.251 (n=697)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=2085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=2114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.85` → IC=+0.295 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.85 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.2061` → IC=+0.225 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2061 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.230 (n=2005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2018.8832` → IC=+0.236 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2018.8832 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.240 (n=1720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.246 (n=860)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.301 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.943` → IC=+0.280 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.943 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3428` → IC=+0.296 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3428 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7482` → IC=+0.234 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7482 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.155` → IC=+0.240 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.155 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1936.1784` → IC=+0.243 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1936.1784 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.252 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4298` → IC=+0.154 (n=2173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4298 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2722` → IC=+0.189 (n=2172)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2722 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.5524` → IC=+0.163 (n=600)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.5524 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.156 (n=890)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.164 (n=1449)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8743 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.184 (n=394)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5221` → IC=+0.161 (n=930)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5221 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.154 (n=959)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7367.7844` → IC=+0.233 (n=985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7367.7844 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.179 (n=683)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 70.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.165 (n=1167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0051 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3487` → IC=+0.139 (n=1539)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3487 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.7339` → IC=+0.178 (n=1749)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7339 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1467` → IC=+0.133 (n=1527)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1467 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.3` → IC=+0.167 (n=265)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.3 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6226` → IC=+0.143 (n=583)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6226 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.227 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.2469` → IC=+0.132 (n=1474)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2469 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4453` → IC=+0.140 (n=1674)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4453 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `8941.9701` → IC=+0.201 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8941.9701 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.131 (n=1677)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 168.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.144 (n=1458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.008 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.5617` → IC=+0.130 (n=2182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.5617 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4621` → IC=+0.202 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4621 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.048` → IC=+0.212 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.048 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.567` → IC=+0.246 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.567 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2309` → IC=+0.138 (n=2182)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2309 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.129 (n=2252)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4592` → IC=+0.128 (n=2124)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4592 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2219)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2550.0226` → IC=+0.235 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2550.0226 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.147 (n=652)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 27.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.181 (n=693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1303` → IC=+0.163 (n=692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1303 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5111` → IC=+0.234 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5111 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.138 (n=1705)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.486` → IC=+0.131 (n=2000)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.486 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.161 (n=913)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7144 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.181 (n=333)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.1597` → IC=+0.134 (n=1681)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1597 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2798.604` → IC=+0.196 (n=692)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2798.604 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.135 (n=1668)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 50.0 (IC base=+0.119)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.231 (n=2129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.218 (n=1539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.261 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.2101` → IC=+0.234 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2101 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.744` → IC=+0.262 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.744 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2371` → IC=+0.217 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2371 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.222 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2873` → IC=+0.242 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2873 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.5107` → IC=+0.247 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5107 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2350.077` → IC=+0.218 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2350.077 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.219 (n=746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.230 (n=1013)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.228 (n=1584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4194` → IC=+0.261 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4194 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `1.2042` → IC=+0.218 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2042 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2938` → IC=+0.215 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2938 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.848` → IC=+0.255 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.848 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.239 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.281 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.211 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2415.5464` → IC=+0.216 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2415.5464 (IC base=+0.212)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=3731)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.227 (n=1242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.5025` → IC=+0.194 (n=3723)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.5025 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=1397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.240 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1696` → IC=+0.192 (n=1403)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1696 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.215` → IC=+0.214 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.215 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.187 (n=1130)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.7119 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8955` → IC=+0.185 (n=1712)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8955 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1688` → IC=+0.210 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1688 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4546` → IC=+0.193 (n=1225)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4546 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.8633` → IC=+0.187 (n=2449)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8633 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=2780)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2921.897` → IC=+0.189 (n=3325)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2921.897 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.220 (n=940)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.4847` → IC=+0.179 (n=2810)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.4847 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.186 (n=1238)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1827 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.6563` → IC=+0.181 (n=525)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6563 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.2354` → IC=+0.156 (n=2489)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2354 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.223` → IC=+0.171 (n=2803)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.223 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2586` → IC=+0.167 (n=2646)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2586 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.168 (n=2563)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.164 (n=584)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5383` → IC=+0.170 (n=1221)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5383 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.8277` → IC=+0.173 (n=1850)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8277 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=3731)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `12369.0188` → IC=+0.169 (n=937)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 12369.0188 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.171 (n=2410)

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
- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.167 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0108 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.172 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.239 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9296 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.2209` → IC=+0.199 (n=257)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.2209 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.097` → IC=+0.216 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.097 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.182 (n=168)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.7119 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.2835` → IC=+0.139 (n=128)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.2835 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.219 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.545` → IC=+0.145 (n=164)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.545 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4567` → IC=+0.193 (n=125)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4567 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=453)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2997.549` → IC=+0.164 (n=382)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2997.549 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.161 (n=322)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 51.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.186 (n=304)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0067 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.392` → IC=+0.198 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.392 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.160 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 16.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.193 (n=216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 10.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.2619` → IC=+0.221 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2619 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.669` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.669 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.325` → IC=+0.166 (n=294)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 5.325 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.3839` → IC=+0.167 (n=304)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.3839 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.1845` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1845 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.219 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.6109` → IC=+0.184 (n=131)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.6109 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.176 (n=134)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3138.4241` → IC=+0.196 (n=304)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3138.4241 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.215 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.161)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.159 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0038 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.123 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 16.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.4606` → IC=+0.158 (n=1122)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.4606 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.143 (n=623)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.190 (n=259)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.184 (n=153)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.2295` → IC=+0.255 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2295 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.11` → IC=+0.137 (n=458)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.11 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.074` → IC=+0.140 (n=384)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.074 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.180 (n=151)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `2.6035` → IC=+0.152 (n=395)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.6035 (IC base=+0.052)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.138 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4301` → IC=+0.174 (n=384)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4301 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.159 (n=209)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.0809` → IC=+0.135 (n=302)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.0809 (IC base=+0.096)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.123 (n=213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0045 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.0689` → IC=+0.140 (n=209)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.0689 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.157 (n=211)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.9649` → IC=+0.127 (n=191)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.9649 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `0.6802` → IC=+0.133 (n=194)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6802 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.155 (n=195)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.082)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=151)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.154 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0047 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.7019` → IC=+0.214 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7019 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.176 (n=205)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.779` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.779 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.8082` → IC=+0.131 (n=247)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8082 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.143 (n=211)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.159 (n=326)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7058 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0108` → IC=-0.250 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=140)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.275 (n=109)

- **PATRÓN** `ibs_20min` > `0.7727` → IC=+0.173 (n=246)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.7727 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.7402` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.7402 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.631` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.631 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.052)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.164 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0087 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.275 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.936` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.936 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.8193` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8193 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.1345` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1345 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.203 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5975 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4436 (IC base=+0.053)

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
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=160)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.389 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.249 (n=177)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=181)

- **FILTRO** `volumen_pendiente_norm` > `0.0549` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=100)

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
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `volumen_regimen` > `0.8507` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8507
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=66)

- **FILTRO** `volumen_spike_ratio` > `1.5874` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5874
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=28)

- **FILTRO** `libro_liquidez` < `3685.6992` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 3685.6992
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=59)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7738` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.354 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=32)

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

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.175 (n=167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0057 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6472` → IC=+0.147 (n=366)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6472 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.4822` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4822 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6625` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6625 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.8223` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8223 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.176 (n=331)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.156 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.682` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.682 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.122 (n=300)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `4049.9464` → IC=+0.174 (n=170)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4049.9464 (IC base=+0.078)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6382` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6382
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=108)

- **PATRÓN** `sigma_h` > `0.0024` → IC=+0.178 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0024 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.216 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.206 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1435 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.0797` → IC=+0.151 (n=170)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.0797 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.332` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 4.332 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1443` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1443 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6691` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6691 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1846` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1846 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.2913` → IC=+0.197 (n=120)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2913 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4563` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4563 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3936.7645` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3936.7645 (IC base=+0.144)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1659` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1659
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=94)

- **FILTRO** `libro_liquidez` < `1457.1387` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 1457.1387
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=115)

- **FILTRO** `ibs_20min` > `0.2038` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2038
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=117)

- **PATRÓN** `volumen_spike_ratio` < `1.8267` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8267 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `1457.1387` → IC=+0.124 (n=115)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1457.1387 (IC base=+0.048)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.135 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.2038` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2038 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.056)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0941` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0941
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=31)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.265 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.252 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.92` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.92 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.025` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.025 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.0151` → IC=+0.267 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0151 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.089` → IC=+0.316 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.089 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.225)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=956)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2925.8106` → IC=+0.154 (n=330)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2925.8106 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=956)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2925.8106` → IC=+0.154 (n=330)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2925.8106 (IC base=+0.105)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2526)

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

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=100)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=162)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=995)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=949)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=584)

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
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=295)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.164 (n=108)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.027)

- **PATRÓN** `libro_liquidez` > `3914.0347` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3914.0347 (IC base=+0.027)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=755)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=755)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.131 (n=242)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=593)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=494)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=494)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=146)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=119)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=132)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=291)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=291)

- **FILTRO** `libro_liquidez` < `553.2637` → IC=-0.136 (n=105)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.2637
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=216)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=179)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=1078)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1109)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.121 (n=151)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=57)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.146 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=203)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.45 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.045)

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

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.51 (IC base=+0.011)

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

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.5 (IC base=+0.083)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.148 (n=143)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=50)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.223 (n=63)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=130)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=163)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.150 (n=158)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=92)

- **FILTRO** `restante_min` < `3.43` → IC=-0.226 (n=82)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=168)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=194)

- **FILTRO** `lag_apertura_s` > `92.29` → IC=-0.209 (n=84)

  - _Acción_: SKIP cuando `lag_apertura_s` > 92.29
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=166)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.45` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.45 (IC base=+0.011)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.156 (n=155)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=86)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.5 (IC base=-0.047)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.222 (n=77)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=219)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.162 (n=4489)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=13652)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=4523)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=14247)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.192 (n=793)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2421)

- **PATRÓN** `libro_liquidez` > `1809.72` → IC=+0.130 (n=1093)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1809.72 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1581.1195` → IC=+0.145 (n=1141)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1581.1195 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.172 (n=814)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2448)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=794)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2606)

- **PATRÓN** `libro_liquidez` > `1808.0376` → IC=+0.129 (n=1110)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1808.0376 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.165 (n=772)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2434)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2445)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3185)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `libro_liquidez` < `16920.0467` → IC=-0.163 (n=176)

  - _Acción_: SKIP cuando `libro_liquidez` < 16920.0467
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=359)

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

- **FILTRO** `libro_liquidez` < `1954.2941` → IC=-0.172 (n=327)

  - _Acción_: SKIP cuando `libro_liquidez` < 1954.2941
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=664)

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
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=28234)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=9588)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=31301)

- **FILTRO** `ibs_7min` < `0.2619` → IC=-0.234 (n=10222)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2619
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=30667)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=13799)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=27090)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=12623)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=39254)

- **FILTRO** `ibs_7min` > `0.2903` → IC=-0.180 (n=12960)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=38917)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=2060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4887)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=1658)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5289)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.251 (n=2292)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4655)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.183 (n=1544)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5403)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.264 (n=2201)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6771)

- **FILTRO** `ibs_7min` > `0.7875` → IC=-0.209 (n=2242)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7875
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6730)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5332)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1717)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5276)

- **FILTRO** `ibs_7min` < `0.7429` → IC=-0.197 (n=1748)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5245)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.180 (n=1746)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5247)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.266 (n=1676)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5445)

- **FILTRO** `ibs_7min` > `0.2646` → IC=-0.194 (n=1780)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2646
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5341)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.190 (n=1772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5349)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.161 (n=1871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4725)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=1564)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5032)

- **FILTRO** `ibs_7min` < `0.7034` → IC=-0.246 (n=2175)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7034
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4421)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.215 (n=1517)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5079)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=2192)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=7380)

- **FILTRO** `ibs_7min` > `0.741` → IC=-0.172 (n=2392)

  - _Acción_: SKIP cuando `ibs_7min` > 0.741
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=7180)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=2171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4549)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.238 (n=1997)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4723)

- **FILTRO** `ibs_7min` < `0.7413` → IC=-0.187 (n=1680)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7413
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5040)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.179 (n=1626)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5094)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.266 (n=1713)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5212)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.180 (n=1731)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5194)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.185 (n=1692)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5233)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=1732)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=5205)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1702)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5235)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.183 (n=2361)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7533)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.274 (n=1582)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=5114)

- **FILTRO** `ibs_7min` < `0.2556` → IC=-0.222 (n=1674)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2556
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=5022)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1660)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=5036)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.206 (n=2347)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7046)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1220)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=613)

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
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=342)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.138 (n=150)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=294)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.159 (n=162)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=489)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.136 (n=904)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `442.2457` → IC=+0.148 (n=302)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 442.2457 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.130 (n=771)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 53.0 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.438` → IC=+0.171 (n=71)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.438 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.139 (n=225)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.04 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2596.4012` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2596.4012 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 12.0 (IC base=+0.139)

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
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.141 (n=157)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.120 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.171 (n=80)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=114)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.236 (n=339)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=168)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0051` → IC=-0.248 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=51)

- **FILTRO** `T_h` > `89.1097` → IC=-0.397 (n=37)

  - _Acción_: SKIP cuando `T_h` > 89.1097
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=115)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.255 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=-0.078)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.078)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `pct_vs_K` |x|> `8.662` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.662
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.200 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=24)

- **FILTRO** `T_h` < `87.1706` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `T_h` < 87.1706
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.7555` → IC=-0.246 (n=116)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7555
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=350)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.306 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=307)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.316 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=307)

- **FILTRO** `T_h` > `57.7978` → IC=-0.314 (n=305)

  - _Acción_: SKIP cuando `T_h` > 57.7978
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=103)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.6765` → IC=-0.149 (n=109)

  - _Acción_: SKIP cuando `T_h` > 87.6765
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.381 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=123)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.316 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=76)

- **FILTRO** `T_h` > `143.1632` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=100)

- **FILTRO** `T_h` < `95.9199` → IC=-0.324 (n=49)

  - _Acción_: SKIP cuando `T_h` < 95.9199
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=101)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.270 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=45)

- **FILTRO** `T_h` > `135.986` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=99)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=94)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.318 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=93)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.7818` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7818
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=77)

- **FILTRO** `sigma_h` > `0.0108` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=42)

- **FILTRO** `T_h` > `41.2311` → IC=-0.373 (n=61)

  - _Acción_: SKIP cuando `T_h` > 41.2311
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.470 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.350)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.378 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.350)

- **PATRÓN** `T_h` > `1.2173` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2173 (IC base=+0.350)

- **PATRÓN** `dist_50` > `0.4086` → IC=+0.460 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4086 (IC base=+0.350)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.371 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.350)

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
- **PATRÓN** `edge` > `0.1992` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1992 (IC base=+0.438)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.470 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.438)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.438)

- **PATRÓN** `dist_50` > `0.3553` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3553 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.438)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=544)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=764)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=911)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=905)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3367)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1753)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.212 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.240 (n=741)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0507` → IC=+0.213 (n=743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0507 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2216` → IC=+0.215 (n=741)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2216 (IC base=+0.203)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1287` → IC=+0.233 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1287 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=2069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=2047)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.6197` → IC=+0.283 (n=2223)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6197 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1193` → IC=+0.204 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1193 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.798` → IC=+0.276 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.798 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2939.6834` → IC=+0.208 (n=1482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2939.6834 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.222 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.203)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=947)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.232 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.282 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.219)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.255 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.219)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.266 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.279 (n=460)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.270 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.607` → IC=+0.286 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.607 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.256 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.219)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.834` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.834
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=566)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.192 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.162 (n=220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2368` → IC=+0.175 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2368 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1217` → IC=+0.168 (n=188)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1217 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5831` → IC=+0.236 (n=499)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5831 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2752` → IC=+0.157 (n=461)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.2752 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.231 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3442.5061` → IC=+0.161 (n=446)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3442.5061 (IC base=+0.146)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.292 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1543` → IC=+0.212 (n=248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1543 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.198 (n=250)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3526` → IC=+0.236 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3526 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.587` → IC=+0.277 (n=280)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.587 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.188 (n=270)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=297)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `3077.8574` → IC=+0.291 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3077.8574 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.228 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.188)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.250 (n=502)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0807` → IC=+0.219 (n=247)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0807 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0429` → IC=+0.214 (n=561)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0429 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0888` → IC=+0.264 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0888 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.5849` → IC=+0.296 (n=561)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5849 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1364` → IC=+0.216 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1364 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.303` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.303 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.318` → IC=+0.215 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.318 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2923.757` → IC=+0.288 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2923.757 (IC base=+0.211)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.149 (n=611)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1143 (IC base=+0.061)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.371 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.365 (n=509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.359)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.360 (n=342)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.383 (n=339)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.388 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.403 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.396 (n=509)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.390 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.370 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.375 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.359)

- **PATRÓN** `ballena_activa_n` < `443.0` → IC=+0.379 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 443.0 (IC base=+0.359)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1118` → IC=+0.364 (n=123)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1118 (IC base=+0.363)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.370 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.364 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.374 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.363)

- **PATRÓN** `drift_15min` |x|≤ `0.5133` → IC=+0.367 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5133 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1537` → IC=+0.382 (n=185)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1537 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.383 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.393 (n=279)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.406 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.106` → IC=+0.371 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.106 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.384 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `500.0` → IC=+0.417 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 500.0 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.356 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.351)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.369 (n=105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.351)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.365 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.351)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.371 (n=207)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.351)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.378 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.351)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.411 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.351)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.401 (n=231)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.352 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.367 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.354 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.358 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.351)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.359 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.351)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.221 (n=827)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=2482)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.203 (n=1194)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2115)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.244 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.063)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.278 (n=803)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` > `0.1071` → IC=+0.195 (n=464)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1071 (IC base=-0.063)

- **PATRÓN** `dist_vwap_pct` < `0.4138` → IC=+0.201 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4138 (IC base=-0.063)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1248` → IC=+0.247 (n=1664)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1248 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1836` → IC=+0.247 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1836 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.273 (n=2496)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.8637` → IC=+0.293 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8637 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.241 (n=2184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=-0.022)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.210 (n=484)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1453)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.231 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1453)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.205 (n=1228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=709)

- **FILTRO** `sigma_ewma_delta_pct` > `23.695` → IC=-0.262 (n=275)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.695
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1662)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.177 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0027 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.302 (n=109)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.325 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.125 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 12.0 (IC base=+0.089)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.334 (n=239)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1012` → IC=+0.298 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1012 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.354` → IC=+0.287 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.354 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0923` → IC=+0.176 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0923 (IC base=-0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.194)

- **PATRÓN** `ibs_15` < `0.5472` → IC=+0.311 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5472 (IC base=-0.194)

- **PATRÓN** `dist_vwap_pct` < `0.0651` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0651 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.194)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=503)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.164 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0064 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.170 (n=349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0038 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.200 (n=261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.157)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.158 (n=390)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.157)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.218 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.181 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.157)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.258 (n=391)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.2696` → IC=+0.170 (n=362)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.2696 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=503)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `9557.6525` → IC=+0.170 (n=177)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 9557.6525 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.239 (n=927)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.234 (n=927)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `0.7694` → IC=+0.243 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7694 (IC base=+0.232)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2084` → IC=+0.256 (n=420)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2084 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.234 (n=629)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.232)

- **PATRÓN** `ibs_15` < `0.3657` → IC=+0.265 (n=927)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3657 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.7403` → IC=+0.311 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7403 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.287` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.287 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.476` → IC=+0.236 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.476 (IC base=+0.232)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.203 (n=581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=195)

- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.240 (n=263)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=513)

- **FILTRO** `drift_15min` |x|> `0.8847` → IC=-0.269 (n=193)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8847
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=583)

- **FILTRO** `sigma_ewma_delta_pct` > `18.27` → IC=-0.144 (n=408)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.27
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.159 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.175)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.229 (n=57)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` > `0.3016` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3016 (IC base=-0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.175)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0786` → IC=+0.227 (n=364)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0786 (IC base=-0.041)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1879` → IC=+0.230 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1879 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.269 (n=409)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.6635` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6635 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.171` → IC=+0.230 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.171 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0194` → IC=-0.263 (n=466)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=468)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.254 (n=283)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=651)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.201)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.147` → IC=+0.272 (n=287)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.147 (IC base=-0.032)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.17` → IC=+0.303 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.17 (IC base=-0.032)

- **PATRÓN** `ibs_15` < `0.3256` → IC=+0.293 (n=632)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3256 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.8265` → IC=+0.352 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8265 (IC base=-0.032)

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
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.302 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.330 (n=275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2411` → IC=+0.304 (n=274)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2411 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.315 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8407` → IC=+0.327 (n=823)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8407 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.339 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.344 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12848.0159` → IC=+0.305 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12848.0159 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.298 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0549` → IC=+0.336 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0549 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.309 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3979` → IC=+0.305 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3979 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.318 (n=449)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4131` → IC=+0.352 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4131 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.329 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.302 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.298 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.319 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.316 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.336 (n=375)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2788` → IC=+0.311 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2788 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.321 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0876` → IC=-0.253 (n=75)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0876
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=226)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.260 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=199)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2665` → IC=-0.156 (n=30)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2665
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
- **PATRÓN** `T_h` > `80.0063` → IC=+0.232 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.215)

- **PATRÓN** `ratio` < `0.9753` → IC=+0.472 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9753 (IC base=+0.215)

- **PATRÓN** `T_h` > `145.7688` → IC=+0.394 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7688 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.012` → IC=+0.323 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `127.068` → IC=+0.243 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.068 (IC base=+0.196)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.469 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.196)

- **PATRÓN** `T_h` > `104.0063` → IC=+0.295 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 104.0063 (IC base=+0.290)

- **PATRÓN** `ratio` > `1.0479` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0479 (IC base=+0.290)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.268 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.248)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.432 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.248)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.344 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.356 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6197 sube el IC de +0.203 a +0.283 en UPDOWN_GBM#15min (n=2223). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.219 a +0.279 en UPDOWN_GBM#BTC#15min (n=460). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5831 sube el IC de +0.146 a +0.236 en UPDOWN_GBM#ETH#15min (n=499). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.587 sube el IC de +0.188 a +0.277 en UPDOWN_GBM#SOL#15min (n=280). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5849 sube el IC de +0.211 a +0.296 en UPDOWN_GBM#XRP#15min (n=561). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6395 sube el IC de -0.063 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=803). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.022 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=2496). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.089 a +0.334 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=239). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5472 sube el IC de -0.194 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=35). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.157 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=391). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3657 sube el IC de +0.232 a +0.265 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=927). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.175 a +0.229 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=57). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.269 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=409). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.201 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3256 sube el IC de -0.032 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=632). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.292 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=823). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.288 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=449). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.294 a +0.336 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=375). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.359 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=509). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.363 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.351 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=231). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1525 | +0.097 | +194.68€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1525 | +0.097 | +194.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1159 | +0.105 | +167.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1159 | +0.105 | +167.77€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 263 | +0.066 | +11.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 263 | +0.066 | +11.20€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 138 | +0.021 | +28.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 138 | +0.021 | +28.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 114 | +0.026 | +24.83€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 114 | +0.026 | +24.83€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 33145 | -0.088 | -4380.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1698 | -0.017 | -217.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 31447 | -0.092 | -4162.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4282 | -0.119 | -737.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4282 | -0.119 | -737.72€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1698 | -0.017 | -217.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1698 | -0.017 | -217.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3894 | -0.112 | -872.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3894 | -0.112 | -872.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8535 | -0.003 | -769.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8535 | -0.003 | -769.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8308 | -0.107 | -567.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8308 | -0.107 | -567.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6428 | -0.162 | -1215.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6428 | -0.162 | -1215.12€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 24858 | -0.020 | +3708.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6434 | +0.001 | +1778.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 18424 | -0.028 | +1930.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 24858 | -0.020 | +3708.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6434 | +0.001 | +1778.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 18424 | -0.028 | +1930.73€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 113303 | +0.113 | -5135.28€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16010 | +0.183 | -482.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 478 | -0.052 | -59.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 89741 | +0.103 | -4320.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7074 | +0.104 | -272.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14904 | +0.102 | -1087.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 52 | -0.130 | +12.55€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14837 | +0.103 | -1087.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22516 | +0.130 | -351.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4826 | +0.198 | -119.89€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14882 | +0.116 | -144.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2766 | +0.091 | -64.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14951 | +0.093 | -1239.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 60 | -0.113 | -5.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14876 | +0.094 | -1222.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 24067 | +0.124 | -421.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6440 | +0.176 | -102.67€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 15046 | +0.107 | -250.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2569 | +0.099 | -59.58€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21943 | +0.115 | -1199.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4578 | +0.188 | -277.16€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 381 | -0.014 | -5.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 15245 | +0.094 | -768.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1739 | +0.130 | -147.88€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14922 | +0.101 | -836.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 54 | -0.036 | +10.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14855 | +0.102 | -846.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 18098 | +0.194 | -1134.61€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 18098 | +0.194 | -1134.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4211 | +0.174 | -395.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4211 | +0.174 | -395.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1906 | +0.202 | -25.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1906 | +0.202 | -25.75€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4152 | +0.181 | -339.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4152 | +0.181 | -339.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3657 | +0.242 | -123.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3657 | +0.242 | -123.04€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4093 | +0.189 | -264.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4093 | +0.189 | -264.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 845 | +0.430 | -22.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 845 | +0.430 | -22.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 335 | +0.438 | -3.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 335 | +0.438 | -3.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 319 | +0.435 | -5.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 319 | +0.435 | -5.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 179 | +0.406 | -11.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 179 | +0.406 | -11.83€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 62716 | +0.199 | -4687.97€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 62716 | +0.199 | -4687.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10793 | +0.182 | -1157.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10793 | +0.182 | -1157.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10076 | +0.224 | -350.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10076 | +0.224 | -350.32€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10797 | +0.176 | -1220.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10797 | +0.176 | -1220.99€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 10140 | +0.220 | -379.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 10140 | +0.220 | -379.23€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10389 | +0.203 | -679.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10389 | +0.203 | -679.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10521 | +0.193 | -900.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10521 | +0.193 | -900.72€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 23847 | +0.116 | +146.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 23847 | +0.116 | +146.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11841 | +0.120 | +135.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11841 | +0.120 | +135.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 12006 | +0.112 | +11.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 12006 | +0.112 | +11.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1715 | +0.288 | -26.21€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1715 | +0.288 | -26.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 772 | +0.279 | -18.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 772 | +0.279 | -18.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 828 | +0.287 | -11.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 828 | +0.287 | -11.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 769 | +0.438 | -1.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 769 | +0.438 | -1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 369 | +0.435 | -3.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 369 | +0.435 | -3.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 354 | +0.441 | +1.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 354 | +0.441 | +1.22€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1311 | +0.071 | -57.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 471 | +0.058 | -37.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 840 | +0.078 | -20.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1028 | +0.077 | -28.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 188 | +0.068 | -8.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 840 | +0.078 | -20.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 217 | +0.034 | -31.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 217 | +0.034 | -31.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 45535 | +0.100 | -1188.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3699 | +0.091 | +43.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 41836 | +0.100 | -1232.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 25283 | +0.104 | -299.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3699 | +0.091 | +43.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21584 | +0.106 | -343.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8966 | +0.110 | -18.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8966 | +0.110 | -18.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11286 | +0.082 | -870.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11286 | +0.082 | -870.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 865 | +0.206 | -102.69€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 865 | +0.206 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 865 | +0.206 | -102.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 865 | +0.206 | -102.69€ | 1 | 4 |
| ✅ GBM_LATE_15M | 31976 | +0.088 | +15842.59€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 31976 | +0.088 | +15842.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5379 | +0.202 | +4131.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5379 | +0.202 | +4131.49€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4737 | +0.177 | +3388.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4737 | +0.177 | +3388.82€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 5680 | +0.199 | +4259.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5680 | +0.199 | +4259.72€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4534 | +0.032 | +1154.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4534 | +0.032 | +1154.97€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4559 | -0.031 | +1001.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4559 | -0.031 | +1001.26€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7087 | -0.036 | +1906.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7087 | -0.036 | +1906.33€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 34454 | +0.087 | +18365.87€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 34454 | +0.087 | +18365.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6638 | +0.012 | +3446.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6638 | +0.012 | +3446.36€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7148 | +0.014 | +1513.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7148 | +0.014 | +1513.92€ | 0 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4876 | +0.267 | +5001.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4876 | +0.267 | +5001.66€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5786 | +0.010 | +1294.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5786 | +0.010 | +1294.46€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5596 | +0.035 | +2255.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5596 | +0.035 | +2255.22€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4410 | +0.284 | +4854.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4410 | +0.284 | +4854.24€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 25636 | +0.173 | +19864.75€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 25636 | +0.173 | +19864.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3872 | +0.217 | +3240.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3872 | +0.217 | +3240.24€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4028 | +0.149 | +2917.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4028 | +0.149 | +2917.37€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4073 | +0.213 | +3317.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4073 | +0.213 | +3317.24€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4298 | +0.137 | +3169.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4298 | +0.137 | +3169.53€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4807 | +0.123 | +3513.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4807 | +0.123 | +3513.97€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4558 | +0.210 | +3706.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4558 | +0.210 | +3706.41€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6968 | +0.137 | +3284.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6968 | +0.137 | +3284.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 339 | +0.142 | +189.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2025 | +0.143 | +1087.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2025 | +0.143 | +1087.90€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 375 | +0.142 | +175.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2098 | +0.153 | +1024.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2098 | +0.153 | +1024.17€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1596 | +0.107 | +571.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1596 | +0.107 | +571.26€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 535 | +0.135 | +236.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 535 | +0.135 | +236.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 32198 | +0.179 | +24769.88€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 32198 | +0.179 | +24769.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5120 | +0.230 | +4536.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5120 | +0.230 | +4536.81€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4983 | +0.148 | +3233.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4983 | +0.148 | +3233.25€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5380 | +0.227 | +4661.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5380 | +0.227 | +4661.69€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5227 | +0.135 | +3653.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5227 | +0.135 | +3653.65€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5674 | +0.123 | +3929.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5674 | +0.123 | +3929.39€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5814 | +0.213 | +4755.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5814 | +0.213 | +4755.09€ | 0 | 23 |
| ✅ GBM_LATE_5M | 8708 | +0.174 | +5817.04€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 8708 | +0.174 | +5817.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 835 | +0.229 | +729.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2097 | +0.169 | +1525.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2097 | +0.169 | +1525.17€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2828 | +0.179 | +1866.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2828 | +0.179 | +1866.92€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 914 | +0.148 | +523.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 914 | +0.148 | +523.33€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1112 | +0.148 | +582.60€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2326 | +0.074 | +868.18€ | 0 | 11 |
| ✅ GBM_LATE_60M#60min | 2326 | +0.074 | +868.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 874 | +0.091 | +330.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 874 | +0.091 | +330.02€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 734 | +0.073 | +331.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 734 | +0.073 | +331.89€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 718 | +0.053 | +206.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 718 | +0.053 | +206.27€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 454 | -0.239 | -10.92€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 454 | -0.239 | -10.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 167 | -0.216 | -5.32€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 167 | -0.216 | -5.32€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 158 | -0.231 | -0.89€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 158 | -0.231 | -0.89€ | 3 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 129 | -0.271 | -4.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 129 | -0.271 | -4.71€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 988 | +0.087 | +252.37€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 988 | +0.087 | +252.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 367 | +0.077 | +75.91€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 367 | +0.077 | +75.91€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 329 | +0.053 | +38.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 329 | +0.053 | +38.30€ | 3 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 292 | +0.136 | +138.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 292 | +0.136 | +138.16€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2671 | +0.102 | +699.06€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2671 | +0.102 | +699.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2671 | +0.102 | +699.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2671 | +0.102 | +699.06€ | 0 | 2 |
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
| ✅ LIQUIDACIONES_5M | 2727 | +0.022 | +74.04€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2727 | +0.022 | +74.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 136 | +0.029 | -1.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 136 | +0.029 | -1.24€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 398 | +0.035 | +34.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 398 | +0.035 | +34.72€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1044 | +0.031 | +30.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1044 | +0.031 | +30.01€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 624 | +0.016 | +2.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 624 | +0.016 | +2.95€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 324 | +0.018 | +13.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 324 | +0.018 | +13.72€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1344 | -0.044 | -27.72€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1344 | -0.044 | -27.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 383 | -0.040 | -12.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 383 | -0.040 | -12.80€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 446 | -0.025 | +0.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 446 | -0.025 | +0.16€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 515 | -0.063 | -15.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 515 | -0.063 | -15.08€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4215 | -0.019 | +79.13€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1993 | -0.022 | +15.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2222 | -0.015 | +63.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 118 | -0.008 | +2.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 61 | +0.040 | +8.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 57 | -0.059 | -5.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1032 | -0.002 | +44.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 488 | -0.008 | +11.03€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 544 | +0.004 | +33.48€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 477 | -0.018 | +13.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 234 | -0.025 | +2.27€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 243 | -0.010 | +11.06€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 860 | -0.031 | -15.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 393 | -0.044 | -20.19€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 467 | -0.020 | +4.95€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 830 | -0.023 | +13.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 402 | -0.030 | +4.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 428 | -0.016 | +9.81€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 898 | -0.023 | +20.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 415 | -0.018 | +10.52€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 483 | -0.028 | +10.10€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 36911 | -0.004 | +1758.22€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 36911 | -0.004 | +1758.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6569 | +0.024 | +872.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6569 | +0.024 | +872.49€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5539 | -0.031 | -76.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5539 | -0.031 | -76.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6662 | +0.018 | +652.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6662 | +0.018 | +652.51€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5326 | -0.053 | -164.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5326 | -0.053 | -164.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6218 | -0.009 | +205.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6218 | -0.009 | +205.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6597 | +0.012 | +269.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6597 | +0.012 | +269.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6128 | -0.059 | -146.42€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6128 | -0.059 | -146.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1499 | -0.079 | -34.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1499 | -0.079 | -34.95€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 704 | -0.126 | -34.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 704 | -0.126 | -34.31€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1808 | -0.076 | -31.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1808 | -0.076 | -31.92€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 92766 | -0.073 | +1729.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 92766 | -0.073 | +1729.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15919 | -0.074 | +928.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15919 | -0.074 | +928.46€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 14114 | -0.098 | -751.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 14114 | -0.098 | -751.55€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 16168 | -0.066 | +890.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 16168 | -0.066 | +890.79€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13645 | -0.094 | -389.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13645 | -0.094 | -389.10€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16831 | -0.051 | +349.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16831 | -0.051 | +349.01€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 16089 | -0.063 | +701.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 16089 | -0.063 | +701.51€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8003 | -0.031 | -148.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8003 | -0.031 | -148.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1895 | -0.043 | -20.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1895 | -0.043 | -20.36€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1096 | -0.048 | -22.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1096 | -0.048 | -22.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 771 | -0.023 | -25.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 771 | -0.023 | -25.39€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1340 | +0.116 | +498.49€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1204 | +0.123 | +485.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 283 | +0.139 | +143.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 283 | +0.139 | +143.26€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 226 | +0.110 | +65.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 226 | +0.110 | +65.51€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 245 | +0.115 | +98.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 245 | +0.115 | +98.12€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 217 | +0.144 | +111.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 217 | +0.144 | +111.48€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 233 | +0.100 | +67.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 233 | +0.100 | +67.52€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 868 | -0.015 | -16.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 868 | -0.015 | -16.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 170 | +0.006 | +8.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 170 | +0.006 | +8.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 125 | -0.012 | -0.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 125 | -0.012 | -0.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 235 | -0.036 | -17.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 235 | -0.036 | -17.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 191 | +0.013 | +4.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 191 | +0.013 | +4.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 147 | -0.044 | -11.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 147 | -0.044 | -11.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 725 | -0.093 | -67.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 330 | -0.148 | -79.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 259 | -0.190 | -74.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 257 | -0.048 | -1.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 186 | -0.053 | -4.01€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 71 | -0.034 | +2.83€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 138 | -0.043 | +13.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 110 | -0.062 | +7.10€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 555 | -0.119 | -71.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 170 | -0.006 | +3.87€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 874 | -0.201 | -49.54€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 363 | -0.193 | -31.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 313 | -0.195 | -31.77€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 295 | -0.217 | -31.22€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 254 | -0.227 | -37.06€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 216 | -0.188 | +13.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 198 | -0.185 | +9.63€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 765 | -0.204 | -59.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 356 | +0.402 | +290.97€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 91 | +0.371 | +75.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 91 | +0.371 | +75.92€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 225 | +0.460 | +216.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 225 | +0.460 | +216.29€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 356 | +0.402 | +290.97€ | 0 | 0 |
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
| ✅ STREAK_FADE_5M | 3063 | -0.022 | -124.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3063 | -0.022 | -124.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 904 | -0.022 | -32.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 904 | -0.022 | -32.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 579 | -0.027 | -25.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 579 | -0.027 | -25.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1424 | -0.018 | -51.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1424 | -0.018 | -51.31€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9566 | +0.019 | +104.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9566 | +0.019 | +104.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2625 | +0.021 | +26.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2625 | +0.021 | +26.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2222 | +0.027 | +48.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2222 | +0.027 | +48.20€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2861 | +0.010 | -0.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2861 | +0.010 | -0.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1858 | +0.021 | +30.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1858 | +0.021 | +30.09€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8589 | +0.013 | -44.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8589 | +0.013 | -44.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3386 | +0.016 | -9.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3386 | +0.016 | -9.68€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3416 | +0.012 | -21.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3416 | +0.012 | -21.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1787 | +0.007 | -13.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1787 | +0.007 | -13.77€ | 1 | 0 |
| ✅ UPDOWN_GBM | 54010 | +0.043 | +4036.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13553 | +0.077 | +2837.04€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1796 | +0.006 | +9.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 35319 | +0.035 | +1154.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3147 | +0.005 | +39.41€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5500 | +0.080 | +739.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1060 | +0.157 | +472.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4407 | +0.062 | +267.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 10408 | +0.049 | +825.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1737 | +0.089 | +402.44€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 482 | +0.012 | +5.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6688 | +0.051 | +379.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1428 | +0.006 | +37.66€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 73 | -0.087 | +0.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6393 | +0.052 | +507.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1034 | +0.138 | +375.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5331 | +0.036 | +133.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11874 | +0.032 | +636.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3319 | +0.054 | +445.64€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 475 | +0.007 | +8.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6949 | +0.030 | +180.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1067 | +0.003 | -1.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 64 | -0.121 | +2.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 12035 | +0.021 | +425.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3219 | +0.031 | +276.84€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 465 | -0.001 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7643 | +0.022 | +151.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 652 | +0.006 | +3.39€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 56 | -0.155 | -4.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7798 | +0.049 | +903.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3184 | +0.096 | +864.10€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 313 | +0.005 | -1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4301 | +0.018 | +40.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 193 | -0.120 | -2.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 678 | +0.359 | +238.80€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 678 | +0.359 | +238.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 371 | +0.363 | +128.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 371 | +0.363 | +128.79€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 307 | +0.351 | +110.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 307 | +0.351 | +110.01€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 15183 | -0.031 | +3455.39€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 15183 | -0.031 | +3455.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1154 | -0.060 | +383.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1154 | -0.060 | +383.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2694 | -0.114 | +106.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2694 | -0.114 | +106.46€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 636 | +0.199 | +474.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 636 | +0.199 | +474.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1755 | +0.210 | +1109.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1755 | +0.210 | +1109.32€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4468 | -0.064 | +606.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4468 | -0.064 | +606.83€ | 4 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4476 | -0.068 | +775.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4476 | -0.068 | +775.07€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 173 | +0.026 | +6.12€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 173 | +0.026 | +6.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 173 | +0.026 | +6.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 173 | +0.026 | +6.12€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1097 | +0.292 | +904.48€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1097 | +0.292 | +904.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 598 | +0.288 | +461.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 598 | +0.288 | +461.29€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 499 | +0.294 | +443.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 499 | +0.294 | +443.19€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 757 | -0.114 | -85.13€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 757 | -0.114 | -85.13€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 224 | -0.088 | -18.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 224 | -0.088 | -18.30€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 73 | -0.167 | -9.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 73 | -0.167 | -9.78€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 81 | -0.187 | -7.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 81 | -0.187 | -7.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2863 | +0.307 | +1417.52€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1010 | +0.261 | +151.82€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1094 | +0.300 | +483.95€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 759 | +0.378 | +781.76€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.050) — sin ventaja clara. oversold(IBS<0.3): IC=+0.052 n=18826 | neutral: IC=+0.044 n=20000 | overbought(IBS>0.7): IC=+0.094 n=19290
  - _Datos_: n=60287 IC=+0.064 PNL=+8124.54€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 615 celda(s) pasan gate riguroso completo de 2425 evaluadas (n>=40) y 3406 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.031 < 0.08 — monitorear
  - _Datos_: n=3219 IC=+0.031 PNL=+276.84€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1094/15 IC=+0.300 PNL=+483.95€ | BTC: n=1010/15 IC=+0.261 PNL=+151.82€ | SOL: n=759/15 IC=+0.378 PNL=+781.76€

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
  - _Estado_: 53948 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.127 n=515/60 | contraria IC=+0.185 n=519 | gap=-0.059 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=368, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 217 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1067/40 IC=+0.003 PNL=-1.64€ | BTC#60min: n=1428/40 IC=+0.006 PNL=+37.66€ | SOL#60min: n=652/40 IC=+0.006 PNL=+3.39€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=422658 | tras_1loss IC=+0.087 n=325085 | tras_2loss IC=+0.056 n=134194/40 | gap=-0.007 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.024 n=6754 | contrario_BTC IC=+0.039 n=6000/40 | gap=+0.014 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.08 con n=447 PNL=+359.15€
  - _Datos_: n=447 IC=+0.213 PNL=+359.15€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.218 > 0.08 con n=523 PNL=+397.83€
  - _Datos_: n=523 IC=+0.218 PNL=+397.83€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=2336 PNL=+1284.39€
  - _Datos_: n=2336 IC=+0.333 PNL=+1284.39€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=437 IC=+0.076 PNL=+51.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=437 IC=+0.076 PNL=+51.65€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=64 IC=+0.182 PNL=+41.73€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=64 IC=+0.182 PNL=+41.73€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=51043 IC=+0.042 PNL=+3815.62€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=51043 IC=+0.042 PNL=+3815.62€

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
  - _Estado_: n=2146 IC=+0.009 PNL=+5.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2146 IC=+0.009 PNL=+5.41€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1001 IC=-0.004 PNL=+34.00€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1001 IC=-0.004 PNL=+34.00€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=688 IC=+0.020 PNL=+31.27€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=688 IC=+0.020 PNL=+31.27€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=2964 PNL=+2112.19€
  - _Datos_: n=2964 IC=+0.203 PNL=+2112.19€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2218 IC=+0.067 PNL=+177.98€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2218 IC=+0.067 PNL=+177.98€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1737 IC=+0.089 PNL=+402.44€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1737 IC=+0.089 PNL=+402.44€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=7761 PNL=+2140.12€
  - _Datos_: n=7761 IC=+0.096 PNL=+2140.12€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=202 IC=-0.265 PNL=-13.35€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=202 IC=-0.265 PNL=-13.35€

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
  - _Estado_: n=709 IC=+0.023 PNL=+57.54€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=709 IC=+0.023 PNL=+57.54€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=76 IC=+0.064 PNL=+5.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=76 IC=+0.064 PNL=+5.31€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6984 IC=+0.008 PNL=+66.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6984 IC=+0.008 PNL=+66.45€

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
  - _Estado_: n=9376 IC=+0.042 PNL=+650.22€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=9376 IC=+0.042 PNL=+650.22€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=3210 IC=+0.063 PNL=+448.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3210 IC=+0.063 PNL=+448.09€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=420 PNL=+129.23€
  - _Datos_: n=420 IC=+0.111 PNL=+129.23€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.153 > 0.08 con n=804 PNL=+216.86€
  - _Datos_: n=804 IC=+0.153 PNL=+216.86€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=621 PNL=+333.26€
  - _Datos_: n=621 IC=+0.107 PNL=+333.26€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64332 IC=+0.118 PNL=+23925.31€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64332 IC=+0.118 PNL=+23925.31€

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
  - _Estado_: n=8223 IC=+0.048 PNL=+718.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8223 IC=+0.048 PNL=+718.67€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.02 con n=768 PNL=+303.46€
  - _Datos_: n=768 IC=+0.122 PNL=+303.46€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=180 IC=-0.066 PNL=+28.48€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=180 IC=-0.066 PNL=+28.48€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.452 > 0.1 con n=1339 PNL=+1313.78€
  - _Datos_: n=1339 IC=+0.452 PNL=+1313.78€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=20100 IC=+0.069 PNL=+2812.45€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=20100 IC=+0.069 PNL=+2812.45€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.1 con n=4809 PNL=+2810.44€
  - _Datos_: n=4809 IC=+0.206 PNL=+2810.44€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.151 < -0.1 con n=316 PNL=+29.97€
  - _Datos_: n=316 IC=-0.151 PNL=+29.97€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2436 IC=+0.061 PNL=+269.88€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2436 IC=+0.061 PNL=+269.88€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=104 IC=-0.132 PNL=+0.42€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=104 IC=-0.132 PNL=+0.42€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.1 con n=574 PNL=+152.22€
  - _Datos_: n=574 IC=+0.121 PNL=+152.22€

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
  - _Estado_: n=23180 IC=-0.136 PNL=+1721.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=23180 IC=-0.136 PNL=+1721.13€

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
  - _Estado_: n=2373 IC=+0.136 PNL=+1359.95€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2373 IC=+0.136 PNL=+1359.95€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.08 con n=2925 PNL=+2099.55€
  - _Datos_: n=2925 IC=+0.204 PNL=+2099.55€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=5598 IC=+0.036 PNL=+319.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5598 IC=+0.036 PNL=+319.42€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=2601 PNL=+1406.25€
  - _Datos_: n=2601 IC=+0.090 PNL=+1406.25€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.218 > 0.08 con n=612 PNL=+333.97€
  - _Datos_: n=612 IC=+0.218 PNL=+333.97€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.226 < -0.1 con n=2328 PNL=-174.65€
  - _Datos_: n=2328 IC=-0.226 PNL=-174.65€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6685 IC=+0.182 PNL=+4658.77€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6685 IC=+0.182 PNL=+4658.77€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=94 PNL=+38.77€
  - _Datos_: n=94 IC=+0.115 PNL=+38.77€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2425 IC=+0.072 PNL=+775.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2425 IC=+0.072 PNL=+775.08€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=2218 PNL=+1570.28€
  - _Datos_: n=2218 IC=+0.179 PNL=+1570.28€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3719 IC=-0.030 PNL=+992.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3719 IC=-0.030 PNL=+992.57€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=605 PNL=-47.78€
  - _Datos_: n=605 IC=+0.086 PNL=-47.78€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=3891 PNL=-332.08€
  - _Datos_: n=3891 IC=+0.239 PNL=-332.08€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=49 IC=-0.010 PNL=+3.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=49 IC=-0.010 PNL=+3.83€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=1355) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1355 IC=+0.099 PNL=+303.53€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.311 > 0.08 con n=347 PNL=+109.96€
  - _Datos_: n=347 IC=+0.311 PNL=+109.96€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.408 n=490) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=490 IC=+0.408 PNL=+690.08€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=10793 IC=+0.182 PNL=-1157.57€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10793 IC=+0.182 PNL=-1157.57€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=172 PNL=+105.24€
  - _Datos_: n=172 IC=+0.207 PNL=+105.24€
