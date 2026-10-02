# Hipótesis automáticas — 2026-10-02 20:46 UTC
_Generado por shadow_postmortem.py sobre 719108 resoluciones (PNL=+86374.29€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=573)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.221 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.218 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.257 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.130)

- **PATRÓN** `banda_z` > `9.307` → IC=+0.196 (n=205)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.307 (IC base=+0.130)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.723` → IC=+0.132 (n=552)

  - _Acción_: Kelly boost +0.66€ cuando `ballenas_wallet_edge_medio` > 0.723 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.131 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=649)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4878.272` → IC=+0.147 (n=205)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4878.272 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `8556.0995` → IC=+0.121 (n=233)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8556.0995 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=438)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.228 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.266 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.140)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=555)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.140)

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
- **FILTRO** `restante_s_al_confirmar` < `144.92` → IC=-0.219 (n=8043)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.92
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=24134)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `133.59` → IC=-0.266 (n=1047)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.59
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3141)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `124.8` → IC=-0.311 (n=960)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.8
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2881)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.14` → IC=-0.215 (n=1993)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.14
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=5979)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.33` → IC=-0.325 (n=1556)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.33
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=4671)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.211 (n=15638)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=3783)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5472.5329` → IC=+0.171 (n=2450)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5472.5329 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=16519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=12738)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=6211)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7705.2031` → IC=+0.169 (n=2374)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7705.2031 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.206 (n=1772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1815)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `16074.9801` → IC=+0.221 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16074.9801 (IC base=+0.201)

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

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4624.034 (IC base=+0.091)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.097)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.141 (n=904)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.151 (n=230)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.097)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.158 (n=2758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 8.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.354 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=1463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.363 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.222)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.253 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=879)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1325.0731` → IC=+0.144 (n=768)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1325.0731 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.405 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=797)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.370 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `1192.3838` → IC=+0.151 (n=236)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1192.3838 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.228 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.119)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=13626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=11570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.224 (n=5800)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.175 (n=3049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=3059)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3097)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=1257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.234 (n=1248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.337 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.233)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=3009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=3031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=2541)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.329 (n=938)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=1984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=2349)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.194 (n=1122)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `11601.187` → IC=+0.456 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11601.187 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `11135.4127` → IC=+0.459 (n=215)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.420 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.417 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.410)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=40651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=17757)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=6994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=5607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=7658)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=3625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.265 (n=4130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=7397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.174 (n=5621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 12.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=7393)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=3664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2471)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2645)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=2903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=3087)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=6200)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=5950)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.5` → IC=+0.136 (n=5755)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.5 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=3116)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=2957)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.132 (n=3305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 6.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.21` → IC=+0.141 (n=2857)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.21 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.182 (n=3084)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.111)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.129 (n=3273)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` > 4.96 (IC base=+0.111)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=2912)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.111)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.288 (n=1255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1552.7677` → IC=+0.293 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1552.7677 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.333 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4351.481` → IC=+0.290 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4351.481 (IC base=+0.279)

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
- **FILTRO** `py_entrada` > `0.735` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=59)

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
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=59)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4955` → IC=+0.129 (n=9710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4955 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `0.9799` → IC=+0.243 (n=3238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9799 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2256` → IC=+0.253 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2256 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.401` → IC=+0.191 (n=2544)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.401 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.2107` → IC=+0.248 (n=2710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2107 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` > `0.6156` → IC=+0.251 (n=2709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6156 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.226 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `1.8934` → IC=+0.215 (n=4512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8934 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.137 (n=11778)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.5667 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.6019` → IC=+0.204 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6019 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.157` → IC=+0.177 (n=3903)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.157 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.179 (n=4263)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1967 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `0.866` → IC=+0.177 (n=2842)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.866 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.223 (n=2044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.269` → IC=+0.197 (n=6416)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.269 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.4449` → IC=+0.200 (n=7290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4449 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.214 (n=7086)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.070)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.205 (n=721)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.187 (n=723)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3557` → IC=+0.180 (n=2163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3557 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=1047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.181 (n=1448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 11.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.715` → IC=+0.296 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.715 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.215 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.178 (n=2040)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.192 (n=2213)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `2034.7686` → IC=+0.179 (n=721)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2034.7686 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.236 (n=1142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1531)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.270 (n=753)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=1553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0613` → IC=+0.287 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0613 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.472` → IC=+0.246 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.472 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.39` → IC=+0.240 (n=1786)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.39 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0689` → IC=+0.232 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0689 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.267 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.5649` → IC=+0.244 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5649 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1583.66` → IC=+0.247 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1583.66 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.235 (n=758)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3578` → IC=+0.226 (n=1718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3578 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=1724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.255 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.3543` → IC=+0.218 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3543 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.703` → IC=+0.255 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.703 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.220 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.692` → IC=+0.219 (n=1535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.692 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.235 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.219 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.3839` → IC=+0.239 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3839 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `11152.7976` → IC=+0.220 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11152.7976 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.170 (n=1156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2593` → IC=+0.151 (n=1525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2593 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.72` → IC=+0.172 (n=1734)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.72 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1329` → IC=+0.156 (n=1561)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1329 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.325` → IC=+0.142 (n=277)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 11.325 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.285` → IC=+0.145 (n=1596)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.285 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.149 (n=1733)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2046 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.6207` → IC=+0.138 (n=1733)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6207 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.175 (n=462)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.150 (n=1622)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.146 (n=1081)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14180.1472` → IC=+0.141 (n=1155)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14180.1472 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.172 (n=678)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 231.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.201 (n=1940)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=2175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=1453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.317` → IC=+0.257 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.317 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.195 (n=1906)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.200 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.1663` → IC=+0.206 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1663 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2587)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2009.87` → IC=+0.197 (n=724)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2009.87 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.221 (n=1683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.6336` → IC=+0.214 (n=1912)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6336 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.0649` → IC=+0.233 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0649 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.236 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.255 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.72` → IC=+0.216 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.72 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.220 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.216 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1927.2984` → IC=+0.216 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.2984 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.211 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.161 (n=119)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2604)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.134 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0043 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.9529` → IC=+0.219 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9529 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.364` → IC=+0.324 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.364 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.871` → IC=+0.170 (n=861)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.871 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.332 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.342 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.354 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.8421` → IC=+0.323 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8421 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.327 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.1014` → IC=+0.156 (n=681)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1014 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.3354` → IC=+0.195 (n=316)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3354 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.6106` → IC=+0.156 (n=350)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6106 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `1.1666` → IC=+0.148 (n=350)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1666 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.193 (n=138)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.168 (n=890)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.023)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=398)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.195 (n=116)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=353)

- **FILTRO** `ibs_20min` > `0.2391` → IC=-0.124 (n=2621)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2391
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=1294)

- **FILTRO** `sigma_ewma_delta_pct` > `8.735` → IC=-0.207 (n=411)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.735
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=3504)

- **PATRÓN** `ibs_20min` > `0.4138` → IC=+0.134 (n=315)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.4138 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.289` → IC=+0.127 (n=164)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 2.289 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8994` → IC=+0.265 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8994 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `1.0824` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0824 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.1712` → IC=+0.286 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1712 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.279 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.2391` → IC=+0.134 (n=1294)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2391 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7098` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7098 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6941` → IC=+0.271 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6941 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.1591` → IC=+0.303 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1591 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.3699` → IC=+0.288 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3699 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.179 (n=680)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2059)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.206 (n=642)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2097)

- **FILTRO** `ibs_20min` > `0.7669` → IC=-0.207 (n=1015)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7669
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=3047)

- **PATRÓN** `dist_vwap_pct` > `0.8113` → IC=+0.315 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8113 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2896` → IC=+0.313 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2896 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` < `0.9837` → IC=+0.292 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9837 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.310 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.0963` → IC=+0.300 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0963 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0698` → IC=+0.300 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0698 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.454` → IC=+0.300 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.454 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.8242` → IC=+0.304 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8242 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5647` → IC=+0.282 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5647 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` < `0.7271` → IC=+0.254 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7271 (IC base=-0.015)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.270 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.270 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.1331` → IC=+0.260 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1331 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.252 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.42 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.199 (n=4187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4716` → IC=+0.188 (n=11220)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4716 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `1.0117` → IC=+0.290 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0117 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.657` → IC=+0.158 (n=5747)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.657 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.1809` → IC=+0.243 (n=4572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1809 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.253 (n=4085)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.267 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.2634` → IC=+0.252 (n=3343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2634 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.275 (n=6924)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.170 (n=4064)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.158 (n=10733)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5455 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7093` → IC=+0.251 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7093 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2496` → IC=+0.249 (n=3529)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2496 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7074` → IC=+0.248 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7074 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1987` → IC=+0.262 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1987 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.304 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5856` → IC=+0.278 (n=2219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5856 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.281 (n=4935)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2587` → IC=-0.157 (n=870)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2587
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2613)

- **FILTRO** `ibs_20min` > `0.7575` → IC=-0.167 (n=713)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7575
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2140)

- **FILTRO** `sigma_ewma_delta_pct` > `4.567` → IC=-0.173 (n=644)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.567
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2209)

- **PATRÓN** `ibs_20min` > `0.904` → IC=+0.276 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.904 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.862` → IC=+0.209 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.862 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.279 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4395` → IC=+0.200 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4395 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.233 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.220 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.0963` → IC=+0.443 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0963 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.448 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4745` → IC=+0.454 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4745 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.467 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.163 (n=841)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8641 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1233` → IC=+0.188 (n=638)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1233 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6746` → IC=+0.174 (n=1052)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6746 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.224 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.196 (n=386)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.4073` → IC=+0.185 (n=385)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.4073 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.222 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 233.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1527` → IC=+0.227 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1527 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.6119` → IC=+0.227 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6119 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.0717` → IC=+0.223 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0717 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2665` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2665 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5536` → IC=+0.227 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5536 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.237 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `459.0` → IC=+0.222 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 459.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.283 (n=1280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.256 (n=1933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=1719)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.714` → IC=+0.282 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.714 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.266 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `1.6226` → IC=+0.259 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6226 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=2264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `1999.8384` → IC=+0.274 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.8384 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.300 (n=1587)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1865` → IC=+0.297 (n=699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1865 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.320 (n=536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.294 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.287)

- **PATRÓN** `ibs_20min` > `0.0994` → IC=+0.288 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0994 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.664` → IC=+0.293 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.664 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.119` → IC=+0.294 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.119 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7149` → IC=+0.299 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7149 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.292 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1919.4741` → IC=+0.306 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.4741 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.292 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7721` → IC=-0.186 (n=725)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7721
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=2176)

- **PATRÓN** `ibs_20min` > `0.9046` → IC=+0.179 (n=649)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9046 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.4125` → IC=+0.224 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4125 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0072` → IC=+0.245 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0072 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0828` → IC=+0.252 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0828 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4078` → IC=+0.268 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4078 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.253 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1443` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1443 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.216 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1804 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.264 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8148 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.468` → IC=+0.236 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.468 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.258 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7571` → IC=-0.186 (n=1327)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7571
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=1327)

- **FILTRO** `ibs_20min` > `0.6744` → IC=-0.239 (n=666)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6744
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2002)

- **FILTRO** `sigma_ewma_delta_pct` > `4.748` → IC=-0.194 (n=570)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.748
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2098)

- **PATRÓN** `ibs_20min` > `0.7571` → IC=+0.283 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7571 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `1.0762` → IC=+0.333 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0762 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.658` → IC=+0.168 (n=420)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.658 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.86` → IC=+0.307 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.86 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.301 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.297 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2714` → IC=+0.298 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2714 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.323 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.322 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5692` → IC=+0.133 (n=1761)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5692 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.2123` → IC=+0.241 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2123 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.262 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.222 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1883 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0947` → IC=+0.228 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0947 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0689` → IC=+0.245 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0689 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4118` → IC=+0.248 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4118 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.258 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.022)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.326 (n=1405)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.303 (n=736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` > `0.6419` → IC=+0.315 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6419 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2171` → IC=+0.316 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2171 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.76` → IC=+0.308 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.76 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.861` → IC=+0.282 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.861 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.296 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.325 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.294 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2472.056` → IC=+0.295 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2472.056 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.322 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.314 (n=1111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1979` → IC=+0.289 (n=733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1979 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.291 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.309 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.3225` → IC=+0.295 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3225 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.283 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.300 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.285 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.315 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.340 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.292 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2426.5417` → IC=+0.288 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2426.5417 (IC base=+0.283)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.176 (n=3173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0049 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.206 (n=3153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3648` → IC=+0.179 (n=8324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3648 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.5711` → IC=+0.224 (n=9459)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5711 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1765` → IC=+0.196 (n=4084)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1765 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.405` → IC=+0.253 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.405 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.2091` → IC=+0.164 (n=6298)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2091 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.160 (n=6298)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6297 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.198 (n=1404)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5576` → IC=+0.170 (n=4008)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5576 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.599` → IC=+0.177 (n=3036)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.599 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1970.7` → IC=+0.174 (n=8451)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1970.7 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.186 (n=8378)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 108.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.187 (n=6071)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0067 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.0824` → IC=+0.216 (n=3036)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0824 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=3483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.4865` → IC=+0.229 (n=9091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4865 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1758` → IC=+0.167 (n=6357)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1758 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.303` → IC=+0.197 (n=1526)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.303 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1765` → IC=+0.161 (n=6531)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1765 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.215 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5529` → IC=+0.173 (n=3697)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5529 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.589` → IC=+0.173 (n=2799)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.589 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.181 (n=8070)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 109.0 (IC base=+0.173)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.229 (n=533)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.206 (n=529)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.3429` → IC=+0.215 (n=1586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3429 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=1674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1065)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.285 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.249` → IC=+0.330 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.249 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.244 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.4293` → IC=+0.192 (n=1481)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4293 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.208 (n=1631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2035.4848` → IC=+0.195 (n=529)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2035.4848 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.252 (n=1059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.252 (n=1076)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1838` → IC=+0.288 (n=803)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1838 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.249 (n=1227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.263 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.213` → IC=+0.245 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.213 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4169` → IC=+0.267 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4169 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1582.26` → IC=+0.257 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.26 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.230 (n=480)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.0723` → IC=+0.193 (n=476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0723 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.176 (n=1431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3883` → IC=+0.221 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3883 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2063` → IC=+0.205 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2063 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.228 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6882` → IC=+0.170 (n=628)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6882 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.200 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.177 (n=611)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.4724` → IC=+0.158 (n=463)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4724 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `11986.8698` → IC=+0.158 (n=1275)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11986.8698 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.166 (n=596)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 235.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=1512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2979` → IC=+0.167 (n=1512)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2979 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5887` → IC=+0.195 (n=1512)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5887 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1378` → IC=+0.168 (n=1494)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1378 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.200 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.161 (n=1512)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2129 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2258` → IC=+0.144 (n=1548)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2258 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.150 (n=458)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.150 (n=1400)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7491` → IC=+0.142 (n=933)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7491 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.171 (n=445)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 209.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.228 (n=527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2513` → IC=+0.218 (n=1052)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2513 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.226 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.277 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.202 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2003` → IC=+0.208 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2003 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.215 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `1999.7921` → IC=+0.216 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.7921 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.236 (n=1195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1443` → IC=+0.256 (n=597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1443 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.272 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.3521` → IC=+0.245 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3521 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.649` → IC=+0.252 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.649 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.253 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7349` → IC=+0.236 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7349 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.7396` → IC=+0.226 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7396 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1993.9956` → IC=+0.220 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1993.9956 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.212 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.220)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.180 (n=1343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.162 (n=1523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.343` → IC=+0.202 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.343 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1493` → IC=+0.183 (n=992)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1493 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.224 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0376` → IC=+0.157 (n=1340)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0376 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.178 (n=638)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4299` → IC=+0.159 (n=497)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4299 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.163 (n=497)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5222.8208` → IC=+0.190 (n=1015)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5222.8208 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.152 (n=1464)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 155.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.156 (n=1597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.149 (n=1597)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6622` → IC=+0.177 (n=1597)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6622 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1563` → IC=+0.144 (n=1566)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1563 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.868` → IC=+0.166 (n=554)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.868 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.152 (n=1065)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8554 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.179 (n=235)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.139 (n=982)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7994 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5177` → IC=+0.135 (n=491)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.5177 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `4262.9422` → IC=+0.157 (n=1065)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4262.9422 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.128 (n=1247)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 128.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.163 (n=781)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0101 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.59` → IC=+0.123 (n=1723)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.59 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.209 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0806` → IC=+0.216 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0806 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.864` → IC=+0.258 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.864 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.133 (n=1723)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2145 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6463` → IC=+0.127 (n=1723)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6463 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.128 (n=1733)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.125 (n=713)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.534` → IC=+0.142 (n=733)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.534 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1805)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2892.276` → IC=+0.197 (n=781)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2892.276 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.140 (n=1357)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 47.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.163 (n=769)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1069` → IC=+0.172 (n=583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1069 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.218 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2097` → IC=+0.148 (n=1619)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2097 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.609` → IC=+0.136 (n=363)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 7.609 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.152 (n=584)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6381 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2259` → IC=+0.159 (n=306)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2259 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.145 (n=533)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4132` → IC=+0.129 (n=532)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4132 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.183 (n=793)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.128 (n=1542)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.229 (n=1452)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.183` → IC=+0.211 (n=717)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.183 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.246 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.2128` → IC=+0.213 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2128 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.248 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.1976` → IC=+0.211 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1976 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.216 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.271 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.4642` → IC=+0.211 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4642 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.216 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2847.4573` → IC=+0.210 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2847.4573 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.225 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.216 (n=1118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.094` → IC=+0.233 (n=559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.094 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.243 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `1.2288` → IC=+0.225 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2288 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.402` → IC=+0.250 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.402 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.222 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.279 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `2.1901` → IC=+0.205 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1901 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.209 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2399.3806` → IC=+0.218 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.3806 (IC base=+0.211)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.188 (n=832)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.174 (n=833)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0085 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3495` → IC=+0.176 (n=2194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3495 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=1239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.203 (n=2228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.816` → IC=+0.187 (n=401)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.816 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.726` → IC=+0.193 (n=1092)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.726 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.187 (n=1476)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8709 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.2092` → IC=+0.177 (n=738)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2092 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1623` → IC=+0.179 (n=667)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1623 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.178 (n=806)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8182` → IC=+0.173 (n=1611)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8182 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=2824)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2675.5939` → IC=+0.169 (n=2227)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2675.5939 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.185 (n=2272)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 143.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.141 (n=1712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0057 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=2419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.067` → IC=+0.193 (n=854)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.067 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6979` → IC=+0.122 (n=1015)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.6979 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1636` → IC=+0.128 (n=627)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1636 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.143 (n=829)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4404 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2760.3927` → IC=+0.124 (n=2288)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2760.3927 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.131 (n=1083)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 28.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.171 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0029 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3377` → IC=+0.161 (n=658)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3377 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6381` → IC=+0.205 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6381 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3033` → IC=+0.160 (n=230)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3033 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.166 (n=288)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8924` → IC=+0.167 (n=439)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8924 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` < `0.155` → IC=+0.142 (n=685)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.155 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0922` → IC=+0.147 (n=230)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0922 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.2024` → IC=+0.148 (n=564)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.2024 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5058` → IC=+0.145 (n=573)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5058 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=852)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10928.2428` → IC=+0.153 (n=658)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10928.2428 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.189 (n=278)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 154.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.210 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3512` → IC=+0.162 (n=806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3512 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.181 (n=709)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6112 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1836` → IC=+0.156 (n=795)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1836 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.278` → IC=+0.142 (n=305)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 4.278 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.07` → IC=+0.145 (n=738)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.07 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2213` → IC=+0.145 (n=806)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2213 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6954` → IC=+0.155 (n=720)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6954 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.201 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1128` → IC=+0.159 (n=701)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1128 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4063` → IC=+0.148 (n=796)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4063 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `12109.7968` → IC=+0.143 (n=720)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 12109.7968 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.156 (n=681)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 295.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.251 (n=520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4108` → IC=+0.221 (n=779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4108 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.6752` → IC=+0.256 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6752 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.215 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2221` → IC=+0.209 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2221 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.272` → IC=+0.233 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.272 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.217 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8392 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.1811` → IC=+0.233 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1811 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.155` → IC=+0.243 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.155 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4185` → IC=+0.237 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4185 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.7694` → IC=+0.232 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7694 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.122 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.146 (n=244)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.087 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6868` → IC=+0.144 (n=321)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6868 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `8098.9392` → IC=+0.133 (n=486)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 8098.9392 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.123 (n=237)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 34.0 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.167 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0059 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.5938` → IC=+0.197 (n=588)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5938 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.9873` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9873 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.339` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.339 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0697` → IC=+0.165 (n=518)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.0697 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.6503` → IC=+0.156 (n=588)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6503 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1714` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1714 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.168 (n=257)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=622)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3090.2601` → IC=+0.187 (n=196)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3090.2601 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.459` → IC=+0.157 (n=494)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.459 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.8255` → IC=+0.128 (n=355)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8255 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `2480.8158` → IC=+0.130 (n=374)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2480.8158 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.122 (n=504)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 41.0 (IC base=+0.071)

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
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.208 (n=4088)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=12832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.9919` → IC=+0.309 (n=4086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9919 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.9235` → IC=+0.202 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9235 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.367` → IC=+0.249 (n=3032)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.367 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.8805` → IC=+0.169 (n=5480)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8805 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.199 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.5776` → IC=+0.194 (n=3946)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5776 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1802.7556` → IC=+0.177 (n=12251)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1802.7556 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.200 (n=9597)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.194 (n=7364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0071 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.193 (n=4854)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4508` → IC=+0.247 (n=9708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4508 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2523` → IC=+0.163 (n=6890)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2523 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.047` → IC=+0.203 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.047 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.734` → IC=+0.183 (n=10663)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.734 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.162 (n=3301)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7053 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2877` → IC=+0.243 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2877 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.5918` → IC=+0.192 (n=3422)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5918 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.204 (n=6674)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.231 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.229 (n=681)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.3618` → IC=+0.206 (n=2033)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3618 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.359 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2266` → IC=+0.257 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2266 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.2327` → IC=+0.214 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2327 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=2064)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2033.8453` → IC=+0.212 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2033.8453 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.221 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.262 (n=1105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.262 (n=1657)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.126` → IC=+0.283 (n=730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.126 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.272 (n=1500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.359` → IC=+0.285 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.359 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.508` → IC=+0.264 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.508 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.293 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.5472` → IC=+0.261 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5472 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6054` → IC=+0.277 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6054 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1581.46` → IC=+0.270 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1581.46 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.205 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.114` → IC=+0.160 (n=869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.114 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.2865` → IC=+0.202 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2865 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1304` → IC=+0.181 (n=1115)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1304 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.723` → IC=+0.178 (n=430)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.723 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.149 (n=1804)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6261` → IC=+0.172 (n=659)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6261 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.151 (n=1748)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.193 (n=281)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.1192` → IC=+0.157 (n=1688)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1192 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7605` → IC=+0.150 (n=1279)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7605 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `11444.8195` → IC=+0.152 (n=1765)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11444.8195 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.171 (n=824)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 278.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=1658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.161 (n=1658)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.2923` → IC=+0.238 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2923 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.135` → IC=+0.165 (n=1510)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.135 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.518` → IC=+0.157 (n=278)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.518 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.304` → IC=+0.149 (n=1512)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.304 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.160 (n=1658)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1954 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1513` → IC=+0.199 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1513 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.156 (n=1559)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.161 (n=1039)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `260.0` → IC=+0.157 (n=496)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 260.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.255 (n=668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=2000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.224 (n=1801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.300 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.2068` → IC=+0.222 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2068 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.230 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2009.96` → IC=+0.234 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.96 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.242 (n=1650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.6219` → IC=+0.237 (n=1875)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6219 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0164` → IC=+0.304 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0164 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.171` → IC=+0.278 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.171 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3403` → IC=+0.297 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3403 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7297` → IC=+0.237 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7297 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1492` → IC=+0.237 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1492 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1992.72` → IC=+0.245 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.72 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.233 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.194 (n=701)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0035 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4376` → IC=+0.149 (n=2099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4376 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.2719` → IC=+0.187 (n=2099)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.2719 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3654` → IC=+0.160 (n=813)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3654 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.528` → IC=+0.167 (n=340)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.528 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.161 (n=1400)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8725 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.191 (n=380)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.153 (n=898)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1659` → IC=+0.153 (n=925)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1659 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7595.2922` → IC=+0.231 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7595.2922 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.166 (n=663)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 72.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.169 (n=1124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0052 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4487` → IC=+0.143 (n=1684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4487 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.5941` → IC=+0.195 (n=1482)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5941 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1579` → IC=+0.133 (n=1477)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1579 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.265` → IC=+0.164 (n=251)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.265 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6994` → IC=+0.142 (n=741)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6994 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.214 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.143 (n=1611)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `9462.6339` → IC=+0.204 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9462.6339 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.131 (n=1607)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 169.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.147 (n=1393)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0082 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.199 (n=2090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0684` → IC=+0.211 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0684 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.558` → IC=+0.242 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.558 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.144 (n=1393)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8919 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1609` → IC=+0.125 (n=2151)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1609 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.4546` → IC=+0.125 (n=2033)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.4546 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2128)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2540.8675` → IC=+0.232 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2540.8675 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.140 (n=1669)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 52.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.181 (n=673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0059 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1375` → IC=+0.159 (n=666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1375 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.234 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2212` → IC=+0.138 (n=1663)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2212 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.469` → IC=+0.128 (n=1921)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.469 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7146` → IC=+0.158 (n=878)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7146 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2194` → IC=+0.187 (n=314)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2194 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.1461` → IC=+0.133 (n=1610)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1461 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2803.9375` → IC=+0.188 (n=665)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2803.9375 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=1621)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.229 (n=2058)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.214 (n=1485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2188` → IC=+0.232 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2188 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.285` → IC=+0.274 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.285 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.0602` → IC=+0.215 (n=1811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0602 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.220 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.242 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4972` → IC=+0.236 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4972 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2455.4649` → IC=+0.216 (n=1838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2455.4649 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.217 (n=723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.229 (n=722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.225 (n=1535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.261 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.5611` → IC=+0.214 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5611 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.2214` → IC=+0.215 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2214 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.256 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.238 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.281 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.1658` → IC=+0.205 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1658 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4276` → IC=+0.208 (n=1977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4276 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2411.1978` → IC=+0.212 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2411.1978 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.202 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.210)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=3681)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.220 (n=1223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.5102` → IC=+0.191 (n=3653)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5102 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=1368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=1669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.239 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1741` → IC=+0.191 (n=1349)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1741 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.212` → IC=+0.213 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.212 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7093` → IC=+0.186 (n=1103)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.7093 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.8942` → IC=+0.184 (n=1670)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8942 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1682` → IC=+0.209 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1682 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.189 (n=1202)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8592` → IC=+0.186 (n=2404)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8592 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=2719)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2520.8066` → IC=+0.186 (n=3653)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2520.8066 (IC base=+0.180)

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
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.230 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.265 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.217 (n=231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.229 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.516 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7629` → IC=+0.209 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7629 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.3306` → IC=+0.212 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3306 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.976` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.976 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.529` → IC=+0.207 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.529 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2189` → IC=+0.211 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2189 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.215 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.224 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `12593.9941` → IC=+0.238 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12593.9941 (IC base=+0.204)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.215 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1529` → IC=+0.204 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1529 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5256` → IC=+0.202 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5256 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.8854` → IC=+0.194 (n=390)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8854 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.209` → IC=+0.199 (n=981)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.209 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.171` → IC=+0.198 (n=1053)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 4.171 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.194 (n=1029)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0845 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.2467` → IC=+0.191 (n=390)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.2467 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.191 (n=1075)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.200 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.4754` → IC=+0.196 (n=1147)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.4754 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=1177)

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

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.161)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.163 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.004 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.6459` → IC=+0.177 (n=951)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6459 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.1483` → IC=+0.144 (n=579)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1483 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.193 (n=249)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.079)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.122 (n=435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0057 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.2308` → IC=+0.254 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2308 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.137 (n=463)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.931` → IC=+0.149 (n=351)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 3.931 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.1396` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1396 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.153 (n=358)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.143 (n=320)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4444 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `3311.1631` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3311.1631 (IC base=+0.051)

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

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.136 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0045 (IC base=+0.091)

- **PATRÓN** `drift_60min` |x|≤ `0.0609` → IC=+0.177 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0609 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.2737` → IC=+0.270 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2737 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.140 (n=223)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.43` → IC=+0.176 (n=177)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 4.43 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `1.1644` → IC=+0.142 (n=199)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1644 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` > `0.6893` → IC=+0.142 (n=177)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6893 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.169 (n=176)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.4035 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `3352.3721` → IC=+0.135 (n=168)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3352.3721 (IC base=+0.091)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.7051` → IC=-0.128 (n=154)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7051
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=313)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=158)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.136 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0049 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.7051` → IC=+0.214 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7051 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.3362` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3362 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.652` → IC=+0.277 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.652 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `1.7779` → IC=+0.147 (n=199)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7779 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.147 (n=310)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.1419` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1419 (IC base=+0.008)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.412` → IC=+0.143 (n=96)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.412 (IC base=+0.008)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0112` → IC=-0.273 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0112
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=128)

- **FILTRO** `ibs_20min` > `0.1304` → IC=-0.278 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1304
  - _Potencial_: sin este filtro IC_bueno=+0.295 (n=86)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.121 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0063 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.175 (n=232)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7778 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.076` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.076 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.053)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.131 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0112 (IC base=+0.029)

- **PATRÓN** `ibs_20min` < `0.1304` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1304 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1324` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1324 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.0771` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.0771 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.7331` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7331 (IC base=+0.029)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.06 (IC base=+0.029)

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
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.405 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=61)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.182 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0059 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6616` → IC=+0.148 (n=333)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6616 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.4967` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4967 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.4189` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4189 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.122 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0052 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.156 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.191 (n=305)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.156 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.769` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.769 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.627` → IC=+0.148 (n=271)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.627 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=367)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `4049.975` → IC=+0.204 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4049.975 (IC base=+0.094)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6292` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6292
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=100)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.183 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0025 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.238 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.234 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1435 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.1131` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1131 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.144` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 4.144 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.1483` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1483 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.6115` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6115 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.234 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.5892` → IC=+0.238 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5892 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.191 (n=124)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3934.0004` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3934.0004 (IC base=+0.165)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1748` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1748
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=87)

- **FILTRO** `libro_liquidez` < `1549.8575` → IC=-0.173 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 1549.8575
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=96)

- **PATRÓN** `libro_liquidez` > `1549.8575` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1549.8575 (IC base=+0.045)

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
- **FILTRO** `volumen_regimen` < `1.0341` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0341
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=46)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.318 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.252 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9714 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7692 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.768` → IC=+0.284 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.768 (IC base=+0.234)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.1711` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1711 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `603.1385` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 603.1385 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.1048` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1048 (IC base=-0.043)

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
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1083)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2846.2656` → IC=+0.150 (n=421)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2846.2656 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.120 (n=1083)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.495 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2846.2656` → IC=+0.150 (n=421)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2846.2656 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=898)
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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2447)

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

- **PATRÓN** `liq_usd_total` > `84131.41` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 84131.41 (IC base=+0.056)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.165 (n=153)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=975)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=929)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=566)

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
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=275)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.495 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `3925.306` → IC=+0.144 (n=99)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3925.306 (IC base=+0.029)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=740)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=740)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=468)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=468)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=203)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=203)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=165)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=116)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=138)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=237)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=112)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=125)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=285)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=285)

- **FILTRO** `libro_liquidez` < `466.9438` → IC=-0.138 (n=78)

  - _Acción_: SKIP cuando `libro_liquidez` < 466.9438
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=237)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=168)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=1054)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1065)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **FILTRO** `lag_apertura_s` > `66.89` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.89
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.124 (n=131)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=69)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.139 (n=70)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=183)

- **PATRÓN** `py_entrada` < `0.56` → IC=+0.123 (n=128)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.56 (IC base=+0.022)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.46 (IC base=+0.040)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

- **FILTRO** `lag_apertura_s` > `290.6` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `lag_apertura_s` > 290.6
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=90)

- **FILTRO** `profundidad_ratio` < `30.1` → IC=-0.137 (n=89)

  - _Acción_: SKIP cuando `profundidad_ratio` < 30.1
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=47)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `restante_min` < `3.99` → IC=-0.126 (n=105)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `lag_apertura_s` > `60.71` → IC=-0.125 (n=110)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.71
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.139 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 9.0 (IC base=+0.084)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.142 (n=135)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=45)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=121)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.237 (n=36)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.147 (n=154)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=85)

- **FILTRO** `restante_min` < `3.43` → IC=-0.237 (n=78)

  - _Acción_: SKIP cuando `restante_min` < 3.43
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=161)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=183)

- **FILTRO** `lag_apertura_s` > `91.82` → IC=-0.223 (n=81)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.82
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=158)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=142)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.156 (n=152)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=82)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.5 (IC base=-0.055)

- **PATRÓN** `profundidad_ratio` > `14.6` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `profundidad_ratio` > 14.6 (IC base=+0.021)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.227 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=213)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=4317)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=13037)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=4339)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=13652)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.200 (n=760)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2304)

- **PATRÓN** `libro_liquidez` > `1800.6` → IC=+0.130 (n=1042)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1800.6 (IC base=+0.032)

- **PATRÓN** `libro_liquidez` > `1569.6379` → IC=+0.145 (n=1096)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1569.6379 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.181 (n=757)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=2356)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=758)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=2498)

- **PATRÓN** `libro_liquidez` > `1794.1561` → IC=+0.129 (n=1059)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1794.1561 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.166 (n=744)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2310)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2409)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3149)

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

- **FILTRO** `ballena_activa_n` > `89.0` → IC=-0.217 (n=118)

  - _Acción_: SKIP cuando `ballena_activa_n` > 89.0
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=234)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1922.7374` → IC=-0.174 (n=323)

  - _Acción_: SKIP cuando `libro_liquidez` < 1922.7374
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=658)

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
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=27129)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.281 (n=9186)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=30059)

- **FILTRO** `ibs_7min` < `0.2623` → IC=-0.233 (n=9811)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2623
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=29434)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12938)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=26307)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=12151)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=37582)

- **FILTRO** `ibs_7min` > `0.2908` → IC=-0.181 (n=12433)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2908
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=37300)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=1963)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4665)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.234 (n=3268)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=3360)

- **FILTRO** `ibs_7min` < `0.7075` → IC=-0.250 (n=2187)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7075
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=4441)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.181 (n=1525)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5103)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.263 (n=2123)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6473)

- **FILTRO** `ibs_7min` > `0.7903` → IC=-0.209 (n=2148)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7903
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6448)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.135 (n=1593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5125)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.248 (n=1649)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5069)

- **FILTRO** `ibs_7min` < `0.7428` → IC=-0.197 (n=1679)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7428
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5039)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.179 (n=1672)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=5046)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1596)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5247)

- **FILTRO** `ibs_7min` > `0.2624` → IC=-0.187 (n=1709)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2624
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5134)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.184 (n=1705)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5138)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=1556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4751)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1490)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4817)

- **FILTRO** `ibs_7min` < `0.7038` → IC=-0.247 (n=2081)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7038
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4226)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.211 (n=1484)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4823)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=2106)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=7068)

- **FILTRO** `ibs_7min` > `0.7436` → IC=-0.176 (n=2292)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=6882)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1918)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4548)

- **FILTRO** `ibs_7min` < `0.7386` → IC=-0.185 (n=1616)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7386
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4850)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.174 (n=1588)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4878)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1645)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4983)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.178 (n=1655)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4973)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.179 (n=1642)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4986)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=1653)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=5037)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.231 (n=1632)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=5058)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2257)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=7246)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.272 (n=1513)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=4923)

- **FILTRO** `ibs_7min` < `0.2639` → IC=-0.221 (n=1609)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2639
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4827)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1486)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4950)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.207 (n=2102)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=6887)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1195)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=591)

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

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4167` → IC=+0.148 (n=583)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4167 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.119)

- **PATRÓN** `total_vol_5m` < `447.889` → IC=+0.153 (n=292)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 447.889 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.127 (n=738)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 53.0 (IC base=+0.119)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.162 (n=69)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.231 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `417.524` → IC=+0.141 (n=179)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 417.524 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2595.9196` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2595.9196 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 10.0 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 11.0 (IC base=+0.107)

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
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.167 (n=154)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.179 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 11.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `5210.77` → IC=+0.167 (n=103)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 5210.77 (IC base=+0.133)

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

- **FILTRO** `pct_vs_K` |x|> `3.0996` → IC=-0.426 (n=133)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0996
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=262)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=234)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=326)

- **PATRÓN** `streak_estiramiento` < `0.4493` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `streak_estiramiento` < 0.4493 (IC base=+0.036)

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

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 48.0 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `2492.9344` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2492.9344 (IC base=+0.066)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=505)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=735)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1319)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=876)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=867)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3266)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1684)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.238 (n=686)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.203 (n=1812)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2193` → IC=+0.209 (n=686)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2193 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1267` → IC=+0.233 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1267 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=2130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.6154` → IC=+0.277 (n=2059)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6154 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.199 (n=1027)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.861` → IC=+0.275 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.861 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2955.5044` → IC=+0.204 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.5044 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.217 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.198)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=888)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.228 (n=442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.280 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.213 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.247 (n=200)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.267 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.275 (n=442)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.395` → IC=+0.264 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.395 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.247 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.212)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.296` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.296
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=532)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.226 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.191)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0623` → IC=+0.206 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0623 (IC base=+0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.236 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.282 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5926 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.3286` → IC=+0.194 (n=243)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.3286 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.263` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.263 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=267)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `3082.6104` → IC=+0.289 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3082.6104 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.191)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.191` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.191 (IC base=+0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.278 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.224 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.205)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0641` → IC=+0.208 (n=467)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0641 (IC base=+0.205)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0847` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0847 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.233 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.5769` → IC=+0.290 (n=522)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5769 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.2174` → IC=+0.218 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2174 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.241` → IC=+0.245 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.241 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.318` → IC=+0.205 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.318 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2935.997` → IC=+0.290 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2935.997 (IC base=+0.205)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.143 (n=592)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.72€ cuando `ibs_15` < 0.1176 (IC base=+0.057)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.359 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.361 (n=487)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.357 (n=327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.380 (n=324)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.388 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.371 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.394 (n=487)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.4313` → IC=+0.386 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4313 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.259` → IC=+0.362 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.259 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.354 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.354)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.359 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `3823.0046` → IC=+0.372 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3823.0046 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `446.0` → IC=+0.375 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 446.0 (IC base=+0.354)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.369 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.379 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.0537` → IC=+0.370 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0537 (IC base=+0.360)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.367 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1528` → IC=+0.383 (n=178)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1528 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.395 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.382 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.392 (n=267)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.414 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.072` → IC=+0.364 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.072 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.360 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `16375.6255` → IC=+0.379 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16375.6255 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `502.0` → IC=+0.413 (n=193)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=2350)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1110)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2022)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.176 (n=507)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=-0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1355` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1355 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.276 (n=760)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.196 (n=619)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1241` → IC=+0.254 (n=1569)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1241 (IC base=-0.021)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1803` → IC=+0.254 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1803 (IC base=-0.021)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.277 (n=2353)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6686` → IC=+0.299 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6686 (IC base=-0.021)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.209 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1429)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.218 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1428)

- **FILTRO** `sigma_ewma_delta_pct` > `23.635` → IC=-0.257 (n=270)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.635
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1634)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.170 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0028 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.302 (n=104)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.085)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.122 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.330 (n=228)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.289 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.275 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.085)

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

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.248 (n=896)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.247 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.7826` → IC=+0.250 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7826 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2077` → IC=+0.265 (n=406)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2077 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.270 (n=896)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.7515` → IC=+0.306 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7515 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.287` → IC=+0.276 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.287 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.242 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.232 (n=248)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=484)

- **FILTRO** `drift_15min` |x|> `0.9054` → IC=-0.272 (n=182)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9054
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=550)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.196 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=369)

- **FILTRO** `sigma_ewma_delta_pct` > `18.27` → IC=-0.139 (n=391)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.27
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3165)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.196 (n=54)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.5625 (IC base=-0.173)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 47.0 (IC base=-0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0785` → IC=+0.226 (n=345)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0785 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.183` → IC=+0.230 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.183 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.271 (n=387)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7153` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7153 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1775` → IC=+0.231 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1775 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.264 (n=443)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=444)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.264 (n=256)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=631)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1446` → IC=+0.277 (n=272)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1446 (IC base=-0.033)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.328 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.033)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.297 (n=599)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` > `0.8782` → IC=+0.352 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8782 (IC base=-0.033)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.298 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.331 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.308 (n=264)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2191` → IC=+0.320 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2191 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.326 (n=792)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.444` → IC=+0.335 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.444 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.346 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14636.8174` → IC=+0.304 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14636.8174 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.294 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.337 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.316 (n=145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.303 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.314 (n=434)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.4191` → IC=+0.350 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4191 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.15` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.15 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `16217.9862` → IC=+0.330 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16217.9862 (IC base=+0.284)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6154 sube el IC de +0.198 a +0.277 en UPDOWN_GBM#15min (n=2059). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.212 a +0.275 en UPDOWN_GBM#BTC#15min (n=442). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.659 sube el IC de +0.142 a +0.264 en UPDOWN_GBM#ETH#15min (n=422). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.191 a +0.282 en UPDOWN_GBM#SOL#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5769 sube el IC de +0.205 a +0.290 en UPDOWN_GBM#XRP#15min (n=522). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.065 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=760). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.021 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=2353). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.085 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=228). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.501 sube el IC de -0.191 a +0.306 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.154 a +0.259 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=367). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.361 sube el IC de +0.237 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=896). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.173 a +0.196 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=54). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.271 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=387). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.033 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=599). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.291 a +0.326 en UPDOWN_GBM_IBS_ALTO (n=792). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.284 a +0.314 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=434). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8722 sube el IC de +0.297 a +0.348 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=320). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.354 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=487). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.360 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=267). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7408 sube el IC de +0.344 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=220). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1505 | +0.096 | +185.62€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1505 | +0.096 | +185.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1143 | +0.104 | +162.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1143 | +0.104 | +162.04€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 260 | +0.061 | +9.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 260 | +0.061 | +9.45€ | 4 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 71 | +0.103 | +14.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 71 | +0.103 | +14.46€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 81 | +0.078 | +20.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 81 | +0.078 | +20.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 67 | +0.094 | +17.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 67 | +0.094 | +17.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 14 | +0.000 | +2.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 14 | +0.000 | +2.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 32177 | -0.089 | -4243.07€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1649 | -0.023 | -223.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 30528 | -0.093 | -4019.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4188 | -0.113 | -701.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4188 | -0.113 | -701.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1649 | -0.023 | -223.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1649 | -0.023 | -223.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3841 | -0.115 | -861.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3841 | -0.115 | -861.66€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8300 | -0.011 | -773.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8300 | -0.011 | -773.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7972 | -0.101 | -517.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7972 | -0.101 | -517.33€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6227 | -0.164 | -1165.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6227 | -0.164 | -1165.57€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 23566 | -0.021 | +3739.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 6097 | +0.001 | +1754.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 17469 | -0.029 | +1985.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 23566 | -0.021 | +3739.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 6097 | +0.001 | +1754.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 17469 | -0.029 | +1985.10€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 109388 | +0.113 | -5243.61€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15669 | +0.183 | -496.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 459 | -0.058 | -58.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 86390 | +0.101 | -4431.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6870 | +0.105 | -256.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14351 | +0.101 | -1083.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 50 | -0.135 | +11.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14286 | +0.102 | -1083.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 21816 | +0.130 | -414.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4772 | +0.198 | -143.92€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14325 | +0.114 | -188.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2677 | +0.094 | -59.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14396 | +0.092 | -1235.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 58 | -0.117 | -8.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14323 | +0.093 | -1216.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 23230 | +0.124 | -442.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6244 | +0.176 | -96.44€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14483 | +0.105 | -280.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2491 | +0.101 | -57.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 21226 | +0.114 | -1202.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4493 | +0.187 | -269.05€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 362 | -0.019 | -4.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14669 | +0.093 | -789.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1702 | +0.131 | -139.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14369 | +0.099 | -864.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14304 | +0.100 | -874.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17410 | +0.194 | -1089.03€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17410 | +0.194 | -1089.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4066 | +0.173 | -388.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4066 | +0.173 | -388.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1763 | +0.200 | -24.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1763 | +0.200 | -24.22€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4008 | +0.181 | -325.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4008 | +0.181 | -325.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3544 | +0.242 | -116.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3544 | +0.242 | -116.05€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3950 | +0.190 | -249.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3950 | +0.190 | -249.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 814 | +0.431 | -20.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 814 | +0.431 | -20.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 320 | +0.441 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 320 | +0.441 | -1.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 307 | +0.432 | -6.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 307 | +0.432 | -6.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 175 | +0.410 | -10.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 175 | +0.410 | -10.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 60438 | +0.198 | -4659.73€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 60438 | +0.198 | -4659.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10403 | +0.179 | -1156.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10403 | +0.179 | -1156.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9694 | +0.222 | -361.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9694 | +0.222 | -361.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10416 | +0.174 | -1209.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10416 | +0.174 | -1209.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9772 | +0.218 | -388.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9772 | +0.218 | -388.24€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 10008 | +0.202 | -662.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 10008 | +0.202 | -662.98€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 10145 | +0.192 | -881.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 10145 | +0.192 | -881.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 22987 | +0.115 | +114.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 22987 | +0.115 | +114.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11413 | +0.119 | +122.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11413 | +0.119 | +122.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11574 | +0.111 | -8.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11574 | +0.111 | -8.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1669 | +0.288 | -25.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1669 | +0.288 | -25.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 749 | +0.279 | -17.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 749 | +0.279 | -17.31€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1279 | +0.065 | -69.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 451 | +0.052 | -41.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 828 | +0.072 | -28.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 66 | +0.103 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1007 | +0.071 | -38.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 179 | +0.064 | -9.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 828 | +0.072 | -28.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 206 | +0.024 | -33.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 206 | +0.024 | -33.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 43716 | +0.098 | -1250.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3564 | +0.091 | +44.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 40152 | +0.098 | -1295.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 24315 | +0.102 | -343.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3564 | +0.091 | +44.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 20751 | +0.104 | -387.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8563 | +0.107 | -43.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8563 | +0.107 | -43.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10838 | +0.080 | -864.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10838 | +0.080 | -864.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 862 | +0.208 | -101.16€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 862 | +0.208 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 862 | +0.208 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 862 | +0.208 | -101.16€ | 1 | 4 |
| ✅ GBM_LATE_15M | 30783 | +0.087 | +15192.97€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 30783 | +0.087 | +15192.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5163 | +0.202 | +3952.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5163 | +0.202 | +3952.77€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 4600 | +0.177 | +3283.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4600 | +0.177 | +3283.59€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5443 | +0.199 | +4091.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5443 | +0.199 | +4091.18€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4392 | +0.029 | +1093.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4392 | +0.029 | +1093.88€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4384 | -0.030 | +976.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4384 | -0.030 | +976.59€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 6801 | -0.037 | +1794.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6801 | -0.037 | +1794.96€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 32995 | +0.088 | +17616.44€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 32995 | +0.088 | +17616.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6336 | +0.013 | +3298.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6336 | +0.013 | +3298.06€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6855 | +0.014 | +1439.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6855 | +0.014 | +1439.60€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4674 | +0.268 | +4813.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4674 | +0.268 | +4813.92€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5492 | +0.009 | +1197.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5492 | +0.009 | +1197.74€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5322 | +0.035 | +2144.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5322 | +0.035 | +2144.83€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4316 | +0.283 | +4722.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4316 | +0.283 | +4722.28€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 24731 | +0.172 | +19061.36€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 24731 | +0.172 | +19061.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3718 | +0.215 | +3090.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3718 | +0.215 | +3090.07€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3917 | +0.149 | +2843.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3917 | +0.149 | +2843.93€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3910 | +0.212 | +3173.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3910 | +0.212 | +3173.58€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4159 | +0.136 | +3069.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4159 | +0.136 | +3069.05€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4627 | +0.121 | +3332.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4627 | +0.121 | +3332.52€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4400 | +0.208 | +3552.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4400 | +0.208 | +3552.21€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6737 | +0.138 | +3164.39€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6737 | +0.138 | +3164.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 337 | +0.143 | +187.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 337 | +0.143 | +187.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1951 | +0.140 | +1028.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1951 | +0.140 | +1028.72€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2010 | +0.153 | +980.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2010 | +0.153 | +980.40€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1531 | +0.111 | +560.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1531 | +0.111 | +560.02€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 534 | +0.134 | +230.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 534 | +0.134 | +230.88€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 31043 | +0.178 | +23748.24€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 31043 | +0.178 | +23748.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4917 | +0.229 | +4335.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4917 | +0.229 | +4335.57€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4843 | +0.147 | +3147.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4843 | +0.147 | +3147.90€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5164 | +0.226 | +4463.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5164 | +0.226 | +4463.49€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5043 | +0.134 | +3550.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5043 | +0.134 | +3550.55€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5445 | +0.120 | +3689.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5445 | +0.120 | +3689.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5631 | +0.211 | +4560.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5631 | +0.211 | +4560.97€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8566 | +0.172 | +5668.82€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8566 | +0.172 | +5668.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2064 | +0.166 | +1485.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2064 | +0.166 | +1485.55€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2816 | +0.178 | +1856.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2816 | +0.178 | +1856.79€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 889 | +0.150 | +514.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 889 | +0.150 | +514.52€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2199 | +0.071 | +797.30€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2199 | +0.071 | +797.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 824 | +0.091 | +293.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 824 | +0.091 | +293.25€ | 0 | 15 |
| ✅ GBM_LATE_60M#ETH | 701 | +0.069 | +312.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 701 | +0.069 | +312.66€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 674 | +0.047 | +191.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 674 | +0.047 | +191.39€ | 2 | 11 |
| 🚫 GBM_LATE_60M_FADE | 435 | -0.237 | -7.19€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 435 | -0.237 | -7.19€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 162 | -0.213 | -3.95€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 162 | -0.213 | -3.95€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 148 | -0.227 | +1.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 148 | -0.227 | +1.04€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 125 | -0.272 | -4.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 125 | -0.272 | -4.28€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 904 | +0.094 | +241.50€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 904 | +0.094 | +241.50€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 340 | +0.088 | +80.69€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 340 | +0.088 | +80.69€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 305 | +0.064 | +44.18€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 305 | +0.064 | +44.18€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 259 | +0.136 | +116.62€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 259 | +0.136 | +116.62€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 122 | +0.258 | +105.64€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 122 | +0.258 | +105.64€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2528 | +0.107 | +704.71€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2528 | +0.107 | +704.71€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2528 | +0.107 | +704.71€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2528 | +0.107 | +704.71€ | 0 | 3 |
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
| ✅ LIQUIDACIONES_5M | 2648 | +0.021 | +72.32€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2648 | +0.021 | +72.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 134 | +0.029 | -0.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 134 | +0.029 | -0.60€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 382 | +0.034 | +35.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 382 | +0.034 | +35.52€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 198 | -0.020 | -5.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 198 | -0.020 | -5.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1024 | +0.032 | +31.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1024 | +0.032 | +31.13€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 606 | +0.008 | -1.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 606 | +0.008 | -1.86€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 304 | +0.020 | +13.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 304 | +0.020 | +13.71€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1303 | -0.046 | -29.76€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1303 | -0.046 | -29.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 371 | -0.042 | -13.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 371 | -0.042 | -13.17€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 434 | -0.030 | -2.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 434 | -0.030 | -2.25€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 498 | -0.062 | -14.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 498 | -0.062 | -14.34€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3988 | -0.024 | +38.66€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1864 | -0.030 | -12.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2124 | -0.018 | +51.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 108 | -0.009 | +2.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 56 | +0.035 | +7.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 52 | -0.056 | -4.31€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 980 | -0.002 | +44.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 453 | -0.008 | +11.83€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 527 | +0.003 | +32.67€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 453 | -0.025 | +7.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 219 | -0.043 | -4.34€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 234 | -0.009 | +12.18€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 804 | -0.043 | -32.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 364 | -0.057 | -27.81€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 440 | -0.032 | -4.78€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 787 | -0.030 | +1.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 377 | -0.038 | -4.26€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 410 | -0.022 | +5.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 856 | -0.026 | +14.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 395 | -0.024 | +4.86€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 461 | -0.027 | +10.06€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 35345 | -0.004 | +1626.36€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 35345 | -0.004 | +1626.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6285 | +0.022 | +810.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6285 | +0.022 | +810.14€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5326 | -0.031 | -80.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5326 | -0.031 | -80.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6369 | +0.018 | +579.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6369 | +0.018 | +579.74€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5114 | -0.052 | -153.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5114 | -0.052 | -153.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5954 | -0.008 | +203.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5954 | -0.008 | +203.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6297 | +0.012 | +267.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6297 | +0.012 | +267.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6092 | -0.060 | -147.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6092 | -0.060 | -147.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1484 | -0.080 | -36.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1484 | -0.080 | -36.26€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 694 | -0.125 | -32.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 694 | -0.125 | -32.71€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1798 | -0.077 | -33.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1798 | -0.077 | -33.40€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 88978 | -0.072 | +1910.85€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 88978 | -0.072 | +1910.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 15224 | -0.074 | +931.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 15224 | -0.074 | +931.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13561 | -0.096 | -714.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13561 | -0.096 | -714.95€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15481 | -0.066 | +858.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15481 | -0.066 | +858.50€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 13094 | -0.092 | -274.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 13094 | -0.092 | -274.00€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 16193 | -0.050 | +354.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 16193 | -0.050 | +354.32€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15425 | -0.062 | +755.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15425 | -0.062 | +755.37€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7932 | -0.029 | -137.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7932 | -0.029 | -137.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1847 | -0.040 | -15.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1847 | -0.040 | -15.72€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1007 | -0.021 | -32.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2238 | -0.024 | -28.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2238 | -0.024 | -28.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1075 | -0.044 | -16.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1075 | -0.044 | -16.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 769 | -0.021 | -24.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 769 | -0.021 | -24.37€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1301 | +0.113 | +466.45€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1165 | +0.119 | +453.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 271 | +0.141 | +139.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 271 | +0.141 | +139.74€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 222 | +0.107 | +61.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 222 | +0.107 | +61.84€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 239 | +0.110 | +90.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 239 | +0.110 | +90.46€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 205 | +0.133 | +95.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 205 | +0.133 | +95.88€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 228 | +0.100 | +65.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 228 | +0.100 | +65.94€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 767 | -0.028 | -32.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 767 | -0.028 | -32.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 151 | +0.010 | +8.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 151 | +0.010 | +8.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 110 | -0.036 | -7.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 110 | -0.036 | -7.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 217 | -0.048 | -19.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 217 | -0.048 | -19.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 165 | -0.009 | -2.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 165 | -0.009 | -2.98€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE | 847 | -0.201 | -43.79€ | 3 | 0 |
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
| ✅ STREAK_FADE_15M | 598 | +0.028 | +16.72€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 598 | +0.028 | +16.72€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 292 | +0.024 | +2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 292 | +0.024 | +2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 43 | +0.056 | +0.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 63 | -0.008 | -1.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 63 | -0.008 | -1.69€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 200 | +0.040 | +14.82€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 200 | +0.040 | +14.82€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 3020 | -0.024 | -125.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3020 | -0.024 | -125.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 902 | -0.021 | -31.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 902 | -0.021 | -31.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 577 | -0.025 | -24.71€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 577 | -0.025 | -24.71€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1385 | -0.022 | -55.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1385 | -0.022 | -55.17€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 83 | -0.053 | -8.48€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 83 | -0.053 | -8.48€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 45 | -0.011 | -4.04€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 45 | -0.011 | -4.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9335 | +0.021 | +120.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9335 | +0.021 | +120.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2596 | +0.023 | +32.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2596 | +0.023 | +32.51€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2134 | +0.030 | +52.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2134 | +0.030 | +52.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2820 | +0.011 | +4.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2820 | +0.011 | +4.14€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1785 | +0.023 | +31.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1785 | +0.023 | +31.48€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8306 | +0.014 | -35.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8306 | +0.014 | -35.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3285 | +0.018 | -3.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3285 | +0.018 | -3.13€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3303 | +0.013 | -19.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3303 | +0.013 | -19.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1718 | +0.008 | -13.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1718 | +0.008 | -13.23€ | 1 | 0 |
| ✅ UPDOWN_GBM | 49978 | +0.039 | +3511.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 12872 | +0.075 | +2593.15€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1720 | +0.005 | +9.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 32214 | +0.030 | +874.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2986 | +0.005 | +36.43€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 5082 | +0.075 | +644.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 961 | +0.158 | +423.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 4088 | +0.057 | +222.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9595 | +0.047 | +746.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1680 | +0.089 | +384.00€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 460 | +0.013 | +5.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 6036 | +0.048 | +321.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1349 | +0.006 | +34.88€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 70 | -0.083 | +0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5823 | +0.045 | +418.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 930 | +0.141 | +338.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4865 | +0.027 | +81.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 11007 | +0.029 | +558.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3201 | +0.053 | +420.89€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 453 | +0.008 | +9.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6282 | +0.024 | +128.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1010 | +0.002 | -3.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 61 | -0.119 | +3.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 11180 | +0.019 | +358.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3055 | +0.029 | +245.16€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 444 | -0.002 | -0.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 7001 | +0.018 | +114.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 627 | +0.007 | +4.63€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 53 | -0.154 | -4.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7289 | +0.044 | +786.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3045 | +0.091 | +781.12€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 302 | +0.003 | -2.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3942 | +0.010 | +7.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 184 | -0.118 | -0.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 649 | +0.354 | +224.12€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 649 | +0.354 | +224.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 356 | +0.360 | +121.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 356 | +0.360 | +121.63€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 293 | +0.344 | +102.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 293 | +0.344 | +102.50€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14513 | -0.030 | +3355.34€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14513 | -0.030 | +3355.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1054 | -0.053 | +383.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1054 | -0.053 | +383.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2632 | -0.115 | +117.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2632 | -0.115 | +117.01€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 578 | +0.202 | +437.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 578 | +0.202 | +437.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1681 | +0.214 | +1086.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1681 | +0.214 | +1086.27€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4288 | -0.062 | +610.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4288 | -0.062 | +610.47€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4280 | -0.069 | +721.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4280 | -0.069 | +721.05€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 168 | +0.035 | +7.74€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 168 | +0.035 | +7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 168 | +0.035 | +7.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 168 | +0.035 | +7.74€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1055 | +0.291 | +875.12€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1055 | +0.291 | +875.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 578 | +0.284 | +442.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 578 | +0.284 | +442.03€ | 0 | 9 |
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