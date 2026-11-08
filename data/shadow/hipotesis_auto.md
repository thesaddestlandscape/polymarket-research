# Hipótesis automáticas — 2026-11-08 22:34 UTC
_Generado por shadow_postmortem.py sobre 1251202 resoluciones (PNL=+170258.70€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=697)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.198 (n=1013)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.505 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.186 (n=323)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 62.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.6125` → IC=+0.240 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6125 (IC base=+0.128)

- **PATRÓN** `banda_z` > `8.618` → IC=+0.201 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.618 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=1039)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.128)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=497)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=878)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.187 (n=276)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 66.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.8128` → IC=+0.274 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8128 (IC base=+0.131)

- **PATRÓN** `banda_z` > `8.901` → IC=+0.208 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.901 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.131 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=939)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.131)

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
- **FILTRO** `restante_s_al_confirmar` < `132.64` → IC=-0.223 (n=11637)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.64
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=34911)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.12` → IC=-0.259 (n=1193)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.12
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3582)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.46` → IC=-0.289 (n=1208)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.46
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3625)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `117.36` → IC=-0.166 (n=3168)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.36
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=9506)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.16` → IC=-0.249 (n=3164)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.16
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9495)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `129.15` → IC=-0.263 (n=2192)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 129.15
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6581)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=27122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8361.9198` → IC=+0.160 (n=2295)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8361.9198 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=23240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=28097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=21304)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=8179)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6596.2331` → IC=+0.147 (n=3160)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 6596.2331 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=2087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2679)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `9392.7207` → IC=+0.181 (n=1864)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9392.7207 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2727)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16078.4757` → IC=+0.184 (n=704)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16078.4757 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=2156)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=591)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=1385)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=4904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=4365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.212 (n=2340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2718)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.143 (n=625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=1125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.254 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=1470)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `951.9496` → IC=-0.127 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 951.9496
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=318)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=457)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.046)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.243 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=23285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=19658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.226 (n=9743)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=5310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.173 (n=5288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 18.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=5333)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.173 (n=4470)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=3108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=2062)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.252 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.210)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=5357)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=4070)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.365 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.249)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=4331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=3804)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.429 (n=838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4484.2424` → IC=+0.444 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4484.2424 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.450 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.457 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12295.9377` → IC=+0.446 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12295.9377 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.426 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4712.9023` → IC=+0.436 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4712.9023 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.401 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.398)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.208 (n=26226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=30866)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=4555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=9713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=13945)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=6336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4350)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.191 (n=4502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=10808)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.227 (n=4277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=4858)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=4286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=4342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=5030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=10953)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=11389)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.49` → IC=+0.137 (n=13333)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.49 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5330)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=5133)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.61` → IC=+0.142 (n=5022)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.61 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=5623)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=6956)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.17` → IC=+0.137 (n=6698)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.17 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.306 (n=1355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.283 (n=911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.365 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.365 (n=94)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.343)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.390 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.343)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.374 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.343)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.431 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.466 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.449 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.448)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.449 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.406)

- **PATRÓN** `libro_liquidez` > `779.6536` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 779.6536 (IC base=+0.406)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4738` → IC=+0.139 (n=17162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4738 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=17372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=11926)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9779` → IC=+0.246 (n=5721)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9779 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7954` → IC=+0.284 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7954 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.501` → IC=+0.184 (n=8582)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.501 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.265 (n=5104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6248 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.304` → IC=+0.250 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.304 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7521` → IC=+0.235 (n=4105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7521 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=8531)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4643.3916` → IC=+0.146 (n=5721)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4643.3916 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=10714)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.5659` → IC=+0.143 (n=21420)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5659 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.6096` → IC=+0.192 (n=1451)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6096 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.1608` → IC=+0.190 (n=8456)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1608 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.196 (n=3831)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6966 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.229 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.6807` → IC=+0.210 (n=4930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6807 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.227 (n=14709)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.081)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3626` → IC=+0.213 (n=3662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3626 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=1783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=2451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9868` → IC=+0.278 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9868 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.497` → IC=+0.278 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.497 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.267 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.213 (n=3509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=4031)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2046.307` → IC=+0.211 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2046.307 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.225 (n=2255)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.243 (n=3212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.244 (n=1458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0891` → IC=+0.279 (n=1071)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0891 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=1201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.5616` → IC=+0.259 (n=3211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5616 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0948` → IC=+0.246 (n=2908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0948 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.249 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.248 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.8556` → IC=+0.243 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8556 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=3691)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1780.3944` → IC=+0.247 (n=2140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1780.3944 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.230 (n=2696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.263 (n=1021)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=2169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9078` → IC=+0.261 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9078 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.233 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.3319` → IC=+0.224 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3319 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.263 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2256` → IC=+0.224 (n=3061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2256 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6994` → IC=+0.230 (n=2735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6994 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.269 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.252 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.152 (n=3262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0063 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.153 (n=1090)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.3498` → IC=+0.198 (n=2175)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.3498 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.936` → IC=+0.137 (n=2977)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.936 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6343` → IC=+0.148 (n=1089)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6343 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.155 (n=1329)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.4413` → IC=+0.139 (n=3136)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4413 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4233)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.171 (n=1367)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 204.0 (IC base=+0.129)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.213 (n=1762)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=4081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.994` → IC=+0.280 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.994 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.198 (n=3477)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.222 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.7305` → IC=+0.215 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7305 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=4694)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1917.74` → IC=+0.203 (n=1760)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.74 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.226 (n=3146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.2924` → IC=+0.232 (n=2382)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2924 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.221 (n=1616)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0439` → IC=+0.270 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0439 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.874` → IC=+0.267 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.874 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.251 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.768` → IC=+0.219 (n=1510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.768 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1618` → IC=+0.228 (n=2288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1618 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1905.7248` → IC=+0.226 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1905.7248 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.223 (n=3398)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=202)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=4668)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.231 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.340 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.7743` → IC=+0.334 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7743 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.202 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `0.7027` → IC=+0.340 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7027 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.335 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.334 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.345 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.2799` → IC=+0.335 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2799 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.338 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0896` → IC=+0.187 (n=1218)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0896 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.3334` → IC=+0.159 (n=596)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3334 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.1384` → IC=+0.151 (n=2173)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1384 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8324` → IC=+0.159 (n=1539)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8324 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.214 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.776` → IC=+0.153 (n=1481)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.776 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.1484` → IC=+0.159 (n=1007)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1484 (IC base=+0.050)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.188 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=738)

- **FILTRO** `ibs_20min` < `0.2615` → IC=-0.174 (n=219)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2615
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=658)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.133 (n=4592)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2267)

- **FILTRO** `sigma_ewma_delta_pct` > `8.29` → IC=-0.225 (n=736)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.29
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6123)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=300)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.75 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.9554` → IC=+0.278 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9554 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.4558` → IC=+0.271 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4558 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.993` → IC=+0.160 (n=207)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.993 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.285 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.285 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.4693` → IC=+0.283 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4693 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5401` → IC=+0.270 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5401 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.275 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.154 (n=2267)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.218` → IC=+0.286 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.218 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.302 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.301 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.301 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7817` → IC=-0.153 (n=3479)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7817
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=1793)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.170 (n=1158)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4114)

- **FILTRO** `ibs_20min` > `0.7419` → IC=-0.193 (n=1832)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7419
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=5500)

- **PATRÓN** `ibs_20min` > `0.7817` → IC=+0.124 (n=1793)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7817 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0084` → IC=+0.361 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0084 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.249` → IC=+0.303 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.249 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.318 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.108` → IC=+0.305 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.108 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.302 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5902` → IC=+0.308 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5902 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.531` → IC=+0.325 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.531 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.8075` → IC=+0.275 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8075 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` < `0.2222` → IC=+0.262 (n=2115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2222 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.6413` → IC=+0.271 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6413 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `1.064` → IC=+0.284 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.064 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.107` → IC=+0.280 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.107 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.266 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.269 (n=2006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.198 (n=7427)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0106 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.8696` → IC=+0.287 (n=10078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8696 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.9381` → IC=+0.301 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9381 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.48` → IC=+0.167 (n=9949)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.48 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.276 (n=7290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.292 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.6569` → IC=+0.286 (n=4298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6569 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.308 (n=12509)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=7159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.641` → IC=+0.154 (n=21425)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.641 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.2545` → IC=+0.278 (n=7224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2545 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6997` → IC=+0.279 (n=3103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6997 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` > `1.193` → IC=+0.279 (n=2350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.193 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.325 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.4544` → IC=+0.304 (n=3461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4544 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `2.284` → IC=+0.301 (n=4706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.284 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.309 (n=10356)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.081)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8011` → IC=-0.127 (n=3957)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8011
  - _Potencial_: sin este filtro IC_bueno=+0.297 (n=2040)

- **FILTRO** `ibs_20min` > `0.7195` → IC=-0.234 (n=1315)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7195
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=3946)

- **FILTRO** `sigma_ewma_delta_pct` > `4.118` → IC=-0.231 (n=1133)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.118
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=4128)

- **PATRÓN** `ibs_20min` > `0.934` → IC=+0.336 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.934 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.983` → IC=+0.189 (n=2002)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.983 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.327 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4469` → IC=+0.279 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4469 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.2395` → IC=+0.302 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2395 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.316 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.017)

- **PATRÓN** `ibs_20min` < `0.1727` → IC=+0.165 (n=1316)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1727 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.401 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4194` → IC=+0.425 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4194 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.398 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.2967` → IC=+0.224 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2967 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.208 (n=2173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.214 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.244 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.231 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.245 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.618` → IC=+0.251 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.618 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.308 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5263` → IC=+0.254 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5263 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.261 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.268 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 212.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.319 (n=2090)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.292 (n=3136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.589` → IC=+0.305 (n=2092)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.589 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.296 (n=2749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.6063` → IC=+0.290 (n=3042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6063 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=3756)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2026.8956` → IC=+0.296 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2026.8956 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.309 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.324 (n=2530)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.306)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.325 (n=1246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.328 (n=1090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.307 (n=1276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.1429` → IC=+0.317 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1429 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.171` → IC=+0.312 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.171 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` < `0.2004` → IC=+0.306 (n=2780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2004 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.3455` → IC=+0.311 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3455 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` < `1.5954` → IC=+0.306 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5954 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.320 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.306)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `1909.8776` → IC=+0.315 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.8776 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.312 (n=2371)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.306)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7262` → IC=-0.182 (n=1396)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7262
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=4191)

- **PATRÓN** `ibs_20min` > `0.8478` → IC=+0.160 (n=1370)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8478 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.1419` → IC=+0.234 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1419 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.3574` → IC=+0.234 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3574 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1628` → IC=+0.234 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1628 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.6735` → IC=+0.231 (n=1762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6735 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.235 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.0761` → IC=+0.237 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0761 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4628` → IC=+0.239 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4628 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.254 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.3486` → IC=+0.251 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3486 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.255 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1942 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.309 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.295 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5219 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.276 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.281 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.246 (n=2301)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2303)

- **FILTRO** `ibs_20min` > `0.6216` → IC=-0.229 (n=1092)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6216
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=3283)

- **FILTRO** `sigma_ewma_delta_pct` > `8.266` → IC=-0.253 (n=500)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.266
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=3875)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.312 (n=2303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.043` → IC=+0.356 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.043 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.441` → IC=+0.153 (n=1864)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.441 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8458` → IC=+0.341 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8458 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.335 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6986 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1567` → IC=+0.335 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1567 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.362 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4306` → IC=+0.362 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4306 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.352 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6216` → IC=+0.149 (n=3283)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.6216 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.7676` → IC=+0.258 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7676 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.3034` → IC=+0.260 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3034 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.014` → IC=+0.129 (n=3084)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.014 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `0.6945` → IC=+0.282 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6945 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.281 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.807` → IC=+0.277 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.807 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.280 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.055)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.359 (n=2091)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.345 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.2113` → IC=+0.339 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2113 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.798` → IC=+0.334 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.798 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `0.8713` → IC=+0.335 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8713 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.348 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.327 (n=2252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2977.9607` → IC=+0.327 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2977.9607 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.345 (n=2059)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.349 (n=1665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.317)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.324 (n=1273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.317)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.317)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.336 (n=2498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.317)

- **PATRÓN** `dist_vwap_pct` < `0.2416` → IC=+0.322 (n=2427)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2416 (IC base=+0.317)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.329 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.321 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.317)

- **PATRÓN** `volumen_regimen` > `1.2131` → IC=+0.345 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2131 (IC base=+0.317)

- **PATRÓN** `volumen_pendiente_norm` > `0.2307` → IC=+0.363 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2307 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.326 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.317)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.318 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.317)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.224 (n=5542)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.1215` → IC=+0.191 (n=7300)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1215 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=17222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.5393` → IC=+0.231 (n=16590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5393 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.161` → IC=+0.205 (n=6382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.161 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.803` → IC=+0.257 (n=3229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.803 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.183` → IC=+0.154 (n=11041)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.183 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.153 (n=11043)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6258 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.204 (n=2411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.6104` → IC=+0.189 (n=5378)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6104 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.193 (n=15536)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 88.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.191 (n=7172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0058 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.08` → IC=+0.220 (n=5427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.08 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.524` → IC=+0.239 (n=16275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.524 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1805` → IC=+0.176 (n=11785)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1805 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.556` → IC=+0.192 (n=2596)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.556 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.516` → IC=+0.189 (n=14476)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.516 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.163 (n=11595)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1823 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.217 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.5602` → IC=+0.182 (n=6807)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5602 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6367` → IC=+0.192 (n=5157)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6367 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.203 (n=13462)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.228 (n=912)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.258 (n=1202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=2845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.230 (n=1854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9423` → IC=+0.298 (n=1821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9423 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.521` → IC=+0.331 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.521 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.295 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8322` → IC=+0.224 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8322 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.228 (n=2605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=3030)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.257 (n=2211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.256 (n=1003)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.097` → IC=+0.311 (n=972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.097 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=2009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0494` → IC=+0.300 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0494 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.258 (n=1939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.272 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4462` → IC=+0.277 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4462 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7009` → IC=+0.258 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7009 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1781.7648` → IC=+0.261 (n=1473)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.7648 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.255 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.199 (n=849)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0644` → IC=+0.180 (n=842)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0644 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.2641` → IC=+0.209 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2641 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1829` → IC=+0.212 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1829 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.711` → IC=+0.207 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.711 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6953` → IC=+0.139 (n=1111)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6953 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.058` → IC=+0.136 (n=1145)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.058 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.174 (n=394)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.5043` → IC=+0.140 (n=1091)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5043 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.4691` → IC=+0.148 (n=827)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4691 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `401.0` → IC=+0.136 (n=2448)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 401.0 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.173 (n=2675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0064 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.301` → IC=+0.164 (n=2675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.301 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=1283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6083` → IC=+0.208 (n=2675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6083 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.871` → IC=+0.177 (n=502)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.871 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.151 (n=2332)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2012` → IC=+0.159 (n=2675)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2012 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.148 (n=2314)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4667` → IC=+0.151 (n=2551)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4667 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.187 (n=1099)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 212.0 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.233 (n=1281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2466` → IC=+0.233 (n=1880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2466 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=1024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.089` → IC=+0.303 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.089 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.211 (n=2449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.234 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7154` → IC=+0.226 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7154 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1913.32` → IC=+0.223 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.32 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.248 (n=2177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4117` → IC=+0.261 (n=2178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4117 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.037` → IC=+0.290 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.037 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.028` → IC=+0.281 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.028 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.283 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7773` → IC=+0.239 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7773 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1898` → IC=+0.249 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1898 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1898.72` → IC=+0.250 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1898.72 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.243 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.206 (n=910)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.183 (n=910)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.2536` → IC=+0.192 (n=2725)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2536 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1379` → IC=+0.186 (n=1585)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1379 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.275` → IC=+0.199 (n=469)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.275 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8447` → IC=+0.137 (n=1818)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8447 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.172 (n=412)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8246` → IC=+0.129 (n=1780)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8246 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.148 (n=890)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6810.9354` → IC=+0.197 (n=1236)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6810.9354 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.134 (n=2671)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 128.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.164 (n=2560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0066 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3915` → IC=+0.144 (n=2906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3915 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6746` → IC=+0.185 (n=2906)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6746 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.156 (n=2934)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.258` → IC=+0.140 (n=696)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.258 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.151 (n=1938)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.852 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.178 (n=433)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.132 (n=1836)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5362` → IC=+0.132 (n=918)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5362 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `6230.6584` → IC=+0.190 (n=1318)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6230.6584 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.148 (n=919)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.168 (n=1382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0112 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.159 (n=1449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.206 (n=3043)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.188 (n=1662)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.014` → IC=+0.289 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.014 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.132 (n=3042)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1741 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.127 (n=3098)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4374` → IC=+0.132 (n=985)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4374 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=3182)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2981.4431` → IC=+0.206 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.4431 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.144 (n=1303)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 20.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.141 (n=3180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0118 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.111` → IC=+0.161 (n=1061)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.111 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=3253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6515` → IC=+0.219 (n=3180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6515 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.142 (n=3108)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.257` → IC=+0.137 (n=2809)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.257 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.1736` → IC=+0.126 (n=3180)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.1736 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.141 (n=438)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4336` → IC=+0.132 (n=1002)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4336 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2536.5467` → IC=+0.183 (n=1442)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2536.5467 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.123 (n=1980)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 27.0 (IC base=+0.117)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.248 (n=2459)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1665` → IC=+0.239 (n=1211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1665 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=2754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.234 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.8052` → IC=+0.225 (n=2834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8052 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.653` → IC=+0.253 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.653 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.234 (n=2751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6237 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2359` → IC=+0.267 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2359 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.228 (n=2683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.8171` → IC=+0.231 (n=1789)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8171 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2840.3298` → IC=+0.230 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2840.3298 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0129` → IC=+0.241 (n=1247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0129 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.249 (n=1287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.5706` → IC=+0.247 (n=2833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5706 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2841)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `1.1261` → IC=+0.255 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1261 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.032` → IC=+0.266 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.032 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.244 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.243 (n=2834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.290 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.5274` → IC=+0.237 (n=2668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5274 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.240 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.240)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.208 (n=1429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.1323` → IC=+0.176 (n=1879)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1323 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=4479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.31` → IC=+0.198 (n=4270)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.31 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2196` → IC=+0.183 (n=1663)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2196 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.628` → IC=+0.211 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.628 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.172 (n=2596)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8616 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.1931` → IC=+0.171 (n=1298)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1931 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.1574` → IC=+0.174 (n=1129)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1574 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.53` → IC=+0.167 (n=1831)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.53 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8129` → IC=+0.164 (n=2774)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8129 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=4783)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `7977.8596` → IC=+0.184 (n=1936)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7977.8596 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.171 (n=3080)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.3846 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.135 (n=1992)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.196 (n=1128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.3283` → IC=+0.198 (n=1126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3283 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.213 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.6075` → IC=+0.236 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6075 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.213 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.956` → IC=+0.206 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.956 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.193 (n=753)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8803 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.192 (n=443)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.195 (n=971)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `15815.8495` → IC=+0.191 (n=510)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15815.8495 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.162 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0031 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.202 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1986 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.135 (n=365)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.179 (n=599)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 162.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.235 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.2084` → IC=+0.166 (n=884)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2084 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=1379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.8019` → IC=+0.263 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8019 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8169` → IC=+0.190 (n=224)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8169 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.864` → IC=+0.214 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.864 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8305` → IC=+0.175 (n=884)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.8305 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `1.1544` → IC=+0.164 (n=442)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1544 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.208 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.164 (n=436)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.7829` → IC=+0.178 (n=871)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.7829 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `8223.8718` → IC=+0.172 (n=601)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8223.8718 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.121 (n=863)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0052 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.198 (n=432)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.0884 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `5148.7656` → IC=+0.135 (n=863)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 5148.7656 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.128 (n=423)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 34.0 (IC base=+0.085)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.155 (n=474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.4571` → IC=+0.185 (n=1079)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4571 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.936` → IC=+0.183 (n=184)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.936 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.848` → IC=+0.232 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.848 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.0478` → IC=+0.137 (n=949)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0478 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.142 (n=964)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7037 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2259` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2259 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.4087` → IC=+0.135 (n=1042)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4087 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.8084` → IC=+0.130 (n=695)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8084 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=1132)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2723.2049` → IC=+0.166 (n=489)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2723.2049 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.180 (n=791)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.3684 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `2591.8999` → IC=+0.151 (n=537)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2591.8999 (IC base=+0.066)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.241 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=171)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.725` → IC=+0.217 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.725 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.2223` → IC=+0.217 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2223 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.732` → IC=+0.215 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.732 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.1036` → IC=+0.206 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1036 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.8284` → IC=+0.219 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8284 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.205 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.203 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `3014.8723` → IC=+0.204 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3014.8723 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0242` → IC=+0.183 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0242 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3039` → IC=+0.151 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3039 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.162 (n=353)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.5 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `1.2295` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2295 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.238` → IC=+0.147 (n=358)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.238 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8805` → IC=+0.188 (n=267)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8805 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.162 (n=368)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.5142` → IC=+0.208 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5142 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.6761` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.6761 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.159 (n=382)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.231 (n=7240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=22670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.431` → IC=+0.228 (n=21720)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.431 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.879` → IC=+0.212 (n=2616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.879 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.949` → IC=+0.255 (n=5316)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.949 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2161` → IC=+0.159 (n=14619)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2161 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.207 (n=3908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6231` → IC=+0.194 (n=7067)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6231 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.202 (n=20344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.198 (n=8778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.006 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.203 (n=6647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.4792` → IC=+0.197 (n=19931)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4792 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=7480)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.243 (n=19932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5915 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.1777` → IC=+0.176 (n=12533)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1777 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.418` → IC=+0.195 (n=2700)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.418 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.377` → IC=+0.199 (n=19410)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 3.377 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.174 (n=5892)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7028 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.251 (n=2748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.6324` → IC=+0.204 (n=6353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6324 (IC base=+0.194)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.210 (n=18849)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.194)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.8654` → IC=+0.301 (n=2319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8654 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.524` → IC=+0.335 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.524 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.300 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.288` → IC=+0.241 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.288 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=3814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2045.72` → IC=+0.236 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2045.72 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.254 (n=2201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.270 (n=3089)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1214` → IC=+0.293 (n=1359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1214 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.269 (n=2792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.545` → IC=+0.285 (n=3088)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.545 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.271 (n=2807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.282 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5594` → IC=+0.270 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5594 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6526` → IC=+0.276 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6526 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.269 (n=3553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1780.127` → IC=+0.274 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1780.127 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.277 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.179 (n=1188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0781` → IC=+0.150 (n=1184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0781 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.199` → IC=+0.189 (n=3551)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.199 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3177` → IC=+0.201 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3177 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.329` → IC=+0.161 (n=744)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.329 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.155 (n=1184)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6348 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0686` → IC=+0.141 (n=1610)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0686 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.178 (n=504)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.140 (n=3067)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5184` → IC=+0.141 (n=3113)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5184 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.158 (n=1158)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 222.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.162 (n=3049)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3218` → IC=+0.147 (n=3046)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3218 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.678` → IC=+0.185 (n=3046)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.678 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.974` → IC=+0.139 (n=2751)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.974 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.0502` → IC=+0.149 (n=2680)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0502 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.196 (n=567)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4305` → IC=+0.142 (n=2936)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4305 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.142 (n=1958)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=3956)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.154 (n=956)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 226.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.244 (n=2421)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=3239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.01` → IC=+0.324 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.01 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.229 (n=3426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.7392` → IC=+0.243 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7392 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=4371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1917.7166` → IC=+0.239 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.7166 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.250 (n=3042)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1774` → IC=+0.264 (n=1520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1774 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.303 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.105` → IC=+0.302 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.105 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.349` → IC=+0.302 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.349 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.1776` → IC=+0.254 (n=2217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1776 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.250 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `2005.7184` → IC=+0.254 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2005.7184 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.253 (n=2259)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.195 (n=1255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0037 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4286` → IC=+0.144 (n=3757)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4286 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=3902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8896` → IC=+0.273 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8896 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1935` → IC=+0.167 (n=1714)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1935 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.948` → IC=+0.155 (n=1668)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.948 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8601` → IC=+0.149 (n=2505)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8601 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.185 (n=669)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.52` → IC=+0.150 (n=1616)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.52 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1817` → IC=+0.143 (n=1665)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1817 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5516.1197` → IC=+0.226 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5516.1197 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.143 (n=2424)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 88.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.169 (n=2774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0067 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.4329` → IC=+0.154 (n=3144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4329 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.5762` → IC=+0.210 (n=2767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5762 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1517` → IC=+0.158 (n=2937)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1517 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.843` → IC=+0.155 (n=465)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.843 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.044` → IC=+0.147 (n=2740)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.044 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.155 (n=2096)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8585 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.213 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5337` → IC=+0.152 (n=2711)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5337 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `6321.6871` → IC=+0.216 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6321.6871 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.156 (n=2077)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 92.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.150 (n=1729)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0112 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.189 (n=3827)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4286 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0026` → IC=+0.202 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0026 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.245` → IC=+0.268 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.245 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8768` → IC=+0.131 (n=2541)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8768 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.121 (n=3614)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4921` → IC=+0.120 (n=3724)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.4921 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2708.6353` → IC=+0.240 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2708.6353 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.152 (n=3161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0108 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.1362` → IC=+0.153 (n=1197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1362 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=1694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.214 (n=3606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.2158` → IC=+0.141 (n=3247)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2158 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.032` → IC=+0.148 (n=3475)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.032 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.150 (n=1198)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6383 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.179 (n=627)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.157 (n=1136)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2605.7243` → IC=+0.207 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2605.7243 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.138 (n=3065)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 43.0 (IC base=+0.126)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.260 (n=3128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=3665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=3135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.271 (n=3129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1938` → IC=+0.252 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1938 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.208` → IC=+0.285 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.208 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.239 (n=3503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.242 (n=3501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.255 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.505` → IC=+0.259 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.505 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2968.8332` → IC=+0.242 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.8332 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0259` → IC=+0.270 (n=1203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0259 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=3409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.272 (n=3610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5207 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` < `0.2984` → IC=+0.248 (n=3560)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2984 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.141` → IC=+0.280 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.141 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` < `0.7153` → IC=+0.243 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7153 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.264 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.304 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.246 (n=3399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.243)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5794)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.246 (n=1998)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5031` → IC=+0.227 (n=5989)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5031 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=2173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9348` → IC=+0.256 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9348 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4271` → IC=+0.221 (n=4367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4271 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.563` → IC=+0.227 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.563 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7094` → IC=+0.230 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7094 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8841` → IC=+0.219 (n=2947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8841 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.219 (n=5586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.226 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.4524` → IC=+0.228 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4524 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `3756.9066` → IC=+0.227 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3756.9066 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4907` → IC=+0.211 (n=4357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4907 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=1469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.213 (n=1925)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.211 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0884 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.657` → IC=+0.210 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.657 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.210 (n=3912)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.205 (n=3656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.200 (n=4014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.201 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5316` → IC=+0.203 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5316 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1871` → IC=+0.205 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1871 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.214 (n=2864)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.199)

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

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.189 (n=1519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.184 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.197 (n=668)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.138 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.198 (n=1488)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.0915` → IC=+0.188 (n=1336)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0915 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.195 (n=463)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.194 (n=504)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.179 (n=689)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.188 (n=1473)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 686.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.225 (n=613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.210 (n=920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.229 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.3947` → IC=+0.202 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3947 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.248 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.424` → IC=+0.251 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.424 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2054` → IC=+0.235 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2054 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `3.3701` → IC=+0.202 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3701 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.8037` → IC=+0.209 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8037 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2777.751` → IC=+0.238 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2777.751 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.210 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.202)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.233 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.1454` → IC=+0.218 (n=728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1454 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.495` → IC=+0.220 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.495 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.8548` → IC=+0.209 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8548 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2066` → IC=+0.215 (n=1473)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2066 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.521` → IC=+0.210 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.521 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8778` → IC=+0.209 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8778 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2312` → IC=+0.205 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2312 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.210 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.215 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1643 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.244 (n=455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4848` → IC=+0.221 (n=1361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4848 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.207 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.405` → IC=+0.201 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.405 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.0908` → IC=+0.204 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0908 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6242` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6242 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.855` → IC=+0.201 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.855 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.346` → IC=+0.204 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.346 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.226 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.229 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.207 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6350.7998` → IC=+0.207 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6350.7998 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.201 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.223 (n=637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.235 (n=670)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.7666` → IC=+0.240 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7666 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.224 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6421` → IC=+0.248 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6421 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.208 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.206 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.1469` → IC=+0.206 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1469 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.204 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4745 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4320.729` → IC=+0.244 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4320.729 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.205 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.220 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.234 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.5947` → IC=+0.237 (n=697)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5947 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.250 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.6522` → IC=+0.252 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6522 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.5279` → IC=+0.222 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5279 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.776` → IC=+0.235 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.776 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `0.9181` → IC=+0.224 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9181 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.2706` → IC=+0.227 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2706 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.0838` → IC=+0.236 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0838 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.6023` → IC=+0.259 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6023 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `3782.8762` → IC=+0.234 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3782.8762 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.256 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.220)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` > `0.6521` → IC=-0.148 (n=475)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6521
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=1428)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.148 (n=722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0037 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.184 (n=1394)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.75 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1429` → IC=+0.140 (n=1034)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1429 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.442` → IC=+0.148 (n=461)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.442 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0602` → IC=+0.268 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0602 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.141 (n=393)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.537` → IC=-0.124 (n=288)

  - _Acción_: SKIP cuando `ibs_20min` < 0.537
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=587)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.126 (n=605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0051 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.537` → IC=+0.164 (n=587)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.537 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.167 (n=316)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.0742` → IC=+0.275 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0742 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2165` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2165 (IC base=+0.047)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6857` → IC=-0.175 (n=152)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6857
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=460)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.126 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0051 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.7783` → IC=+0.219 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7783 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.173 (n=328)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.677` → IC=+0.202 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.677 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0296` → IC=+0.269 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0296 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.59` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.59 (IC base=+0.024)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7241` → IC=+0.137 (n=497)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7241 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.129 (n=173)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.664` → IC=+0.136 (n=163)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.664 (IC base=+0.019)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.148 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0111 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.172 (n=403)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.132 (n=384)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.838` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.838 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.162 (n=134)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0818 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1557` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1557 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0058` → IC=-0.239 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=187)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=280)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=357)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=176)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=307)

- **FILTRO** `sigma_ewma_delta_pct` > `9.697` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.697
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=299)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=206)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=92)

- **FILTRO** `volumen_regimen` < `0.89` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=82)

- **FILTRO** `drift_60min` |x|> `0.0922` → IC=-0.308 (n=71)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0922
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=110)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5857` → IC=-0.471 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5857
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=98)

- **FILTRO** `volumen_regimen` > `1.0679` → IC=-0.174 (n=44)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0679
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=86)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=91)

- **FILTRO** `ibs_20min` > `0.681` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.681
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=84)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=69)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.298 (n=112)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

- **FILTRO** `volumen_spike_ratio` > `2.3401` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3401
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=72)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.329 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` > `2.412` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.412
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `volumen_regimen` < `0.9051` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9051
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=36)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.242 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.181 (n=693)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6757 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7967` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7967 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.614` → IC=+0.155 (n=381)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.614 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.554` → IC=+0.141 (n=706)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 8.554 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.179 (n=232)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6249 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.175 (n=512)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.187 (n=196)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.53` → IC=+0.156 (n=190)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 10.53 (IC base=+0.033)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7805` → IC=-0.126 (n=89)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7805
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=183)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.157 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0062 (IC base=+0.036)

- **PATRÓN** `ibs_20min` > `0.9071` → IC=+0.123 (n=136)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.9071 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.6135` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6135 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.215` → IC=+0.147 (n=383)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.215 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.339` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 11.339 (IC base=+0.088)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1848` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1848
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=247)

- **FILTRO** `ibs_20min` > `0.1452` → IC=-0.126 (n=137)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1452
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=267)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.123 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0056 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.129 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.8899` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8899 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.0953` → IC=+0.141 (n=193)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0953 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.38` → IC=+0.143 (n=242)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 9.38 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6249 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1848` → IC=+0.143 (n=247)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1848 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.7623` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.7623 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=200)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.584` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.584 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2839` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2839 (IC base=+0.012)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=128)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.281 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.357 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.4812` → IC=+0.324 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4812 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.244)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.322 (n=105)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.391 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.377 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1208.0` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1208.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.258)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.258)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.258)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.297 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.258)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.322 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `1728.0` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1728.0 (IC base=+0.258)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.322 (n=105)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3975` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3975 (IC base=+0.332)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.391 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.332)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.377 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.332)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `1208.0` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1208.0 (IC base=+0.332)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.258)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.258)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.258)

- **PATRÓN** `drift_15min` |x|≤ `2.3044` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.297 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.258)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.322 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `1728.0` → IC=+0.308 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1728.0 (IC base=+0.258)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1435)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1435)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=243)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=243)

- **FILTRO** `libro_liquidez` < `6868.5329` → IC=-0.149 (n=129)

  - _Acción_: SKIP cuando `libro_liquidez` < 6868.5329
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=130)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=744)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12112.4745` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 12112.4745
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=87)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3907)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=139)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=96)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=126)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.160 (n=92)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=34)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.080)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=146)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=273)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.333 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.267)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.267)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1594)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1548)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=727)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=442)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=423)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=187)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=984)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=984)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1211)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1211)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=275)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=275)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.139 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=209)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=336)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=384)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=297)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=397)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=397)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=242)

- **FILTRO** `libro_liquidez` < `659.869` → IC=-0.134 (n=140)

  - _Acción_: SKIP cuando `libro_liquidez` < 659.869
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=287)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=348)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.59` → IC=-0.141 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=72)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.188 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=95)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.159 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=93)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.241 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=266)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=683)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.131 (n=315)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.51 (IC base=-0.010)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.152 (n=159)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=340)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.121 (n=336)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=352)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.122 (n=329)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=392)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=145)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=645)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=530)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=282)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.138 (n=114)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=353)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.141 (n=472)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=474)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.172 (n=7686)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=24626)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=8196)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=25128)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.182 (n=1478)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=4498)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.149 (n=1987)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3920)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.133 (n=1547)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.125 (n=3006)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.171 (n=1062)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3446)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.179 (n=1174)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3523)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=1466)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4579)

- **PATRÓN** `ibs_20min` > `0.963` → IC=+0.134 (n=2032)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.963 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1746.7372` → IC=+0.122 (n=2031)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1746.7372 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.180 (n=1111)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=3648)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.159 (n=1488)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4522)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2432)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2356)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3024)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3976)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.198 (n=336)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1064)

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
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=360)

- **FILTRO** `ballena_activa_n` > `84.0` → IC=-0.179 (n=157)

  - _Acción_: SKIP cuando `ballena_activa_n` > 84.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=308)

- **FILTRO** `libro_liquidez` < `3222.056` → IC=-0.183 (n=156)

  - _Acción_: SKIP cuando `libro_liquidez` < 3222.056
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=317)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=968)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.191 (n=390)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=782)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=239)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.024)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=21935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=49596)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=17094)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=54437)

- **FILTRO** `ibs_7min` < `0.2191` → IC=-0.232 (n=17882)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2191
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=53649)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=23441)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=48090)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.251 (n=20920)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=68629)

- **FILTRO** `ibs_7min` > `0.2827` → IC=-0.184 (n=22386)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2827
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=67163)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=3075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=9653)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=3130)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=9598)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.250 (n=4198)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8530)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.152 (n=2767)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=9961)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.276 (n=3767)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=11701)

- **FILTRO** `ibs_7min` > `0.7768` → IC=-0.211 (n=3865)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7768
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=11603)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2871)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9045)

- **FILTRO** `ibs_7min` < `0.7147` → IC=-0.207 (n=2979)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7147
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8937)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.200 (n=2966)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8950)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2798)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=9383)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.195 (n=3043)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=9138)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.182 (n=3037)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9144)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=2929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9238)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.323 (n=2886)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=9281)

- **FILTRO** `ibs_7min` < `0.2895` → IC=-0.249 (n=4014)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2895
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=8153)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.200 (n=2463)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9704)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.257 (n=3962)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12421)

- **FILTRO** `ibs_7min` > `0.7321` → IC=-0.182 (n=4093)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7321
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=12290)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2862)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8713)

- **FILTRO** `ibs_7min` < `0.7159` → IC=-0.195 (n=2893)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7159
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8682)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.189 (n=2824)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8751)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.259 (n=2789)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=9272)

- **FILTRO** `ibs_7min` > `0.2741` → IC=-0.177 (n=3014)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2741
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9047)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.170 (n=2947)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9114)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=2702)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8777)

- **FILTRO** `ibs_7min` < `0.7031` → IC=-0.230 (n=3788)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7031
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=7691)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.216 (n=2842)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8637)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.198 (n=4197)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=13131)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=3741)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=7925)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=2762)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8904)

- **FILTRO** `ibs_7min` < `0.1667` → IC=-0.230 (n=2913)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8753)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.205 (n=2599)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=9067)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3745)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=12383)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1010)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1296)

- **FILTRO** `libro_liquidez` < `10498.4421` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `libro_liquidez` < 10498.4421
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=585)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=888)

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

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=578)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=578)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=394)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.152 (n=671)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `418.1817` → IC=+0.163 (n=494)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 418.1817 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2321.735` → IC=+0.132 (n=1322)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2321.735 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.180 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.159 (n=312)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 375.759 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2517.123` → IC=+0.242 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2517.123 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 6.0 (IC base=+0.133)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.154 (n=102)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.125 (n=366)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.118)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.184 (n=185)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `655.7381` → IC=+0.159 (n=244)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 655.7381 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 59.0 (IC base=+0.128)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4318` → IC=+0.209 (n=115)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4318 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.144)

- **PATRÓN** `total_vol_5m` < `4608.276` → IC=+0.180 (n=170)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4608.276 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3709.6192` → IC=+0.167 (n=169)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3709.6192 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 27.0 (IC base=+0.144)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.124 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `T_h` > `129.6211` → IC=-0.186 (n=208)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=625)

- **FILTRO** `pct_vs_K` |x|> `3.4135` → IC=-0.195 (n=283)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4135
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=550)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.150 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0045 (IC base=-0.075)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `88.1766` → IC=-0.234 (n=62)

  - _Acción_: SKIP cuando `T_h` > 88.1766
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=187)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.277 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.030)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7112` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `pct_vs_K` |x|≤ 1.7112 (IC base=-0.030)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` < `0.01` → IC=-0.136 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=28)

- **FILTRO** `T_h` < `251.7955` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `66.2576` → IC=-0.185 (n=52)

  - _Acción_: SKIP cuando `T_h` < 66.2576
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=106)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0164` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0164
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0102` → IC=-0.235 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=260)

- **FILTRO** `T_h` > `70.1154` → IC=-0.227 (n=511)

  - _Acción_: SKIP cuando `T_h` > 70.1154
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=253)

- **FILTRO** `pct_vs_K` |x|> `2.0455` → IC=-0.345 (n=328)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0455
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=329)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.205 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=63)

- **FILTRO** `T_h` > `49.5461` → IC=-0.204 (n=187)

  - _Acción_: SKIP cuando `T_h` > 49.5461
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=64)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.226 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=183)

- **FILTRO** `T_h` > `143.4358` → IC=-0.258 (n=60)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=183)

- **FILTRO** `T_h` < `88.1777` → IC=-0.244 (n=80)

  - _Acción_: SKIP cuando `T_h` < 88.1777
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=163)

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
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.310 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `T_h` > `95.4524` → IC=-0.287 (n=106)

  - _Acción_: SKIP cuando `T_h` > 95.4524
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=108)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.365 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=151)

- **FILTRO** `T_h` > `57.2198` → IC=-0.235 (n=134)

  - _Acción_: SKIP cuando `T_h` > 57.2198
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8095` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `pct_vs_K` |x|≤ 0.8095 (IC base=-0.160)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.264 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=162)

- **FILTRO** `T_h` > `66.1685` → IC=-0.224 (n=161)

  - _Acción_: SKIP cuando `T_h` > 66.1685
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=54)

- **FILTRO** `sigma_h` > `0.0142` → IC=-0.304 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=96)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=109)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.383 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.333)

- **PATRÓN** `T_h` < `0.3261` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3261 (IC base=+0.333)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.333)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.333)

- **PATRÓN** `edge` > `0.1` → IC=+0.429 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.394)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.400 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.394)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.410 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.394)

- **PATRÓN** `T_h` > `1.4832` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4832 (IC base=+0.394)

- **PATRÓN** `dist_50` > `0.3717` → IC=+0.444 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3717 (IC base=+0.394)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.394)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1235` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1235 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.269 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.179)

- **PATRÓN** `T_h` > `1.484` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.179)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.219 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.179)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.406)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.419 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.406)

- **PATRÓN** `T_h` < `1.2415` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2415 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.406)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.175` → IC=+0.486 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.175 (IC base=+0.436)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.468 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.436)

- **PATRÓN** `T_h` > `0.5264` → IC=+0.452 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5264 (IC base=+0.436)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.436)

- **PATRÓN** `edge` > `0.2008` → IC=+0.471 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2008 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.474 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.463)

- **PATRÓN** `T_h` < `0.8102` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8102 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.493 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=409)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=474)

- **PATRÓN** `streak_estiramiento` < `0.5343` → IC=+0.185 (n=217)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.5343 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.128 (n=240)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 29.0 (IC base=+0.059)

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
- **FILTRO** `regimen_ma_toques` < `2.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `regimen_ma_toques` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=162)

- **PATRÓN** `streak_estiramiento` < `0.2206` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.2206 (IC base=+0.034)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.097)

- **PATRÓN** `streak_estiramiento` < `0.4354` → IC=+0.183 (n=137)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.4354 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 31.0 (IC base=+0.097)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `streak_len` > `5.0` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=111)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=112)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=36)

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

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

- **FILTRO** `libro_liquidez` < `3449.8988` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3449.8988
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1062)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1338)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1294)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4808)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2780)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.191 (n=1713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0053 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.218` → IC=+0.160 (n=5141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.218 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3577` → IC=+0.153 (n=4790)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3577 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.153 (n=4761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.230 (n=4605)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1322` → IC=+0.136 (n=2445)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1322 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.4958` → IC=+0.130 (n=4794)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4958 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.305` → IC=+0.256 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.305 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=2986)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `4609.1668` → IC=+0.170 (n=1713)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4609.1668 (IC base=+0.145)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1953)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.221 (n=775)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.258 (n=258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2676` → IC=+0.219 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2676 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.220 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7086` → IC=+0.276 (n=774)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7086 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.228 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.206 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.54` → IC=+0.307 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.54 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11859.2402` → IC=+0.218 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11859.2402 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.147 (n=954)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0069 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.144 (n=636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.134 (n=637)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.134 (n=1005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4934` → IC=+0.216 (n=954)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4934 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1163` → IC=+0.151 (n=599)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1163 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.4255` → IC=+0.131 (n=1010)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4255 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.81` → IC=+0.283 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.81 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5879.8519` → IC=+0.162 (n=433)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5879.8519 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.6` → IC=+0.135 (n=936)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.6 (IC base=+0.060)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0255` → IC=+0.169 (n=1269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0255 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.221` → IC=+0.174 (n=1269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.221 (IC base=+0.157)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0986` → IC=+0.216 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0986 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.162 (n=1167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.165 (n=1121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 14.0 (IC base=+0.157)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.235 (n=1138)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.5184` → IC=+0.199 (n=310)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.5184 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.036` → IC=+0.209 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.036 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `2713.7902` → IC=+0.188 (n=846)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2713.7902 (IC base=+0.157)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.156 (n=987)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.388 (n=247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.365 (n=493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.377 (n=492)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1074` → IC=+0.377 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1074 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.371 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.363 (n=496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.393 (n=739)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.379 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.398 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9740.6649` → IC=+0.381 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9740.6649 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.371 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2194` → IC=+0.374 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2194 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.397 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.379 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.385 (n=364)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.391 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.389 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.385 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.404 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.368 (n=376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.378 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.366 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0824` → IC=+0.372 (n=335)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0824 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.373 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.365 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.374 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.762` → IC=+0.391 (n=375)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.762 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.370 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.365 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.991` → IC=+0.402 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.991 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4142.643` → IC=+0.378 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4142.643 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.193 (n=2655)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2658)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=2227)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1398` → IC=+0.221 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1398 (IC base=-0.080)

- **PATRÓN** `ibs_15` > `0.6296` → IC=+0.279 (n=1208)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6296 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1102` → IC=+0.204 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1102 (IC base=-0.080)

- **PATRÓN** `dist_vwap_pct` < `0.5564` → IC=+0.200 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5564 (IC base=-0.080)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2354` → IC=+0.271 (n=1597)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2354 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.284 (n=4795)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.649` → IC=+0.280 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.649 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0316` → IC=-0.222 (n=2489)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0316
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=830)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.218 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=2490)

- **FILTRO** `sigma_ewma_delta_pct` > `22.228` → IC=-0.257 (n=475)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.228
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2844)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.154 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.003 (IC base=+0.072)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.282 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.072)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.326 (n=418)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1023` → IC=+0.277 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1023 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.4912` → IC=+0.286 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4912 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.337` → IC=+0.148 (n=217)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.337 (IC base=+0.072)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.186)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.289 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.186)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.186)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.186)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=791)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.159 (n=607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.181 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.195 (n=474)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5679` → IC=+0.242 (n=606)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5679 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.2696` → IC=+0.152 (n=567)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2696 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=791)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `8988.4246` → IC=+0.162 (n=202)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8988.4246 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.249 (n=1823)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3541` → IC=+0.248 (n=1604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3541 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7736` → IC=+0.258 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7736 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2152` → IC=+0.264 (n=827)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2152 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.243 (n=1238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.183` → IC=+0.303 (n=1216)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.183 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.5991` → IC=+0.269 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5991 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.253` → IC=+0.246 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.253 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.248 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1822` → IC=-0.261 (n=308)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1822
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=925)

- **FILTRO** `drift_60min` |x|> `0.1722` → IC=-0.260 (n=419)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=814)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.283 (n=307)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=926)

- **FILTRO** `sigma_ewma_delta_pct` > `6.133` → IC=-0.200 (n=285)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.133
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=948)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.196)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.196)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.196)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0639` → IC=+0.233 (n=813)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0639 (IC base=-0.032)

- **PATRÓN** `ibs_15` < `0.383` → IC=+0.294 (n=813)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.383 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` > `0.6745` → IC=+0.240 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6745 (IC base=-0.032)

- **PATRÓN** `dist_vwap_pct` < `0.1921` → IC=+0.244 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1921 (IC base=-0.032)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0133` → IC=-0.242 (n=1128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=377)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=1486)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.216)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1189` → IC=+0.295 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1189 (IC base=-0.017)

- **PATRÓN** `ibs_15` < `0.1343` → IC=+0.309 (n=753)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1343 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.7632` → IC=+0.337 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7632 (IC base=-0.017)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0061 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1564` → IC=+0.144 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1564 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4735 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.097)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0061 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1564` → IC=+0.144 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1564 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.3763` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3763 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.340 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4735` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4735 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.097)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.299 (n=441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.310 (n=583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.286 (n=880)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2235` → IC=+0.291 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2235 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=1364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8385` → IC=+0.312 (n=1320)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8385 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.262` → IC=+0.313 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.262 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.932` → IC=+0.389 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.932 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `13286.7566` → IC=+0.305 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13286.7566 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.305 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.278 (n=318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.314 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.282 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.304 (n=701)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2467` → IC=+0.309 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2467 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.392 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `14783.8555` → IC=+0.306 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14783.8555 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.304 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.313 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.291 (n=620)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.326 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.295 (n=569)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.318 (n=620)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.1233` → IC=+0.307 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1233 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.164` → IC=+0.379 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.164 (IC base=+0.290)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0848` → IC=-0.157 (n=246)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0848
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=83)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1387` → IC=-0.136 (n=53)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1387
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=161)

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
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

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
- **PATRÓN** `ratio` < `0.9704` → IC=+0.398 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9704 (IC base=+0.175)

- **PATRÓN** `T_h` > `120.2753` → IC=+0.355 (n=2753)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 120.2753 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0221` → IC=+0.390 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0221 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9936` → IC=+0.145 (n=260)

  - _Acción_: Kelly boost +0.73€ cuando `T_h` > 111.9936 (IC base=+0.133)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.268 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.133)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.318 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.303)

- **PATRÓN** `ratio` > `1.0187` → IC=+0.361 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0187 (IC base=+0.303)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `85.7585` → IC=+0.225 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 85.7585 (IC base=+0.223)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.405 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.223)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.356 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0314` → IC=+0.401 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0314 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.419 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.145 a +0.230 en UPDOWN_GBM#15min (n=4605). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7086 sube el IC de +0.202 a +0.276 en UPDOWN_GBM#BTC#15min (n=774). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4934 sube el IC de +0.131 a +0.216 en UPDOWN_GBM#ETH#15min (n=954). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.157 a +0.235 en UPDOWN_GBM#XRP#15min (n=1138). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.068 a +0.156 en UPDOWN_GBM#XRP#15min (n=987). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6296 sube el IC de -0.080 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1208). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3684 sube el IC de -0.005 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4795). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.072 a +0.326 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=418). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.186 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5679 sube el IC de +0.147 a +0.242 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=606). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.183 sube el IC de +0.243 a +0.303 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1216). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.196 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.383 sube el IC de -0.032 a +0.294 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=813). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.216 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1343 sube el IC de -0.017 a +0.309 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=753). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7 (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.097 a +0.340 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8385 sube el IC de +0.283 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=1320). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.277 a +0.304 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=701). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.290 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=620). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.363 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=739). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=364). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.762 sube el IC de +0.362 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=375). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2165 | +0.085 | +236.37€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2165 | +0.085 | +236.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1760 | +0.085 | +197.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1760 | +0.085 | +197.08€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1109 | -0.021 | +73.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1109 | -0.021 | +73.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 856 | -0.036 | +58.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 856 | -0.036 | +58.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 169 | +0.056 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 169 | +0.056 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 77 | -0.032 | -6.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 46548 | -0.086 | -5971.97€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2834 | +0.064 | -295.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 43714 | -0.096 | -5676.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4775 | -0.113 | -805.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4775 | -0.113 | -805.43€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2834 | +0.064 | -295.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2834 | +0.064 | -295.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4833 | -0.108 | -934.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4833 | -0.108 | -934.18€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12674 | -0.043 | -1172.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12674 | -0.043 | -1172.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12659 | -0.115 | -1338.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12659 | -0.115 | -1338.19€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8773 | -0.128 | -1426.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8773 | -0.128 | -1426.49€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 47457 | -0.012 | +2891.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 12267 | +0.005 | +1541.92€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 35190 | -0.018 | +1349.23€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 47457 | -0.012 | +2891.15€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 12267 | +0.005 | +1541.92€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 35190 | -0.018 | +1349.23€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 183179 | +0.113 | -7654.52€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21467 | +0.180 | -690.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 839 | +0.005 | -78.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 150373 | +0.105 | -6508.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10500 | +0.093 | -376.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 24920 | +0.102 | -1764.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 75 | -0.175 | +11.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 24830 | +0.104 | -1763.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 34809 | +0.124 | -582.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5594 | +0.179 | -224.57€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 24897 | +0.120 | -182.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4276 | +0.079 | -153.31€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 24968 | +0.097 | -1850.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 84 | -0.116 | +5.91€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 24869 | +0.098 | -1845.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 39108 | +0.123 | -823.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9881 | +0.177 | -246.05€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 25286 | +0.105 | -517.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3929 | +0.103 | -50.59€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 34430 | +0.113 | -1521.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5748 | +0.199 | -244.77€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 742 | +0.032 | -24.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 25645 | +0.096 | -1078.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2295 | +0.102 | -172.97€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 24944 | +0.106 | -1112.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 85 | -0.121 | +7.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 24846 | +0.107 | -1119.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 29677 | +0.193 | -2015.81€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 29677 | +0.193 | -2015.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6714 | +0.172 | -660.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6714 | +0.172 | -660.94€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4233 | +0.197 | -153.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4233 | +0.197 | -153.64€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6598 | +0.176 | -567.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6598 | +0.176 | -567.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5554 | +0.249 | -202.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5554 | +0.249 | -202.85€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6499 | +0.185 | -445.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6499 | +0.185 | -445.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1215 | +0.426 | -43.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1215 | +0.426 | -43.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 498 | +0.440 | -3.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 498 | +0.440 | -3.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 490 | +0.425 | -17.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 490 | +0.425 | -17.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 104849 | +0.199 | -7762.32€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 104849 | +0.199 | -7762.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 18112 | +0.179 | -2051.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 18112 | +0.179 | -2051.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16905 | +0.224 | -566.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16905 | +0.224 | -566.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 18002 | +0.179 | -1927.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 18002 | +0.179 | -1927.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 17040 | +0.218 | -684.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 17040 | +0.218 | -684.03€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 17331 | +0.202 | -1114.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 17331 | +0.202 | -1114.41€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 17459 | +0.196 | -1418.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 17459 | +0.196 | -1418.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 40332 | +0.117 | +331.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 40332 | +0.117 | +331.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 20082 | +0.117 | +201.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 20082 | +0.117 | +201.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 20250 | +0.116 | +130.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 20250 | +0.116 | +130.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2525 | +0.292 | -12.95€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2525 | +0.292 | -12.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1156 | +0.279 | -35.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1156 | +0.279 | -35.01€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1231 | +0.298 | +17.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1231 | +0.298 | +17.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 138 | +0.343 | +5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 138 | +0.343 | +5.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1160 | +0.440 | -0.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1160 | +0.440 | -0.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 557 | +0.432 | -10.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 557 | +0.432 | -10.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 552 | +0.448 | +8.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 552 | +0.448 | +8.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 51 | +0.406 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 51 | +0.406 | +1.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1915 | +0.068 | -85.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1190 | +0.081 | -21.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1481 | +0.075 | -40.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1190 | +0.081 | -21.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 81598 | +0.101 | -1963.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6574 | +0.096 | +134.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 75024 | +0.101 | -2098.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 44625 | +0.105 | -450.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6574 | +0.096 | +134.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 38051 | +0.107 | -585.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 17282 | +0.109 | -104.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 17282 | +0.109 | -104.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 19691 | +0.082 | -1408.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 19691 | +0.082 | -1408.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 55332 | +0.099 | +30672.82€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 55332 | +0.099 | +30672.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9162 | +0.226 | +7913.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9162 | +0.226 | +7913.92€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8429 | +0.175 | +6569.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8429 | +0.175 | +6569.28€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 9937 | +0.207 | +7836.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9937 | +0.207 | +7836.06€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7464 | +0.052 | +2337.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7464 | +0.052 | +2337.02€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7736 | -0.031 | +2004.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7736 | -0.031 | +2004.97€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 12604 | -0.023 | +4011.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12604 | -0.023 | +4011.57€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 58199 | +0.085 | +33707.34€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 58199 | +0.085 | +33707.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11258 | -0.002 | +6033.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11258 | -0.002 | +6033.71€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12503 | +0.004 | +3296.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12503 | +0.004 | +3296.17€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7948 | +0.294 | +9053.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7948 | +0.294 | +9053.42€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11065 | +0.013 | +3415.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11065 | +0.013 | +3415.47€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8979 | +0.044 | +4009.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8979 | +0.044 | +4009.12€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6446 | +0.316 | +7899.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6446 | +0.316 | +7899.45€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 43817 | +0.178 | +36094.59€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 43817 | +0.178 | +36094.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6587 | +0.240 | +6147.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6587 | +0.240 | +6147.37€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6931 | +0.139 | +5107.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6931 | +0.139 | +5107.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7053 | +0.224 | +6110.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7053 | +0.224 | +6110.58€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7507 | +0.129 | +5802.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7507 | +0.129 | +5802.34€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8294 | +0.119 | +6204.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8294 | +0.119 | +6204.30€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7445 | +0.233 | +6722.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7445 | +0.233 | +6722.99€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11852 | +0.126 | +5914.98€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11852 | +0.126 | +5914.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3354 | +0.129 | +1823.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3354 | +0.129 | +1823.10€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 505 | +0.159 | +279.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3491 | +0.125 | +1678.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3491 | +0.125 | +1678.97€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3013 | +0.096 | +1194.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3013 | +0.096 | +1194.49€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1021 | +0.169 | +630.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1021 | +0.169 | +630.22€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 55529 | +0.187 | +45529.65€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 55529 | +0.187 | +45529.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8752 | +0.251 | +8492.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8752 | +0.251 | +8492.00€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8794 | +0.137 | +6032.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8794 | +0.137 | +6032.79€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9436 | +0.235 | +8527.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9436 | +0.235 | +8527.11€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9199 | +0.139 | +6754.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9199 | +0.139 | +6754.99€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9868 | +0.121 | +6951.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9868 | +0.121 | +6951.63€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9480 | +0.240 | +8771.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9480 | +0.240 | +8771.13€ | 0 | 20 |
| ✅ GBM_LATE_5M | 13793 | +0.210 | +11177.34€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13793 | +0.210 | +11177.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3257 | +0.211 | +2804.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3257 | +0.211 | +2804.80€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1305 | +0.204 | +1010.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1305 | +0.204 | +1010.70€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4018 | +0.203 | +3004.91€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4018 | +0.203 | +3004.91€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 2200 | +0.208 | +1819.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2200 | +0.208 | +1819.52€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4889 | +0.050 | +1332.93€ | 1 | 6 |
| ✅ GBM_LATE_60M#60min | 4889 | +0.050 | +1332.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1706 | +0.059 | +527.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1706 | +0.059 | +527.27€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1575 | +0.052 | +486.31€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1575 | +0.052 | +486.31€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1608 | +0.038 | +319.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1608 | +0.038 | +319.35€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 699 | -0.249 | -35.65€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 699 | -0.249 | -35.65€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 255 | -0.251 | -20.81€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 255 | -0.251 | -20.81€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 257 | -0.241 | -5.52€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 257 | -0.241 | -5.52€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 187 | -0.251 | -9.32€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 187 | -0.251 | -9.32€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2024 | +0.082 | +525.47€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2024 | +0.082 | +525.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 782 | +0.070 | +191.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 782 | +0.070 | +191.01€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 714 | +0.057 | +138.46€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 714 | +0.057 | +138.46€ | 2 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 528 | +0.132 | +196.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 528 | +0.132 | +196.00€ | 1 | 8 |
| ✅ LATE_WINDOW_5MIN | 227 | +0.295 | +256.39€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN#5min | 227 | +0.295 | +256.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 227 | +0.295 | +256.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 227 | +0.295 | +256.39€ | 1 | 13 |
| ✅ LEADLAG_BTC_XRP_15M | 4283 | +0.097 | +970.50€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4283 | +0.097 | +970.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4283 | +0.097 | +970.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4283 | +0.097 | +970.50€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1024 | -0.013 | +12.35€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1024 | -0.013 | +12.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 56 | +0.017 | +0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 56 | +0.017 | +0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 271 | -0.009 | +6.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 271 | -0.009 | +6.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 35 | -0.149 | -5.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 35 | -0.149 | -5.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 274 | +0.018 | +17.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 274 | +0.018 | +17.33€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 306 | -0.013 | +1.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 306 | -0.013 | +1.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 82 | -0.083 | -7.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 82 | -0.083 | -7.78€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4152 | +0.017 | +126.32€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4152 | +0.017 | +126.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 203 | +0.022 | -1.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 203 | +0.022 | -1.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 825 | +0.015 | +40.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 825 | +0.015 | +40.47€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 238 | +0.029 | +28.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 238 | +0.029 | +28.31€ | 0 | 2 |
| ✅ LIQUIDACIONES_5M#ETH | 1646 | +0.019 | +27.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1646 | +0.019 | +27.39€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 768 | +0.012 | +2.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 768 | +0.012 | +2.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 472 | +0.015 | +29.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 472 | +0.015 | +29.54€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2290 | -0.033 | -10.12€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2290 | -0.033 | -10.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 689 | -0.033 | -12.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 689 | -0.033 | -12.95€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 811 | -0.008 | +18.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 811 | -0.008 | +18.64€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 790 | -0.059 | -15.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 790 | -0.059 | -15.81€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 14611 | -0.031 | -114.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 7012 | -0.033 | -84.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7599 | -0.029 | -30.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 522 | -0.050 | -26.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 265 | -0.021 | +4.14€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 257 | -0.079 | -30.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3817 | -0.025 | -5.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1818 | -0.024 | +0.03€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1999 | -0.025 | -5.45€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1444 | -0.028 | +12.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 737 | -0.033 | -0.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 707 | -0.023 | +13.68€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3300 | -0.033 | -45.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1552 | -0.036 | -35.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1748 | -0.030 | -10.21€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2811 | -0.025 | +25.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1361 | -0.030 | -4.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1450 | -0.020 | +29.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2717 | -0.043 | -75.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1279 | -0.050 | -48.46€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1438 | -0.036 | -26.88€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 65636 | -0.000 | +3540.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 65636 | -0.000 | +3540.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11883 | +0.027 | +1625.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11883 | +0.027 | +1625.71€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9205 | -0.036 | -114.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9205 | -0.036 | -114.63€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12017 | +0.025 | +1313.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12017 | +0.025 | +1313.41€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9124 | -0.051 | -201.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9124 | -0.051 | -201.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11182 | -0.004 | +317.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11182 | -0.004 | +317.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 12225 | +0.017 | +599.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 12225 | +0.017 | +599.12€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7126 | -0.055 | -118.34€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7126 | -0.055 | -118.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1972 | -0.065 | -27.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1972 | -0.065 | -27.77€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 72 | -0.013 | +0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 72 | -0.013 | +0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 807 | -0.119 | -34.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 807 | -0.119 | -34.96€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2168 | -0.068 | -12.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2168 | -0.068 | -12.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 863 | -0.018 | -27.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 863 | -0.018 | -27.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3376 | +0.004 | -1.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3376 | +0.004 | -1.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 161080 | -0.078 | +2315.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 161080 | -0.078 | +2315.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 28196 | -0.078 | +1627.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 28196 | -0.078 | +1627.63€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 24097 | -0.101 | -1206.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 24097 | -0.101 | -1206.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 28550 | -0.068 | +1438.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 28550 | -0.068 | +1438.08€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 23636 | -0.098 | -696.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 23636 | -0.098 | -696.50€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 28807 | -0.058 | +340.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 28807 | -0.058 | +340.20€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 27794 | -0.069 | +812.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 27794 | -0.069 | +812.22€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9022 | -0.035 | -182.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9022 | -0.035 | -182.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2091 | -0.046 | -27.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2091 | -0.046 | -27.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2639 | -0.026 | -38.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2639 | -0.026 | -38.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1270 | -0.065 | -32.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1270 | -0.065 | -32.51€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1011 | -0.031 | -33.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1011 | -0.031 | -33.00€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2108 | +0.120 | +838.49€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1972 | +0.124 | +825.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 472 | +0.133 | +227.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 472 | +0.133 | +227.96€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 401 | +0.118 | +139.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 401 | +0.118 | +139.50€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 369 | +0.128 | +169.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 369 | +0.128 | +169.75€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 338 | +0.144 | +177.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 338 | +0.144 | +177.10€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 392 | +0.096 | +111.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 392 | +0.096 | +111.58€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2110 | -0.017 | -20.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2110 | -0.017 | -20.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 391 | +0.014 | +25.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 391 | +0.014 | +25.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 387 | -0.048 | -27.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 387 | -0.048 | -27.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 531 | -0.035 | -26.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 531 | -0.035 | -26.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 432 | -0.002 | -0.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 432 | -0.002 | -0.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 369 | -0.007 | +8.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 369 | -0.007 | +8.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1122 | -0.075 | -43.18€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 516 | -0.108 | -77.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 404 | -0.123 | -58.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 394 | -0.035 | +25.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 283 | -0.019 | +34.47€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 212 | -0.065 | +8.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 176 | -0.062 | +7.05€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 863 | -0.077 | -17.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1421 | -0.207 | -90.14€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 561 | -0.205 | -49.85€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 494 | -0.204 | -45.54€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 473 | -0.212 | -39.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 415 | -0.222 | -45.98€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 387 | -0.202 | -1.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 360 | -0.199 | -3.62€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1269 | -0.209 | -95.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 535 | +0.377 | +503.19€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 107 | +0.151 | +88.66€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 107 | +0.151 | +88.66€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 123 | +0.364 | +103.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 123 | +0.364 | +103.53€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 305 | +0.458 | +311.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 305 | +0.458 | +311.00€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 535 | +0.377 | +503.19€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 921 | +0.044 | +83.01€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 921 | +0.044 | +83.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 347 | +0.027 | +8.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 347 | +0.027 | +8.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 71 | +0.007 | +0.21€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 71 | +0.007 | +0.21€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 420 | +0.069 | +68.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 420 | +0.069 | +68.62€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3563 | -0.023 | -142.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3563 | -0.023 | -142.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 609 | -0.029 | -27.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 609 | -0.029 | -27.28€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 171 | -0.043 | -14.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 171 | -0.043 | -14.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1656 | -0.019 | -60.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1656 | -0.019 | -60.37€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 116 | -0.042 | -10.16€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 116 | -0.042 | -10.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 72 | -0.013 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 72 | -0.013 | -5.54€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11483 | +0.014 | +74.54€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11483 | +0.014 | +74.54€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2994 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2994 | +0.018 | +23.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2992 | +0.017 | +36.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2992 | +0.017 | +36.27€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2917 | +0.008 | -3.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2917 | +0.008 | -3.28€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2580 | +0.014 | +17.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2580 | +0.014 | +17.68€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11631 | +0.017 | -20.21€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 11631 | +0.017 | -20.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4827 | +0.021 | +5.29€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4827 | +0.021 | +5.29€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3990 | +0.015 | -12.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3990 | +0.015 | -12.72€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2814 | +0.011 | -12.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2814 | +0.011 | -12.78€ | 1 | 0 |
| ✅ UPDOWN_GBM | 103196 | +0.060 | +9888.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 25122 | +0.080 | +5164.83€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3084 | +0.000 | +33.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 68544 | +0.062 | +4582.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6089 | -0.000 | +111.28€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8501 | +0.105 | +1574.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6630 | +0.091 | +755.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 23531 | +0.057 | +2075.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3355 | +0.080 | +762.00€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 874 | +0.001 | +15.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 16445 | +0.066 | +1218.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2727 | -0.004 | +74.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 130 | -0.061 | +4.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 11218 | +0.080 | +1314.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 9371 | +0.066 | +577.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 24541 | +0.050 | +1714.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5941 | +0.072 | +905.24€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 842 | +0.005 | +16.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 15402 | +0.051 | +759.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2237 | +0.002 | +31.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 119 | -0.103 | +1.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 22021 | +0.040 | +1271.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6674 | +0.032 | +435.11€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 795 | -0.009 | +5.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 13321 | +0.051 | +832.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1125 | +0.002 | +5.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 106 | -0.139 | -7.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 13382 | +0.073 | +1941.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5610 | +0.095 | +1503.85€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7375 | +0.061 | +438.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 355 | -0.099 | -1.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 985 | +0.363 | +356.66€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 985 | +0.363 | +356.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 485 | +0.362 | +169.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 485 | +0.362 | +169.66€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 500 | +0.362 | +187.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 500 | +0.362 | +187.00€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 24752 | -0.021 | +6125.91€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 24752 | -0.021 | +6125.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4606 | -0.114 | +234.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4606 | -0.114 | +234.63€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3238 | +0.219 | +2065.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3238 | +0.219 | +2065.26€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7005 | -0.060 | +1045.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7005 | -0.060 | +1045.63€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6851 | -0.061 | +1319.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6851 | -0.061 | +1319.35€ | 2 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 299 | +0.061 | +23.77€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 299 | +0.061 | +23.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 299 | +0.061 | +23.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 299 | +0.061 | +23.77€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1760 | +0.283 | +1475.06€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1760 | +0.283 | +1475.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 934 | +0.277 | +733.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 934 | +0.277 | +733.65€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 826 | +0.290 | +741.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 826 | +0.290 | +741.40€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 859 | -0.113 | -85.36€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 859 | -0.113 | -85.36€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 270 | -0.081 | -20.33€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 270 | -0.081 | -20.33€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 96 | -0.173 | -11.45€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 96 | -0.173 | -11.45€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 110 | -0.179 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 110 | -0.179 | -4.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4560 | +0.303 | +2099.95€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1730 | +0.260 | +234.76€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1756 | +0.297 | +758.75€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1074 | +0.381 | +1106.43€ | 0 | 1 |