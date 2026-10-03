# Hipótesis automáticas — 2026-10-03 13:49 UTC
_Generado por shadow_postmortem.py sobre 729787 resoluciones (PNL=+87782.29€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.222 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.218 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.258 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.131)

- **PATRÓN** `banda_z` > `9.249` → IC=+0.197 (n=206)

  - _Acción_: Kelly boost +0.99€ cuando `banda_z` > 9.249 (IC base=+0.131)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.723` → IC=+0.132 (n=553)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.723 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.132 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=651)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4869.7265` → IC=+0.149 (n=206)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4869.7265 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.229 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.266 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=556)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.140)

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
- **FILTRO** `restante_s_al_confirmar` < `144.47` → IC=-0.219 (n=8130)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.47
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=24396)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `132.7` → IC=-0.267 (n=1052)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.7
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3157)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.8` → IC=-0.311 (n=962)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.8
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2887)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.95` → IC=-0.219 (n=2021)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.95
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6066)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.69` → IC=-0.326 (n=1578)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.69
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=4735)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.212 (n=15798)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=3809)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `5446.5896` → IC=+0.171 (n=2469)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5446.5896 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=16845)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=12914)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=6250)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7661.4913` → IC=+0.169 (n=2391)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7661.4913 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1825)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.222 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=1646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2347)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `15960.1808` → IC=+0.209 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15960.1808 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=391)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4624.034 (IC base=+0.091)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.095)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=914)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.095)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.355 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=1475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.364 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.256 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=894)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1317.494` → IC=+0.146 (n=780)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1317.494 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.406 (n=944)

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

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.226 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=13811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=11773)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.226 (n=5883)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=3268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=3100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=3137)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.235 (n=1291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.340 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.234)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=3075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2568)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.330 (n=956)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2022)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=2377)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1138)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `11651.323` → IC=+0.457 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11651.323 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.448 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.456 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `14760.7483` → IC=+0.446 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14760.7483 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.445 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.465 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.450 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.433)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=41109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.240 (n=18030)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=7072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.184 (n=5710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=7776)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=3650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.267 (n=4191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=7489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7496)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=3692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=2503)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2690)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=3136)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=6299)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=6048)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.137 (n=5829)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.49 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=3168)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=3012)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=3847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.2` → IC=+0.143 (n=2903)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.2 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.182 (n=3131)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.129 (n=3322)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.133 (n=2947)

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

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.735` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=60)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4919` → IC=+0.130 (n=9842)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4919 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.243 (n=3284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2214` → IC=+0.255 (n=2208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2214 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.401` → IC=+0.192 (n=2574)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.401 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.250 (n=2749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6158` → IC=+0.253 (n=2749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6158 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.3011` → IC=+0.228 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3011 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `1.4608` → IC=+0.211 (n=6870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4608 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.568` → IC=+0.137 (n=11948)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.568 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5966` → IC=+0.202 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5966 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1522` → IC=+0.177 (n=3975)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1522 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.178 (n=4333)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1942 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `0.8632` → IC=+0.176 (n=2888)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8632 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.220 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.272` → IC=+0.196 (n=6527)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.272 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.5599` → IC=+0.199 (n=6625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5599 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.213 (n=7211)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 119.0 (IC base=+0.069)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.215 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.187 (n=732)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3505` → IC=+0.183 (n=2190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3505 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=1056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.184 (n=1470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.279 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.713` → IC=+0.296 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.713 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.220 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.181 (n=2067)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2246)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2038.9448` → IC=+0.186 (n=730)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2038.9448 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.234 (n=1162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1553)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1251` → IC=+0.269 (n=764)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1251 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.251 (n=1190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.286 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.484` → IC=+0.244 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.484 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.39` → IC=+0.240 (n=1813)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.39 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0926` → IC=+0.232 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0926 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.262 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.5704` → IC=+0.244 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5704 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1587.18` → IC=+0.246 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1587.18 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.245 (n=764)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=1739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9789` → IC=+0.259 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9789 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.3504` → IC=+0.218 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3504 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.762` → IC=+0.254 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.762 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2505` → IC=+0.220 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2505 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.220 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.238 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4022` → IC=+0.216 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4022 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.3944` → IC=+0.239 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3944 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `11121.9309` → IC=+0.219 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11121.9309 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.168 (n=1170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.167 (n=584)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7206` → IC=+0.174 (n=1752)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.7206 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.154 (n=1579)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.292` → IC=+0.138 (n=280)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 11.292 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.285` → IC=+0.144 (n=1611)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.285 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.148 (n=1752)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2035 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.8505` → IC=+0.139 (n=1168)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8505 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.172 (n=468)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4443` → IC=+0.149 (n=1641)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4443 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.147 (n=1094)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `14180.1472` → IC=+0.142 (n=1168)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14180.1472 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.172 (n=690)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.199 (n=2208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.193 (n=2208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=1485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.319` → IC=+0.260 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.319 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.193 (n=1936)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.3472` → IC=+0.202 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3472 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.7627` → IC=+0.199 (n=1894)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.7627 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2636)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `1944.7352` → IC=+0.192 (n=1001)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 1944.7352 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.219 (n=1712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.1319` → IC=+0.219 (n=649)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1319 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.233 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.68` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.68 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.253 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7224` → IC=+0.215 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7224 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.221 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1935.0406` → IC=+0.214 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1935.0406 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.211 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.209)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=120)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2641)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.153 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0037 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9556` → IC=+0.219 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9556 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1966` → IC=+0.329 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1966 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.896` → IC=+0.171 (n=871)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.896 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.332 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.211` → IC=+0.319 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.211 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.345 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.349 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.8416` → IC=+0.326 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8416 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.329 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1017` → IC=+0.158 (n=691)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1017 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.3288` → IC=+0.198 (n=319)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3288 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.844` → IC=+0.150 (n=716)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.844 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `1.1641` → IC=+0.144 (n=358)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1641 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.194 (n=142)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.164 (n=912)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.023)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=401)

- **FILTRO** `ibs_20min` < `0.3111` → IC=-0.183 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3111
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=354)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.125 (n=2663)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=1312)

- **FILTRO** `sigma_ewma_delta_pct` > `8.769` → IC=-0.215 (n=419)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.769
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3556)

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

- **PATRÓN** `ibs_20min` < `0.2381` → IC=+0.132 (n=1312)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2381 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7014` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7014 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.271 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.3699` → IC=+0.289 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3699 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6494` → IC=-0.180 (n=691)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6494
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2091)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.206 (n=657)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2125)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.210 (n=1014)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=3110)

- **PATRÓN** `dist_vwap_pct` > `0.8005` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8005 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2116` → IC=+0.316 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2116 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.637` → IC=+0.310 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.637 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.297 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.303 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.299 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8321` → IC=+0.306 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8321 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.5558` → IC=+0.279 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5558 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.7234` → IC=+0.253 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7234 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.0783` → IC=+0.271 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0783 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.268 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.1375` → IC=+0.259 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1375 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.4191` → IC=+0.253 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4191 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.200 (n=4266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4715` → IC=+0.188 (n=11409)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4715 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0088` → IC=+0.289 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0088 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.158 (n=5838)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1772` → IC=+0.245 (n=4651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1772 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.692` → IC=+0.254 (n=4155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.692 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2934` → IC=+0.266 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2934 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6371` → IC=+0.256 (n=2502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6371 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=7041)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.167 (n=4133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0091 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5457` → IC=+0.157 (n=10892)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5457 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7027` → IC=+0.251 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7027 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.244` → IC=+0.249 (n=3584)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.244 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.248 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.261 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1961 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.304 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5869` → IC=+0.276 (n=2259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5869 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.280 (n=5016)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2593` → IC=-0.160 (n=886)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2593
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2658)

- **FILTRO** `ibs_20min` > `0.758` → IC=-0.171 (n=724)

  - _Acción_: SKIP cuando `ibs_20min` > 0.758
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2175)

- **FILTRO** `sigma_ewma_delta_pct` > `4.564` → IC=-0.176 (n=653)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.564
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2246)

- **PATRÓN** `ibs_20min` > `0.9049` → IC=+0.278 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9049 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.21` → IC=+0.201 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.21 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2262` → IC=+0.277 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2262 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.203 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.185` → IC=+0.239 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.185 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.234 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.434 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4828` → IC=+0.446 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4828 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.436 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8651` → IC=+0.163 (n=856)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8651 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.3003` → IC=+0.194 (n=462)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3003 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6746` → IC=+0.176 (n=1074)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6746 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.223 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.200 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4118` → IC=+0.187 (n=394)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4118 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.222 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 231.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.225 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6101` → IC=+0.227 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6101 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0722` → IC=+0.223 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0722 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.278 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.4375` → IC=+0.226 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4375 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1658` → IC=+0.232 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1658 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.276 (n=1745)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.254 (n=1963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=1748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.173` → IC=+0.284 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.173 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.264 (n=1668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `1.6197` → IC=+0.258 (n=1863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6197 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `2008.6449` → IC=+0.272 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.6449 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.301 (n=1617)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.184` → IC=+0.300 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.184 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.318 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3563` → IC=+0.291 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3563 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `0.0986` → IC=+0.287 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0986 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.684` → IC=+0.292 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.684 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1193` → IC=+0.292 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1193 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.57` → IC=+0.298 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.57 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6513` → IC=+0.293 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6513 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1928.6248` → IC=+0.305 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1928.6248 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.288 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7715` → IC=-0.186 (n=737)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7715
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=2216)

- **PATRÓN** `ibs_20min` > `0.9037` → IC=+0.176 (n=662)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.9037 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.4008` → IC=+0.231 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4008 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.009` → IC=+0.248 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.009 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0816` → IC=+0.254 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0816 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4046` → IC=+0.267 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4046 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.258 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.135` → IC=+0.232 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.135 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `1.1677` → IC=+0.218 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1677 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.8268` → IC=+0.268 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8268 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.4743` → IC=+0.236 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4743 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.255 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7586` → IC=-0.184 (n=1351)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7586
  - _Potencial_: sin este filtro IC_bueno=+0.284 (n=1354)

- **FILTRO** `ibs_20min` > `0.675` → IC=-0.240 (n=678)

  - _Acción_: SKIP cuando `ibs_20min` > 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2039)

- **FILTRO** `sigma_ewma_delta_pct` > `4.794` → IC=-0.201 (n=579)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.794
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2138)

- **PATRÓN** `ibs_20min` > `0.7586` → IC=+0.284 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7586 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `1.0762` → IC=+0.333 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0762 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.169 (n=430)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8573` → IC=+0.309 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8573 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.302 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.300 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2733` → IC=+0.294 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2733 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.324 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.323 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.132 (n=1797)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.2709` → IC=+0.240 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2709 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.268 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1879` → IC=+0.225 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1879 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.0949` → IC=+0.227 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0949 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0688` → IC=+0.249 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0688 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4082` → IC=+0.248 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4082 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.257 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.020)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.327 (n=1415)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.303 (n=744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `0.6454` → IC=+0.315 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6454 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2152` → IC=+0.316 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2152 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.309 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `0.6276` → IC=+0.296 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6276 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.328 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.294 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2474.544` → IC=+0.295 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.544 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.321 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.315 (n=1116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1961` → IC=+0.288 (n=737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1961 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.288 (n=1593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.3774` → IC=+0.309 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3774 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.3173` → IC=+0.296 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3173 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` < `0.2319` → IC=+0.283 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2319 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.54` → IC=+0.298 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.54 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` < `0.642` → IC=+0.284 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.642 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.316 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.340 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.292 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.1363` → IC=+0.280 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1363 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2430.526` → IC=+0.288 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2430.526 (IC base=+0.283)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.182 (n=3208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0048 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.206 (n=3203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.3622` → IC=+0.182 (n=8456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3622 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=10018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.226 (n=9606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1737` → IC=+0.196 (n=4132)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1737 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.405` → IC=+0.255 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.405 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.166 (n=6394)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2068 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.629` → IC=+0.161 (n=6395)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.629 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.199 (n=1422)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.559` → IC=+0.170 (n=4073)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.559 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.599` → IC=+0.181 (n=3084)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.599 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1976.9103` → IC=+0.175 (n=8582)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1976.9103 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.188 (n=8531)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 107.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.186 (n=6148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.217 (n=3071)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=3504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.4876` → IC=+0.229 (n=9202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4876 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1727` → IC=+0.167 (n=6430)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1727 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.316` → IC=+0.196 (n=1546)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.316 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.160 (n=6608)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1777 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.215 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5534` → IC=+0.172 (n=3743)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5534 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5977` → IC=+0.172 (n=2836)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5977 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.181 (n=8172)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 108.0 (IC base=+0.172)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.238 (n=537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.207 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.3412` → IC=+0.219 (n=1609)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3412 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.9126` → IC=+0.287 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9126 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.245` → IC=+0.331 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.245 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.246 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.196 (n=1503)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2040.92` → IC=+0.201 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2040.92 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.251 (n=1075)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=1096)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0705` → IC=+0.309 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0705 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=1090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.263 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.213` → IC=+0.249 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.213 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.263 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4163` → IC=+0.267 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4163 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1585.6447` → IC=+0.255 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1585.6447 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.231 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0712` → IC=+0.194 (n=482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0712 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=1446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.3884` → IC=+0.222 (n=1445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3884 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.204 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.227 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6882` → IC=+0.169 (n=636)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6882 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.201 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4117` → IC=+0.177 (n=469)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4117 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4812` → IC=+0.158 (n=469)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4812 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `11954.6752` → IC=+0.157 (n=1291)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 11954.6752 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.165 (n=601)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 235.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2319` → IC=+0.174 (n=1343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2319 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.591` → IC=+0.195 (n=1526)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.591 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1346` → IC=+0.168 (n=1512)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1346 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.882` → IC=+0.196 (n=301)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.882 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2126` → IC=+0.160 (n=1526)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2126 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0696` → IC=+0.148 (n=682)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0696 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4573` → IC=+0.150 (n=1414)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4573 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.752` → IC=+0.141 (n=943)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.752 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=445)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.226 (n=727)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2513` → IC=+0.217 (n=1070)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2513 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.464` → IC=+0.281 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.464 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1277` → IC=+0.208 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1277 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.7137` → IC=+0.217 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7137 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2007.5584` → IC=+0.211 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.5584 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.236 (n=1212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1012` → IC=+0.261 (n=459)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1012 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.246 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.649` → IC=+0.252 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.649 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3508` → IC=+0.259 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3508 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7377` → IC=+0.236 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7377 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.7427` → IC=+0.227 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7427 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1930.703` → IC=+0.224 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.703 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.212 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.184 (n=1361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4235` → IC=+0.166 (n=1547)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4235 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.34` → IC=+0.204 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.34 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.186 (n=1007)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.946` → IC=+0.227 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.946 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.163 (n=1032)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.856 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.181 (n=646)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4269` → IC=+0.167 (n=505)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4269 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5102` → IC=+0.165 (n=505)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5102 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5139.067` → IC=+0.192 (n=1030)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 5139.067 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.155 (n=1485)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 154.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=1616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3872` → IC=+0.146 (n=1616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3872 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6652` → IC=+0.179 (n=1616)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6652 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1534` → IC=+0.145 (n=1583)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1534 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.865` → IC=+0.166 (n=560)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.865 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8555` → IC=+0.153 (n=1078)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8555 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.180 (n=239)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.139 (n=994)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.5241` → IC=+0.129 (n=497)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5241 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `4266.2624` → IC=+0.158 (n=1077)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4266.2624 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.125 (n=1263)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 127.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.164 (n=796)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0101 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.585` → IC=+0.126 (n=1755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.585 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.211 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0806` → IC=+0.216 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0806 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.866` → IC=+0.261 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.866 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2106` → IC=+0.136 (n=1754)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2106 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.131 (n=1755)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6466 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1613` → IC=+0.132 (n=1765)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1613 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.0704` → IC=+0.127 (n=727)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0704 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.5371` → IC=+0.144 (n=746)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5371 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1835)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.200 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.144 (n=1393)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 47.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.159 (n=782)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.174 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5773` → IC=+0.217 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5773 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.1993` → IC=+0.148 (n=1639)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1993 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.334` → IC=+0.133 (n=540)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 5.334 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.151 (n=592)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6381 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.227` → IC=+0.159 (n=309)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.227 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.143 (n=541)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4132` → IC=+0.126 (n=541)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4132 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2744.0462` → IC=+0.181 (n=805)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2744.0462 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.126 (n=1573)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.230 (n=1475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2933` → IC=+0.213 (n=1102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2933 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.209` → IC=+0.214 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.209 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.602` → IC=+0.248 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.602 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.1926` → IC=+0.211 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1926 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.217 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2779` → IC=+0.270 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2779 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.212 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.8022` → IC=+0.217 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8022 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2466.2754` → IC=+0.208 (n=1475)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2466.2754 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.226 (n=745)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.216 (n=1129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.235 (n=564)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4305` → IC=+0.243 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4305 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `1.2084` → IC=+0.226 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2084 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.253 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.1733` → IC=+0.212 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1733 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.703` → IC=+0.221 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.703 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.275 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.1933` → IC=+0.205 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1933 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.212 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2404.776` → IC=+0.218 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.776 (IC base=+0.212)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.191 (n=1115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0042 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.171 (n=844)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0085 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3463` → IC=+0.178 (n=2227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3463 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=1249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.4951` → IC=+0.204 (n=2260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4951 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.8093` → IC=+0.186 (n=403)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.8093 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.742` → IC=+0.192 (n=1107)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.742 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8717` → IC=+0.189 (n=1501)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8717 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.176 (n=752)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2084 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1629` → IC=+0.178 (n=672)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1629 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4373` → IC=+0.183 (n=818)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4373 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.8204` → IC=+0.173 (n=1636)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8204 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2873)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2687.8872` → IC=+0.170 (n=2260)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2687.8872 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.187 (n=2308)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 142.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.137 (n=1735)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0056 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0699` → IC=+0.192 (n=867)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0699 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.123 (n=985)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.144 (n=840)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4404 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2751.2995` → IC=+0.124 (n=2321)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2751.2995 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.126 (n=1099)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 28.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.185 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0029 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3342` → IC=+0.162 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3342 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.6393` → IC=+0.204 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6393 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.2987` → IC=+0.162 (n=232)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.2987 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.164 (n=293)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.952` → IC=+0.142 (n=704)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.952 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8924` → IC=+0.170 (n=449)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8924 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1564` → IC=+0.144 (n=701)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1564 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.144 (n=265)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.2117` → IC=+0.151 (n=577)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2117 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.5114` → IC=+0.147 (n=585)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5114 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10893.4165` → IC=+0.151 (n=672)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10893.4165 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.193 (n=285)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 152.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3463` → IC=+0.160 (n=813)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3463 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.179 (n=715)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6119 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1832` → IC=+0.155 (n=804)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1832 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.074` → IC=+0.146 (n=743)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.074 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2204` → IC=+0.144 (n=813)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2204 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.154 (n=726)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.693 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.200 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.156 (n=707)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4081` → IC=+0.147 (n=803)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4081 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `12071.9003` → IC=+0.143 (n=726)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 12071.9003 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `294.0` → IC=+0.154 (n=688)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 294.0 (IC base=+0.140)

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

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.123 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 11.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0873` → IC=+0.148 (n=248)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.0873 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.139 (n=328)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6872 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `7918.7339` → IC=+0.135 (n=496)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7918.7339 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.169 (n=533)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0059 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.5425` → IC=+0.154 (n=597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.5425 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.189 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.9831` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9831 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.339` → IC=+0.207 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.339 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.174 (n=525)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0671 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6526` → IC=+0.161 (n=597)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6526 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1709` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1709 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4613` → IC=+0.155 (n=192)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4613 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.169 (n=261)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=632)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3082.2108` → IC=+0.192 (n=199)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3082.2108 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.4722` → IC=+0.152 (n=507)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.4722 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.5684` → IC=+0.138 (n=241)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5684 (IC base=+0.061)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.177 (n=4166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.210 (n=4142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=12994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.9919` → IC=+0.309 (n=4143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9919 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.9227` → IC=+0.202 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9227 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.250 (n=3073)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.8798` → IC=+0.171 (n=5557)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8798 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.200 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5787` → IC=+0.197 (n=4002)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.5787 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `1806.84` → IC=+0.179 (n=12423)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1806.84 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.202 (n=9723)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=7463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1502` → IC=+0.192 (n=4919)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1502 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.246 (n=9838)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4524 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2477` → IC=+0.163 (n=6986)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2477 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.05` → IC=+0.203 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.05 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.731` → IC=+0.183 (n=10798)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.731 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.162 (n=3342)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7044 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.245 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.5999` → IC=+0.191 (n=3471)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5999 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1738.9` → IC=+0.183 (n=11179)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1738.9 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=6725)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.241 (n=696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.228 (n=688)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.3577` → IC=+0.209 (n=2059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3577 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.331 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.358 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.260 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.2347` → IC=+0.218 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2347 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2039.32` → IC=+0.217 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2039.32 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.231 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.263 (n=1121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=1685)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1255` → IC=+0.283 (n=741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1255 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=1515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3605` → IC=+0.285 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3605 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.508` → IC=+0.260 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.508 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.438` → IC=+0.259 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.438 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.291 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.5472` → IC=+0.258 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5472 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6156` → IC=+0.275 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6156 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1585.6447` → IC=+0.270 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1585.6447 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.204 (n=666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.161 (n=878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.2876` → IC=+0.203 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2876 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1267` → IC=+0.181 (n=1126)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1267 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.178 (n=436)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.182` → IC=+0.149 (n=1823)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.182 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.7006` → IC=+0.168 (n=878)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7006 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.194 (n=282)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.1285` → IC=+0.158 (n=1706)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1285 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.5107` → IC=+0.150 (n=1732)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5107 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `11444.8195` → IC=+0.153 (n=1783)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11444.8195 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.172 (n=833)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 278.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.3306` → IC=+0.160 (n=1675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3306 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.2936` → IC=+0.239 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2936 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.164 (n=1529)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.211` → IC=+0.150 (n=796)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.211 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.148 (n=1525)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.160 (n=1675)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1894 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.199 (n=446)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4127` → IC=+0.155 (n=1576)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4127 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7588` → IC=+0.160 (n=1051)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7588 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `348.0` → IC=+0.147 (n=995)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 348.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.257 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=1830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.302 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.2056` → IC=+0.223 (n=2042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2056 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.231 (n=1745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2420)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2015.955` → IC=+0.231 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2015.955 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.240 (n=1677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.233 (n=1702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.1832` → IC=+0.242 (n=839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1832 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.300 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.902` → IC=+0.278 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.902 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3406` → IC=+0.293 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3406 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.237 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1475` → IC=+0.238 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1475 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1929.0262` → IC=+0.245 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1929.0262 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.233 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.200 (n=711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4358` → IC=+0.153 (n=2125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4358 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2719` → IC=+0.189 (n=2124)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2719 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3627` → IC=+0.160 (n=819)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3627 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.168 (n=344)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8727` → IC=+0.162 (n=1417)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8727 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.159 (n=909)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1631` → IC=+0.155 (n=937)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1631 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7528.5122` → IC=+0.231 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7528.5122 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.176 (n=668)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 71.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.167 (n=1141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0051 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4451` → IC=+0.141 (n=1711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4451 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.5979` → IC=+0.195 (n=1506)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5979 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1542` → IC=+0.131 (n=1502)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1542 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.285` → IC=+0.165 (n=258)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.285 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8727` → IC=+0.137 (n=1141)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8727 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.218 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.140 (n=1638)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `9323.6962` → IC=+0.202 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9323.6962 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.129 (n=1643)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 169.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.143 (n=1423)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0081 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5742` → IC=+0.128 (n=2128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5742 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.202 (n=2127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0673` → IC=+0.211 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0673 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.552` → IC=+0.244 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.552 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8904` → IC=+0.148 (n=1419)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8904 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1604` → IC=+0.128 (n=2193)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1604 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.125 (n=1380)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4546` → IC=+0.127 (n=2070)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4546 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2164)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2549.1679` → IC=+0.234 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2549.1679 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.145 (n=1301)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 42.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.181 (n=679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0058 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1353` → IC=+0.157 (n=675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1353 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5065` → IC=+0.233 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5065 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.139 (n=1688)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.463` → IC=+0.127 (n=1952)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.463 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.645` → IC=+0.163 (n=675)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.645 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2195` → IC=+0.186 (n=320)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2195 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.1452` → IC=+0.133 (n=1636)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1452 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2799.1755` → IC=+0.193 (n=675)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2799.1755 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.133 (n=1615)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.231 (n=1865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.216 (n=1513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2134` → IC=+0.233 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2134 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.264` → IC=+0.277 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.264 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.0566` → IC=+0.216 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0566 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.221 (n=2088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.242 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.241 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2464.3002` → IC=+0.218 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.3002 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.219 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.228 (n=992)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0228 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.226 (n=1542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.262 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `1.2245` → IC=+0.217 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2245 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.216 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.857` → IC=+0.259 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.857 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.237 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.283 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `2.1751` → IC=+0.204 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1751 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.210 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2413.8398` → IC=+0.214 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2413.8398 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.202 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.211)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=3688)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.221 (n=1224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.5066` → IC=+0.191 (n=3667)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5066 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=1368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=1674)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.239 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1719` → IC=+0.191 (n=1356)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1719 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.4483` → IC=+0.179 (n=2412)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.4483 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.22` → IC=+0.214 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.22 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7106` → IC=+0.186 (n=1108)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7106 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.8944` → IC=+0.183 (n=1678)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8944 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.209 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.190 (n=1207)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.186 (n=2413)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8611 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2733)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2523.314` → IC=+0.186 (n=3666)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2523.314 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.216 (n=927)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3841` → IC=+0.181 (n=2444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3841 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.1825` → IC=+0.185 (n=1222)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1825 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.183 (n=518)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` < `0.2383` → IC=+0.153 (n=2467)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2383 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.211` → IC=+0.169 (n=2771)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.211 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2581` → IC=+0.165 (n=2614)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2581 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.166 (n=2538)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2219` → IC=+0.162 (n=575)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2219 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.169 (n=1208)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8237` → IC=+0.171 (n=1829)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8237 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=3688)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `5324.87` → IC=+0.166 (n=2482)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5324.87 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.166 (n=1809)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 86.0 (IC base=+0.161)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.233 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.267 (n=170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.220 (n=234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.231 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.516 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.7635` → IC=+0.208 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7635 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3275` → IC=+0.215 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3275 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.566` → IC=+0.208 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.566 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2189` → IC=+0.214 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2189 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.5931` → IC=+0.218 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5931 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.221 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `12584.6611` → IC=+0.237 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12584.6611 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.225 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.162 (n=1051)
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

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.151 (n=476)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6084 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6676` → IC=+0.193 (n=99)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6676 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.377` → IC=+0.167 (n=1033)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.377 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.187 (n=701)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8812 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.5395` → IC=+0.156 (n=1047)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5395 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.164 (n=698)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `12148.8643` → IC=+0.159 (n=938)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12148.8643 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.159 (n=1006)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.171 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.121 (n=534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 16.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6471` → IC=+0.181 (n=969)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6471 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1429` → IC=+0.145 (n=587)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1429 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.190 (n=253)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.191 (n=147)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.2302` → IC=+0.260 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2302 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.201` → IC=+0.135 (n=475)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.201 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.09` → IC=+0.149 (n=360)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.09 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.1401` → IC=+0.202 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1401 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.5523` → IC=+0.152 (n=369)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5523 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` > `1.4507` → IC=+0.143 (n=329)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4507 (IC base=+0.051)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.140 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0058 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4419` → IC=+0.169 (n=373)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4419 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.165 (n=198)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.126 (n=332)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.124 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0053 (IC base=+0.089)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.202 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.2737` → IC=+0.268 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2737 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.0689` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0689 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.178 (n=197)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `1.151` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.151 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.8122` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8122 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.412` → IC=+0.167 (n=181)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.412 (IC base=+0.089)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.127 (n=156)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=319)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=162)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.144 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0048 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.220 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.279 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.7834` → IC=+0.149 (n=203)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7834 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.154 (n=316)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.7058` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7058 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.011` → IC=-0.256 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=131)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.261 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=89)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.178 (n=237)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7647 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.052)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.139 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.011 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `0.5953` → IC=+0.128 (n=100)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.5953 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1332` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1332 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.0771` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.0771 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.7925` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7925 (IC base=+0.040)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.040)

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
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=152)

- **FILTRO** `ibs_20min` > `0.92` → IC=-0.327 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` > 0.92
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=152)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=180)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=97)

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
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=55)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=49)

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
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.179 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0059 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.126 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6472` → IC=+0.143 (n=345)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6472 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.4941` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4941 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.7233` → IC=+0.123 (n=152)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.7233 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.127 (n=164)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.138 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 14.0 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.181 (n=318)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1558 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.636` → IC=+0.218 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.636 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.132 (n=286)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.084)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6292` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6292
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=102)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.183 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0025 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.230 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.222 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1381 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1082` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1082 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.611` → IC=+0.189 (n=130)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 4.611 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.1471` → IC=+0.167 (n=160)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1471 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6754 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1891` → IC=+0.221 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1891 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.6699` → IC=+0.210 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6699 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.179 (n=129)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `4599.6467` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4599.6467 (IC base=+0.156)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.252 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9459` → IC=+0.228 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9459 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.6436` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6436 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.768` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.768 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.224)

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
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1106)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2936.2954` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2936.2954 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1106)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2936.2954` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2936.2954 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.102)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2486)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=572)

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
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=748)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=748)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=480)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=480)

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
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=288)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=288)

- **FILTRO** `libro_liquidez` < `553.1995` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `libro_liquidez` < 553.1995
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=172)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.48` → IC=-0.120 (n=1386)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=757)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **FILTRO** `lag_apertura_s` > `66.89` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.89
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

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

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.150 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=48)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.230 (n=61)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=125)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=154)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=198)

- **FILTRO** `restante_min` < `3.43` → IC=-0.228 (n=79)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=163)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=186)

- **FILTRO** `lag_apertura_s` > `91.82` → IC=-0.214 (n=82)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.82
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=160)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.163 (n=4382)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=13268)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.164 (n=4396)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=13872)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.198 (n=772)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2350)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.151 (n=775)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=2494)

- **PATRÓN** `libro_liquidez` > `1803.16` → IC=+0.133 (n=1062)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1803.16 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `1573.34` → IC=+0.143 (n=1112)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1573.34 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.177 (n=770)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2397)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=767)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2541)

- **PATRÓN** `libro_liquidez` > `1800.4784` → IC=+0.131 (n=1077)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1800.4784 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.163 (n=755)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2356)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2420)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3160)

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
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=281)

- **FILTRO** `ibs_20min` > `0.9763` → IC=-0.210 (n=91)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9763
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=276)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1934.3745` → IC=-0.173 (n=325)

  - _Acción_: SKIP cuando `libro_liquidez` < 1934.3745
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=660)

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
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=27479)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=9352)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=30520)

- **FILTRO** `ibs_7min` < `0.2612` → IC=-0.233 (n=9968)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2612
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=29904)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=13527)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=26345)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=12317)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=38216)

- **FILTRO** `ibs_7min` > `0.2908` → IC=-0.181 (n=12627)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2908
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=37906)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=2016)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4742)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=1620)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=5138)

- **FILTRO** `ibs_7min` < `0.7077` → IC=-0.250 (n=2229)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7077
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=4529)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.182 (n=1534)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5224)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.265 (n=2150)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6581)

- **FILTRO** `ibs_7min` > `0.7895` → IC=-0.208 (n=2181)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7895
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=6550)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=1626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5195)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.248 (n=1673)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5148)

- **FILTRO** `ibs_7min` < `0.7428` → IC=-0.197 (n=1703)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7428
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5118)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.177 (n=1697)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=5124)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1624)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5322)

- **FILTRO** `ibs_7min` > `0.2631` → IC=-0.190 (n=1735)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2631
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5211)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.187 (n=1726)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5220)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.160 (n=1834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=4586)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1525)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4895)

- **FILTRO** `ibs_7min` < `0.7022` → IC=-0.246 (n=2117)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7022
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4303)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.213 (n=1494)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4926)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=2136)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=7191)

- **FILTRO** `ibs_7min` > `0.7431` → IC=-0.174 (n=2331)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7431
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=6996)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.236 (n=1951)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4605)

- **FILTRO** `ibs_7min` < `0.7392` → IC=-0.188 (n=1639)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7392
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4917)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.176 (n=1602)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4954)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1668)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5076)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.179 (n=1685)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=5059)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.182 (n=1658)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=5086)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.264 (n=1687)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=5094)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1661)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=5120)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2298)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7357)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.273 (n=1540)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=4996)

- **FILTRO** `ibs_7min` < `0.26` → IC=-0.221 (n=1633)

  - _Acción_: SKIP cuando `ibs_7min` < 0.26
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4903)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1494)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5042)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.210 (n=2130)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=7000)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1200)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=598)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=483)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.134 (n=886)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 14.0 (IC base=+0.120)

- **PATRÓN** `total_vol_5m` < `442.4725` → IC=+0.150 (n=295)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 442.4725 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.128 (n=750)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 53.0 (IC base=+0.120)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.167 (n=70)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.231 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.140 (n=223)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.04 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2602.0106` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2602.0106 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.170 (n=92)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 12.0 (IC base=+0.140)

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
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.173 (n=157)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `8082.459` → IC=+0.154 (n=157)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 8082.459 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 28.0 (IC base=+0.135)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.147 (n=154)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.126 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=113)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.235 (n=326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=162)

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
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.202 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0087` → IC=-0.180 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=154)

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
- **FILTRO** `T_h` > `68.7654` → IC=-0.147 (n=117)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=40)

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
- **FILTRO** `T_h` > `135.9851` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=96)

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

- **FILTRO** `pct_vs_K` |x|> `4.1091` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.1091
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=52)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=522)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=744)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=889)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=884)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3292)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1709)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.213 (n=708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.242 (n=707)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0507` → IC=+0.210 (n=708)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0507 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2202` → IC=+0.212 (n=707)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2202 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.235 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=1967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=2195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.6173` → IC=+0.281 (n=2121)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6173 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.204 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.825` → IC=+0.279 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.825 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2951.9394` → IC=+0.209 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2951.9394 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.220 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.202)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=911)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.230 (n=450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.276 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.246 (n=203)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.215)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.271 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.276 (n=449)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.269 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.215)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.104` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.104
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=545)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.195 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0035 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.170 (n=213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.177 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1204` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1204 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.166 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.149 (n=223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.6559` → IC=+0.270 (n=433)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6559 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.2829` → IC=+0.159 (n=447)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2829 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.546` → IC=+0.238 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.546 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3410.3513` → IC=+0.164 (n=433)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3410.3513 (IC base=+0.149)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.286 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.217 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0615` → IC=+0.201 (n=259)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0615 (IC base=+0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3438` → IC=+0.243 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3438 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_15` > `0.5897` → IC=+0.278 (n=259)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5897 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.1223` → IC=+0.219 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1223 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.362 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3201.6733` → IC=+0.298 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3201.6733 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.217 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.189)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.289 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.226 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.210)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0641` → IC=+0.215 (n=478)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0641 (IC base=+0.210)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0847` → IC=+0.264 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0847 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.210)

- **PATRÓN** `ibs_15` > `0.5806` → IC=+0.293 (n=534)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5806 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.1349` → IC=+0.221 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1349 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.567` → IC=+0.210 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.567 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.188` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.188 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.305` → IC=+0.210 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.305 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2932.3706` → IC=+0.294 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2932.3706 (IC base=+0.210)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.147 (n=598)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` < 0.1154 (IC base=+0.059)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.366 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.364 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.360 (n=333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.383 (n=332)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.391 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.373 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.396 (n=498)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.4306` → IC=+0.387 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4306 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.366 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.357 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.357)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.362 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `3819.0399` → IC=+0.375 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3819.0399 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.379 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 446.0 (IC base=+0.357)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.348)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.348)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.363 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.348)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.368 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.348)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.375 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.348)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.408 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.348)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.399 (n=226)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.348)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.348)

- **PATRÓN** `dist_vwap_pct` < `0.2966` → IC=+0.350 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2966 (IC base=+0.348)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.363 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.348)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.352 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.348)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.354 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.348)

- **PATRÓN** `libro_liquidez` > `4242.86` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.86 (IC base=+0.348)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.356 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.348)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.220 (n=798)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=2396)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.203 (n=1137)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2057)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.183 (n=519)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=-0.061)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.252 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=-0.061)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.281 (n=778)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.4246` → IC=+0.203 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4246 (IC base=-0.061)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1241` → IC=+0.252 (n=1608)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1241 (IC base=-0.021)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1819` → IC=+0.251 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1819 (IC base=-0.021)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.275 (n=2414)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6631` → IC=+0.298 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6631 (IC base=-0.021)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.206 (n=478)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1436)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.219 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1436)

- **FILTRO** `sigma_ewma_delta_pct` > `23.635` → IC=-0.257 (n=270)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.635
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1644)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.163 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0028 (IC base=+0.087)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.304 (n=105)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.087)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.330 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.122 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.087)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.333 (n=231)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.290 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.2377` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2377 (IC base=+0.087)

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
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=485)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.170 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0065 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.168 (n=377)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0034 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.220 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.163)

- **PATRÓN** `drift_15min` |x|≤ `0.4128` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4128 (IC base=+0.163)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.164 (n=251)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.163)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.234 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.188 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 11.0 (IC base=+0.163)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.266 (n=378)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.2829` → IC=+0.175 (n=349)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2829 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=485)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3762.3` → IC=+0.167 (n=337)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3762.3 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.247 (n=907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1026` → IC=+0.244 (n=303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1026 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.774` → IC=+0.250 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.774 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2074` → IC=+0.266 (n=412)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2074 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.239 (n=639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.270 (n=907)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.7515` → IC=+0.306 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7515 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.25` → IC=+0.277 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.25 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.241 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.232 (n=252)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=493)

- **FILTRO** `drift_15min` |x|> `0.8935` → IC=-0.271 (n=186)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8935
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=559)

- **FILTRO** `sigma_ewma_delta_pct` > `18.27` → IC=-0.144 (n=400)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.27
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.151 (n=41)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.173)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.219 (n=55)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=-0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1248` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1248 (IC base=-0.173)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 44.0 (IC base=-0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0777` → IC=+0.228 (n=351)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0777 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1843` → IC=+0.228 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1843 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.271 (n=395)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.6964` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6964 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1683` → IC=+0.235 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1683 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0196` → IC=-0.259 (n=450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=451)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=265)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=636)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1449` → IC=+0.273 (n=276)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1449 (IC base=-0.033)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1679` → IC=+0.308 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1679 (IC base=-0.033)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=610)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` > `0.8607` → IC=+0.355 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8607 (IC base=-0.033)

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
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.307 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.330 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.311 (n=268)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.221` → IC=+0.323 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.221 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.328 (n=804)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2727` → IC=+0.330 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2727 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.348 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `14611.6311` → IC=+0.304 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14611.6311 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.294 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.332 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.286)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.286 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.312 (n=147)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.304 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.315 (n=440)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.341 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.15` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.15 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.326 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.320 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.301)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.300 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0035 (IC base=+0.301)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.322 (n=161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.301)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.300 (n=243)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.301)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.332 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.319 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.301)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.339 (n=364)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.312 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.337 (n=170)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6173 sube el IC de +0.202 a +0.281 en UPDOWN_GBM#15min (n=2121). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.215 a +0.276 en UPDOWN_GBM#BTC#15min (n=449). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6559 sube el IC de +0.149 a +0.270 en UPDOWN_GBM#ETH#15min (n=433). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5897 sube el IC de +0.189 a +0.278 en UPDOWN_GBM#SOL#15min (n=259). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5806 sube el IC de +0.210 a +0.293 en UPDOWN_GBM#XRP#15min (n=534). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.061 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=778). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.021 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=2414). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.087 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=231). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.192 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.163 a +0.266 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=378). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.361 sube el IC de +0.237 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=907). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de -0.173 a +0.219 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.040 a +0.271 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=395). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.033 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=610). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.293 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=804). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.286 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=440). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.301 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=364). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.357 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=498). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.363 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=273). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.348 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=226). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1507 | +0.096 | +187.84€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1507 | +0.096 | +187.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1144 | +0.105 | +163.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1144 | +0.105 | +163.74€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 261 | +0.063 | +9.98€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 261 | +0.063 | +9.98€ | 6 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 71 | +0.103 | +14.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 71 | +0.103 | +14.46€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 101 | +0.034 | +17.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 101 | +0.034 | +17.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 80 | +0.049 | +14.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 80 | +0.049 | +14.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 21 | -0.022 | +3.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 21 | -0.022 | +3.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 32526 | -0.090 | -4336.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1670 | -0.020 | -220.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 30856 | -0.093 | -4116.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4209 | -0.114 | -703.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4209 | -0.114 | -703.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1670 | -0.020 | -220.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1670 | -0.020 | -220.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3849 | -0.116 | -866.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3849 | -0.116 | -866.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8398 | -0.007 | -763.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8398 | -0.007 | -763.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 8087 | -0.104 | -572.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 8087 | -0.104 | -572.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6313 | -0.167 | -1210.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6313 | -0.167 | -1210.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 24052 | -0.021 | +3689.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6226 | +0.001 | +1745.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 17826 | -0.029 | +1944.30€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 24052 | -0.021 | +3689.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6226 | +0.001 | +1745.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 17826 | -0.029 | +1944.30€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 110836 | +0.113 | -5227.28€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15789 | +0.183 | -492.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 466 | -0.056 | -59.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 87631 | +0.102 | -4406.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6950 | +0.105 | -269.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14557 | +0.101 | -1092.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 51 | -0.141 | +9.84€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14491 | +0.102 | -1090.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 22076 | +0.130 | -380.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4794 | +0.199 | -129.87€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14530 | +0.115 | -162.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2710 | +0.093 | -65.92€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14601 | +0.092 | -1229.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 59 | -0.107 | -4.41€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14527 | +0.094 | -1214.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23544 | +0.124 | -445.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6317 | +0.176 | -102.41€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14691 | +0.106 | -273.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2524 | +0.099 | -61.64€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21485 | +0.114 | -1220.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4516 | +0.187 | -275.10€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 369 | -0.018 | -5.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14884 | +0.093 | -797.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1716 | +0.130 | -142.13€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14573 | +0.100 | -858.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14508 | +0.100 | -868.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17669 | +0.195 | -1093.59€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17669 | +0.195 | -1093.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4119 | +0.175 | -382.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4119 | +0.175 | -382.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1815 | +0.202 | -21.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1815 | +0.202 | -21.43€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4066 | +0.181 | -334.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4066 | +0.181 | -334.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3586 | +0.242 | -116.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3586 | +0.242 | -116.93€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4004 | +0.190 | -251.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4004 | +0.190 | -251.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 827 | +0.432 | -18.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 827 | +0.432 | -18.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 325 | +0.442 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 325 | +0.442 | -0.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 313 | +0.433 | -5.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 313 | +0.433 | -5.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 177 | +0.411 | -9.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 177 | +0.411 | -9.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 61288 | +0.198 | -4657.72€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 61288 | +0.198 | -4657.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10542 | +0.181 | -1154.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10542 | +0.181 | -1154.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9834 | +0.224 | -347.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9834 | +0.224 | -347.81€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10565 | +0.174 | -1220.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10565 | +0.174 | -1220.26€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9909 | +0.219 | -378.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9909 | +0.219 | -378.53€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10152 | +0.203 | -665.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10152 | +0.203 | -665.55€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10286 | +0.193 | -890.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10286 | +0.193 | -890.92€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 23309 | +0.115 | +123.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 23309 | +0.115 | +123.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11575 | +0.119 | +121.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11575 | +0.119 | +121.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11734 | +0.112 | +2.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11734 | +0.112 | +2.49€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1292 | +0.068 | -64.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 459 | +0.055 | -39.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 833 | +0.075 | -25.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1016 | +0.075 | -31.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 183 | +0.073 | -6.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 833 | +0.075 | -25.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 210 | +0.024 | -34.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 210 | +0.024 | -34.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 44380 | +0.099 | -1222.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3610 | +0.092 | +45.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 40770 | +0.099 | -1268.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 24662 | +0.103 | -319.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3610 | +0.092 | +45.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 21052 | +0.105 | -364.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8715 | +0.107 | -43.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8715 | +0.107 | -43.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 11003 | +0.081 | -860.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 11003 | +0.081 | -860.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 863 | +0.207 | -101.67€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 863 | +0.207 | -101.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 863 | +0.207 | -101.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 863 | +0.207 | -101.67€ | 1 | 4 |
| ✅ GBM_LATE_15M | 31219 | +0.087 | +15416.40€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 31219 | +0.087 | +15416.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5233 | +0.203 | +4025.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5233 | +0.203 | +4025.88€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 4649 | +0.177 | +3331.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4649 | +0.177 | +3331.63€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5537 | +0.198 | +4139.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5537 | +0.198 | +4139.58€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4447 | +0.030 | +1114.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4447 | +0.030 | +1114.75€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4447 | -0.031 | +979.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4447 | -0.031 | +979.53€ | 4 | 11 |
| ✅ GBM_LATE_15M#XRP | 6906 | -0.036 | +1825.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6906 | -0.036 | +1825.02€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 33528 | +0.087 | +17846.50€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 33528 | +0.087 | +17846.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6443 | +0.012 | +3334.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6443 | +0.012 | +3334.49€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6966 | +0.014 | +1466.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6966 | +0.014 | +1466.78€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4755 | +0.266 | +4868.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4755 | +0.266 | +4868.85€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5600 | +0.009 | +1232.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5600 | +0.009 | +1232.78€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5422 | +0.035 | +2186.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5422 | +0.035 | +2186.64€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4342 | +0.283 | +4756.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4342 | +0.283 | +4756.95€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 25077 | +0.173 | +19386.92€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 25077 | +0.173 | +19386.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3771 | +0.217 | +3154.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3771 | +0.217 | +3154.25€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3960 | +0.148 | +2870.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3960 | +0.148 | +2870.75€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3973 | +0.212 | +3221.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3973 | +0.212 | +3221.27€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4214 | +0.137 | +3120.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4214 | +0.137 | +3120.26€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4703 | +0.122 | +3409.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4703 | +0.122 | +3409.89€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4456 | +0.209 | +3610.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4456 | +0.209 | +3610.52€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6837 | +0.137 | +3209.97€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6837 | +0.137 | +3209.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 338 | +0.141 | +185.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 338 | +0.141 | +185.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1979 | +0.141 | +1045.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1979 | +0.141 | +1045.85€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2049 | +0.153 | +1007.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2049 | +0.153 | +1007.06€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1563 | +0.108 | +563.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1563 | +0.108 | +563.85€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 534 | +0.134 | +230.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 534 | +0.134 | +230.88€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 31469 | +0.179 | +24153.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 31469 | +0.179 | +24153.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4983 | +0.230 | +4420.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4983 | +0.230 | +4420.84€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4893 | +0.147 | +3172.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4893 | +0.147 | +3172.32€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5248 | +0.226 | +4535.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5248 | +0.226 | +4535.32€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5113 | +0.134 | +3592.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5113 | +0.134 | +3592.16€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5535 | +0.121 | +3790.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5535 | +0.121 | +3790.39€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5697 | +0.212 | +4642.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5697 | +0.212 | +4642.26€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8591 | +0.172 | +5677.27€ | 1 | 31 |
| ✅ GBM_LATE_5M#5min | 8591 | +0.172 | +5677.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 828 | +0.227 | +715.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 828 | +0.227 | +715.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2077 | +0.167 | +1497.22€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2077 | +0.167 | +1497.22€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2822 | +0.179 | +1857.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2822 | +0.179 | +1857.72€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 893 | +0.147 | +506.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 893 | +0.147 | +506.36€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2239 | +0.072 | +813.71€ | 0 | 12 |
| ✅ GBM_LATE_60M#60min | 2239 | +0.072 | +813.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 840 | +0.093 | +300.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 840 | +0.093 | +300.43€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 713 | +0.071 | +316.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 713 | +0.071 | +316.86€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 686 | +0.049 | +196.42€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 686 | +0.049 | +196.42€ | 2 | 11 |
| 🚫 GBM_LATE_60M_FADE | 443 | -0.239 | -10.18€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 443 | -0.239 | -10.18€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 165 | -0.219 | -5.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 165 | -0.219 | -5.48€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 152 | -0.227 | +0.08€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 152 | -0.227 | +0.08€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 126 | -0.273 | -4.79€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 126 | -0.273 | -4.79€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 940 | +0.088 | +238.08€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 940 | +0.088 | +238.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 348 | +0.083 | +74.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 348 | +0.083 | +74.53€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 314 | +0.054 | +37.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 314 | +0.054 | +37.09€ | 3 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 278 | +0.132 | +126.45€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 278 | +0.132 | +126.45€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2584 | +0.106 | +704.21€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2584 | +0.106 | +704.21€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2584 | +0.106 | +704.21€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2584 | +0.106 | +704.21€ | 0 | 3 |
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
| ✅ LIQUIDACIONES_5M | 2687 | +0.022 | +76.68€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2687 | +0.022 | +76.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 134 | +0.029 | -0.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 134 | +0.029 | -0.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 391 | +0.037 | +37.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 391 | +0.037 | +37.07€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 201 | -0.022 | -6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1034 | +0.032 | +31.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1034 | +0.032 | +31.04€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 612 | +0.011 | +0.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 612 | +0.011 | +0.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 315 | +0.021 | +15.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 315 | +0.021 | +15.22€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1323 | -0.046 | -31.29€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1323 | -0.046 | -31.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 379 | -0.043 | -14.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 379 | -0.043 | -14.04€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 439 | -0.028 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 439 | -0.028 | -1.60€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 505 | -0.064 | -15.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 505 | -0.064 | -15.66€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 4076 | -0.023 | +42.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1919 | -0.029 | -14.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2157 | -0.017 | +56.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 108 | -0.009 | +2.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 56 | +0.035 | +7.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 52 | -0.056 | -4.31€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1002 | -0.001 | +45.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 469 | -0.007 | +11.08€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 533 | +0.005 | +34.31€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 461 | -0.025 | +7.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 223 | -0.038 | -2.48€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 238 | -0.013 | +9.74€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 827 | -0.040 | -29.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 377 | -0.057 | -29.85€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 450 | -0.026 | +0.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 803 | -0.027 | +8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 388 | -0.033 | +1.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 415 | -0.020 | +7.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 875 | -0.029 | +7.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 406 | -0.029 | -1.67€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 469 | -0.029 | +8.68€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 35918 | -0.004 | +1710.60€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 35918 | -0.004 | +1710.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6391 | +0.023 | +829.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6391 | +0.023 | +829.61€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5403 | -0.031 | -70.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5403 | -0.031 | -70.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6475 | +0.019 | +625.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6475 | +0.019 | +625.31€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5192 | -0.052 | -154.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5192 | -0.052 | -154.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6050 | -0.008 | +208.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6050 | -0.008 | +208.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6407 | +0.012 | +272.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6407 | +0.012 | +272.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6103 | -0.059 | -147.04€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6103 | -0.059 | -147.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1484 | -0.080 | -36.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1484 | -0.080 | -36.26€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 701 | -0.126 | -33.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 701 | -0.126 | -33.93€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1802 | -0.076 | -32.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1802 | -0.076 | -32.13€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 90405 | -0.073 | +1788.91€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 90405 | -0.073 | +1788.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15489 | -0.075 | +892.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15489 | -0.075 | +892.99€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13767 | -0.097 | -747.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13767 | -0.097 | -747.39€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15747 | -0.066 | +897.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15747 | -0.066 | +897.07€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13300 | -0.093 | -332.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13300 | -0.093 | -332.79€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16436 | -0.051 | +348.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16436 | -0.051 | +348.48€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15666 | -0.063 | +730.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15666 | -0.063 | +730.55€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7950 | -0.030 | -141.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7950 | -0.030 | -141.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1859 | -0.041 | -16.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1859 | -0.041 | -16.93€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1081 | -0.047 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1081 | -0.047 | -19.84€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 769 | -0.021 | -24.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 769 | -0.021 | -24.37€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1315 | +0.114 | +473.85€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1179 | +0.120 | +461.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 276 | +0.140 | +141.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 276 | +0.140 | +141.66€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 224 | +0.106 | +61.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 224 | +0.106 | +61.70€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 241 | +0.109 | +90.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 241 | +0.109 | +90.42€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 209 | +0.135 | +99.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 209 | +0.135 | +99.80€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 229 | +0.102 | +67.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 229 | +0.102 | +67.68€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 792 | -0.030 | -39.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 792 | -0.030 | -39.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 154 | +0.000 | +5.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 154 | +0.000 | +5.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 113 | -0.030 | -5.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 113 | -0.030 | -5.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 220 | -0.054 | -23.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 220 | -0.054 | -23.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 172 | -0.006 | -2.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 172 | -0.006 | -2.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 133 | -0.056 | -13.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 133 | -0.056 | -13.38€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 247 | -0.227 | -33.90€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 208 | -0.186 | +15.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 190 | -0.182 | +11.55€ | 4 | 0 |
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
| ✅ STREAK_FADE_5M | 3038 | -0.023 | -126.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3038 | -0.023 | -126.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 903 | -0.021 | -32.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 903 | -0.021 | -32.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 577 | -0.025 | -24.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 577 | -0.025 | -24.71€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1402 | -0.021 | -54.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1402 | -0.021 | -54.94€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 85 | -0.052 | -8.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 85 | -0.052 | -8.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 47 | -0.010 | -4.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9437 | +0.020 | +113.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9437 | +0.020 | +113.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2620 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2620 | +0.021 | +28.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2163 | +0.029 | +50.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2163 | +0.029 | +50.31€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2839 | +0.011 | +2.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2839 | +0.011 | +2.43€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1815 | +0.023 | +32.13€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1815 | +0.023 | +32.13€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8402 | +0.013 | -41.89€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8402 | +0.013 | -41.89€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3311 | +0.018 | -4.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3311 | +0.018 | -4.70€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3348 | +0.012 | -23.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3348 | +0.012 | -23.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1743 | +0.007 | -14.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1743 | +0.007 | -14.10€ | 1 | 0 |
| ✅ UPDOWN_GBM | 51454 | +0.040 | +3718.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 13145 | +0.076 | +2704.19€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1747 | +0.006 | +10.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 33330 | +0.032 | +967.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3046 | +0.005 | +38.88€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5249 | +0.076 | +680.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1010 | +0.156 | +445.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4206 | +0.058 | +235.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9874 | +0.048 | +778.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1698 | +0.090 | +389.51€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 468 | +0.013 | +5.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6260 | +0.051 | +348.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1378 | +0.006 | +35.55€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 70 | -0.083 | +0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 6056 | +0.046 | +438.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 984 | +0.137 | +347.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 5044 | +0.029 | +92.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11347 | +0.031 | +603.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3250 | +0.054 | +446.27€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 461 | +0.008 | +9.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6543 | +0.026 | +146.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1032 | +0.003 | -1.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 61 | -0.119 | +3.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11490 | +0.021 | +392.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3112 | +0.029 | +258.96€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 451 | -0.001 | -0.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7238 | +0.020 | +132.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 636 | +0.008 | +5.24€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 53 | -0.154 | -4.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7436 | +0.045 | +827.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3091 | +0.094 | +816.35€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 306 | +0.006 | -1.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 4039 | +0.011 | +12.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 184 | -0.118 | -0.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 664 | +0.357 | +231.75€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 664 | +0.357 | +231.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 363 | +0.363 | +124.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 363 | +0.363 | +124.59€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 301 | +0.348 | +107.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 301 | +0.348 | +107.16€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14781 | -0.030 | +3421.87€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14781 | -0.030 | +3421.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1100 | -0.057 | +372.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1100 | -0.057 | +372.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2653 | -0.114 | +113.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2653 | -0.114 | +113.67€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 609 | +0.201 | +458.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 609 | +0.201 | +458.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1711 | +0.216 | +1119.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1711 | +0.216 | +1119.17€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4356 | -0.063 | +616.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4356 | -0.063 | +616.38€ | 3 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4352 | -0.068 | +741.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4352 | -0.068 | +741.93€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 171 | +0.026 | +6.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 171 | +0.026 | +6.16€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1071 | +0.293 | +891.51€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1071 | +0.293 | +891.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 586 | +0.286 | +447.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 586 | +0.286 | +447.56€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 485 | +0.301 | +443.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 485 | +0.301 | +443.95€ | 0 | 9 |
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
| ✅ UPDOWN_OU_5M#SOL#5min | 78 | -0.175 | -5.47€ | 2 | 0 |
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
  - _Estado_: Spread bajo (0.051) — sin ventaja clara. oversold(IBS<0.3): IC=+0.051 n=18084 | neutral: IC=+0.042 n=19102 | overbought(IBS>0.7): IC=+0.093 n=18336
  - _Datos_: n=57544 IC=+0.063 PNL=+7724.99€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 601 celda(s) pasan gate riguroso completo de 2392 evaluadas (n>=40) y 3388 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.029 < 0.08 — monitorear
  - _Datos_: n=3112 IC=+0.029 PNL=+258.96€

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
  - _Estado_: 51392 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.123 n=489/60 | contraria IC=+0.188 n=489 | gap=-0.065 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=356, boost estimado=+0.008. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 209 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1032/40 IC=+0.003 PNL=-1.91€ | BTC#60min: n=1378/40 IC=+0.006 PNL=+35.55€ | SOL#60min: n=636/40 IC=+0.008 PNL=+5.23€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=411990 | tras_1loss IC=+0.086 n=317502 | tras_2loss IC=+0.055 n=131416/40 | gap=-0.006 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.023 n=6422 | contrario_BTC IC=+0.037 n=5667/40 | gap=+0.014 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.08 con n=481 PNL=+363.52€
  - _Datos_: n=481 IC=+0.216 PNL=+363.52€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2270 PNL=+1248.26€
  - _Datos_: n=2270 IC=+0.332 PNL=+1248.26€

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
  - _Estado_: n=49101 IC=+0.040 PNL=+3549.13€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49101 IC=+0.040 PNL=+3549.13€

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
  - _Estado_: n=2081 IC=+0.007 PNL=+2.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2081 IC=+0.007 PNL=+2.19€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=965 IC=+0.001 PNL=+36.69€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=965 IC=+0.001 PNL=+36.69€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=2828 PNL=+2005.61€
  - _Datos_: n=2828 IC=+0.202 PNL=+2005.61€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1718 IC=+0.064 PNL=+135.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1718 IC=+0.064 PNL=+135.48€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1698 IC=+0.090 PNL=+389.51€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1698 IC=+0.090 PNL=+389.51€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=7507 PNL=+2032.08€
  - _Datos_: n=7507 IC=+0.095 PNL=+2032.08€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=199 IC=-0.261 PNL=-11.77€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=199 IC=-0.261 PNL=-11.77€

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
  - _Estado_: n=9225 IC=+0.042 PNL=+627.69€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=9225 IC=+0.042 PNL=+627.69€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=3112 IC=+0.060 PNL=+414.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3112 IC=+0.060 PNL=+414.85€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=416 PNL=+125.46€
  - _Datos_: n=416 IC=+0.110 PNL=+125.46€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=783 PNL=+207.51€
  - _Datos_: n=783 IC=+0.150 PNL=+207.51€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.08 con n=601 PNL=+345.64€
  - _Datos_: n=601 IC=+0.114 PNL=+345.64€

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
  - _Estado_: n=7648 IC=+0.046 PNL=+663.78€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7648 IC=+0.046 PNL=+663.78€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=752 PNL=+292.12€
  - _Datos_: n=752 IC=+0.121 PNL=+292.12€

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
  - _Estado_: n=18944 IC=+0.065 PNL=+2576.53€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=18944 IC=+0.065 PNL=+2576.53€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=4593 PNL=+2686.67€
  - _Datos_: n=4593 IC=+0.207 PNL=+2686.67€

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
  - _Estado_: n=2379 IC=+0.059 PNL=+252.96€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2379 IC=+0.059 PNL=+252.96€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.1 con n=558 PNL=+145.25€
  - _Datos_: n=558 IC=+0.120 PNL=+145.25€

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
  - _Estado_: n=22700 IC=-0.136 PNL=+1708.93€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=22700 IC=-0.136 PNL=+1708.93€

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
  - _Estado_: n=2335 IC=+0.137 PNL=+1360.44€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2335 IC=+0.137 PNL=+1360.44€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.08 con n=2789 PNL=+1992.97€
  - _Datos_: n=2789 IC=+0.203 PNL=+1992.97€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=597 PNL=+318.50€
  - _Datos_: n=597 IC=+0.214 PNL=+318.50€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.227 < -0.1 con n=2252 PNL=-178.71€
  - _Datos_: n=2252 IC=-0.227 PNL=-178.71€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6591 IC=+0.181 PNL=+4582.79€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6591 IC=+0.181 PNL=+4582.79€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=90 PNL=+30.93€
  - _Datos_: n=90 IC=+0.098 PNL=+30.93€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2370 IC=+0.070 PNL=+747.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2370 IC=+0.070 PNL=+747.44€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=2170 PNL=+1528.80€
  - _Datos_: n=2170 IC=+0.177 PNL=+1528.80€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3625 IC=-0.030 PNL=+951.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3625 IC=-0.030 PNL=+951.86€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=3823 PNL=-323.55€
  - _Datos_: n=3823 IC=+0.239 PNL=-323.55€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1316) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1316 IC=+0.102 PNL=+305.98€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.321 > 0.08 con n=333 PNL=+109.90€
  - _Datos_: n=333 IC=+0.321 PNL=+109.90€

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
  - _Estado_: n=10542 IC=+0.181 PNL=-1154.66€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10542 IC=+0.181 PNL=-1154.66€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.1 con n=168 PNL=+102.14€
  - _Datos_: n=168 IC=+0.206 PNL=+102.14€
