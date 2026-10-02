# Hipótesis automáticas — 2026-10-02 11:04 UTC
_Generado por shadow_postmortem.py sobre 712532 resoluciones (PNL=+85400.55€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.234 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.221 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.8038` → IC=+0.253 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8038 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.403` → IC=+0.190 (n=201)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 9.403 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=637)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3025.1949` → IC=+0.153 (n=402)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3025.1949 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.240 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.147)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.208 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.147)

- **PATRÓN** `banda_hit_calibrado` > `0.802` → IC=+0.262 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.802 (IC base=+0.147)

- **PATRÓN** `banda_z` > `9.998` → IC=+0.212 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.998 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=543)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `6348.9626` → IC=+0.150 (n=161)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6348.9626 (IC base=+0.147)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=106)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=112)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **PATRÓN** `py_entrada` > `0.35` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.35 (IC base=+0.117)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.250 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.117)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `banda_z` > 6.043 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.125 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.175 (n=112)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `1196.2423` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1196.2423 (IC base=+0.117)

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
- **FILTRO** `restante_s_al_confirmar` < `145.08` → IC=-0.219 (n=7969)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.08
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=23907)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `135.36` → IC=-0.257 (n=1041)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.36
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3123)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.23` → IC=-0.311 (n=947)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.23
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=2844)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.29` → IC=-0.212 (n=1972)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.29
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5916)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.69` → IC=-0.327 (n=1539)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.69
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=4618)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.211 (n=15540)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=3769)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `5474.7679` → IC=+0.172 (n=2439)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5474.7679 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=16519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=12644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=6191)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7709.3208` → IC=+0.168 (n=2365)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7709.3208 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `16028.2025` → IC=+0.231 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16028.2025 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.201 (n=1635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2336)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `15980.1695` → IC=+0.209 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15980.1695 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.170 (n=365)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4624.034 (IC base=+0.093)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.096)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.141 (n=898)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.151 (n=230)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.096)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.159 (n=2884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.357 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=1450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.363 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.140 (n=767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.252 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=872)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1322.2406` → IC=+0.148 (n=762)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1322.2406 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.406 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.153 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=796)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.370 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `1192.3838` → IC=+0.154 (n=235)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1192.3838 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.226 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=13489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=12910)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.232 (n=4274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=3196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3035)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3067)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.243 (n=1230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.241 (n=1228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.339 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.238)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=3150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=3010)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=2531)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=2780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.244)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=3073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=2963)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.194 (n=2328)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.195 (n=1119)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.441 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `11570.9911` → IC=+0.461 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11570.9911 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.443 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.444)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.447 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `11081.0568` → IC=+0.463 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11081.0568 (IC base=+0.444)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `3376.5741` → IC=+0.449 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3376.5741 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.417 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.415 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.414)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.414)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.414)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=40163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=17658)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=8154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=5586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=7593)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=3580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.265 (n=4103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7332)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=3618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2628)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=2873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=3077)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=6147)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=5886)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.51` → IC=+0.136 (n=5705)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.51 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=3093)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.139 (n=2924)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=3763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.22` → IC=+0.139 (n=2839)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 3.22 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.183 (n=3054)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.111)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.129 (n=3240)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` > 4.96 (IC base=+0.111)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=2886)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.111)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.290 (n=1248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1551.1157` → IC=+0.296 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1551.1157 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.333 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5199.2442` → IC=+0.304 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5199.2442 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1448.4724` → IC=+0.305 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1448.4724 (IC base=+0.288)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.437 (n=493)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.456 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1965.9066` → IC=+0.458 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.9066 (IC base=+0.441)

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
- **FILTRO** `py_entrada` > `0.72` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.72` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.495` → IC=+0.131 (n=9613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.495 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.244 (n=3206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2216` → IC=+0.259 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2216 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.389` → IC=+0.192 (n=2521)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.389 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.253 (n=2674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.255 (n=2675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.232 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.3213` → IC=+0.222 (n=3033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3213 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.135 (n=11668)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5676 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.5941` → IC=+0.202 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5941 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1554` → IC=+0.176 (n=3857)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1554 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.183 (n=1860)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.697 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.8679` → IC=+0.176 (n=2814)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8679 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.222 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.2708` → IC=+0.196 (n=6351)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2708 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.4458` → IC=+0.198 (n=7218)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4458 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.213 (n=7013)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.207 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.187 (n=717)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0081 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3557` → IC=+0.181 (n=2141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3557 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=1031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.181 (n=1444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 11.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.227` → IC=+0.288 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.227 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.217 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.179 (n=2018)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.193 (n=2187)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.235 (n=1131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.241 (n=1517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.268 (n=747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0604` → IC=+0.286 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0604 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.481` → IC=+0.244 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.481 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.405` → IC=+0.239 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.405 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.231 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.265 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.566` → IC=+0.243 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.566 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=1857)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1579.1972` → IC=+0.245 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1579.1972 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.238 (n=749)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.357` → IC=+0.228 (n=1699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.357 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=1698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8952` → IC=+0.262 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8952 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3479` → IC=+0.222 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3479 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.672` → IC=+0.256 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.672 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2518` → IC=+0.223 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2518 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.225 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.241 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.224 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3817` → IC=+0.240 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3817 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11128.7666` → IC=+0.224 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11128.7666 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=1143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2578` → IC=+0.150 (n=1509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2578 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7169` → IC=+0.170 (n=1714)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7169 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1316` → IC=+0.154 (n=1541)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1316 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.294` → IC=+0.142 (n=272)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 11.294 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.274` → IC=+0.143 (n=1581)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.274 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.148 (n=1714)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2049 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.174 (n=458)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.149 (n=1603)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.144 (n=1069)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `14134.8887` → IC=+0.140 (n=1143)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 14134.8887 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.174 (n=672)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 231.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.203 (n=1924)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=1938)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.317` → IC=+0.258 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.317 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.197 (n=1888)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.205 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.1663` → IC=+0.209 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1663 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=2561)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2007.5584` → IC=+0.198 (n=717)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2007.5584 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.220 (n=1668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.6292` → IC=+0.213 (n=1893)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6292 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0649` → IC=+0.233 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0649 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.68` → IC=+0.234 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.68 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3464` → IC=+0.251 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3464 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7224` → IC=+0.215 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7224 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7427` → IC=+0.217 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7427 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1924.7784` → IC=+0.209 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1924.7784 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.209 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.209)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=118)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=2584)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.133 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0043 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9556` → IC=+0.224 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9556 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1962` → IC=+0.333 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1962 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.861` → IC=+0.173 (n=852)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.861 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.341 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.329 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.360 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1917` → IC=+0.336 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1917 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.331 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1014` → IC=+0.155 (n=676)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1014 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.3334` → IC=+0.197 (n=315)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3334 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.150 (n=696)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8475 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1669` → IC=+0.146 (n=348)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1669 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2837` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2837 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.166 (n=884)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.021)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=391)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.192 (n=115)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=346)

- **FILTRO** `ibs_20min` > `0.24` → IC=-0.127 (n=2596)

  - _Acción_: SKIP cuando `ibs_20min` > 0.24
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=1283)

- **FILTRO** `sigma_ewma_delta_pct` > `8.728` → IC=-0.208 (n=409)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.728
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=3470)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.174 (n=231)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.6364 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.332` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.332 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.278 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4704 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.303 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.24` → IC=+0.131 (n=1283)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.24 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7032` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7032 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4376` → IC=+0.245 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4376 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6807` → IC=+0.268 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6807 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.239 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.38` → IC=+0.288 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.38 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.179 (n=672)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2043)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=639)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2076)

- **FILTRO** `ibs_20min` > `0.7674` → IC=-0.209 (n=1006)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7674
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=3020)

- **PATRÓN** `dist_vwap_pct` > `0.4707` → IC=+0.325 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4707 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.285` → IC=+0.317 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.285 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6271` → IC=+0.314 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6271 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.306 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0704` → IC=+0.304 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0704 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.305 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.8139` → IC=+0.311 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8139 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.8782` → IC=+0.278 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8782 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.7271` → IC=+0.256 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7271 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.270 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.1658` → IC=+0.266 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1658 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.1375` → IC=+0.259 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1375 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.252 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.42 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.202 (n=4152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.4731` → IC=+0.190 (n=11111)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4731 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.7113` → IC=+0.286 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7113 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.160 (n=5699)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `1.1809` → IC=+0.246 (n=4519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1809 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.255 (n=4037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` < `0.0804` → IC=+0.242 (n=6680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0804 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.274 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `1.4638` → IC=+0.243 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4638 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `2.2622` → IC=+0.256 (n=3303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2622 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.278 (n=6815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.101)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.168 (n=4026)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5461` → IC=+0.156 (n=10615)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5461 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7014` → IC=+0.250 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7014 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2474` → IC=+0.248 (n=3481)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2474 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7075` → IC=+0.248 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7075 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1988` → IC=+0.262 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1988 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.303 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5864` → IC=+0.275 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5864 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.279 (n=4871)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2578` → IC=-0.157 (n=861)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2578
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2585)

- **FILTRO** `ibs_20min` > `0.758` → IC=-0.167 (n=704)

  - _Acción_: SKIP cuando `ibs_20min` > 0.758
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2114)

- **FILTRO** `sigma_ewma_delta_pct` > `4.568` → IC=-0.175 (n=638)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.568
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2180)

- **PATRÓN** `ibs_20min` > `0.9032` → IC=+0.278 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9032 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.861` → IC=+0.213 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.861 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2262` → IC=+0.275 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2262 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.203 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.185` → IC=+0.234 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.185 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.221 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.440 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1478` → IC=+0.447 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1478 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.453 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.467 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.166 (n=834)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8641 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.3014` → IC=+0.197 (n=453)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3014 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.178 (n=1038)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6754 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.229 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.202 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4058` → IC=+0.183 (n=380)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.4058 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.220 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 233.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1524` → IC=+0.226 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1524 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6178` → IC=+0.228 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6178 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0717` → IC=+0.221 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0717 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2665` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2665 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5537` → IC=+0.224 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5537 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.236 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `458.0` → IC=+0.221 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 458.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.288 (n=1268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.259 (n=1908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.256 (n=1268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.725` → IC=+0.281 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.725 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.269 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.1834` → IC=+0.268 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1834 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.265 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1998.2464` → IC=+0.278 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1998.2464 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.318 (n=712)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1847` → IC=+0.296 (n=691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1847 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.321 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.293 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.685` → IC=+0.291 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.685 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.119` → IC=+0.292 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.119 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.57` → IC=+0.302 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.57 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.290 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1917.241` → IC=+0.304 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.241 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.290 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7729` → IC=-0.190 (n=718)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7729
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=2155)

- **PATRÓN** `ibs_20min` > `0.905` → IC=+0.184 (n=641)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.905 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1818` → IC=+0.237 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1818 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.0067` → IC=+0.252 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0067 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0813` → IC=+0.261 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0813 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4046` → IC=+0.274 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4046 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.262 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.228 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1412 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1801` → IC=+0.216 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1801 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.234 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.263 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8106 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.258 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 134.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7568` → IC=-0.185 (n=1314)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7568
  - _Potencial_: sin este filtro IC_bueno=+0.285 (n=1318)

- **FILTRO** `ibs_20min` > `0.6744` → IC=-0.241 (n=659)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6744
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=1979)

- **FILTRO** `sigma_ewma_delta_pct` > `4.76` → IC=-0.194 (n=566)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.76
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=2072)

- **PATRÓN** `ibs_20min` > `0.7568` → IC=+0.285 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7568 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.320 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.169 (n=418)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.310 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.304 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.301 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.298 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.325 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.326 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.131 (n=1747)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.4662` → IC=+0.234 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4662 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.261 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1866` → IC=+0.222 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1866 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.227 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.245 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.245 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.4337` → IC=+0.225 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4337 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.256 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.020)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.328 (n=1395)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.303 (n=736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.315 (n=1560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6429 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2152` → IC=+0.317 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2152 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.755` → IC=+0.309 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.755 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.297 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.333 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.295 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2469.502` → IC=+0.295 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2469.502 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.323 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.313 (n=1102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.1973` → IC=+0.288 (n=728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1973 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.286 (n=1574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.307 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.3215` → IC=+0.295 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3215 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.513` → IC=+0.298 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.513 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` < `0.642` → IC=+0.285 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.642 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` > `1.2368` → IC=+0.316 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2368 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.339 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.291 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.278 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2422.6754` → IC=+0.286 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2422.6754 (IC base=+0.282)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=3132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0049 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.208 (n=3131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3649` → IC=+0.180 (n=8258)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3649 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=9778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.226 (n=9389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1754` → IC=+0.198 (n=4059)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1754 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.392` → IC=+0.256 (n=1898)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.392 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2094` → IC=+0.166 (n=6251)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2094 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.162 (n=6254)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6297 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.202 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5993` → IC=+0.180 (n=3011)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5993 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1967.22` → IC=+0.175 (n=8384)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1967.22 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.187 (n=8307)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 108.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.187 (n=5995)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0819` → IC=+0.215 (n=2997)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0819 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=3436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4865` → IC=+0.228 (n=8988)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4865 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.1746` → IC=+0.166 (n=6272)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1746 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.307` → IC=+0.196 (n=1510)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.307 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1764` → IC=+0.158 (n=6455)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1764 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.214 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5531` → IC=+0.171 (n=3650)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5531 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.5884` → IC=+0.172 (n=2765)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5884 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.179 (n=7950)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 108.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.232 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.208 (n=525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.3446` → IC=+0.216 (n=1570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3446 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1061)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.9093` → IC=+0.284 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9093 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.239` → IC=+0.333 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.239 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.247 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.194 (n=1464)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.210 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.248 (n=1054)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.250 (n=1067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1838` → IC=+0.286 (n=796)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1838 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.3514` → IC=+0.260 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3514 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.215` → IC=+0.243 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.215 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.262 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4169` → IC=+0.264 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4169 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1576.15` → IC=+0.256 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.15 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.233 (n=474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0719` → IC=+0.193 (n=471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0719 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=1491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3916` → IC=+0.223 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3916 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.2039` → IC=+0.208 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2039 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.230 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.174 (n=623)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6892 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.0753` → IC=+0.159 (n=641)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0753 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.202 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.5031` → IC=+0.180 (n=605)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5031 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.4724` → IC=+0.161 (n=458)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4724 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `11954.6752` → IC=+0.163 (n=1262)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11954.6752 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.167 (n=587)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 234.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.2943` → IC=+0.166 (n=1492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2943 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.5844` → IC=+0.193 (n=1492)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5844 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1357` → IC=+0.167 (n=1474)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1357 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.199 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2126` → IC=+0.159 (n=1492)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2126 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.149 (n=454)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4507` → IC=+0.148 (n=1381)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4507 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.177 (n=434)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 208.0 (IC base=+0.140)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.230 (n=523)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2519` → IC=+0.221 (n=1044)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2519 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.441` → IC=+0.278 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.441 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2004` → IC=+0.213 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2004 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.217 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `1999.301` → IC=+0.220 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.301 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.234 (n=1180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1439` → IC=+0.253 (n=590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1439 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.3521` → IC=+0.244 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3521 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.647` → IC=+0.248 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.647 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3508` → IC=+0.252 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3508 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7349` → IC=+0.233 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7349 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.1556` → IC=+0.222 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1556 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.209 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.182 (n=1334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0065 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4277` → IC=+0.163 (n=1512)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4277 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=1575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3498` → IC=+0.204 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3498 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1478` → IC=+0.184 (n=985)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1478 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.946` → IC=+0.228 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.946 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.163 (n=1008)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8561 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.195 (n=231)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4299` → IC=+0.159 (n=494)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4299 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.165 (n=493)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5174.4297` → IC=+0.194 (n=1008)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 5174.4297 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.154 (n=1453)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 155.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.156 (n=1579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3879` → IC=+0.146 (n=1579)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3879 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.66` → IC=+0.175 (n=1579)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.66 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1551` → IC=+0.141 (n=1548)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1551 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.878` → IC=+0.164 (n=549)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.878 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.149 (n=1053)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8556 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.178 (n=234)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.137 (n=970)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.7994 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.5121` → IC=+0.131 (n=486)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5121 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9224.5065` → IC=+0.164 (n=716)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 9224.5065 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.125 (n=1227)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 127.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.165 (n=775)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0101 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.210 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0784` → IC=+0.216 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0784 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.853` → IC=+0.260 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.853 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.134 (n=1710)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2145 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6461` → IC=+0.130 (n=1710)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6461 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1613` → IC=+0.129 (n=1719)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1613 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.0708` → IC=+0.127 (n=709)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0708 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.534` → IC=+0.141 (n=727)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.534 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=1790)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2883.9504` → IC=+0.204 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2883.9504 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.142 (n=1344)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 47.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=760)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1069` → IC=+0.168 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1069 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.217 (n=1729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5778 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.9997` → IC=+0.123 (n=234)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.9997 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.148 (n=1596)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2029 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.583` → IC=+0.133 (n=358)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 7.583 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6379` → IC=+0.150 (n=576)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6379 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2259` → IC=+0.159 (n=303)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2259 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.142 (n=526)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4113` → IC=+0.129 (n=526)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.4113 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2744.0462` → IC=+0.181 (n=784)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2744.0462 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.127 (n=1524)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.229 (n=1448)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.183` → IC=+0.210 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.183 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.246 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.214 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.247 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.1976` → IC=+0.210 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1976 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.217 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6287 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.274 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.4642` → IC=+0.211 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4642 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.215 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2844.5756` → IC=+0.209 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2844.5756 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.225 (n=729)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.214 (n=1105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.232 (n=554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.242 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `1.2049` → IC=+0.228 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2049 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.425` → IC=+0.247 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.425 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.703` → IC=+0.220 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.703 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.281 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.1883` → IC=+0.202 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1883 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.207 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2393.5592` → IC=+0.215 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2393.5592 (IC base=+0.210)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.191 (n=822)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0037 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.178 (n=821)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0085 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3484` → IC=+0.176 (n=2168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3484 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5066` → IC=+0.203 (n=2201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5066 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.7962` → IC=+0.188 (n=402)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7962 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.714` → IC=+0.195 (n=1082)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.714 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.188 (n=1458)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8725 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.2088` → IC=+0.178 (n=729)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2088 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.181 (n=895)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.177 (n=796)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.8174` → IC=+0.172 (n=1591)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8174 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2787)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2665.5936` → IC=+0.171 (n=2201)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2665.5936 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.184 (n=2242)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 142.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.141 (n=1693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0056 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=2385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.0657` → IC=+0.191 (n=846)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0657 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.6979` → IC=+0.122 (n=1004)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.6979 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.126 (n=621)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.4406` → IC=+0.141 (n=819)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4406 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2753.0147` → IC=+0.122 (n=2265)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2753.0147 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.133 (n=1052)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 27.0 (IC base=+0.108)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.175 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0029 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3325` → IC=+0.161 (n=643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3325 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.6458` → IC=+0.208 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6458 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.165 (n=228)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1241` → IC=+0.142 (n=521)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1241 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.243` → IC=+0.164 (n=284)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.243 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.859` → IC=+0.142 (n=672)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.859 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8974` → IC=+0.173 (n=429)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8974 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.1548` → IC=+0.145 (n=668)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1548 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.0915` → IC=+0.158 (n=226)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0915 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.2005` → IC=+0.155 (n=551)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.2005 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.395` → IC=+0.148 (n=626)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.395 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=832)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `10893.4165` → IC=+0.154 (n=643)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10893.4165 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.189 (n=271)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 155.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.209 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3426` → IC=+0.158 (n=793)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3426 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.177 (n=697)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6119 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1813` → IC=+0.154 (n=779)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1813 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.279` → IC=+0.139 (n=300)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 4.279 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.088` → IC=+0.142 (n=725)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.088 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2204` → IC=+0.145 (n=793)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2204 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.6958` → IC=+0.151 (n=708)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6958 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.200 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1115` → IC=+0.157 (n=689)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1115 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4081` → IC=+0.146 (n=783)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4081 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `12002.2202` → IC=+0.139 (n=708)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 12002.2202 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `357.0` → IC=+0.150 (n=760)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 357.0 (IC base=+0.138)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.253 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.4096` → IC=+0.222 (n=772)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4096 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.3755` → IC=+0.244 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3755 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1485` → IC=+0.219 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1485 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.2194` → IC=+0.213 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2194 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.007` → IC=+0.234 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.007 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.220 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.1791` → IC=+0.237 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1791 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.254 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4109` → IC=+0.238 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4109 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.4379` → IC=+0.246 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4379 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.0873 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.6865` → IC=+0.144 (n=318)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6865 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `8022.2855` → IC=+0.132 (n=482)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8022.2855 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.164 (n=522)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0059 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.193 (n=585)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5882 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.9831` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9831 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.200 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.163 (n=515)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0699 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6475` → IC=+0.152 (n=585)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6475 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1714` → IC=+0.165 (n=162)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1714 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.1991` → IC=+0.165 (n=255)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.1991 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=618)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3094.7708` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3094.7708 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.4571` → IC=+0.159 (n=490)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4571 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.8255` → IC=+0.127 (n=352)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8255 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `2481.4994` → IC=+0.133 (n=371)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2481.4994 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.126 (n=500)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 41.0 (IC base=+0.073)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.172 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0238 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.190 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0069 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2425` → IC=+0.177 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2425 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.206 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.188 (n=187)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.2434` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2434 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `1.103` → IC=+0.164 (n=209)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 1.103 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.737` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.737 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.6829` → IC=+0.180 (n=167)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6829 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2526` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2526 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4437` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4437 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.6057` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.6057 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=191)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=125)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.153)

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
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.211 (n=4050)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=12677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.4607` → IC=+0.223 (n=12136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4607 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.9134` → IC=+0.201 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9134 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.367` → IC=+0.249 (n=3011)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.367 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.8809` → IC=+0.171 (n=5431)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8809 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.203 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.5752` → IC=+0.197 (n=3907)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5752 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1799.976` → IC=+0.179 (n=12135)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1799.976 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.202 (n=9488)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.193 (n=7295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0071 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1516` → IC=+0.191 (n=4809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1516 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4523` → IC=+0.245 (n=9617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4523 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2499` → IC=+0.162 (n=6803)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2499 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.045` → IC=+0.201 (n=1538)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.045 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.183 (n=10563)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.6337` → IC=+0.162 (n=2477)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6337 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2878` → IC=+0.241 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2878 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.5896` → IC=+0.191 (n=3387)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5896 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.202 (n=6598)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.232 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.230 (n=675)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.3617` → IC=+0.207 (n=2011)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3617 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.359 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.260 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.2352` → IC=+0.213 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2352 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2031.32` → IC=+0.207 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.32 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.223 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.262 (n=1097)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.261 (n=1647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.126` → IC=+0.281 (n=724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.126 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3614` → IC=+0.284 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3614 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.511` → IC=+0.261 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.511 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.291 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.5466` → IC=+0.259 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5466 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6054` → IC=+0.275 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6054 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1578.8947` → IC=+0.267 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1578.8947 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.205 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1128` → IC=+0.159 (n=862)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1128 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2907` → IC=+0.204 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2907 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.333` → IC=+0.191 (n=784)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.333 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.177 (n=428)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.167` → IC=+0.152 (n=1786)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.167 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6272` → IC=+0.176 (n=652)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6272 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.073` → IC=+0.154 (n=1729)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.073 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.192 (n=280)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1192` → IC=+0.161 (n=1671)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1192 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `11407.4678` → IC=+0.156 (n=1747)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 11407.4678 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.173 (n=815)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 278.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1640)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.33` → IC=+0.161 (n=1640)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.33 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.2923` → IC=+0.236 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2923 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.648` → IC=+0.150 (n=264)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.648 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.164 (n=1490)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.157 (n=275)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.285` → IC=+0.148 (n=1495)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.285 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.160 (n=1640)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1954 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.196 (n=439)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.408` → IC=+0.155 (n=1541)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.408 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.159 (n=1027)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `259.0` → IC=+0.159 (n=482)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 259.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.260 (n=661)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2077)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.226 (n=2008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.366` → IC=+0.301 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.366 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2061` → IC=+0.224 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2061 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7731` → IC=+0.233 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7731 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2008.6449` → IC=+0.239 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.6449 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.241 (n=1633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.6153` → IC=+0.235 (n=1856)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6153 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.0159` → IC=+0.302 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0159 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.157` → IC=+0.276 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.157 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3404` → IC=+0.294 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3404 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7265` → IC=+0.236 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7265 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.147` → IC=+0.236 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.147 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1991.0984` → IC=+0.242 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.0984 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.231 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.231)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.193 (n=694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.436` → IC=+0.151 (n=2080)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.436 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2739` → IC=+0.189 (n=2080)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2739 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3629` → IC=+0.163 (n=810)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3629 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.555` → IC=+0.168 (n=335)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.555 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.163 (n=1388)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8725 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.206 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5213` → IC=+0.155 (n=890)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5213 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.156 (n=917)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7595.287` → IC=+0.235 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7595.287 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.170 (n=656)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 72.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.169 (n=1115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0052 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.36` → IC=+0.139 (n=1470)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.36 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.594` → IC=+0.196 (n=1470)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.594 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1561` → IC=+0.131 (n=1462)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1561 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.265` → IC=+0.161 (n=249)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.265 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8727` → IC=+0.137 (n=1114)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8727 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.214 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.141 (n=1596)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `9467.2986` → IC=+0.203 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9467.2986 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.150 (n=1382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0082 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.5812` → IC=+0.127 (n=2069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.5812 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.463` → IC=+0.201 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.463 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0629` → IC=+0.210 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0629 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.567` → IC=+0.242 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.567 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8911` → IC=+0.145 (n=1380)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8911 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1608` → IC=+0.127 (n=2129)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1608 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8299` → IC=+0.124 (n=1342)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.8299 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.4546` → IC=+0.127 (n=2014)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4546 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=2106)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2884.9328` → IC=+0.253 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2884.9328 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.142 (n=1648)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 52.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.180 (n=658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0058 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1375` → IC=+0.157 (n=659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1375 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.207 (n=1977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.136 (n=1637)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.463` → IC=+0.127 (n=1899)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.463 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.645` → IC=+0.162 (n=658)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.645 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2197` → IC=+0.182 (n=309)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2197 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `2.1505` → IC=+0.131 (n=1591)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.1505 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2799.1755` → IC=+0.186 (n=658)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2799.1755 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.131 (n=1601)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.232 (n=1824)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.218 (n=1362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.601` → IC=+0.263 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.601 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.2177` → IC=+0.235 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2177 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.596` → IC=+0.259 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.596 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.0607` → IC=+0.216 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0607 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.222 (n=2042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2856` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2856 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.4788` → IC=+0.238 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4788 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1988)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2626.1883` → IC=+0.221 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2626.1883 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.217 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.231 (n=716)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.223 (n=1508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.4214` → IC=+0.260 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4214 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `1.2224` → IC=+0.219 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2224 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2201` → IC=+0.214 (n=1896)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2201 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.255 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.238 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.279 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `2.1658` → IC=+0.203 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1658 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4276` → IC=+0.207 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4276 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2407.4896` → IC=+0.211 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.4896 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.200 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.209)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=3680)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.219 (n=1220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.5106` → IC=+0.191 (n=3647)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5106 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=1365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=1669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.239 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1738` → IC=+0.190 (n=1347)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1738 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.4517` → IC=+0.179 (n=2391)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.4517 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.206` → IC=+0.212 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.206 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7103` → IC=+0.186 (n=1100)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7103 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.184 (n=1667)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8944 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1682` → IC=+0.208 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1682 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.189 (n=1201)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8592` → IC=+0.186 (n=2400)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8592 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2712)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2520.4396` → IC=+0.186 (n=3647)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2520.4396 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.217 (n=925)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.182 (n=2439)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.1825` → IC=+0.186 (n=1220)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1825 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6653` → IC=+0.181 (n=516)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6653 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` < `0.2399` → IC=+0.153 (n=2461)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2399 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.170 (n=2766)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2566` → IC=+0.166 (n=2608)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2566 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.167 (n=2534)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.168 (n=1204)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8235` → IC=+0.170 (n=1824)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8235 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=3680)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `5320.6072` → IC=+0.166 (n=2476)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5320.6072 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.167 (n=1800)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 85.0 (IC base=+0.161)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.229 (n=441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.265 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.5157` → IC=+0.227 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5157 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.761` → IC=+0.209 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.761 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.329` → IC=+0.211 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.329 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.976` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.976 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.206 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.210 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.837` → IC=+0.226 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.837 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.224 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `12593.964` → IC=+0.236 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12593.964 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.224 (n=461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.162 (n=1045)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.184 (n=460)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1435 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.153 (n=474)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6084 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6676` → IC=+0.193 (n=99)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6676 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.2156` → IC=+0.150 (n=1061)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2156 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.377` → IC=+0.168 (n=1028)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.377 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.190 (n=697)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8812 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.169 (n=479)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.5318` → IC=+0.156 (n=1042)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5318 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8167` → IC=+0.164 (n=694)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8167 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `12148.8643` → IC=+0.159 (n=934)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12148.8643 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.158 (n=1001)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 699.0 (IC base=+0.148)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.214 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1529` → IC=+0.203 (n=514)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1529 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.201 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5305 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.193 (n=389)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8854 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.198 (n=978)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.171` → IC=+0.197 (n=1050)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 4.171 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `1.0854` → IC=+0.193 (n=1027)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.0854 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.2477` → IC=+0.193 (n=389)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.2477 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.190 (n=1073)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.200 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.196 (n=1144)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=1173)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.223 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3844` → IC=+0.197 (n=830)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3844 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.176 (n=633)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 10.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.7538` → IC=+0.170 (n=943)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7538 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.0908` → IC=+0.171 (n=943)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0908 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.6069` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6069 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.718` → IC=+0.169 (n=965)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.718 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6432` → IC=+0.203 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6432 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.7257` → IC=+0.165 (n=843)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7257 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.183 (n=399)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.180 (n=814)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.7855` → IC=+0.167 (n=616)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7855 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `7440.1914` → IC=+0.178 (n=943)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7440.1914 (IC base=+0.165)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.168 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.011 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.171 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 3.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.144 (n=372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 14.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.9326` → IC=+0.244 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9326 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2317` → IC=+0.195 (n=244)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2317 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.224 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.7119` → IC=+0.195 (n=162)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.7119 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.282` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.282 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.4173` → IC=+0.203 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4173 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=433)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2978.1742` → IC=+0.169 (n=366)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2978.1742 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.165 (n=305)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 51.0 (IC base=+0.143)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.165 (n=506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0039 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.6459` → IC=+0.181 (n=945)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6459 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.147 (n=573)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.429` → IC=+0.196 (n=248)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.429 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.190 (n=143)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.081)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.120 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0045 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.0406` → IC=+0.300 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0406 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` < `0.1922` → IC=+0.134 (n=449)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1922 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.074` → IC=+0.144 (n=338)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.074 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.180 (n=148)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.145 (n=345)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.139 (n=308)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4436 (IC base=+0.044)

- **PATRÓN** `libro_liquidez` > `3310.3815` → IC=+0.135 (n=165)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3310.3815 (IC base=+0.044)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.137 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0058 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4301` → IC=+0.167 (n=364)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.4301 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.162 (n=193)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `2.0809` → IC=+0.136 (n=284)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.0809 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.131 (n=215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0052 (IC base=+0.087)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.198 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.2737` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2737 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.0689` → IC=+0.141 (n=193)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0689 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.069` → IC=+0.183 (n=184)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 7.069 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `1.1635` → IC=+0.137 (n=191)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1635 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6903` → IC=+0.136 (n=171)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6903 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.0669` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0669 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.167 (n=169)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4035 (IC base=+0.087)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.7019` → IC=-0.126 (n=153)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7019
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=311)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=157)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.138 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0049 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.7019` → IC=+0.219 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7019 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.3353` → IC=+0.196 (n=136)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3353 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.652` → IC=+0.284 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.652 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.8058` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8058 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.7617` → IC=+0.153 (n=197)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7617 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.154 (n=307)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.1322` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1322 (IC base=+0.005)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0118` → IC=-0.262 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0118
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=123)

- **FILTRO** `ibs_20min` > `0.15` → IC=-0.291 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=81)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.125 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0063 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.178 (n=231)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7778 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.064` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.064 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.056)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.136 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0092 (IC base=+0.015)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.015)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4436 (IC base=+0.015)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=181)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=224)

- **FILTRO** `volumen_regimen` < `0.7307` → IC=-0.352 (n=59)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7307
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=180)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.368 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=129)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=174)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=165)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=90)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `sigma_ewma_delta_pct` > `2.55` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.55
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=52)

- **FILTRO** `volumen_regimen` > `0.8664` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8664
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=62)

- **FILTRO** `libro_liquidez` < `3685.6992` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3685.6992
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5843` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5843
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `volumen_regimen` < `0.6765` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6765
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=59)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.395 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=53)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=50)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=47)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.188)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=65)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `volumen_spike_ratio` < `1.6212` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6212
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=38)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.184 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0059 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6645` → IC=+0.151 (n=330)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6645 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.4944` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.4944 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.123 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0051 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.189 (n=297)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.156 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.173` → IC=+0.188 (n=136)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 6.173 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `2.627` → IC=+0.144 (n=262)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.627 (IC base=+0.090)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=284)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `4049.9464` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4049.9464 (IC base=+0.090)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6292` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6292
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=100)

- **FILTRO** `volumen_regimen` < `0.7777` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7777
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=100)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.189 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0033 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.237 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.226 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1524 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.1046` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1046 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.62` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 6.62 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.1483` → IC=+0.173 (n=151)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.1483 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `0.8617` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.8617 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` < `0.1954` → IC=+0.233 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1954 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `2.5919` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5919 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.4576` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4576 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `4542.5709` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 4542.5709 (IC base=+0.160)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1682` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1682
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=86)

- **FILTRO** `libro_liquidez` < `1549.4073` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 1549.4073
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=95)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.198 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0027 (IC base=+0.074)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.134 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 13.0 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.3115` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.3115 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.734` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.734 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.8247` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.8247 (IC base=+0.074)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=67)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.318 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.265 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.248 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.265 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9714 (IC base=+0.242)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.243 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7692 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.768` → IC=+0.284 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.768 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `592.1486` → IC=+0.252 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 592.1486 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.044)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4923` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4923 (IC base=+0.278)

- **PATRÓN** `elapsed_s` > `210.3` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.3 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.8301` → IC=+0.360 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8301 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.278)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.217)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.217)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.312 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `1457.0` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1457.0 (IC base=+0.217)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4923` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4923 (IC base=+0.278)

- **PATRÓN** `elapsed_s` > `210.3` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.3 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.8301` → IC=+0.360 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8301 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.278)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.217)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.217)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.312 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `1457.0` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1457.0 (IC base=+0.217)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.124 (n=1065)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.495 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2928.7604` → IC=+0.163 (n=304)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2928.7604 (IC base=+0.113)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.124 (n=1065)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.495 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2928.7604` → IC=+0.163 (n=304)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2928.7604 (IC base=+0.113)

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
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=230)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=216)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=95)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2378)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=827)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.034)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=95)

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

- **PATRÓN** `liq_usd_total` > `134844.05` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `liq_usd_total` > 134844.05 (IC base=+0.057)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.173 (n=151)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.495 (IC base=+0.057)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=961)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=915)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=554)

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
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=257)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.495 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `3872.1814` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3872.1814 (IC base=+0.035)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=729)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=729)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=459)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=459)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=199)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=199)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=113)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=135)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=236)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=108)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=121)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=279)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=279)

- **FILTRO** `libro_liquidez` < `466.8293` → IC=-0.133 (n=77)

  - _Acción_: SKIP cuando `libro_liquidez` < 466.8293
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=232)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=166)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=982)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=984)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.136 (n=86)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=97)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.157 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=175)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=-0.019)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.48 (IC base=+0.006)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.47` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.47 (IC base=+0.038)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=108)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=89)

- **FILTRO** `profundidad_ratio` < `29.8` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `profundidad_ratio` < 29.8
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.150 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 9.0 (IC base=+0.091)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.123 (n=120)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=42)

- **FILTRO** `profundidad_ratio` < `51.8` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `profundidad_ratio` < 51.8
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=109)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=147)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.53 (IC base=-0.043)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.171 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=78)

- **FILTRO** `restante_min` < `3.44` → IC=-0.267 (n=71)

  - _Acción_: SKIP cuando `restante_min` < 3.44
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=145)

- **FILTRO** `lag_apertura_s` > `91.82` → IC=-0.260 (n=73)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.82
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=143)

- **FILTRO** `profundidad_ratio` < `79.7` → IC=-0.154 (n=108)

  - _Acción_: SKIP cuando `profundidad_ratio` < 79.7
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=108)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.153 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=78)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` > 0.5 (IC base=-0.045)

- **PATRÓN** `profundidad_ratio` > `14.4` → IC=+0.125 (n=54)

  - _Acción_: Kelly boost +0.62€ cuando `profundidad_ratio` > 14.4 (IC base=+0.019)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=198)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.165 (n=4289)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=12944)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.166 (n=4299)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13486)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.198 (n=754)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2280)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.153 (n=756)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2429)

- **PATRÓN** `libro_liquidez` > `1796.98` → IC=+0.128 (n=1032)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1796.98 (IC base=+0.032)

- **PATRÓN** `libro_liquidez` > `1567.2992` → IC=+0.143 (n=1083)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1567.2992 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.179 (n=750)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2338)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=754)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2467)

- **PATRÓN** `libro_liquidez` > `1793.2556` → IC=+0.128 (n=1050)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1793.2556 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.165 (n=739)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=2289)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2385)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3125)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

- **FILTRO** `libro_liquidez` < `17081.1281` → IC=-0.143 (n=233)

  - _Acción_: SKIP cuando `libro_liquidez` < 17081.1281
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=700)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=270)

- **FILTRO** `ibs_20min` > `0.981` → IC=-0.211 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` > 0.981
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=268)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1922.3295` → IC=-0.176 (n=322)

  - _Acción_: SKIP cuando `libro_liquidez` < 1922.3295
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=655)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=12116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=26786)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=9089)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=29813)

- **FILTRO** `ibs_7min` < `0.2645` → IC=-0.234 (n=9725)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2645
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=29177)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12842)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=26060)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=12032)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=37216)

- **FILTRO** `ibs_7min` > `0.2909` → IC=-0.181 (n=12304)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2909
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=36944)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=1963)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4594)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.234 (n=3235)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=3322)

- **FILTRO** `ibs_7min` < `0.7075` → IC=-0.251 (n=2163)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7075
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=4394)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.181 (n=1514)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5043)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.262 (n=2097)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6408)

- **FILTRO** `ibs_7min` > `0.7895` → IC=-0.210 (n=2126)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7895
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6379)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.135 (n=1593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5074)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.248 (n=1631)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5036)

- **FILTRO** `ibs_7min` < `0.7437` → IC=-0.195 (n=1666)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7437
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5001)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.179 (n=1660)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5007)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.266 (n=1581)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5196)

- **FILTRO** `ibs_7min` > `0.2622` → IC=-0.187 (n=1694)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2622
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5083)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.186 (n=1686)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5091)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.160 (n=1782)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=4469)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1479)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4772)

- **FILTRO** `ibs_7min` < `0.7034` → IC=-0.248 (n=2059)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7034
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4192)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.212 (n=1479)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4772)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=2083)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7001)

- **FILTRO** `ibs_7min` > `0.7433` → IC=-0.177 (n=2270)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7433
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=6814)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1900)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4512)

- **FILTRO** `ibs_7min` < `0.7394` → IC=-0.187 (n=1603)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7394
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4809)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.174 (n=1575)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4837)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1629)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4936)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.180 (n=1640)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4925)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.180 (n=1634)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4931)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1628)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=5005)

- **FILTRO** `ibs_7min` < `0.2549` → IC=-0.230 (n=1658)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2549
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4975)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.183 (n=2232)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7185)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.272 (n=1499)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=4883)

- **FILTRO** `ibs_7min` < `0.2679` → IC=-0.224 (n=1594)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2679
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4788)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1476)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4906)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=2087)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6813)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1190)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=588)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7904.1448` → IC=-0.131 (n=345)

  - _Acción_: SKIP cuando `libro_liquidez` < 7904.1448
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=701)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=333)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.150 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=477)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4167` → IC=+0.147 (n=578)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4167 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.117)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.153 (n=289)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 445.688 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.123 (n=736)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 54.0 (IC base=+0.117)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.162 (n=69)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `421.686` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 421.686 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2584.1425` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.1425 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 13.0 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 11.0 (IC base=+0.108)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4137` → IC=+0.186 (n=119)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.4137 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.108)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `7354.4583` → IC=+0.123 (n=160)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 7354.4583 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 73.0 (IC base=+0.108)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.165 (n=150)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.179 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.154 (n=151)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 8043.774 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3077.3625` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3077.3625 (IC base=+0.129)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.122 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 15.0 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.097)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=113)

- **FILTRO** `sigma_h` > `0.0055` → IC=-0.275 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=239)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `95.0392` → IC=-0.419 (n=35)

  - _Acción_: SKIP cuando `T_h` > 95.0392
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.097)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.227 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=44)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.181 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=112)

- **FILTRO** `pct_vs_K` |x|> `3.1007` → IC=-0.425 (n=131)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1007
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=257)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `68.7654` → IC=-0.150 (n=115)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.375 (n=38)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=116)

- **FILTRO** `T_h` > `143.9199` → IC=-0.296 (n=47)

  - _Acción_: SKIP cuando `T_h` > 143.9199
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=94)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=94)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9851` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=95)

- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.403 (n=29)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=95)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.339 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=90)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.339 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=90)

- **FILTRO** `T_h` > `57.801` → IC=-0.340 (n=79)

  - _Acción_: SKIP cuando `T_h` > 57.801
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.155 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=83)

- **FILTRO** `T_h` > `135.1308` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=83)

- **FILTRO** `pct_vs_K` |x|> `4.7` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.7
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=83)

- **FILTRO** `sigma_h` > `0.0081` → IC=-0.365 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=26)

- **FILTRO** `T_h` > `52.8235` → IC=-0.379 (n=56)

  - _Acción_: SKIP cuando `T_h` > 52.8235
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0286` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.0286 (IC base=-0.062)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.354)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.389 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.387 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.354)

- **PATRÓN** `T_h` < `0.6188` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6188 (IC base=+0.354)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.354)

- **PATRÓN** `dist_50` > `0.4067` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4067 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.379 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.354)

- **PATRÓN** `edge` > `0.097` → IC=+0.453 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.420)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.433 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.448 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.420)

- **PATRÓN** `T_h` < `0.608` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.420)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.4077` → IC=+0.482 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4077 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.420)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1072` → IC=+0.450 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.419)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.406 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.455 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.8618` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8618 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.4166` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4166 (IC base=+0.419)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.434)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.469 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.434)

- **PATRÓN** `T_h` > `0.8294` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8294 (IC base=+0.434)

- **PATRÓN** `dist_50` > `0.3691` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3691 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `edge` > `0.1155` → IC=+0.471 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.487 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.463)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.465 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.491 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.468 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=229)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=325)

- **PATRÓN** `streak_estiramiento` < `0.4493` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.4493 (IC base=+0.034)

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
- **FILTRO** `py_entrada` < `0.505` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

- **FILTRO** `streak_estiramiento` > `0.4382` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4382
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=40)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_racha` < 991078.0 (IC base=-0.015)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.4382 (IC base=-0.015)

- **PATRÓN** `streak_estiramiento` < `0.4967` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `streak_estiramiento` < 0.4967 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 48.0 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `2479.8468` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2479.8468 (IC base=+0.063)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=500)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=729)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=870)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=859)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3259)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1673)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.236 (n=923)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.204 (n=1791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.199)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2194` → IC=+0.209 (n=678)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2194 (IC base=+0.199)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1283` → IC=+0.239 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1283 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.208 (n=1890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=2104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_15` > `0.6176` → IC=+0.277 (n=2035)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6176 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.198 (n=1019)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.77` → IC=+0.291 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.77 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2957.795` → IC=+0.205 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2957.795 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.219 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.199)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=866)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.226 (n=439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.285 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2017` → IC=+0.246 (n=199)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2017 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3979` → IC=+0.242 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3979 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.273 (n=439)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.3854` → IC=+0.269 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3854 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.395` → IC=+0.263 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.395 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.252 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.212)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.296` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.296
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=523)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.167 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0036 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.150 (n=312)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.005 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.159 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2356` → IC=+0.177 (n=156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2356 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1217` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1217 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.146 (n=489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.6602` → IC=+0.265 (n=419)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6602 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.2869` → IC=+0.151 (n=433)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2869 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.232 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3403.8093` → IC=+0.156 (n=419)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3403.8093 (IC base=+0.142)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.298 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.225 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0615` → IC=+0.204 (n=245)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0615 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3271` → IC=+0.240 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3271 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.201 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.281 (n=245)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5926 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.208 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.191 (n=241)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.128` → IC=+0.406 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.128 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=267)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3083.8765` → IC=+0.288 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3083.8765 (IC base=+0.192)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.191` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.191 (IC base=-0.011)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.283 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.226 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0641` → IC=+0.205 (n=463)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0641 (IC base=+0.205)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0848` → IC=+0.269 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0848 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.233 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.5758` → IC=+0.290 (n=518)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5758 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3602` → IC=+0.221 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3602 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.5623` → IC=+0.205 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5623 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.241` → IC=+0.252 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.241 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2925.3906` → IC=+0.294 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2925.3906 (IC base=+0.205)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.358 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.356)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.383 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.356)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.358 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.356)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.379 (n=321)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.356)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.393 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.356)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.374 (n=489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.356)

- **PATRÓN** `ibs_15` > `0.7863` → IC=+0.393 (n=482)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7863 (IC base=+0.356)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.391 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.356)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.364 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.356)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.355 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.356)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.360 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.356)

- **PATRÓN** `libro_liquidez` > `3823.0046` → IC=+0.373 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3823.0046 (IC base=+0.356)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.376 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 446.0 (IC base=+0.356)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.368 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.378 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.379 (n=89)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.4202` → IC=+0.374 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4202 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.373 (n=265)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.394 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.384 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.391 (n=264)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.401 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.106` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.106 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.363 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `502.0` → IC=+0.411 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 502.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.346)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.358 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.346)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.368 (n=195)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.346)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.376 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.346)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.406 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.346)

- **PATRÓN** `ibs_15` > `0.743` → IC=+0.396 (n=218)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.743 (IC base=+0.346)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.382 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.346)

- **PATRÓN** `dist_vwap_pct` < `0.2994` → IC=+0.345 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2994 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.347 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.346)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.353 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `4305.62` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4305.62 (IC base=+0.346)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.225 (n=779)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=2341)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.205 (n=1104)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2016)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1355` → IC=+0.247 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1355 (IC base=-0.064)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.273 (n=757)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.2663` → IC=+0.196 (n=617)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2663 (IC base=-0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1238` → IC=+0.251 (n=1549)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1238 (IC base=-0.023)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1802` → IC=+0.251 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1802 (IC base=-0.023)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.276 (n=2328)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.023)

- **PATRÓN** `dist_vwap_pct` > `0.6644` → IC=+0.297 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6644 (IC base=-0.023)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.217 (n=471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1414)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.215 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1263)

- **FILTRO** `sigma_ewma_delta_pct` > `23.635` → IC=-0.263 (n=268)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.635
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1617)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.169 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0028 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.298 (n=102)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.084)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=+0.084)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.328 (n=225)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.286 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.2346` → IC=+0.273 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2346 (IC base=+0.084)

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
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=469)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.157 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0065 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.170 (n=365)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0035 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.212 (n=161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.154)

- **PATRÓN** `drift_15min` |x|≤ `0.4157` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.4157 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.228 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.182 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.258 (n=366)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.1102` → IC=+0.176 (n=260)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1102 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=469)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.179 (n=166)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.245 (n=885)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.4445` → IC=+0.238 (n=885)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4445 (IC base=+0.235)

- **PATRÓN** `drift_15min` |x|≤ `0.778` → IC=+0.249 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.778 (IC base=+0.235)

- **PATRÓN** `delta_ratio_macro` |x|> `0.208` → IC=+0.262 (n=401)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.208 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.236 (n=782)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.235)

- **PATRÓN** `ibs_15` < `0.2757` → IC=+0.280 (n=779)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2757 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.7403` → IC=+0.311 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7403 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.301` → IC=+0.272 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.301 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.239 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.235)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.232 (n=248)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=482)

- **FILTRO** `drift_15min` |x|> `0.9048` → IC=-0.272 (n=182)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9048
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=548)

- **FILTRO** `sigma_ewma_delta_pct` > `18.243` → IC=-0.139 (n=389)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.243
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3134)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.196 (n=54)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.5625 (IC base=-0.172)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 47.0 (IC base=-0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0786` → IC=+0.228 (n=343)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0786 (IC base=-0.041)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1843` → IC=+0.225 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1843 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.269 (n=384)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7153` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7153 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1747` → IC=+0.230 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1747 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.263 (n=441)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=443)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.263 (n=255)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=629)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0629` → IC=+0.271 (n=530)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0629 (IC base=-0.035)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.327 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.035)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=595)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` > `0.8782` → IC=+0.351 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8782 (IC base=-0.035)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `dist_vwap_pct` > `0.1526` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1526 (IC base=+0.046)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `dist_vwap_pct` > `0.1526` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1526 (IC base=+0.046)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.299 (n=525)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.330 (n=263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.307 (n=262)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2191` → IC=+0.319 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2191 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.325 (n=787)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.327 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.345 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.299 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.293 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.336 (n=144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.315 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3917` → IC=+0.302 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3917 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.313 (n=432)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.339 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.322 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.306 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.296 (n=356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.318 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.299 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.327 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.315 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.335 (n=356)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2911` → IC=+0.307 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2911 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.333 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2521` → IC=-0.153 (n=73)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2521
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=221)

- **FILTRO** `ballena_activa_n` > `46.0` → IC=-0.136 (n=196)

  - _Acción_: SKIP cuando `ballena_activa_n` > 46.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=66)

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
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=116)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
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
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0928` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0928
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.188 (n=30)
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
- **PATRÓN** `T_h` > `79.5964` → IC=+0.226 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.5964 (IC base=+0.212)

- **PATRÓN** `ratio` < `0.9763` → IC=+0.470 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9763 (IC base=+0.212)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0112` → IC=+0.314 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0112 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.1277` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.1277 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.467 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.193)

- **PATRÓN** `T_h` > `103.8914` → IC=+0.295 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.8914 (IC base=+0.286)

- **PATRÓN** `ratio` > `1.0474` → IC=+0.373 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0474 (IC base=+0.286)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `80.0063` → IC=+0.269 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.247)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.428 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.247)

- **PATRÓN** `T_h` > `106.9024` → IC=+0.333 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.9024 (IC base=+0.318)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.349 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.318)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6176 sube el IC de +0.199 a +0.277 en UPDOWN_GBM#15min (n=2035). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.212 a +0.273 en UPDOWN_GBM#BTC#15min (n=439). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6602 sube el IC de +0.142 a +0.265 en UPDOWN_GBM#ETH#15min (n=419). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.192 a +0.281 en UPDOWN_GBM#SOL#15min (n=245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5758 sube el IC de +0.205 a +0.290 en UPDOWN_GBM#XRP#15min (n=518). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.064 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=757). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.023 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=2328). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.084 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=225). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.193 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.154 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=366). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2757 sube el IC de +0.235 a +0.280 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=779). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.172 a +0.196 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=54). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.269 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=384). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.035 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=595). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.290 a +0.325 en UPDOWN_GBM_IBS_ALTO (n=787). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.283 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=432). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.296 a +0.335 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=356). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.356 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=482). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.362 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=264). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.743 sube el IC de +0.346 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=218). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1489 | +0.100 | +201.93€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1489 | +0.100 | +201.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1131 | +0.108 | +175.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1131 | +0.108 | +175.02€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 260 | +0.061 | +9.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 260 | +0.061 | +9.45€ | 4 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 67 | +0.123 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 67 | +0.123 | +17.79€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 51 | +0.028 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 51 | +0.028 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 43 | +0.033 | -1.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 43 | +0.033 | -1.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 8 | +0.000 | +0.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 8 | +0.000 | +0.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 31876 | -0.088 | -4183.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1633 | -0.022 | -216.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 30243 | -0.092 | -3967.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4164 | -0.111 | -675.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4164 | -0.111 | -675.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1633 | -0.022 | -216.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1633 | -0.022 | -216.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3791 | -0.112 | -864.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3791 | -0.112 | -864.54€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8243 | -0.013 | -774.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8243 | -0.013 | -774.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7888 | -0.099 | -491.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7888 | -0.099 | -491.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6157 | -0.164 | -1160.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6157 | -0.164 | -1160.67€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 23287 | -0.022 | +3753.75€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6026 | +0.001 | +1755.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 17261 | -0.030 | +1997.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 23287 | -0.022 | +3753.75€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6026 | +0.001 | +1755.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 17261 | -0.030 | +1997.96€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 108545 | +0.113 | -5162.00€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15594 | +0.184 | -472.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 453 | -0.058 | -58.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 85676 | +0.101 | -4380.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6822 | +0.106 | -250.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14233 | +0.100 | -1079.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 50 | -0.135 | +11.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14168 | +0.102 | -1079.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 21665 | +0.130 | -398.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4759 | +0.199 | -134.27€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14207 | +0.114 | -184.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2657 | +0.095 | -57.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14277 | +0.092 | -1218.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 58 | -0.117 | -8.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14204 | +0.093 | -1199.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23050 | +0.124 | -434.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6201 | +0.177 | -90.49€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14364 | +0.105 | -282.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2473 | +0.101 | -52.44€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21070 | +0.114 | -1184.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4474 | +0.188 | -260.36€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 356 | -0.020 | -4.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14548 | +0.093 | -779.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1692 | +0.131 | -140.75€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14250 | +0.099 | -846.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14185 | +0.100 | -856.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17273 | +0.196 | -1042.17€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17273 | +0.196 | -1042.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4034 | +0.173 | -382.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4034 | +0.173 | -382.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1736 | +0.204 | -13.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1736 | +0.204 | -13.17€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3980 | +0.183 | -314.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3980 | +0.183 | -314.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3521 | +0.244 | -106.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3521 | +0.244 | -106.58€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3923 | +0.191 | -239.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3923 | +0.191 | -239.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 809 | +0.433 | -16.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 809 | +0.433 | -16.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 318 | +0.444 | +0.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 318 | +0.444 | +0.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 307 | +0.432 | -6.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 307 | +0.432 | -6.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 172 | +0.414 | -8.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 172 | +0.414 | -8.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 59950 | +0.198 | -4617.32€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 59950 | +0.198 | -4617.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10317 | +0.179 | -1150.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10317 | +0.179 | -1150.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9613 | +0.222 | -355.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9613 | +0.222 | -355.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10331 | +0.174 | -1191.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10331 | +0.174 | -1191.10€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9693 | +0.218 | -386.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9693 | +0.218 | -386.13€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9930 | +0.202 | -656.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9930 | +0.202 | -656.52€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10066 | +0.192 | -877.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10066 | +0.192 | -877.06€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 22785 | +0.115 | +104.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 22785 | +0.115 | +104.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11312 | +0.119 | +114.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11312 | +0.119 | +114.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11473 | +0.111 | -9.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11473 | +0.111 | -9.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1661 | +0.289 | -20.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1661 | +0.289 | -20.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 745 | +0.281 | -14.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 745 | +0.281 | -14.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 801 | +0.288 | -8.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 801 | +0.288 | -8.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 738 | +0.438 | -1.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 738 | +0.438 | -1.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 353 | +0.435 | -3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 353 | +0.435 | -3.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 339 | +0.441 | +1.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 339 | +0.441 | +1.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1269 | +0.067 | -64.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 446 | +0.056 | -37.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 823 | +0.073 | -27.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1001 | +0.072 | -35.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 178 | +0.067 | -8.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 823 | +0.073 | -27.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 203 | +0.027 | -31.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 203 | +0.027 | -31.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 43282 | +0.098 | -1238.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3531 | +0.090 | +31.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 39751 | +0.099 | -1269.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 24083 | +0.102 | -348.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3531 | +0.090 | +31.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 20552 | +0.104 | -380.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8461 | +0.107 | -41.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8461 | +0.107 | -41.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10738 | +0.081 | -847.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10738 | +0.081 | -847.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 862 | +0.208 | -101.16€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 862 | +0.208 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 862 | +0.208 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 862 | +0.208 | -101.16€ | 1 | 4 |
| ✅ GBM_LATE_15M | 30492 | +0.087 | +14998.38€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 30492 | +0.087 | +14998.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5114 | +0.202 | +3912.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5114 | +0.202 | +3912.78€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4549 | +0.178 | +3245.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4549 | +0.178 | +3245.44€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5390 | +0.200 | +4059.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5390 | +0.200 | +4059.03€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4358 | +0.029 | +1073.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4358 | +0.029 | +1073.75€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4340 | -0.032 | +946.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4340 | -0.032 | +946.91€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 6741 | -0.038 | +1760.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6741 | -0.038 | +1760.46€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 32666 | +0.088 | +17437.46€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 32666 | +0.088 | +17437.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6264 | +0.013 | +3262.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6264 | +0.013 | +3262.51€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6790 | +0.014 | +1418.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6790 | +0.014 | +1418.01€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4626 | +0.269 | +4779.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4626 | +0.269 | +4779.56€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5432 | +0.009 | +1180.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5432 | +0.009 | +1180.86€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5270 | +0.035 | +2112.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5270 | +0.035 | +2112.95€ | 3 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4284 | +0.282 | +4683.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4284 | +0.282 | +4683.57€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 24495 | +0.172 | +18840.77€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 24495 | +0.172 | +18840.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3682 | +0.215 | +3059.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3682 | +0.215 | +3059.21€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3872 | +0.149 | +2805.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3872 | +0.149 | +2805.07€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3873 | +0.211 | +3136.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3873 | +0.211 | +3136.61€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4120 | +0.136 | +3016.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4120 | +0.136 | +3016.64€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4582 | +0.121 | +3314.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4582 | +0.121 | +3314.01€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4366 | +0.207 | +3509.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4366 | +0.207 | +3509.23€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6664 | +0.138 | +3121.93€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6664 | +0.138 | +3121.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 335 | +0.141 | +183.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 335 | +0.141 | +183.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1913 | +0.140 | +1003.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1913 | +0.140 | +1003.20€ | 0 | 30 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1991 | +0.154 | +978.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1991 | +0.154 | +978.42€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1520 | +0.111 | +550.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1520 | +0.111 | +550.95€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 531 | +0.134 | +228.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 531 | +0.134 | +228.83€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 30748 | +0.178 | +23533.97€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 30748 | +0.178 | +23533.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4871 | +0.229 | +4293.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4871 | +0.229 | +4293.46€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4793 | +0.148 | +3120.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4793 | +0.148 | +3120.58€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5112 | +0.227 | +4429.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5112 | +0.227 | +4429.31€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5000 | +0.135 | +3527.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5000 | +0.135 | +3527.22€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5389 | +0.120 | +3640.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5389 | +0.120 | +3640.54€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5583 | +0.211 | +4522.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5583 | +0.211 | +4522.85€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8557 | +0.172 | +5671.42€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 8557 | +0.172 | +5671.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2061 | +0.166 | +1486.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2061 | +0.166 | +1486.37€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2812 | +0.178 | +1854.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2812 | +0.178 | +1854.48€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 887 | +0.151 | +518.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 887 | +0.151 | +518.60€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2172 | +0.070 | +787.86€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2172 | +0.070 | +787.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 812 | +0.090 | +284.55€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 812 | +0.090 | +284.55€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 697 | +0.071 | +316.76€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 697 | +0.071 | +316.76€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 663 | +0.046 | +186.55€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 663 | +0.046 | +186.55€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 434 | -0.238 | -8.68€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 434 | -0.238 | -8.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 162 | -0.213 | -3.95€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 162 | -0.213 | -3.95€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 148 | -0.227 | +1.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 148 | -0.227 | +1.04€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 124 | -0.278 | -5.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 124 | -0.278 | -5.77€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 888 | +0.092 | +230.74€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 888 | +0.092 | +230.74€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 334 | +0.083 | +77.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 334 | +0.083 | +77.95€ | 2 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 301 | +0.058 | +37.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 301 | +0.058 | +37.16€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 253 | +0.143 | +115.63€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 253 | +0.143 | +115.63€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 119 | +0.252 | +99.64€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 119 | +0.252 | +99.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 119 | +0.252 | +99.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 119 | +0.252 | +99.64€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 2499 | +0.108 | +703.87€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2499 | +0.108 | +703.87€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2499 | +0.108 | +703.87€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2499 | +0.108 | +703.87€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 414 | -0.072 | -32.72€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 414 | -0.072 | -32.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 111 | -0.040 | -2.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 111 | -0.040 | -2.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 154 | -0.026 | -5.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 154 | -0.026 | -5.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2579 | +0.023 | +78.24€ | 6 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 2579 | +0.023 | +78.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 131 | +0.026 | -1.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 131 | +0.026 | -1.64€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 369 | +0.034 | +38.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 369 | +0.034 | +38.65€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 189 | -0.013 | -3.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 189 | -0.013 | -3.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1010 | +0.033 | +31.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1010 | +0.033 | +31.94€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 594 | +0.008 | -1.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 594 | +0.008 | -1.72€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 286 | +0.024 | +14.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 286 | +0.024 | +14.99€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1283 | -0.043 | -26.06€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1283 | -0.043 | -26.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 364 | -0.038 | -11.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 364 | -0.038 | -11.68€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 429 | -0.031 | -2.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 429 | -0.031 | -2.90€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 490 | -0.057 | -11.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 490 | -0.057 | -11.48€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3786 | -0.021 | +56.26€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1767 | -0.027 | -1.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2019 | -0.016 | +58.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 102 | +0.010 | +7.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 52 | +0.056 | +9.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 50 | -0.038 | -2.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 923 | -0.001 | +43.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 426 | -0.005 | +12.28€ | 2 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 497 | +0.003 | +31.32€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 437 | -0.017 | +15.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 212 | -0.042 | -3.41€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 225 | +0.007 | +19.12€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 755 | -0.043 | -32.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 342 | -0.052 | -23.75€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 413 | -0.035 | -9.02€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 753 | -0.030 | +1.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 359 | -0.040 | -5.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 394 | -0.020 | +6.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 816 | -0.021 | +20.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 376 | -0.018 | +8.58€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 440 | -0.023 | +12.29€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 35018 | -0.005 | +1586.79€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 35018 | -0.005 | +1586.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6219 | +0.022 | +791.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6219 | +0.022 | +791.56€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5282 | -0.032 | -87.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5282 | -0.032 | -87.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6309 | +0.018 | +577.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6309 | +0.018 | +577.29€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5072 | -0.053 | -163.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5072 | -0.053 | -163.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5901 | -0.008 | +202.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5901 | -0.008 | +202.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6235 | +0.012 | +267.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6235 | +0.012 | +267.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6068 | -0.061 | -153.66€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6068 | -0.061 | -153.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1468 | -0.084 | -41.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1468 | -0.084 | -41.16€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 690 | -0.126 | -33.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 690 | -0.126 | -33.03€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1794 | -0.078 | -34.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1794 | -0.078 | -34.75€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 88150 | -0.073 | +1840.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 88150 | -0.073 | +1840.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15062 | -0.075 | +923.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15062 | -0.075 | +923.88€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13444 | -0.096 | -713.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13444 | -0.096 | -713.46€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15335 | -0.066 | +819.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15335 | -0.066 | +819.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12977 | -0.093 | -282.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12977 | -0.093 | -282.34€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16050 | -0.050 | +366.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16050 | -0.050 | +366.12€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15282 | -0.063 | +726.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15282 | -0.063 | +726.97€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7916 | -0.029 | -134.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7916 | -0.029 | -134.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1839 | -0.039 | -14.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1839 | -0.039 | -14.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2235 | -0.024 | -29.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2235 | -0.024 | -29.06€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1071 | -0.043 | -15.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1071 | -0.043 | -15.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 768 | -0.021 | -23.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 768 | -0.021 | -23.86€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1289 | +0.111 | +451.58€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1153 | +0.117 | +438.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 269 | +0.138 | +135.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 269 | +0.138 | +135.74€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 220 | +0.108 | +61.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 220 | +0.108 | +61.90€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 238 | +0.108 | +88.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 238 | +0.108 | +88.83€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 200 | +0.129 | +90.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 200 | +0.129 | +90.05€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 226 | +0.097 | +62.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 226 | +0.097 | +62.46€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 752 | -0.029 | -34.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 752 | -0.029 | -34.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 150 | +0.013 | +9.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 150 | +0.013 | +9.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 108 | -0.045 | -9.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 108 | -0.045 | -9.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 211 | -0.049 | -20.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 211 | -0.049 | -20.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 162 | -0.012 | -3.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 162 | -0.012 | -3.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 121 | -0.053 | -10.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 121 | -0.053 | -10.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 694 | -0.095 | -64.60€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 317 | -0.146 | -74.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 246 | -0.190 | -70.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 245 | -0.059 | -3.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 176 | -0.067 | -6.25€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 69 | -0.035 | +3.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 132 | -0.037 | +13.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 104 | -0.057 | +7.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 526 | -0.123 | -68.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 168 | -0.006 | +4.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 833 | -0.201 | -40.70€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 345 | -0.195 | -30.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 295 | -0.197 | -30.77€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 284 | -0.217 | -26.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 243 | -0.227 | -32.11€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 204 | -0.184 | +16.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 186 | -0.181 | +12.51€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 724 | -0.204 | -50.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 349 | +0.403 | +268.41€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#BTC | 39 | +0.134 | +0.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 39 | +0.134 | +0.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 89 | +0.368 | +73.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 89 | +0.368 | +73.91€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 221 | +0.460 | +193.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 221 | +0.460 | +193.70€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 349 | +0.403 | +268.41€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 592 | +0.032 | +18.50€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 592 | +0.032 | +18.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 288 | +0.031 | +5.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 288 | +0.031 | +5.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 42 | +0.068 | +1.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 42 | +0.068 | +1.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 63 | -0.008 | -1.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 63 | -0.008 | -1.69€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 199 | +0.037 | +13.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 199 | +0.037 | +13.28€ | 2 | 5 |
| ✅ STREAK_FADE_5M | 3012 | -0.023 | -124.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3012 | -0.023 | -124.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 899 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 899 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 577 | -0.025 | -24.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 577 | -0.025 | -24.71€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1380 | -0.022 | -54.60€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1380 | -0.022 | -54.60€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 83 | -0.053 | -8.48€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 83 | -0.053 | -8.48€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 45 | -0.011 | -4.04€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 45 | -0.011 | -4.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9271 | +0.021 | +123.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9271 | +0.021 | +123.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2572 | +0.024 | +33.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2572 | +0.024 | +33.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2119 | +0.030 | +52.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2119 | +0.030 | +52.72€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2809 | +0.012 | +6.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2809 | +0.012 | +6.75€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1771 | +0.022 | +30.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1771 | +0.022 | +30.56€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8277 | +0.013 | -42.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8277 | +0.013 | -42.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3278 | +0.017 | -5.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3278 | +0.017 | -5.50€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3292 | +0.012 | -21.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3292 | +0.012 | -21.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1707 | +0.006 | -15.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1707 | +0.006 | -15.54€ | 1 | 0 |
| ✅ UPDOWN_GBM | 49321 | +0.039 | +3457.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 12708 | +0.074 | +2548.41€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1697 | +0.005 | +9.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 31791 | +0.030 | +867.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2943 | +0.004 | +33.68€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4999 | +0.075 | +633.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 943 | +0.158 | +415.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4023 | +0.057 | +218.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9485 | +0.047 | +741.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1656 | +0.088 | +378.01€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 454 | +0.013 | +5.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5975 | +0.049 | +321.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1332 | +0.005 | +34.19€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 68 | -0.086 | +1.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5739 | +0.046 | +415.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 907 | +0.140 | +331.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4804 | +0.029 | +85.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 10859 | +0.028 | +546.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3167 | +0.051 | +412.86€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 447 | +0.008 | +9.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6191 | +0.024 | +124.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 994 | +0.001 | -3.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 60 | -0.113 | +3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11051 | +0.019 | +350.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3027 | +0.028 | +241.65€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 438 | -0.002 | -0.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6917 | +0.018 | +110.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 617 | +0.007 | +3.32€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 52 | -0.148 | -3.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7186 | +0.043 | +772.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3008 | +0.090 | +768.77€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 297 | +0.002 | -2.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3881 | +0.010 | +6.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 180 | -0.115 | +0.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 642 | +0.356 | +224.10€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 642 | +0.356 | +224.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 352 | +0.362 | +121.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 352 | +0.362 | +121.58€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 290 | +0.346 | +102.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 290 | +0.346 | +102.53€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14370 | -0.032 | +3204.31€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14370 | -0.032 | +3204.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1036 | -0.053 | +380.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1036 | -0.053 | +380.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2609 | -0.116 | +55.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2609 | -0.116 | +55.89€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 564 | +0.198 | +418.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 564 | +0.198 | +418.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1665 | +0.211 | +1062.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1665 | +0.211 | +1062.50€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4253 | -0.064 | +591.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4253 | -0.064 | +591.90€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4243 | -0.071 | +695.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4243 | -0.071 | +695.00€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 168 | +0.035 | +7.74€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 168 | +0.035 | +7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 168 | +0.035 | +7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 168 | +0.035 | +7.74€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1049 | +0.290 | +869.05€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1049 | +0.290 | +869.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 575 | +0.283 | +439.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 575 | +0.283 | +439.93€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 474 | +0.296 | +429.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 474 | +0.296 | +429.12€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 747 | -0.112 | -82.30€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 747 | -0.112 | -82.30€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 222 | -0.085 | -17.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 222 | -0.085 | -17.28€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 76 | -0.179 | -5.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 76 | -0.179 | -5.64€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2733 | +0.305 | +1353.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 958 | +0.257 | +142.14€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1043 | +0.296 | +460.38€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 732 | +0.377 | +750.88€ | 0 | 1 |