# Hipótesis automáticas — 2026-10-02 16:27 UTC
_Generado por shadow_postmortem.py sobre 716271 resoluciones (PNL=+85926.02€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.223 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.218 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.8032` → IC=+0.256 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8032 (IC base=+0.131)

- **PATRÓN** `banda_z` > `9.307` → IC=+0.196 (n=205)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.307 (IC base=+0.131)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.132 (n=550)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.131 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=645)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4766.038` → IC=+0.150 (n=204)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4766.038 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.230 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.8011` → IC=+0.265 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8011 (IC base=+0.141)

- **PATRÓN** `banda_z` > `9.988` → IC=+0.203 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.988 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=551)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.141)

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
- **FILTRO** `restante_s_al_confirmar` < `145.04` → IC=-0.219 (n=8010)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.04
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=24032)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `133.84` → IC=-0.263 (n=1045)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.84
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3135)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.3` → IC=-0.313 (n=954)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.3
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2864)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.29` → IC=-0.213 (n=1983)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.29
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5950)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.33` → IC=-0.327 (n=1549)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.33
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=4648)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.211 (n=15602)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=3775)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5472.5329` → IC=+0.171 (n=2444)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5472.5329 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=16519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=12704)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=6203)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7709.8469` → IC=+0.169 (n=2371)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7709.8469 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.208 (n=1766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=1812)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.224 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.201 (n=1638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2339)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `16003.8489` → IC=+0.212 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16003.8489 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.170 (n=365)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4624.034 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.097)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.141 (n=901)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.151 (n=230)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.097)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.157 (n=2900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.355 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=1458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.363 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.253 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=875)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1324.629` → IC=+0.147 (n=765)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1324.629 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.405 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.155 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 14.0 (IC base=+0.149)

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

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.227 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=13561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=12982)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.232 (n=4297)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=3213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3052)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3082)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.246 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.236 (n=1243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.339 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.234)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=2996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=3025)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=2538)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.331 (n=936)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=1984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=2338)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.194 (n=1120)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `11601.187` → IC=+0.456 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11601.187 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.447 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `11135.4127` → IC=+0.458 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11135.4127 (IC base=+0.441)

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
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.411 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.411 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=40439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=17702)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=6957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=5607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=7632)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=3591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.265 (n=4117)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=7361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=7368)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=3628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2462)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=2873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=3081)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=6179)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=5925)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.5` → IC=+0.136 (n=5730)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.5 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=3105)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=2945)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=3763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.21` → IC=+0.141 (n=2845)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.21 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.182 (n=3074)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.111)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.128 (n=3260)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` > 4.96 (IC base=+0.111)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=2904)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.111)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.314 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.288 (n=1255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1552.7677` → IC=+0.294 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1552.7677 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.333 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `4351.481` → IC=+0.293 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4351.481 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=632)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1448.4724` → IC=+0.303 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1448.4724 (IC base=+0.287)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.438 (n=496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.442 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.456 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `1966.3827` → IC=+0.458 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.3827 (IC base=+0.442)

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
- **PATRÓN** `drift_60min` |x|≤ `0.495` → IC=+0.130 (n=9664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.495 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.243 (n=3221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2239` → IC=+0.257 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2239 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.406` → IC=+0.192 (n=2537)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.406 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.211` → IC=+0.251 (n=2693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.211 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.252 (n=2693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.229 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3209` → IC=+0.220 (n=3051)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3209 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.137 (n=11729)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5667 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5966` → IC=+0.202 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5966 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.156` → IC=+0.176 (n=3876)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.156 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.183 (n=1868)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.697 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `0.8676` → IC=+0.177 (n=2829)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8676 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.223 (n=2034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.2685` → IC=+0.197 (n=6385)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2685 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4452` → IC=+0.199 (n=7256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4452 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.214 (n=7053)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.207 (n=719)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.187 (n=720)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3557` → IC=+0.181 (n=2153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3557 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=1033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.181 (n=1448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 11.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.715` → IC=+0.297 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.715 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.216 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.178 (n=2030)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.193 (n=2200)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.235 (n=1137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.242 (n=1527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.272 (n=569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0613` → IC=+0.286 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0613 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.472` → IC=+0.244 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.472 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.403` → IC=+0.240 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.403 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0923` → IC=+0.232 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0923 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.265 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.5634` → IC=+0.243 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5634 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1581.46` → IC=+0.246 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1581.46 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.236 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.3576` → IC=+0.228 (n=1711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3576 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=1713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.217 (n=1748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.8946` → IC=+0.257 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8946 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.3504` → IC=+0.220 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3504 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.703` → IC=+0.254 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.703 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.221 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.221 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.238 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.221 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3804` → IC=+0.240 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3804 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `11136.1557` → IC=+0.221 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11136.1557 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.170 (n=1149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.166 (n=575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7172` → IC=+0.171 (n=1723)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7172 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1323` → IC=+0.155 (n=1547)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1323 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.294` → IC=+0.145 (n=274)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 11.294 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.261` → IC=+0.144 (n=1588)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.261 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.149 (n=1723)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2085 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.175 (n=460)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.151 (n=1612)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.145 (n=1075)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `14150.2717` → IC=+0.142 (n=1149)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14150.2717 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.174 (n=673)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 231.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.202 (n=1935)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=2162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=1453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.319` → IC=+0.257 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.319 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.197 (n=1896)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.202 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1652` → IC=+0.207 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1652 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2575)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2008.6449` → IC=+0.199 (n=721)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2008.6449 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.221 (n=1674)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.6301` → IC=+0.214 (n=1902)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6301 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.0649` → IC=+0.234 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0649 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.235 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.253 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.72` → IC=+0.216 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.72 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7414` → IC=+0.218 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7414 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1926.5448` → IC=+0.215 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.5448 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.211 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=118)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2596)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.135 (n=551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0043 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.220 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.3636` → IC=+0.328 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3636 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.871` → IC=+0.171 (n=858)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.871 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.339 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.360 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `1.8421` → IC=+0.326 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8421 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.328 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.1017` → IC=+0.156 (n=679)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1017 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.3334` → IC=+0.196 (n=317)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3334 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.150 (n=698)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8475 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1669` → IC=+0.147 (n=349)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1669 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.193 (n=138)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.167 (n=887)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.022)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=391)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.192 (n=115)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=346)

- **FILTRO** `ibs_20min` > `0.24` → IC=-0.126 (n=2606)

  - _Acción_: SKIP cuando `ibs_20min` > 0.24
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=1294)

- **FILTRO** `sigma_ewma_delta_pct` > `8.739` → IC=-0.206 (n=410)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.739
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3490)

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

- **PATRÓN** `ibs_20min` < `0.24` → IC=+0.134 (n=1294)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.24 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7032` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7032 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.6851` → IC=+0.269 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6851 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` > `0.887` → IC=+0.242 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.887 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.302 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.371` → IC=+0.289 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.371 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.179 (n=677)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2053)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.208 (n=641)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2089)

- **FILTRO** `ibs_20min` > `0.7669` → IC=-0.208 (n=1010)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7669
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=3037)

- **PATRÓN** `dist_vwap_pct` > `0.7963` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7963 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2881` → IC=+0.317 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2881 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` < `0.9845` → IC=+0.296 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9845 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6304` → IC=+0.311 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6304 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.303 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.300 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.302 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.8226` → IC=+0.309 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8226 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5629` → IC=+0.284 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5629 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` < `0.728` → IC=+0.256 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.728 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.269 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.269 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.1331` → IC=+0.261 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1331 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.253 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.42 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.200 (n=4173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4715` → IC=+0.189 (n=11172)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4715 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.999` → IC=+0.287 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.999 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.654` → IC=+0.159 (n=5725)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.654 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1814` → IC=+0.244 (n=4548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1814 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6148` → IC=+0.250 (n=4548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6148 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.271 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.4637` → IC=+0.241 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4637 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6301` → IC=+0.255 (n=2445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6301 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.276 (n=6881)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.170 (n=4047)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.158 (n=10681)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5455 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.250 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2474` → IC=+0.249 (n=3500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2474 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7084` → IC=+0.249 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7084 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.199` → IC=+0.262 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.199 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.239` → IC=+0.303 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.239 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5854` → IC=+0.278 (n=2207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5854 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.281 (n=4907)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.157 (n=866)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2600)

- **FILTRO** `ibs_20min` > `0.7582` → IC=-0.170 (n=709)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7582
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2128)

- **FILTRO** `sigma_ewma_delta_pct` > `4.567` → IC=-0.174 (n=643)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.567
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2194)

- **PATRÓN** `ibs_20min` > `0.9039` → IC=+0.278 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9039 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.862` → IC=+0.212 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.862 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.277 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4395` → IC=+0.203 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4395 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.232 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.221 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.0963` → IC=+0.442 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0963 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1478` → IC=+0.447 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1478 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.454 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.466 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8636` → IC=+0.163 (n=838)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8636 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.188 (n=638)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.175 (n=1046)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6754 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.229 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.199 (n=383)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.4028` → IC=+0.180 (n=383)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.4028 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.221 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 233.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.227 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6178` → IC=+0.229 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6178 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.0717` → IC=+0.222 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0717 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2644` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2644 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.3745` → IC=+0.222 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3745 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.237 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `459.0` → IC=+0.222 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 459.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.286 (n=1275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=1922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.736` → IC=+0.282 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.736 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.268 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `1.6236` → IC=+0.260 (n=1823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6236 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.263 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1999.591` → IC=+0.275 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.591 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.300 (n=1580)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1855` → IC=+0.298 (n=695)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1855 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.321 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.294 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.287)

- **PATRÓN** `ibs_20min` > `0.0986` → IC=+0.288 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0986 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.684` → IC=+0.293 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.684 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.119` → IC=+0.293 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.119 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.57` → IC=+0.303 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.57 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.291 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1918.7584` → IC=+0.305 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.7584 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.292 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7725` → IC=-0.187 (n=721)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7725
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=2167)

- **PATRÓN** `ibs_20min` > `0.9046` → IC=+0.181 (n=646)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.9046 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1824` → IC=+0.231 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1824 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0078` → IC=+0.249 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0078 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0813` → IC=+0.255 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0813 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4079` → IC=+0.270 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4079 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.256 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1418` → IC=+0.230 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1418 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.216 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1804 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` < `0.1015` → IC=+0.235 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1015 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.265 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.808 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.259 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 134.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7568` → IC=-0.187 (n=1319)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7568
  - _Potencial_: sin este filtro IC_bueno=+0.284 (n=1325)

- **FILTRO** `ibs_20min` > `0.6742` → IC=-0.243 (n=664)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6742
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=1993)

- **FILTRO** `sigma_ewma_delta_pct` > `4.743` → IC=-0.194 (n=569)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.743
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2088)

- **PATRÓN** `ibs_20min` > `0.7568` → IC=+0.284 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7568 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.2174` → IC=+0.318 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2174 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.668` → IC=+0.170 (n=419)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.668 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.309 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8605 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.302 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.299 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2714` → IC=+0.298 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2714 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.323 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.326 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.569` → IC=+0.133 (n=1754)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.569 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.4655` → IC=+0.239 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4655 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.264 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1889` → IC=+0.224 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1889 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0957` → IC=+0.230 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0957 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.247 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.249 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.259 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.022)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.327 (n=1399)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.303 (n=736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `0.64` → IC=+0.314 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.64 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.316 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.765` → IC=+0.308 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.765 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.861` → IC=+0.282 (n=1759)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.861 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.296 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.329 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.294 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2471.2826` → IC=+0.296 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2471.2826 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.323 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.313 (n=1107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.1973` → IC=+0.288 (n=731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1973 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.291 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.309 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.3215` → IC=+0.296 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3215 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.298 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.284 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.315 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.339 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.292 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2424.4333` → IC=+0.287 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2424.4333 (IC base=+0.282)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.176 (n=3165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0049 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.206 (n=3149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3652` → IC=+0.180 (n=8305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3652 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5711` → IC=+0.225 (n=9437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5711 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1761` → IC=+0.196 (n=4086)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1761 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.405` → IC=+0.254 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.405 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.2102` → IC=+0.164 (n=6286)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2102 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.160 (n=6285)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6307 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.198 (n=1401)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5576` → IC=+0.170 (n=3998)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5576 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5992` → IC=+0.178 (n=3029)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.5992 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `1969.857` → IC=+0.174 (n=8430)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1969.857 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.186 (n=8355)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 108.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.187 (n=6034)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0821` → IC=+0.215 (n=3018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0821 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=3436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.4863` → IC=+0.229 (n=9043)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4863 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1749` → IC=+0.167 (n=6307)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1749 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.291` → IC=+0.196 (n=1519)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.291 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1778` → IC=+0.160 (n=6497)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1778 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.29` → IC=+0.215 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.29 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5529` → IC=+0.173 (n=3676)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5529 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5853` → IC=+0.172 (n=2783)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5853 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.181 (n=8024)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 109.0 (IC base=+0.172)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.232 (n=528)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.207 (n=528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.3432` → IC=+0.216 (n=1580)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3432 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=1666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.285 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.245` → IC=+0.332 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.245 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.245 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.429` → IC=+0.194 (n=1476)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.429 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.209 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.249 (n=1058)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=1072)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.184` → IC=+0.287 (n=800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.184 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.3514` → IC=+0.261 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3514 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.215` → IC=+0.245 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.215 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.262 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4156` → IC=+0.268 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4156 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1577.6848` → IC=+0.256 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1577.6848 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.232 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.192 (n=475)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=1425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.389` → IC=+0.221 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.389 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2054` → IC=+0.205 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2054 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.227 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6891` → IC=+0.170 (n=626)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6891 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.200 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.178 (n=609)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.160 (n=462)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `11985.6464` → IC=+0.159 (n=1271)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11985.6464 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.164 (n=594)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 235.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.176 (n=1322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.5887` → IC=+0.194 (n=1503)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5887 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1372` → IC=+0.168 (n=1481)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1372 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.201 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.215` → IC=+0.161 (n=1503)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.215 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.151 (n=456)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.150 (n=1391)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.173 (n=442)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 209.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.226 (n=713)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2513` → IC=+0.220 (n=1049)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2513 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.464` → IC=+0.277 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.464 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.203 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2004` → IC=+0.208 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2004 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7293` → IC=+0.215 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7293 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `1999.6584` → IC=+0.217 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.6584 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.234 (n=1188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.144` → IC=+0.255 (n=594)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.144 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.3519` → IC=+0.246 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3519 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.649` → IC=+0.251 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.649 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.251 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.73` → IC=+0.236 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.73 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.154` → IC=+0.224 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.154 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1992.8384` → IC=+0.221 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.8384 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.211 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.220)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.180 (n=1342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.162 (n=1522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3451` → IC=+0.203 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3451 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1493` → IC=+0.183 (n=992)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1493 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.946` → IC=+0.227 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.946 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0379` → IC=+0.157 (n=1339)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0379 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.178 (n=638)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.159 (n=497)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.163 (n=497)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5222.8208` → IC=+0.190 (n=1014)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5222.8208 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.152 (n=1462)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 155.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1590)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3922` → IC=+0.148 (n=1590)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3922 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6622` → IC=+0.176 (n=1590)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6622 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1552` → IC=+0.142 (n=1556)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1552 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.869` → IC=+0.166 (n=552)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.869 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8571` → IC=+0.150 (n=1060)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8571 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.179 (n=235)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8007` → IC=+0.137 (n=977)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8007 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.5127` → IC=+0.133 (n=488)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5127 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `9258.4062` → IC=+0.167 (n=721)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9258.4062 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.126 (n=1240)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 128.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.164 (n=780)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0101 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.5902` → IC=+0.123 (n=1721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.5902 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.209 (n=1734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0784` → IC=+0.216 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0784 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.874` → IC=+0.257 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.874 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.133 (n=1720)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2151 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.127 (n=1720)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6466 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1613` → IC=+0.128 (n=1729)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1613 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.125 (n=712)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5355` → IC=+0.141 (n=731)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5355 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1801)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2892.276` → IC=+0.198 (n=780)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2892.276 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.141 (n=1353)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 47.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.163 (n=767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0063 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1064` → IC=+0.170 (n=580)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1064 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.218 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.9997` → IC=+0.123 (n=234)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.9997 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2057` → IC=+0.149 (n=1605)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2057 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.604` → IC=+0.136 (n=361)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 7.604 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.150 (n=581)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6382 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2259` → IC=+0.161 (n=305)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2259 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.446` → IC=+0.142 (n=529)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.446 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4117` → IC=+0.129 (n=529)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4117 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.183 (n=788)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.128 (n=1532)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.229 (n=1450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2942` → IC=+0.209 (n=1083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2942 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.213 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.248 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.1979` → IC=+0.210 (n=1624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1979 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.216 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6297 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.271 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.4647` → IC=+0.211 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4647 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.8002` → IC=+0.215 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8002 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2846.2656` → IC=+0.210 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2846.2656 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.224 (n=734)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.215 (n=1112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.234 (n=557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.242 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `1.2002` → IC=+0.229 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2002 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.42` → IC=+0.248 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.42 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.221 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.281 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `2.1862` → IC=+0.204 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1862 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.208 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2398.9192` → IC=+0.216 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2398.9192 (IC base=+0.211)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.191 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0037 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.175 (n=829)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0086 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3486` → IC=+0.176 (n=2184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3486 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.207 (n=1225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.202 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.189 (n=406)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7982 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.719` → IC=+0.194 (n=1088)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.719 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.188 (n=1469)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8725 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.2093` → IC=+0.177 (n=735)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2093 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1623` → IC=+0.181 (n=663)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1623 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4359` → IC=+0.179 (n=802)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4359 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8176` → IC=+0.172 (n=1604)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8176 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=2811)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2671.4273` → IC=+0.169 (n=2218)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2671.4273 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.184 (n=2262)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 142.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.141 (n=1701)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0056 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=2402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.0667` → IC=+0.191 (n=850)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0667 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.124 (n=1010)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.6989 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.128 (n=624)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.4405` → IC=+0.143 (n=824)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4405 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2760.3927` → IC=+0.124 (n=2276)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2760.3927 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.133 (n=1053)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 27.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.170 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0029 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3342` → IC=+0.161 (n=650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3342 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.6393` → IC=+0.203 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6393 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.164 (n=233)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.166 (n=285)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8937` → IC=+0.172 (n=434)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8937 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1546` → IC=+0.142 (n=676)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1546 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0922` → IC=+0.151 (n=227)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0922 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1959` → IC=+0.151 (n=557)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1959 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.3995` → IC=+0.144 (n=633)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.3995 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=841)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10902.4411` → IC=+0.152 (n=650)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10902.4411 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.188 (n=274)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 154.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.210 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3449` → IC=+0.160 (n=799)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3449 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.141 (n=815)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.181 (n=703)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6112 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.183` → IC=+0.157 (n=785)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.183 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.275` → IC=+0.142 (n=305)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 4.275 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.07` → IC=+0.145 (n=730)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.07 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.147 (n=799)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2216 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.7012` → IC=+0.155 (n=714)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7012 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.204 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1115` → IC=+0.160 (n=695)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1115 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.407` → IC=+0.147 (n=789)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.407 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `12082.5549` → IC=+0.144 (n=714)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 12082.5549 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.157 (n=675)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 295.0 (IC base=+0.141)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.251 (n=520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4099` → IC=+0.221 (n=778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4099 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.3658` → IC=+0.240 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3658 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.215 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2221` → IC=+0.210 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2221 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.261` → IC=+0.239 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.261 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.218 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8392 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.1811` → IC=+0.233 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1811 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.246 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4183` → IC=+0.240 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4183 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.4379` → IC=+0.244 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4379 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.0873 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.143 (n=320)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6872 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `8098.9392` → IC=+0.132 (n=485)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8098.9392 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.165 (n=524)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0059 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.9831` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9831 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.339` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.339 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.165 (n=517)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0699 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6503` → IC=+0.155 (n=587)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6503 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1717` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1717 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.168 (n=257)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=621)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3090.2601` → IC=+0.187 (n=196)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3090.2601 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.4556` → IC=+0.157 (n=490)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4556 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.8278` → IC=+0.128 (n=353)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8278 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `2481.4994` → IC=+0.133 (n=371)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2481.4994 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.124 (n=501)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 41.0 (IC base=+0.073)

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
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.209 (n=4070)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=12764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.9924` → IC=+0.309 (n=4067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9924 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.9142` → IC=+0.200 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9142 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.369` → IC=+0.250 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.369 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.170 (n=5460)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8812 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.201 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.5741` → IC=+0.195 (n=3929)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5741 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1801.22` → IC=+0.178 (n=12201)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1801.22 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.201 (n=9546)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.193 (n=7324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0071 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.152` → IC=+0.192 (n=4833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.152 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4516` → IC=+0.246 (n=9667)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4516 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2507` → IC=+0.163 (n=6836)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2507 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.045` → IC=+0.203 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.045 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.183 (n=10612)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7063` → IC=+0.162 (n=3286)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7063 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.242 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.589` → IC=+0.191 (n=3405)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.589 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `1732.46` → IC=+0.182 (n=10981)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1732.46 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.203 (n=6639)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.232 (n=676)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.229 (n=678)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.3618` → IC=+0.207 (n=2023)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3618 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.704` → IC=+0.358 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.704 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.259 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.2341` → IC=+0.213 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2341 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2031.7296` → IC=+0.209 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.7296 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.221 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.262 (n=1101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.261 (n=1652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1263` → IC=+0.282 (n=727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1263 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=1493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3605` → IC=+0.284 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3605 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.511` → IC=+0.262 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.511 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.292 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.5466` → IC=+0.260 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5466 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6038` → IC=+0.277 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6038 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1580.4772` → IC=+0.269 (n=1650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1580.4772 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.206 (n=658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1131` → IC=+0.159 (n=866)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1131 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.2876` → IC=+0.202 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2876 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.181 (n=1117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.177 (n=429)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.15` → IC=+0.150 (n=1796)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.15 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.173 (n=656)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6267 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.151 (n=1741)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.193 (n=281)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1166` → IC=+0.158 (n=1681)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1166 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7596` → IC=+0.152 (n=1273)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7596 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11426.5156` → IC=+0.154 (n=1757)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 11426.5156 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.170 (n=821)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 278.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=1648)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.331` → IC=+0.160 (n=1648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.331 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.2934` → IC=+0.237 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2934 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1343` → IC=+0.164 (n=1496)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1343 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.160 (n=277)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.285` → IC=+0.149 (n=1502)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.285 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.161 (n=1648)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1967 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.197 (n=440)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.408` → IC=+0.156 (n=1549)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.408 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.160 (n=1033)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `260.0` → IC=+0.160 (n=492)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 260.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.256 (n=663)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=2022)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.366` → IC=+0.300 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.366 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.2068` → IC=+0.223 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2068 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.232 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.235 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.242 (n=1643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.6177` → IC=+0.236 (n=1865)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6177 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0159` → IC=+0.303 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0159 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.171` → IC=+0.277 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.171 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3399` → IC=+0.296 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3399 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.236 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1472` → IC=+0.237 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1472 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1991.7884` → IC=+0.245 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.7884 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.233 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.195 (n=699)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0035 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4371` → IC=+0.150 (n=2093)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4371 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2721` → IC=+0.188 (n=2093)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2721 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.364` → IC=+0.161 (n=815)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.364 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.555` → IC=+0.168 (n=338)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.555 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.873` → IC=+0.162 (n=1396)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.873 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.195 (n=280)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.152 (n=895)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.153 (n=923)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7601.2069` → IC=+0.231 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7601.2069 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.168 (n=660)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 72.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.168 (n=1120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0052 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4486` → IC=+0.143 (n=1678)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4486 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.5941` → IC=+0.196 (n=1476)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5941 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1573` → IC=+0.132 (n=1467)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1573 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.273` → IC=+0.164 (n=251)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.273 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6226` → IC=+0.143 (n=561)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6226 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.214 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.142 (n=1603)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `9483.0008` → IC=+0.202 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9483.0008 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.131 (n=1601)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 169.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.148 (n=1387)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0082 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.5827` → IC=+0.126 (n=2081)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.5827 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.200 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0629` → IC=+0.211 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0629 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.574` → IC=+0.241 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.574 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8928` → IC=+0.145 (n=1388)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8928 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1608` → IC=+0.126 (n=2142)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1608 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.4501` → IC=+0.131 (n=675)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4501 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2118)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2538.6407` → IC=+0.234 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2538.6407 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.141 (n=1660)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 52.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.180 (n=663)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0059 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1375` → IC=+0.159 (n=663)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1375 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.234 (n=1747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.138 (n=1646)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.128 (n=1910)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6463` → IC=+0.161 (n=662)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6463 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2197` → IC=+0.185 (n=312)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2197 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.1493` → IC=+0.133 (n=1601)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1493 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2799.6738` → IC=+0.188 (n=662)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2799.6738 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=1609)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.229 (n=2049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.214 (n=1485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2182` → IC=+0.232 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2182 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.285` → IC=+0.274 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.285 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.0608` → IC=+0.216 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0608 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.6424` → IC=+0.221 (n=2049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6424 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2856` → IC=+0.245 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2856 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4788` → IC=+0.236 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4788 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2453.7234` → IC=+0.216 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2453.7234 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.216 (n=720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.230 (n=719)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.225 (n=1523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.4211` → IC=+0.261 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4211 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `1.222` → IC=+0.219 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.222 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2205` → IC=+0.214 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2205 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.256 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.238 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.280 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `2.1632` → IC=+0.205 (n=1732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1632 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4249` → IC=+0.207 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4249 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2409.4925` → IC=+0.212 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2409.4925 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.201 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.209)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=3681)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.220 (n=1221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.5106` → IC=+0.191 (n=3651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5106 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=1365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=1669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.239 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1738` → IC=+0.191 (n=1350)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1738 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.206` → IC=+0.212 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.206 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7103` → IC=+0.186 (n=1102)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7103 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.183 (n=1669)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8944 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1682` → IC=+0.209 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1682 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.189 (n=1202)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8592` → IC=+0.186 (n=2402)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8592 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2716)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2520.4396` → IC=+0.186 (n=3651)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2520.4396 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.217 (n=925)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.182 (n=2440)
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

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.183 (n=518)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` < `0.2399` → IC=+0.153 (n=2461)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2399 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.170 (n=2767)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2562` → IC=+0.165 (n=2608)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2562 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.167 (n=2534)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5345` → IC=+0.169 (n=1205)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5345 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8229` → IC=+0.171 (n=1825)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8229 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=3681)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `5320.6072` → IC=+0.166 (n=2477)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5320.6072 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.167 (n=1800)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 85.0 (IC base=+0.161)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.230 (n=442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.265 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.5157` → IC=+0.227 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5157 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7622` → IC=+0.209 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7622 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.329` → IC=+0.211 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.329 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.96` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.96 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.529` → IC=+0.206 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.529 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2189` → IC=+0.210 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2189 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.214 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.224 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `12593.964` → IC=+0.236 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12593.964 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.224 (n=461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.161 (n=1046)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.182 (n=461)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.144 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.151 (n=474)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6091 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6676` → IC=+0.193 (n=99)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6676 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.216` → IC=+0.150 (n=1061)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.216 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.377` → IC=+0.167 (n=1029)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.377 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.189 (n=698)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8812 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.168 (n=480)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4156` → IC=+0.154 (n=348)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4156 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.163 (n=695)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `14889.24` → IC=+0.170 (n=474)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14889.24 (IC base=+0.148)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1526` → IC=+0.205 (n=514)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1526 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.202 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5305 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.194 (n=390)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8854 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.198 (n=978)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.197 (n=1051)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `1.0851` → IC=+0.193 (n=1028)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0851 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.2467` → IC=+0.191 (n=390)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.2467 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.190 (n=1073)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.200 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.196 (n=1145)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=1175)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.189)

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
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.169 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0111 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.168 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 3.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.143 (n=373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.2235` → IC=+0.196 (n=245)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2235 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.097` → IC=+0.227 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.097 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.7117` → IC=+0.189 (n=162)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.7117 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.2801` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.2801 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.4173` → IC=+0.203 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4173 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=435)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2974.6892` → IC=+0.168 (n=368)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2974.6892 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.158 (n=311)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 52.0 (IC base=+0.140)

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
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.165 (n=508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.004 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.6459` → IC=+0.178 (n=949)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6459 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1475` → IC=+0.144 (n=579)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1475 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.429` → IC=+0.196 (n=248)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.429 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.188 (n=142)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.124 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0045 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.0417` → IC=+0.300 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0417 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.201` → IC=+0.135 (n=455)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.201 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.074` → IC=+0.145 (n=345)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.074 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.1401` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1401 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.1255` → IC=+0.152 (n=311)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1255 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.140 (n=315)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4444 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `3329.7378` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3329.7378 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.201 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.426` → IC=+0.163 (n=366)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.426 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.160 (n=195)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.124 (n=325)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.122 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.0606` → IC=+0.188 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0606 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.307 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.4088` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.4088 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.069` → IC=+0.145 (n=195)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.069 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.462` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 4.462 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `1.1644` → IC=+0.141 (n=196)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1644 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.6903` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6903 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.169 (n=173)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.4035 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `3376.236` → IC=+0.141 (n=165)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3376.236 (IC base=+0.088)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.7019` → IC=-0.126 (n=153)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7019
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=313)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=158)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.138 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.7019` → IC=+0.214 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7019 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.3362` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3362 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.652` → IC=+0.284 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.652 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.8058` → IC=+0.127 (n=234)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8058 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.7617` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7617 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.149 (n=309)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1419` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1419 (IC base=+0.008)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.412` → IC=+0.143 (n=96)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.412 (IC base=+0.008)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0117` → IC=-0.267 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0117
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=126)

- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.273 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.279 (n=84)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.181 (n=233)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.7647 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.076` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.076 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.054)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.137 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0094 (IC base=+0.021)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.936` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.936 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1324` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1324 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.6706` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6706 (IC base=+0.021)

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
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=130)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=175)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=166)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=91)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.238 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

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

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.184 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0059 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6645` → IC=+0.149 (n=331)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6645 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.4944` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.4944 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.4189` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4189 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.120 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0052 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.142 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.1613` → IC=+0.190 (n=301)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1613 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.706` → IC=+0.203 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.706 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `2.627` → IC=+0.147 (n=267)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.627 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `1.4576` → IC=+0.121 (n=267)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.4576 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=362)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.209 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.092)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6292` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6292
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=100)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.195 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0033 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.237 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.229 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1524 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.1046` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1046 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.079` → IC=+0.167 (n=157)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.079 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.62` → IC=+0.179 (n=138)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.62 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.1644` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1644 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.6961` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6961 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.1954` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1954 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `2.5892` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5892 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.4576` → IC=+0.191 (n=121)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4576 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `4570.9788` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 4570.9788 (IC base=+0.163)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1748` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1748
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=87)

- **FILTRO** `libro_liquidez` < `1549.4073` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 1549.4073
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=96)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.198 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0027 (IC base=+0.079)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.131 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.1821` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1821 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.706` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.706 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.9961` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.9961 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `1938.4449` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1938.4449 (IC base=+0.079)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0793` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0793
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.318 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.258 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9714 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7647 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.314 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.1711` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1711 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `592.1486` → IC=+0.246 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 592.1486 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.048)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.221)

- **PATRÓN** `elapsed_s` > `194.4` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 194.4 (IC base=+0.221)

- **PATRÓN** `elapsed_s` < `204.4` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 204.4 (IC base=+0.221)

- **PATRÓN** `drift_15min` |x|≤ `1.4068` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4068 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.312 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `1450.0` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1450.0 (IC base=+0.221)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.221)

- **PATRÓN** `elapsed_s` > `194.4` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 194.4 (IC base=+0.221)

- **PATRÓN** `elapsed_s` < `204.4` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 204.4 (IC base=+0.221)

- **PATRÓN** `drift_15min` |x|≤ `1.4068` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4068 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.312 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `1450.0` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1450.0 (IC base=+0.221)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.122 (n=1074)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.495 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2843.9766` → IC=+0.152 (n=418)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2843.9766 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.122 (n=1074)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.495 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2843.9766` → IC=+0.152 (n=418)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2843.9766 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.105)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2416)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.120 (n=833)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.033)

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

- **PATRÓN** `liq_usd_total` > `134844.05` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `liq_usd_total` > 134844.05 (IC base=+0.056)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.165 (n=153)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=969)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=923)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=562)

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
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=267)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.495 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `3909.4956` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3909.4956 (IC base=+0.033)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=735)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=735)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=466)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=466)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=201)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=201)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=115)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=137)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=237)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=111)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=124)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=282)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=282)

- **FILTRO** `libro_liquidez` < `466.9438` → IC=-0.138 (n=78)

  - _Acción_: SKIP cuando `libro_liquidez` < 466.9438
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=234)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=168)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=1019)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=1024)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **FILTRO** `lag_apertura_s` > `78.26` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `lag_apertura_s` > 78.26
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.122 (n=125)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=66)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.139 (n=70)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=180)

- **PATRÓN** `py_entrada` < `0.56` → IC=+0.128 (n=127)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.56 (IC base=+0.020)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.46 (IC base=+0.039)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=91)

- **FILTRO** `profundidad_ratio` < `29.8` → IC=-0.129 (n=87)

  - _Acción_: SKIP cuando `profundidad_ratio` < 29.8
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `restante_min` < `3.99` → IC=-0.121 (n=101)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=41)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.139 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 9.0 (IC base=+0.084)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.141 (n=129)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=43)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.224 (n=56)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=116)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.257 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=147)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `restante_min` < `3.43` → IC=-0.263 (n=74)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=153)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=171)

- **FILTRO** `lag_apertura_s` > `91.82` → IC=-0.247 (n=77)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.82
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=150)

- **FILTRO** `profundidad_ratio` < `79.7` → IC=-0.152 (n=113)

  - _Acción_: SKIP cuando `profundidad_ratio` < 79.7
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=114)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.156 (n=149)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=80)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.5 (IC base=-0.054)

- **PATRÓN** `profundidad_ratio` > `14.6` → IC=+0.125 (n=54)

  - _Acción_: Kelly boost +0.62€ cuando `profundidad_ratio` > 14.6 (IC base=+0.025)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.224 (n=74)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=206)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=4308)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=12994)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=4324)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=13577)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.199 (n=758)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2294)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.153 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2444)

- **PATRÓN** `libro_liquidez` > `1798.6031` → IC=+0.128 (n=1038)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1798.6031 (IC base=+0.032)

- **PATRÓN** `libro_liquidez` > `1567.2992` → IC=+0.145 (n=1090)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1567.2992 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.182 (n=755)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2350)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.206 (n=757)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2485)

- **PATRÓN** `libro_liquidez` > `1794.1561` → IC=+0.130 (n=1056)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1794.1561 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.166 (n=743)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2299)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2394)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3134)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

- **FILTRO** `libro_liquidez` < `17089.2107` → IC=-0.140 (n=234)

  - _Acción_: SKIP cuando `libro_liquidez` < 17089.2107
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=705)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ballena_activa_n` > `89.0` → IC=-0.217 (n=118)

  - _Acción_: SKIP cuando `ballena_activa_n` > 89.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=232)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1922.3295` → IC=-0.176 (n=322)

  - _Acción_: SKIP cuando `libro_liquidez` < 1922.3295
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=656)

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
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=26985)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.281 (n=9155)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=29946)

- **FILTRO** `ibs_7min` < `0.2632` → IC=-0.234 (n=9769)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2632
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=29332)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=12902)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=26199)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=12108)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=37410)

- **FILTRO** `ibs_7min` > `0.2909` → IC=-0.180 (n=12377)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2909
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=37141)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=1963)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4634)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.234 (n=3256)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=3341)

- **FILTRO** `ibs_7min` < `0.7077` → IC=-0.251 (n=2177)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7077
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=4420)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.181 (n=1519)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5078)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.263 (n=2115)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6440)

- **FILTRO** `ibs_7min` > `0.7903` → IC=-0.210 (n=2138)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7903
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=6417)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.135 (n=1593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5105)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.248 (n=1644)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5054)

- **FILTRO** `ibs_7min` < `0.7428` → IC=-0.197 (n=1672)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7428
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5026)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.179 (n=1668)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=5030)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1589)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5222)

- **FILTRO** `ibs_7min` > `0.2628` → IC=-0.187 (n=1700)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2628
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5111)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.184 (n=1696)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5115)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.160 (n=1782)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=4501)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1487)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4796)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.249 (n=2073)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4210)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.212 (n=1481)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4802)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2099)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=7038)

- **FILTRO** `ibs_7min` > `0.7436` → IC=-0.175 (n=2284)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=6853)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1913)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4531)

- **FILTRO** `ibs_7min` < `0.7386` → IC=-0.186 (n=1610)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7386
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4834)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.174 (n=1582)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4862)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1638)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4960)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.178 (n=1648)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4950)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.179 (n=1640)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4958)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=1646)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=5021)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1621)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=5046)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2246)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7218)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.272 (n=1510)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=4902)

- **FILTRO** `ibs_7min` < `0.2662` → IC=-0.222 (n=1603)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2662
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4809)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1483)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4929)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.207 (n=2097)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=6856)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1193)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=590)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7904.1448` → IC=-0.131 (n=345)

  - _Acción_: SKIP cuando `libro_liquidez` < 7904.1448
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=703)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=333)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4167` → IC=+0.148 (n=581)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4167 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.119)

- **PATRÓN** `total_vol_5m` < `447.889` → IC=+0.151 (n=290)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 447.889 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.125 (n=739)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 54.0 (IC base=+0.119)

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
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 11.0 (IC base=+0.110)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4137` → IC=+0.189 (n=120)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.4137 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.110)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 73.0 (IC base=+0.110)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.162 (n=152)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.169 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 14.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `8082.459` → IC=+0.149 (n=152)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 8082.459 (IC base=+0.132)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.145 (n=153)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.126 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3602.5746` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3602.5746 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=113)

- **FILTRO** `sigma_h` > `0.0055` → IC=-0.276 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=245)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.258 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.245 (n=49)

- **FILTRO** `T_h` > `87.9981` → IC=-0.395 (n=36)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=110)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.245 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.088)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.210 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.183 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=113)

- **FILTRO** `T_h` > `72.5264` → IC=-0.147 (n=338)

  - _Acción_: SKIP cuando `T_h` > 72.5264
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=114)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.320 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=297)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.310 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=297)

- **FILTRO** `T_h` > `59.6469` → IC=-0.315 (n=296)

  - _Acción_: SKIP cuando `T_h` > 59.6469
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=99)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.159 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=118)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=118)

- **FILTRO** `T_h` > `143.8015` → IC=-0.300 (n=48)

  - _Acción_: SKIP cuando `T_h` > 143.8015
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=96)

- **FILTRO** `pct_vs_K` |x|> `3.0893` → IC=-0.446 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0893
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=109)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=96)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=91)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.190 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=85)

- **FILTRO** `sigma_h` < `0.0073` → IC=-0.200 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=84)

- **FILTRO** `T_h` > `135.1308` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=85)

- **FILTRO** `sigma_h` > `0.0109` → IC=-0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.309 (n=40)

- **FILTRO** `T_h` > `49.3826` → IC=-0.383 (n=58)

  - _Acción_: SKIP cuando `T_h` > 49.3826
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.469 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.346)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.396 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.346)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.346)

- **PATRÓN** `dist_50` > `0.4067` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4067 (IC base=+0.346)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.365 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.346)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=231)

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

- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=34)

- **FILTRO** `streak_estiramiento` > `0.4382` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4382
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=40)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_racha` < 991078.0 (IC base=-0.015)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.4382 (IC base=-0.015)

- **PATRÓN** `streak_estiramiento` < `0.381` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.381 (IC base=+0.063)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=502)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=732)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=872)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=865)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3264)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1682)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.238 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.203 (n=1807)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2192` → IC=+0.209 (n=685)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2192 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1268` → IC=+0.234 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1268 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.206 (n=1912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=2126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.6154` → IC=+0.277 (n=2053)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6154 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1201` → IC=+0.199 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1201 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.822` → IC=+0.284 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.822 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2956.4998` → IC=+0.205 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2956.4998 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.217 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.198)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=877)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.225 (n=442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.280 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.213 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2017` → IC=+0.247 (n=200)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2017 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.267 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.244 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.274 (n=441)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.395` → IC=+0.264 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.395 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.212)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.209` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.209
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=528)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.169 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0036 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.150 (n=315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.005 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.167 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.175 (n=158)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2698` → IC=+0.155 (n=352)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2698 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.659` → IC=+0.264 (n=422)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.659 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.2911` → IC=+0.151 (n=434)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2911 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.234 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3403.8093` → IC=+0.156 (n=422)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3403.8093 (IC base=+0.142)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.286 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.225 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0615` → IC=+0.202 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0615 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3271` → IC=+0.236 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3271 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.5897` → IC=+0.278 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5897 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.191 (n=241)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.263` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.263 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=267)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3082.6104` → IC=+0.289 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3082.6104 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.219 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.190)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.191` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.191 (IC base=-0.009)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.278 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.224 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0641` → IC=+0.207 (n=466)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0641 (IC base=+0.204)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0847` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0847 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.233 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.5758` → IC=+0.290 (n=522)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5758 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.2174` → IC=+0.218 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2174 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.006` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.006 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.318` → IC=+0.204 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.318 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2932.3706` → IC=+0.290 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2932.3706 (IC base=+0.204)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.141 (n=589)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` < 0.1176 (IC base=+0.057)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.359 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.361 (n=486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.357 (n=327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.380 (n=324)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.388 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.371 (n=495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.393 (n=486)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.4311` → IC=+0.387 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4311 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.362 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.954` → IC=+0.354 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.954 (IC base=+0.354)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.359 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.372 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.375 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 446.0 (IC base=+0.354)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.369 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.379 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.368 (n=89)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.360)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.367 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.383 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.395 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.382 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.392 (n=267)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.414 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.072` → IC=+0.364 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.072 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.360 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `11580.2639` → IC=+0.372 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11580.2639 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `502.0` → IC=+0.412 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 502.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.372 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.344)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.359 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.344)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.364 (n=197)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.344)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.371 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.344)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.406 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.344)

- **PATRÓN** `ibs_15` > `0.7408` → IC=+0.396 (n=220)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7408 (IC base=+0.344)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.384 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.344)

- **PATRÓN** `dist_vwap_pct` < `0.1212` → IC=+0.345 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1212 (IC base=+0.344)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.357 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.344)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.348 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.350 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `4304.5454` → IC=+0.368 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4304.5454 (IC base=+0.344)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.351 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.344)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.226 (n=782)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=2347)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1108)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2021)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1355` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1355 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.275 (n=759)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.195 (n=618)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1241` → IC=+0.254 (n=1561)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1241 (IC base=-0.021)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1797` → IC=+0.253 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1797 (IC base=-0.021)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.278 (n=2344)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6644` → IC=+0.298 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6644 (IC base=-0.021)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.210 (n=474)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1423)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.215 (n=626)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1271)

- **FILTRO** `sigma_ewma_delta_pct` > `23.623` → IC=-0.258 (n=271)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.623
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1626)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.169 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0028 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.300 (n=103)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.084)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.121 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.084)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.330 (n=227)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.289 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.274 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0841` → IC=+0.176 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0841 (IC base=-0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.191)

- **PATRÓN** `ibs_15` < `0.501` → IC=+0.306 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.501 (IC base=-0.191)

- **PATRÓN** `dist_vwap_pct` < `0.0553` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0553 (IC base=-0.191)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.191)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=470)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.158 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.171 (n=366)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0035 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.0751` → IC=+0.212 (n=161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0751 (IC base=+0.154)

- **PATRÓN** `drift_15min` |x|≤ `0.4157` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.4157 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.228 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.183 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.259 (n=367)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.1102` → IC=+0.176 (n=260)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1102 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=470)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.179 (n=166)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.247 (n=891)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1041` → IC=+0.247 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1041 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.7799` → IC=+0.249 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7799 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.264 (n=404)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.269 (n=891)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.7435` → IC=+0.311 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7435 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.25` → IC=+0.275 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.25 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.241 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.232 (n=248)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=483)

- **FILTRO** `drift_15min` |x|> `0.9054` → IC=-0.272 (n=182)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9054
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=549)

- **FILTRO** `sigma_ewma_delta_pct` > `18.27` → IC=-0.139 (n=391)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.27
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3152)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.196 (n=54)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.5625 (IC base=-0.173)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 47.0 (IC base=-0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0786` → IC=+0.228 (n=344)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0786 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1843` → IC=+0.226 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1843 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.271 (n=386)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7023` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7023 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1775` → IC=+0.230 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1775 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.264 (n=443)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=444)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.264 (n=256)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=631)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1446` → IC=+0.277 (n=271)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1446 (IC base=-0.034)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.328 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.034)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.297 (n=599)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` > `0.8735` → IC=+0.352 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8735 (IC base=-0.034)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.298 (n=696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.331 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.304 (n=264)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.218` → IC=+0.319 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.218 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.326 (n=791)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4435` → IC=+0.335 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4435 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.346 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14611.6311` → IC=+0.304 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14611.6311 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.294 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.337 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.315 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3931` → IC=+0.303 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3931 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.314 (n=433)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.352 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.15` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.15 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.323 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.308 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.297 (n=358)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.319 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.297 (n=239)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.329 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.317 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8722` → IC=+0.348 (n=320)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8722 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.312 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.334 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.297)

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
- **PATRÓN** `T_h` > `80.0063` → IC=+0.228 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.214)

- **PATRÓN** `ratio` < `0.9753` → IC=+0.471 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9753 (IC base=+0.214)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.318 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.1277` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.1277 (IC base=+0.194)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.194)

- **PATRÓN** `T_h` > `103.9325` → IC=+0.296 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.9325 (IC base=+0.288)

- **PATRÓN** `ratio` > `1.0479` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0479 (IC base=+0.288)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `81.6471` → IC=+0.273 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6471 (IC base=+0.249)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.430 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.249)

- **PATRÓN** `T_h` > `110.1026` → IC=+0.339 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.1026 (IC base=+0.320)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.353 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.320)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6154 sube el IC de +0.198 a +0.277 en UPDOWN_GBM#15min (n=2053). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.212 a +0.274 en UPDOWN_GBM#BTC#15min (n=441). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.659 sube el IC de +0.142 a +0.264 en UPDOWN_GBM#ETH#15min (n=422). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5897 sube el IC de +0.190 a +0.278 en UPDOWN_GBM#SOL#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5758 sube el IC de +0.204 a +0.290 en UPDOWN_GBM#XRP#15min (n=522). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.065 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=759). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.021 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=2344). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.084 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=227). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.191 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.154 a +0.259 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=367). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.237 a +0.269 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=891). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.173 a +0.196 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=54). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.271 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=386). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.034 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=599). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.291 a +0.326 en UPDOWN_GBM_IBS_ALTO (n=791). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.284 a +0.314 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=433). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8722 sube el IC de +0.297 a +0.348 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=320). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.354 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.360 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=267). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7408 sube el IC de +0.344 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=220). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1499 | +0.096 | +186.36€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1499 | +0.096 | +186.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1139 | +0.105 | +162.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1139 | +0.105 | +162.51€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 260 | +0.061 | +9.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 260 | +0.061 | +9.45€ | 4 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 69 | +0.106 | +14.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 69 | +0.106 | +14.73€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 66 | +0.088 | +14.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 66 | +0.088 | +14.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 55 | +0.097 | +10.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 55 | +0.097 | +10.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 11 | +0.021 | +3.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 11 | +0.021 | +3.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 32042 | -0.089 | -4243.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1640 | -0.024 | -222.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 30402 | -0.093 | -4021.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4180 | -0.112 | -692.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4180 | -0.112 | -692.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1640 | -0.024 | -222.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1640 | -0.024 | -222.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3818 | -0.114 | -880.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3818 | -0.114 | -880.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8274 | -0.012 | -777.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8274 | -0.012 | -777.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7933 | -0.100 | -500.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7933 | -0.100 | -500.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6197 | -0.164 | -1170.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6197 | -0.164 | -1170.14€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 23441 | -0.022 | +3742.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6066 | +0.001 | +1754.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 17375 | -0.029 | +1987.46€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 23441 | -0.022 | +3742.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6066 | +0.001 | +1754.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 17375 | -0.029 | +1987.46€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 109019 | +0.113 | -5208.98€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15636 | +0.183 | -484.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 457 | -0.058 | -58.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 86077 | +0.101 | -4412.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6849 | +0.106 | -253.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14299 | +0.100 | -1085.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 50 | -0.135 | +11.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14234 | +0.102 | -1084.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 21750 | +0.130 | -403.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4766 | +0.199 | -138.51€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14273 | +0.114 | -184.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2669 | +0.094 | -58.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14344 | +0.092 | -1226.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 58 | -0.117 | -8.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14271 | +0.093 | -1206.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23151 | +0.124 | -440.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6225 | +0.176 | -94.96€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14431 | +0.105 | -283.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2483 | +0.101 | -53.56€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21158 | +0.114 | -1191.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4485 | +0.188 | -264.10€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 360 | -0.019 | -4.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14616 | +0.093 | -781.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1697 | +0.130 | -141.02€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14317 | +0.099 | -861.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14252 | +0.100 | -871.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17345 | +0.195 | -1071.54€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17345 | +0.195 | -1071.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4051 | +0.173 | -385.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4051 | +0.173 | -385.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1751 | +0.201 | -21.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1751 | +0.201 | -21.80€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3995 | +0.182 | -320.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3995 | +0.182 | -320.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3532 | +0.243 | -112.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3532 | +0.243 | -112.10€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3937 | +0.190 | -245.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3937 | +0.190 | -245.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 812 | +0.431 | -20.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 812 | +0.431 | -20.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 319 | +0.441 | -1.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 319 | +0.441 | -1.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 307 | +0.432 | -6.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 307 | +0.432 | -6.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 174 | +0.409 | -10.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 174 | +0.409 | -10.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 60226 | +0.197 | -4653.52€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 60226 | +0.197 | -4653.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10366 | +0.179 | -1157.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10366 | +0.179 | -1157.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9660 | +0.222 | -362.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9660 | +0.222 | -362.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10380 | +0.174 | -1201.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10380 | +0.174 | -1201.88€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9736 | +0.218 | -389.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9736 | +0.218 | -389.95€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9974 | +0.202 | -658.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9974 | +0.202 | -658.28€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10110 | +0.192 | -883.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10110 | +0.192 | -883.32€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 22898 | +0.115 | +112.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 22898 | +0.115 | +112.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11367 | +0.119 | +119.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11367 | +0.119 | +119.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11531 | +0.111 | -6.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11531 | +0.111 | -6.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1668 | +0.289 | -23.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1668 | +0.289 | -23.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 748 | +0.280 | -15.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 748 | +0.280 | -15.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 805 | +0.287 | -11.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 805 | +0.287 | -11.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 741 | +0.438 | -0.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 741 | +0.438 | -0.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 355 | +0.436 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 355 | +0.436 | -2.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 340 | +0.442 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 340 | +0.442 | +1.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1275 | +0.066 | -67.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 448 | +0.056 | -38.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 827 | +0.072 | -29.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1005 | +0.071 | -38.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 178 | +0.067 | -8.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 827 | +0.072 | -29.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 205 | +0.027 | -32.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 205 | +0.027 | -32.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 43520 | +0.098 | -1230.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3551 | +0.091 | +39.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 39969 | +0.099 | -1270.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 24210 | +0.102 | -339.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3551 | +0.091 | +39.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 20659 | +0.104 | -379.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8518 | +0.107 | -38.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8518 | +0.107 | -38.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10792 | +0.081 | -852.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10792 | +0.081 | -852.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 862 | +0.208 | -101.16€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 862 | +0.208 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 862 | +0.208 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 862 | +0.208 | -101.16€ | 1 | 4 |
| ✅ GBM_LATE_15M | 30650 | +0.087 | +15105.47€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 30650 | +0.087 | +15105.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5142 | +0.202 | +3931.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5142 | +0.202 | +3931.87€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4576 | +0.177 | +3262.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4576 | +0.177 | +3262.21€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5416 | +0.200 | +4082.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5416 | +0.200 | +4082.20€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4378 | +0.029 | +1079.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4378 | +0.029 | +1079.55€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4361 | -0.030 | +966.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4361 | -0.030 | +966.90€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6777 | -0.037 | +1782.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6777 | -0.037 | +1782.73€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 32846 | +0.088 | +17545.27€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 32846 | +0.088 | +17545.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6303 | +0.013 | +3282.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6303 | +0.013 | +3282.05€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6825 | +0.014 | +1430.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6825 | +0.014 | +1430.48€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4652 | +0.269 | +4802.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4652 | +0.269 | +4802.72€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5466 | +0.009 | +1190.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5466 | +0.009 | +1190.14€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5301 | +0.035 | +2138.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5301 | +0.035 | +2138.71€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4299 | +0.283 | +4701.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4299 | +0.283 | +4701.15€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 24639 | +0.172 | +18941.54€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 24639 | +0.172 | +18941.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3704 | +0.215 | +3078.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3704 | +0.215 | +3078.54€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3899 | +0.149 | +2821.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3899 | +0.149 | +2821.78€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3893 | +0.212 | +3160.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3893 | +0.212 | +3160.01€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4147 | +0.136 | +3030.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4147 | +0.136 | +3030.39€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4609 | +0.121 | +3320.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4609 | +0.121 | +3320.25€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4387 | +0.207 | +3530.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4387 | +0.207 | +3530.56€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6706 | +0.138 | +3148.08€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6706 | +0.138 | +3148.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 337 | +0.143 | +187.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 337 | +0.143 | +187.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1931 | +0.141 | +1023.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1931 | +0.141 | +1023.86€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2006 | +0.153 | +977.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2006 | +0.153 | +977.82€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1524 | +0.111 | +551.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1524 | +0.111 | +551.15€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 534 | +0.134 | +230.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 534 | +0.134 | +230.88€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 30907 | +0.178 | +23625.86€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 30907 | +0.178 | +23625.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4896 | +0.229 | +4314.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4896 | +0.229 | +4314.67€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4819 | +0.148 | +3133.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4819 | +0.148 | +3133.01€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5138 | +0.227 | +4452.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5138 | +0.227 | +4452.47€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5026 | +0.134 | +3521.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5026 | +0.134 | +3521.07€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5420 | +0.120 | +3664.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5420 | +0.120 | +3664.68€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5608 | +0.211 | +4539.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5608 | +0.211 | +4539.95€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8563 | +0.172 | +5666.96€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8563 | +0.172 | +5666.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2063 | +0.166 | +1484.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2063 | +0.166 | +1484.97€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2814 | +0.178 | +1855.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2814 | +0.178 | +1855.50€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 889 | +0.150 | +514.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 889 | +0.150 | +514.52€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2190 | +0.070 | +796.80€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2190 | +0.070 | +796.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 820 | +0.090 | +292.82€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 820 | +0.090 | +292.82€ | 0 | 16 |
| ✅ GBM_LATE_60M#ETH | 700 | +0.070 | +314.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 700 | +0.070 | +314.63€ | 2 | 11 |
| ✅ GBM_LATE_60M#SOL | 670 | +0.046 | +189.36€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 670 | +0.046 | +189.36€ | 2 | 8 |
| 🚫 GBM_LATE_60M_FADE | 435 | -0.237 | -7.19€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 435 | -0.237 | -7.19€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 162 | -0.213 | -3.95€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 162 | -0.213 | -3.95€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 148 | -0.227 | +1.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 148 | -0.227 | +1.04€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 125 | -0.272 | -4.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 125 | -0.272 | -4.28€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 897 | +0.093 | +238.29€ | 0 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 897 | +0.093 | +238.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 336 | +0.086 | +79.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 336 | +0.086 | +79.03€ | 1 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 304 | +0.062 | +41.63€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 304 | +0.062 | +41.63€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 257 | +0.137 | +117.63€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 257 | +0.137 | +117.63€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 121 | +0.256 | +103.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 121 | +0.256 | +103.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 121 | +0.256 | +103.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 121 | +0.256 | +103.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2516 | +0.108 | +705.67€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2516 | +0.108 | +705.67€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2516 | +0.108 | +705.67€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2516 | +0.108 | +705.67€ | 0 | 3 |
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
| ✅ LIQUIDACIONES_5M | 2617 | +0.022 | +77.46€ | 6 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 2617 | +0.022 | +77.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 134 | +0.029 | -0.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 134 | +0.029 | -0.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 375 | +0.033 | +37.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 375 | +0.033 | +37.54€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 192 | -0.015 | -4.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 192 | -0.015 | -4.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1018 | +0.032 | +31.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1018 | +0.032 | +31.22€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 602 | +0.008 | -1.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 602 | +0.008 | -1.82€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 296 | +0.024 | +15.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 296 | +0.024 | +15.63€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1296 | -0.045 | -28.29€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1296 | -0.045 | -28.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 368 | -0.041 | -12.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 368 | -0.041 | -12.69€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 433 | -0.031 | -2.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 433 | -0.031 | -2.79€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 495 | -0.059 | -12.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 495 | -0.059 | -12.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3895 | -0.023 | +46.93€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1822 | -0.030 | -9.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2073 | -0.017 | +56.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 105 | -0.005 | +4.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 54 | +0.036 | +7.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 51 | -0.047 | -3.24€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 955 | -0.002 | +44.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 441 | -0.006 | +12.96€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 514 | +0.002 | +31.35€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 444 | -0.022 | +10.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 215 | -0.044 | -3.93€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 229 | -0.002 | +14.84€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 781 | -0.045 | -36.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 354 | -0.059 | -28.63€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 427 | -0.034 | -7.77€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 771 | -0.028 | +4.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 371 | -0.039 | -4.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 400 | -0.017 | +9.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 839 | -0.023 | +19.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 387 | -0.022 | +6.84€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 452 | -0.024 | +12.52€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 35203 | -0.004 | +1612.29€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 35203 | -0.004 | +1612.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6257 | +0.022 | +802.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6257 | +0.022 | +802.35€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5304 | -0.031 | -79.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5304 | -0.031 | -79.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6347 | +0.018 | +577.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6347 | +0.018 | +577.84€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5095 | -0.053 | -157.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5095 | -0.053 | -157.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5931 | -0.008 | +202.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5931 | -0.008 | +202.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6269 | +0.012 | +266.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6269 | +0.012 | +266.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6077 | -0.060 | -149.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6077 | -0.060 | -149.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1474 | -0.081 | -37.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1474 | -0.081 | -37.74€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 692 | -0.125 | -32.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 692 | -0.125 | -32.90€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1795 | -0.078 | -34.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1795 | -0.078 | -34.13€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 88619 | -0.072 | +1899.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 88619 | -0.072 | +1899.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15152 | -0.075 | +929.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15152 | -0.075 | +929.24€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13509 | -0.096 | -708.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13509 | -0.096 | -708.40€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15420 | -0.066 | +831.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15420 | -0.066 | +831.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13042 | -0.092 | -266.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13042 | -0.092 | -266.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16131 | -0.050 | +364.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16131 | -0.050 | +364.33€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15365 | -0.063 | +749.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15365 | -0.063 | +749.57€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7925 | -0.029 | -134.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7925 | -0.029 | -134.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1844 | -0.040 | -15.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1844 | -0.040 | -15.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2237 | -0.024 | -27.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2237 | -0.024 | -27.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1073 | -0.043 | -15.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1073 | -0.043 | -15.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 768 | -0.021 | -23.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 768 | -0.021 | -23.86€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1295 | +0.113 | +462.37€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1159 | +0.119 | +449.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 269 | +0.138 | +135.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 269 | +0.138 | +135.74€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 221 | +0.110 | +63.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 221 | +0.110 | +63.71€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 239 | +0.110 | +90.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 239 | +0.110 | +90.46€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 202 | +0.132 | +93.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 202 | +0.132 | +93.92€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 228 | +0.100 | +65.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 228 | +0.100 | +65.94€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 761 | -0.027 | -30.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 761 | -0.027 | -30.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 150 | +0.013 | +9.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 150 | +0.013 | +9.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 110 | -0.036 | -7.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 110 | -0.036 | -7.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 213 | -0.049 | -19.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 213 | -0.049 | -19.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 164 | -0.006 | -1.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 164 | -0.006 | -1.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 124 | -0.056 | -11.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 124 | -0.056 | -11.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 705 | -0.093 | -63.48€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 322 | -0.145 | -76.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 251 | -0.188 | -71.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 249 | -0.054 | -0.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 180 | -0.060 | -4.18€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 69 | -0.035 | +3.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 134 | -0.037 | +13.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 106 | -0.056 | +7.79€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 537 | -0.120 | -67.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 168 | -0.006 | +4.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 847 | -0.201 | -43.79€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 351 | -0.194 | -30.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 301 | -0.196 | -31.11€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 288 | -0.217 | -28.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 247 | -0.227 | -33.90€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 208 | -0.186 | +15.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 190 | -0.182 | +11.55€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 738 | -0.204 | -53.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 352 | +0.401 | +284.61€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 40 | +0.119 | -1.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 90 | +0.370 | +74.48€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 90 | +0.370 | +74.48€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 222 | +0.460 | +211.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 222 | +0.460 | +211.37€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 352 | +0.401 | +284.61€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 594 | +0.030 | +17.43€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 594 | +0.030 | +17.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 290 | +0.027 | +3.96€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 290 | +0.027 | +3.96€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 42 | +0.068 | +1.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 42 | +0.068 | +1.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 63 | -0.008 | -1.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 63 | -0.008 | -1.69€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 199 | +0.037 | +13.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 199 | +0.037 | +13.28€ | 3 | 5 |
| ✅ STREAK_FADE_5M | 3014 | -0.023 | -124.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3014 | -0.023 | -124.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 899 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 899 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 577 | -0.025 | -24.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 577 | -0.025 | -24.71€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1382 | -0.022 | -54.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1382 | -0.022 | -54.63€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 83 | -0.053 | -8.48€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 83 | -0.053 | -8.48€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 45 | -0.011 | -4.04€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 45 | -0.011 | -4.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9299 | +0.021 | +122.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9299 | +0.021 | +122.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2583 | +0.023 | +33.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2583 | +0.023 | +33.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2124 | +0.030 | +52.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2124 | +0.030 | +52.17€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2813 | +0.012 | +5.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2813 | +0.012 | +5.71€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1779 | +0.023 | +31.54€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1779 | +0.023 | +31.54€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8299 | +0.014 | -37.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8299 | +0.014 | -37.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3283 | +0.018 | -3.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3283 | +0.018 | -3.10€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3300 | +0.012 | -20.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3300 | +0.012 | -20.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1716 | +0.008 | -13.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1716 | +0.008 | -13.20€ | 1 | 0 |
| ✅ UPDOWN_GBM | 49710 | +0.039 | +3495.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 12808 | +0.075 | +2582.19€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1713 | +0.005 | +9.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 32036 | +0.030 | +874.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2967 | +0.004 | +32.52€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5052 | +0.075 | +640.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 955 | +0.158 | +420.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4064 | +0.057 | +221.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9552 | +0.047 | +747.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1671 | +0.090 | +383.31€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 458 | +0.013 | +5.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6011 | +0.049 | +323.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1342 | +0.005 | +34.24€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 70 | -0.083 | +0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5789 | +0.046 | +419.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 920 | +0.142 | +338.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4841 | +0.028 | +82.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 10941 | +0.029 | +553.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3188 | +0.053 | +419.06€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 451 | +0.008 | +9.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6237 | +0.024 | +125.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1004 | +0.001 | -4.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 61 | -0.119 | +3.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11126 | +0.019 | +355.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3042 | +0.029 | +244.71€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 442 | -0.002 | -0.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6968 | +0.018 | +113.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 621 | +0.006 | +2.36€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 53 | -0.154 | -4.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7248 | +0.044 | +781.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3032 | +0.091 | +775.99€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 301 | +0.002 | -2.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3915 | +0.010 | +8.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 184 | -0.118 | -0.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 648 | +0.354 | +223.58€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 648 | +0.354 | +223.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 355 | +0.360 | +121.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 355 | +0.360 | +121.09€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 293 | +0.344 | +102.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 293 | +0.344 | +102.50€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14458 | -0.031 | +3278.86€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14458 | -0.031 | +3278.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1046 | -0.052 | +381.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1046 | -0.052 | +381.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2624 | -0.115 | +66.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2624 | -0.115 | +66.20€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 573 | +0.203 | +435.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 573 | +0.203 | +435.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1674 | +0.213 | +1077.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1674 | +0.213 | +1077.83€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4274 | -0.062 | +603.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4274 | -0.062 | +603.67€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4267 | -0.070 | +713.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4267 | -0.070 | +713.68€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 168 | +0.035 | +7.74€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 168 | +0.035 | +7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 168 | +0.035 | +7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 168 | +0.035 | +7.74€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1054 | +0.291 | +874.58€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1054 | +0.291 | +874.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 577 | +0.284 | +441.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 577 | +0.284 | +441.49€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 477 | +0.297 | +433.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 477 | +0.297 | +433.09€ | 0 | 9 |
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
| ✅ WEEKLY_PRICE | 2782 | +0.306 | +1378.93€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 978 | +0.259 | +147.53€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1063 | +0.298 | +469.33€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 741 | +0.378 | +762.07€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.052) — sin ventaja clara. oversold(IBS<0.3): IC=+0.051 n=17533 | neutral: IC=+0.040 n=18512 | overbought(IBS>0.7): IC=+0.092 n=17678
  - _Datos_: n=55649 IC=+0.061 PNL=+7388.12€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 594 celda(s) pasan gate riguroso completo de 2377 evaluadas (n>=40) y 3366 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.029 < 0.08 — monitorear
  - _Datos_: n=3042 IC=+0.029 PNL=+244.71€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1063/15 IC=+0.298 PNL=+469.33€ | BTC: n=978/15 IC=+0.259 PNL=+147.53€ | SOL: n=741/15 IC=+0.378 PNL=+762.07€

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
  - _Estado_: 49648 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.115 n=460/60 | contraria IC=+0.181 n=456 | gap=-0.067 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=347, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 202 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1004/40 IC=+0.001 PNL=-4.08€ | BTC#60min: n=1342/40 IC=+0.005 PNL=+34.24€ | SOL#60min: n=621/40 IC=+0.006 PNL=+2.36€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=404226 | tras_1loss IC=+0.085 n=311750 | tras_2loss IC=+0.054 n=129252/40 | gap=-0.005 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.021 n=6202 | contrario_BTC IC=+0.036 n=5475/40 | gap=+0.015 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=416 PNL=+329.98€
  - _Datos_: n=416 IC=+0.210 PNL=+329.98€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.218 > 0.08 con n=476 PNL=+363.17€
  - _Datos_: n=476 IC=+0.218 PNL=+363.17€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.235 > 0.08 con n=47 PNL=+34.80€
  - _Datos_: n=47 IC=+0.235 PNL=+34.80€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2270 PNL=+1248.26€
  - _Datos_: n=2270 IC=+0.332 PNL=+1248.26€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=386 IC=+0.064 PNL=+39.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=386 IC=+0.064 PNL=+39.51€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=59 IC=+0.172 PNL=+35.85€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=59 IC=+0.172 PNL=+35.85€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=47648 IC=+0.038 PNL=+3355.15€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=47648 IC=+0.038 PNL=+3355.15€

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
  - _Estado_: n=2036 IC=+0.006 PNL=-0.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2036 IC=+0.006 PNL=-0.57€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=931 IC=-0.002 PNL=+33.09€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=931 IC=-0.002 PNL=+33.09€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=619 IC=+0.018 PNL=+27.70€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=619 IC=+0.018 PNL=+27.70€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.1 con n=2735 PNL=+1897.97€
  - _Datos_: n=2735 IC=+0.198 PNL=+1897.97€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1487 IC=+0.055 PNL=+107.30€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1487 IC=+0.055 PNL=+107.30€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1671 IC=+0.090 PNL=+383.31€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1671 IC=+0.090 PNL=+383.31€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.092 > 0.08 con n=7321 PNL=+1920.95€
  - _Datos_: n=7321 IC=+0.092 PNL=+1920.95€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=198 IC=-0.260 PNL=-11.26€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=198 IC=-0.260 PNL=-11.26€

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
  - _Estado_: n=669 IC=+0.022 PNL=+49.18€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=669 IC=+0.022 PNL=+49.18€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=72 IC=+0.068 PNL=+5.33€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=72 IC=+0.068 PNL=+5.33€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6743 IC=+0.006 PNL=+45.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6743 IC=+0.006 PNL=+45.23€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.256 n=121) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=121 IC=+0.256 PNL=+103.64€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=9055 IC=+0.041 PNL=+604.91€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=9055 IC=+0.041 PNL=+604.91€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=3032 IC=+0.058 PNL=+393.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3032 IC=+0.058 PNL=+393.99€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=413 PNL=+127.48€
  - _Datos_: n=413 IC=+0.112 PNL=+127.48€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.08 con n=765 PNL=+200.43€
  - _Datos_: n=765 IC=+0.147 PNL=+200.43€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.08 con n=589 PNL=+334.60€
  - _Datos_: n=589 IC=+0.114 PNL=+334.60€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64236 IC=+0.118 PNL=+23896.07€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64236 IC=+0.118 PNL=+23896.07€

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
  - _Estado_: n=7342 IC=+0.044 PNL=+616.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7342 IC=+0.044 PNL=+616.77€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=736 PNL=+280.29€
  - _Datos_: n=736 IC=+0.119 PNL=+280.29€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=1299 PNL=+1277.66€
  - _Datos_: n=1299 IC=+0.451 PNL=+1277.66€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=18191 IC=+0.061 PNL=+2389.93€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=18191 IC=+0.061 PNL=+2389.93€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.1 con n=4437 PNL=+2556.20€
  - _Datos_: n=4437 IC=+0.205 PNL=+2556.20€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.155 < -0.1 con n=302 PNL=+27.12€
  - _Datos_: n=302 IC=-0.155 PNL=+27.12€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2337 IC=+0.057 PNL=+241.58€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2337 IC=+0.057 PNL=+241.58€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.1 con n=542 PNL=+142.83€
  - _Datos_: n=542 IC=+0.121 PNL=+142.83€

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
  - _Estado_: n=22275 IC=-0.136 PNL=+1659.16€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=22275 IC=-0.136 PNL=+1659.16€

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
  - _Estado_: n=2297 IC=+0.137 PNL=+1302.20€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2297 IC=+0.137 PNL=+1302.20€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.199 > 0.08 con n=2696 PNL=+1885.34€
  - _Datos_: n=2696 IC=+0.199 PNL=+1885.34€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=5191 IC=+0.032 PNL=+266.00€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5191 IC=+0.032 PNL=+266.00€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=2502 PNL=+1348.36€
  - _Datos_: n=2502 IC=+0.090 PNL=+1348.36€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.08 con n=587 PNL=+312.08€
  - _Datos_: n=587 IC=+0.211 PNL=+312.08€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.227 < -0.1 con n=2213 PNL=-180.39€
  - _Datos_: n=2213 IC=-0.227 PNL=-180.39€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6488 IC=+0.182 PNL=+4549.75€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6488 IC=+0.182 PNL=+4549.75€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=87 PNL=+33.01€
  - _Datos_: n=87 IC=+0.107 PNL=+33.01€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2331 IC=+0.070 PNL=+723.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2331 IC=+0.070 PNL=+723.51€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.178 > 0.08 con n=2138 PNL=+1500.66€
  - _Datos_: n=2138 IC=+0.178 PNL=+1500.66€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3560 IC=-0.031 PNL=+933.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3560 IC=-0.031 PNL=+933.62€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=594 PNL=-49.01€
  - _Datos_: n=594 IC=+0.087 PNL=-49.01€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=3772 PNL=-325.05€
  - _Datos_: n=3772 IC=+0.238 PNL=-325.05€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=45 IC=+0.011 PNL=+6.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=45 IC=+0.011 PNL=+6.42€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.105 n=1289) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1289 IC=+0.105 PNL=+310.82€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.320 > 0.08 con n=326 PNL=+107.80€
  - _Datos_: n=326 IC=+0.320 PNL=+107.80€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.408 n=478) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=478 IC=+0.408 PNL=+671.48€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=10366 IC=+0.179 PNL=-1157.56€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10366 IC=+0.179 PNL=-1157.56€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.1 con n=162 PNL=+102.93€
  - _Datos_: n=162 IC=+0.213 PNL=+102.93€
