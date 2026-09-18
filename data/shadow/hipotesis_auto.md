# Hipótesis automáticas — 2026-09-18 05:11 UTC
_Generado por shadow_postmortem.py sobre 491961 resoluciones (PNL=+53119.20€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=443)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=416)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.248 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8028` → IC=+0.260 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8028 (IC base=+0.123)

- **PATRÓN** `banda_z` > `10.232` → IC=+0.226 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.232 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.139 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=514)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2807.4678` → IC=+0.131 (n=323)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2807.4678 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=342)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=292)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=317)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.256 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.220 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.7972` → IC=+0.268 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7972 (IC base=+0.130)

- **PATRÓN** `banda_z` > `11.377` → IC=+0.250 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.377 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=429)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 88.0 (IC base=+0.032)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=87)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.103)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.103)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.043 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `1185.8848` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1185.8848 (IC base=+0.103)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.194)

- **PATRÓN** `banda_hit_calibrado` > `0.5987` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `banda_hit_calibrado` > 0.5987 (IC base=+0.194)

- **PATRÓN** `banda_z` > `3.283` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 3.283 (IC base=+0.194)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.278 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.194)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `144.2` → IC=-0.249 (n=6043)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.2
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=18131)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `141.1` → IC=-0.261 (n=833)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.1
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=2501)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `493.2` → IC=-0.158 (n=320)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 493.2
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=960)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `132.89` → IC=-0.295 (n=736)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.89
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2210)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.99` → IC=-0.239 (n=1431)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.99
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4293)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `118.1` → IC=-0.366 (n=1173)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 118.1
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=3520)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.245 (n=288)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=326)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.162 (n=140)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=449)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.252 (n=147)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=167)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.186 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=222)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.255 (n=92)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=118)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.198 (n=12179)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.69 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3047)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `5349.0852` → IC=+0.172 (n=1942)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5349.0852 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=9581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=11472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.246 (n=8368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=5026)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1656.9197` → IC=+0.162 (n=5666)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 1656.9197 (IC base=+0.134)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15379.9983` → IC=+0.231 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15379.9983 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.37` → IC=+0.271 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `13498.7511` → IC=+0.216 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13498.7511 (IC base=+0.201)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.176 (n=285)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4641.025` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4641.025 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.166 (n=303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.435` → IC=+0.153 (n=682)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.435 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=549)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3855.8996` → IC=+0.149 (n=425)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3855.8996 (IC base=+0.125)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=2077)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.328 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.330 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `3755.7636` → IC=+0.247 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3755.7636 (IC base=+0.241)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.133 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.150 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.230 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=475)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `1910.0703` → IC=+0.157 (n=377)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1910.0703 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.225 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.196 (n=1123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 12.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.427 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.268 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.175 (n=1146)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.03 (IC base=+0.172)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.172 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 13.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.359 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.222 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=337)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.116)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=9603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=9226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.223 (n=3372)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.177 (n=2386)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.300 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.273 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.270)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.358 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.270)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=1995)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.323 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.237)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1955)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.195 (n=1641)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.436 (n=388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `2044.7957` → IC=+0.443 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2044.7957 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.440 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.457 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `12599.6821` → IC=+0.446 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12599.6821 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.453 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.465 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.439 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.417 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.410 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.406 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.410)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=28522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.238 (n=10800)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=4923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=5303)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=5080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=5080)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=2760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=5267)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=1953)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.265 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=4716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.255 (n=2395)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=5615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.250 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.204 (n=4369)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.08` → IC=+0.134 (n=3986)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.08 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.150 (n=4052)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.95 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=5269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.26` → IC=+0.150 (n=3989)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.26 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=2202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.128)

- **PATRÓN** `restante_min` < `4.02` → IC=+0.136 (n=1983)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.02 (IC base=+0.128)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.147 (n=1984)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.94 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.142 (n=2929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 8.0 (IC base=+0.128)

- **PATRÓN** `lag_apertura_s` < `3.87` → IC=+0.148 (n=1977)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 3.87 (IC base=+0.128)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.202 (n=2167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2655)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.147 (n=2084)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.96 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=2669)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.43` → IC=+0.148 (n=2009)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 2.43 (IC base=+0.120)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.312 (n=685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1604.6829` → IC=+0.294 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.6829 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.288 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.267)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `4209.1188` → IC=+0.285 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4209.1188 (IC base=+0.267)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1491.7936` → IC=+0.317 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1491.7936 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.342 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.335)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.361 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.335)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.371 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.335)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.442 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.440 (n=382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.436 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `1860.5823` → IC=+0.440 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.5823 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.449 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.436 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `2089.6231` → IC=+0.456 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2089.6231 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.375 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.378)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.735` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.298 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.735` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.298 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.349` → IC=+0.121 (n=5781)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.349 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.9773` → IC=+0.233 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9773 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.1998` → IC=+0.246 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1998 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.835` → IC=+0.169 (n=2547)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 5.835 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.2223` → IC=+0.244 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2223 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `1.0678` → IC=+0.244 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0678 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.308` → IC=+0.208 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.308 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `1.9158` → IC=+0.200 (n=2915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9158 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.571` → IC=+0.131 (n=8014)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.571 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.5492` → IC=+0.184 (n=486)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5492 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1358` → IC=+0.170 (n=2490)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1358 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.7018` → IC=+0.174 (n=1170)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7018 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `0.8721` → IC=+0.174 (n=1772)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8721 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.220 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `1.5864` → IC=+0.200 (n=3945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5864 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.209 (n=4187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.060)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.183 (n=496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.175 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.008 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.329` → IC=+0.164 (n=1485)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.329 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.181 (n=737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 8.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.269 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.977` → IC=+0.273 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.977 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.207 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4319` → IC=+0.164 (n=1371)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4319 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=1409)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.249 (n=979)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0878` → IC=+0.292 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0878 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.291 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.353` → IC=+0.247 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.353 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.232 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.258 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.253 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1749.389` → IC=+0.251 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1749.389 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.225 (n=989)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1157` → IC=+0.244 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1157 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9153` → IC=+0.259 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9153 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1847` → IC=+0.215 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1847 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.3501` → IC=+0.215 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3501 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.811` → IC=+0.232 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.811 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.224 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8755` → IC=+0.214 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8755 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.216 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.226 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.225 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11045.5521` → IC=+0.224 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11045.5521 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.152 (n=1057)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0049 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.154 (n=400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.165 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6747` → IC=+0.172 (n=1198)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6747 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.123` → IC=+0.150 (n=1094)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.123 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.596` → IC=+0.159 (n=391)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 6.596 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.144 (n=1198)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2116 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.138 (n=1198)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6183 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.178 (n=324)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.150 (n=1089)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4244` → IC=+0.141 (n=1090)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4244 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `13589.8332` → IC=+0.147 (n=799)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 13589.8332 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `241.0` → IC=+0.156 (n=443)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 241.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.193 (n=1453)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0059 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=1520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.183 (n=967)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.471` → IC=+0.232 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.471 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1059` → IC=+0.186 (n=1235)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1059 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.374` → IC=+0.186 (n=189)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.374 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.987` → IC=+0.198 (n=618)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.987 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.192 (n=1677)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.224 (n=1239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.3824` → IC=+0.232 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3824 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.234 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.323` → IC=+0.216 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.323 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.266 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.846` → IC=+0.205 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.846 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.3036` → IC=+0.225 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3036 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1900.3784` → IC=+0.235 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1900.3784 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.221 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1836)

- **PATRÓN** `ibs_20min` > `0.9367` → IC=+0.181 (n=299)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.9367 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.328` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.328 (IC base=+0.008)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.418` → IC=+0.136 (n=570)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.418 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6604` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6604 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.366 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1956 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.4916` → IC=+0.346 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4916 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.7922` → IC=+0.334 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7922 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.344 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.1655` → IC=+0.183 (n=225)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1655 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.163 (n=274)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6955 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2668` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2668 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.5033` → IC=+0.185 (n=510)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.5033 (IC base=+0.007)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=261)

- **FILTRO** `ibs_20min` < `0.375` → IC=-0.173 (n=102)

  - _Acción_: SKIP cuando `ibs_20min` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=212)

- **FILTRO** `ibs_20min` > `0.2727` → IC=-0.132 (n=1830)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=909)

- **FILTRO** `sigma_ewma_delta_pct` > `8.632` → IC=-0.210 (n=301)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.632
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2438)

- **PATRÓN** `ibs_20min` > `0.7576` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7576 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.6368` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6368 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `0.7957` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7957 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.8428` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8428 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.2727` → IC=+0.121 (n=909)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2727 (IC base=-0.048)

- **PATRÓN** `dist_vwap_pct` > `0.7042` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7042 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` < `1.1047` → IC=+0.210 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1047 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1972` → IC=+0.216 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1972 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.0844` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0844 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.048)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6598` → IC=-0.192 (n=459)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6598
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=1380)

- **FILTRO** `ibs_20min` < `0.6689` → IC=-0.159 (n=1213)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6689
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=626)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=383)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1456)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.200 (n=692)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2081)

- **PATRÓN** `dist_vwap_pct` > `0.9583` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9583 (IC base=-0.081)

- **PATRÓN** `dist_vwap_pct` < `0.2397` → IC=+0.314 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2397 (IC base=-0.081)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.288 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=-0.081)

- **PATRÓN** `volumen_spike_ratio` < `2.5002` → IC=+0.276 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5002 (IC base=-0.081)

- **PATRÓN** `volumen_spike_ratio` > `1.8422` → IC=+0.285 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8422 (IC base=-0.081)

- **PATRÓN** `dist_vwap_pct` > `0.9769` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9769 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2574` → IC=+0.247 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2574 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7359` → IC=+0.252 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7359 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.293 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.272 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.2213` → IC=+0.258 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2213 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4734` → IC=+0.245 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4734 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.246 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.184 (n=2740)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0093 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.4593` → IC=+0.180 (n=7318)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4593 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.694` → IC=+0.281 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.694 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.503` → IC=+0.148 (n=3878)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.503 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.6792` → IC=+0.241 (n=2502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6792 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.262 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4779` → IC=+0.245 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4779 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.7512` → IC=+0.240 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7512 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.278 (n=3982)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.089)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.139 (n=2772)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0086 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.5543` → IC=+0.150 (n=7307)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5543 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.238 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1626` → IC=+0.234 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1626 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `0.7166` → IC=+0.236 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7166 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.201` → IC=+0.249 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.201 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.2499` → IC=+0.316 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2499 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `2.3657` → IC=+0.256 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3657 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.257 (n=2872)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.069)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.274` → IC=-0.166 (n=423)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.274
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1414)

- **PATRÓN** `ibs_20min` > `0.8772` → IC=+0.260 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8772 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.657` → IC=+0.188 (n=302)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 8.657 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.211 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8214` → IC=-0.146 (n=608)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8214
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1832)

- **PATRÓN** `dist_vwap_pct` > `0.2872` → IC=+0.147 (n=267)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.2872 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.1582` → IC=+0.138 (n=619)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1582 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.0507` → IC=+0.135 (n=637)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0507 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.6591` → IC=+0.145 (n=646)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6591 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.188 (n=235)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.191 (n=231)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 229.0 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.210 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `1.1444` → IC=+0.214 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1444 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `485.0` → IC=+0.210 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 485.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.286 (n=870)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.244 (n=435)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.246 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.257 (n=495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.826` → IC=+0.281 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.826 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.11` → IC=+0.257 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.11 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.8724` → IC=+0.245 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8724 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `3.5936` → IC=+0.257 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5936 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1912.1584` → IC=+0.246 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1584 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.297 (n=1032)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.317 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.284 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.883` → IC=+0.299 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.883 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.304 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` < `1.6355` → IC=+0.284 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6355 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `2.2184` → IC=+0.280 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2184 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `1887.9956` → IC=+0.303 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.9956 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.277 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.279)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2517` → IC=-0.213 (n=382)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2517
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1146)

- **FILTRO** `ibs_20min` > `0.8009` → IC=-0.183 (n=490)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8009
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1474)

- **PATRÓN** `ibs_20min` > `0.8055` → IC=+0.153 (n=520)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.8055 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` > `0.4369` → IC=+0.206 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4369 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.1812` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1812 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `0.9592` → IC=+0.218 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9592 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` > `0.6273` → IC=+0.199 (n=333)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.6273 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2642` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2642 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.0676` → IC=+0.241 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0676 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.3739` → IC=+0.221 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3739 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.249 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` > `0.1219` → IC=+0.215 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1219 (IC base=-0.012)

- **PATRÓN** `volumen_regimen` < `0.6651` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6651 (IC base=-0.012)

- **PATRÓN** `volumen_regimen` > `0.7266` → IC=+0.186 (n=243)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.7266 (IC base=-0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=-0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.7898` → IC=+0.244 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7898 (IC base=-0.012)

- **PATRÓN** `volumen_spike_ratio` > `1.5204` → IC=+0.250 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5204 (IC base=-0.012)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.251 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=-0.012)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6824` → IC=-0.213 (n=882)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6824
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=882)

- **FILTRO** `ibs_20min` > `0.7083` → IC=-0.232 (n=460)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7083
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=1389)

- **FILTRO** `sigma_ewma_delta_pct` > `4.635` → IC=-0.174 (n=427)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.635
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1422)

- **PATRÓN** `ibs_20min` > `0.6824` → IC=+0.265 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6824 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7895` → IC=+0.336 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7895 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.399` → IC=+0.149 (n=274)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 9.399 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.293 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6366` → IC=+0.282 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6366 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1055` → IC=+0.279 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1055 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.312 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.320 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.1081` → IC=+0.200 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1081 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` < `0.3962` → IC=+0.193 (n=408)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.3962 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.7171` → IC=+0.239 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7171 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.180 (n=364)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2666` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2666 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.5876` → IC=+0.200 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5876 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4993` → IC=+0.178 (n=371)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4993 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.215 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.323 (n=726)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.280 (n=1140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.348 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.2673` → IC=+0.319 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2673 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.398` → IC=+0.300 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.398 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `0.6887` → IC=+0.290 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6887 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2876` → IC=+0.305 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2876 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `1.5463` → IC=+0.281 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5463 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.199` → IC=+0.284 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.199 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.277 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `2433.8665` → IC=+0.284 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2433.8665 (IC base=+0.274)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.272 (n=402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.296 (n=802)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.285 (n=603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3953` → IC=+0.306 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3953 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.5341` → IC=+0.289 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5341 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.441` → IC=+0.289 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.441 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `0.6384` → IC=+0.270 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6384 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.2435` → IC=+0.306 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2435 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.243` → IC=+0.364 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.243 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.5453` → IC=+0.264 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5453 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.17` → IC=+0.274 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.17 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.269 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2358.368` → IC=+0.275 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2358.368 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.176 (n=2157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.200 (n=2158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3411` → IC=+0.174 (n=5694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3411 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=6704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.5827` → IC=+0.215 (n=6469)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5827 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.9298` → IC=+0.217 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9298 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.206` → IC=+0.250 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.206 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.2173` → IC=+0.162 (n=4288)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2173 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.158 (n=4287)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6248 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2981` → IC=+0.192 (n=955)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2981 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.5658` → IC=+0.173 (n=2710)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5658 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6626` → IC=+0.171 (n=2053)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6626 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3823.5619` → IC=+0.168 (n=2157)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3823.5619 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.181 (n=5393)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 121.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.186 (n=4178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0064 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.079` → IC=+0.204 (n=2084)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.079 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=2108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4737` → IC=+0.228 (n=6253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4737 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.2201` → IC=+0.160 (n=4647)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2201 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.163` → IC=+0.194 (n=1074)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.163 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.1842` → IC=+0.153 (n=4574)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1842 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6252` → IC=+0.147 (n=4575)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6252 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.227 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.575` → IC=+0.168 (n=2461)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.575 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6493` → IC=+0.174 (n=1864)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6493 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.171 (n=5211)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 122.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.222 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.193 (n=369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0082 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.3276` → IC=+0.203 (n=1106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3276 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.204 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.992` → IC=+0.306 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.992 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.238 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.4266` → IC=+0.178 (n=1009)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4266 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.243 (n=692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=703)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1803` → IC=+0.287 (n=524)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1803 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.239 (n=790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.1059` → IC=+0.272 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1059 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.016` → IC=+0.252 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.016 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.235 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.261 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.254 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1752.6996` → IC=+0.254 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1752.6996 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.256 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.0759` → IC=+0.193 (n=317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0759 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4244` → IC=+0.227 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4244 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.1954` → IC=+0.208 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1954 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.222 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.173 (n=949)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2629 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.232` → IC=+0.187 (n=209)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.232 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4154` → IC=+0.200 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4154 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `10191.6179` → IC=+0.179 (n=948)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 10191.6179 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1072)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.059` → IC=+0.194 (n=358)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.059 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.161 (n=992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 7.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5437` → IC=+0.188 (n=1072)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5437 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1321` → IC=+0.163 (n=1093)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1321 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.156 (n=1072)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2116 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1575` → IC=+0.172 (n=330)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1575 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.152 (n=962)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.159 (n=294)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 223.0 (IC base=+0.142)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.201 (n=1077)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1996` → IC=+0.207 (n=718)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1996 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.63` → IC=+0.273 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.63 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.2141` → IC=+0.189 (n=1037)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2141 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.1338` → IC=+0.187 (n=417)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1338 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.6649` → IC=+0.194 (n=338)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.6649 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `3.5942` → IC=+0.205 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5942 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.204 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.239 (n=894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0885` → IC=+0.240 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0885 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.270 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.253 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.679` → IC=+0.273 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.679 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3606` → IC=+0.271 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3606 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.6443` → IC=+0.215 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6443 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `3.5248` → IC=+0.244 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5248 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1899.5579` → IC=+0.240 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.5579 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.207 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.178 (n=898)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0066 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4277` → IC=+0.164 (n=1021)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.4277 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3958` → IC=+0.201 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3958 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1357` → IC=+0.185 (n=671)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1357 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.01` → IC=+0.249 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.01 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.0523` → IC=+0.155 (n=899)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0523 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.1952` → IC=+0.164 (n=340)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1952 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.223 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.5341` → IC=+0.164 (n=439)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5341 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.5113` → IC=+0.174 (n=332)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5113 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `7083.9363` → IC=+0.186 (n=680)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7083.9363 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.157 (n=645)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 118.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.165 (n=1092)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0071 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.145 (n=1092)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6052` → IC=+0.182 (n=1092)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6052 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.147 (n=1090)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.785` → IC=+0.195 (n=211)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.785 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.145 (n=728)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8556 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.209 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.134 (n=651)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7982 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.4781` → IC=+0.148 (n=325)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.4781 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `10077.5355` → IC=+0.158 (n=495)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10077.5355 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `174.0` → IC=+0.128 (n=905)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 174.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5652` → IC=-0.178 (n=402)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5652
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=1207)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.160 (n=542)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0099 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `0.5156` → IC=+0.200 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5156 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `1.024` → IC=+0.220 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.024 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.465` → IC=+0.257 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.465 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.2251` → IC=+0.122 (n=1194)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2251 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` < `0.1695` → IC=+0.124 (n=1192)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1695 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.8208` → IC=+0.128 (n=765)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8208 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=1234)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2904.4304` → IC=+0.189 (n=541)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2904.4304 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.131 (n=885)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 49.0 (IC base=+0.112)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.154 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0053 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.204 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.134 (n=1093)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.147 (n=259)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.4645` → IC=+0.135 (n=354)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4645 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `2.179` → IC=+0.122 (n=482)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.179 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `3082.2041` → IC=+0.162 (n=403)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3082.2041 (IC base=+0.108)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0183` → IC=+0.212 (n=751)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0183 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1688` → IC=+0.211 (n=496)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1688 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.7267` → IC=+0.254 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7267 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2097` → IC=+0.231 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2097 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.371` → IC=+0.242 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.371 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.207 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2075 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6145` → IC=+0.209 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6145 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.269 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1918` → IC=+0.215 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1918 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4271` → IC=+0.207 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4271 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.203 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.238 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.211 (n=803)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.218 (n=403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.243 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1311` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1311 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.699` → IC=+0.229 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.699 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.216 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6261 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.277 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2422` → IC=+0.196 (n=938)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2422 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4601` → IC=+0.197 (n=1066)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4601 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2553.7488` → IC=+0.212 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2553.7488 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.157 (n=531)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.165 (n=527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.148 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.3929` → IC=+0.170 (n=1581)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3929 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.8094` → IC=+0.170 (n=225)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.8094 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.676` → IC=+0.167 (n=727)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.676 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8707` → IC=+0.154 (n=909)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8707 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.2058` → IC=+0.143 (n=455)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2058 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1642` → IC=+0.171 (n=435)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1642 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4361` → IC=+0.153 (n=505)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4361 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.5693` → IC=+0.171 (n=505)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5693 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=1767)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `8647.8396` → IC=+0.151 (n=717)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8647.8396 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.159 (n=1358)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 160.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.136 (n=1112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0057 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3392` → IC=+0.128 (n=1467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3392 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.4882` → IC=+0.154 (n=1467)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.4882 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.009` → IC=+0.128 (n=482)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 6.009 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2207` → IC=+0.121 (n=1477)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2207 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.142 (n=423)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.2358` → IC=+0.133 (n=1406)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2358 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.123 (n=664)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 25.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.125 (n=374)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.142 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 9.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.2558` → IC=+0.138 (n=374)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.2558 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.2828` → IC=+0.124 (n=123)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.2828 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6135` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6135 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `10454.9515` → IC=+0.130 (n=374)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 10454.9515 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 151.0 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.210 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3374` → IC=+0.147 (n=522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3374 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.3422` → IC=+0.200 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3422 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.453` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 4.453 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.093` → IC=+0.133 (n=592)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 9.093 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.208` → IC=+0.136 (n=522)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.208 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.7175` → IC=+0.150 (n=466)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.7175 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.211 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.152 (n=512)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.415` → IC=+0.142 (n=512)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.415 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `332.0` → IC=+0.146 (n=433)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 332.0 (IC base=+0.131)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.259 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.207 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.220 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.3958` → IC=+0.241 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3958 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.138` → IC=+0.230 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.138 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.085` → IC=+0.237 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.085 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.202 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.226 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2479` → IC=+0.321 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2479 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.3839` → IC=+0.223 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3839 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.391` → IC=+0.266 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.391 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `12307.7364` → IC=+0.213 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12307.7364 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.124 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0067 (IC base=+0.101)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.152 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.128 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 11.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.0561` → IC=+0.181 (n=139)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.0561 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.1427` → IC=+0.123 (n=165)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.1427 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.432` → IC=+0.149 (n=112)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.432 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.170 (n=98)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.8125` → IC=+0.137 (n=265)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8125 (IC base=+0.101)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3272` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3272
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=417)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.129 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.203 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.6084` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6084 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.092` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 5.092 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `2.2136` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.2136 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `3081.1151` → IC=+0.214 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3081.1151 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 21.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.149 (n=340)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.4872 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.7121` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.7121 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.56 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.8803` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8803 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.1233` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1233 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.177 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.022 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.08` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.08 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.126 (n=177)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0734 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6508` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6508 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.133 (n=178)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.6702` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.6702 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.0068` → IC=+0.127 (n=124)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.0068 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.194 (n=3731)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0088 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=8532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.214 (n=8219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.883` → IC=+0.197 (n=1069)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.883 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.233 (n=3071)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8842` → IC=+0.165 (n=3674)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8842 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.194 (n=1550)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.6346` → IC=+0.184 (n=2612)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6346 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3790.4821` → IC=+0.169 (n=2737)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3790.4821 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.193 (n=6036)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 92.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.195 (n=5011)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0068 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.4814` → IC=+0.182 (n=7512)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.4814 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5636` → IC=+0.238 (n=7513)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5636 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2302` → IC=+0.162 (n=4758)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2302 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.835` → IC=+0.195 (n=1077)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.835 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.684` → IC=+0.181 (n=7266)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.684 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.158 (n=2291)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7054 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.2052` → IC=+0.156 (n=1735)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2052 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.244 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.2951` → IC=+0.189 (n=3071)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2951 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.190 (n=2167)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 25.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.208 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.209 (n=933)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3293` → IC=+0.190 (n=1390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3293 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.346 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.246 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.198 (n=590)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.257 (n=714)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.265 (n=1070)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.2039` → IC=+0.282 (n=714)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2039 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=966)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.287 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.416` → IC=+0.262 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.416 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.297 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `1.8803` → IC=+0.277 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8803 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1749.9034` → IC=+0.272 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1749.9034 (IC base=+0.255)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1852` → IC=+0.157 (n=872)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1852 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3149` → IC=+0.201 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3149 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.3233` → IC=+0.194 (n=498)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3233 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.774` → IC=+0.159 (n=306)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.774 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.29` → IC=+0.155 (n=1162)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.29 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6976` → IC=+0.181 (n=575)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6976 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0736` → IC=+0.155 (n=1136)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0736 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.265` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.265 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1195` → IC=+0.159 (n=1102)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1195 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7596` → IC=+0.161 (n=835)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7596 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10984.4814` → IC=+0.168 (n=1168)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10984.4814 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `486.0` → IC=+0.162 (n=1184)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 486.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.166 (n=1161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.263` → IC=+0.167 (n=1022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.263 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.175 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 16.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.6377` → IC=+0.203 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6377 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.167 (n=172)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1262` → IC=+0.163 (n=1073)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1262 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.170 (n=207)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2029` → IC=+0.160 (n=1161)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2029 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1506` → IC=+0.200 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1506 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.409` → IC=+0.164 (n=1063)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.409 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.7532` → IC=+0.157 (n=709)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7532 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `12617.1565` → IC=+0.152 (n=774)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12617.1565 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `366.0` → IC=+0.164 (n=646)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 366.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.230 (n=1314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.215 (n=1329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6721` → IC=+0.253 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6721 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.545` → IC=+0.299 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.545 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.2156` → IC=+0.217 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2156 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.9655` → IC=+0.235 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9655 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1912.5584` → IC=+0.214 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.5584 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.238 (n=1240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.3648` → IC=+0.266 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3648 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.718` → IC=+0.275 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.718 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3588` → IC=+0.295 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3588 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7962` → IC=+0.224 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7962 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.2483` → IC=+0.230 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2483 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1902.0032` → IC=+0.242 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.0032 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.256 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.176 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0034 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4338` → IC=+0.137 (n=1396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.4338 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6982` → IC=+0.230 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6982 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.5525` → IC=+0.175 (n=373)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.5525 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.171` → IC=+0.160 (n=587)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.171 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.156 (n=931)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8782 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.230 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5119` → IC=+0.148 (n=592)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5119 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4087` → IC=+0.148 (n=1343)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4087 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8595.8962` → IC=+0.228 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8595.8962 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.164 (n=427)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 85.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.162 (n=1130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0075 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4443` → IC=+0.159 (n=1130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4443 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6874` → IC=+0.195 (n=1130)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6874 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.2039` → IC=+0.144 (n=1049)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2039 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.985` → IC=+0.186 (n=170)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.985 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.149 (n=497)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6958 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.1764` → IC=+0.154 (n=377)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1764 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.157 (n=1059)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `11048.3545` → IC=+0.202 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11048.3545 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `189.0` → IC=+0.150 (n=1053)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 189.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` > `0.6458` → IC=-0.170 (n=452)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6458
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=1360)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.123 (n=934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0078 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4694` → IC=+0.183 (n=1401)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4694 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0106` → IC=+0.188 (n=251)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 1.0106 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.373` → IC=+0.226 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.373 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=968)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2917.9058` → IC=+0.238 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2917.9058 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.124 (n=1050)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 53.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.178 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0056 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.1279` → IC=+0.156 (n=454)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1279 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.148 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.6458` → IC=+0.202 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6458 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.4725` → IC=+0.127 (n=1324)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.4725 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.454` → IC=+0.123 (n=1307)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.454 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.7211` → IC=+0.148 (n=598)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.7211 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.170 (n=210)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.4685` → IC=+0.148 (n=401)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4685 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2887.2604` → IC=+0.159 (n=453)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2887.2604 (IC base=+0.109)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0243` → IC=+0.219 (n=638)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0243 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.5124` → IC=+0.246 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5124 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1844` → IC=+0.231 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1844 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.388` → IC=+0.250 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.388 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2484` → IC=+0.209 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2484 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6312` → IC=+0.209 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6312 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.233 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.5676` → IC=+0.239 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5676 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2587.456` → IC=+0.208 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.456 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.233 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.220 (n=519)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.214 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.199 (n=1644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 18.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5166` → IC=+0.253 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5166 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.4958` → IC=+0.200 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4958 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2651` → IC=+0.203 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2651 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.11` → IC=+0.253 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.11 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.235 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.256 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2257` → IC=+0.193 (n=1209)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2257 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4437` → IC=+0.198 (n=1374)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4437 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2565.5748` → IC=+0.199 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2565.5748 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=2608)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.156 (n=2242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0094 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.526` → IC=+0.156 (n=2546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.526 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.162 (n=892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9392` → IC=+0.213 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9392 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1876` → IC=+0.156 (n=838)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1876 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.764` → IC=+0.168 (n=822)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.764 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.9082` → IC=+0.153 (n=1037)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9082 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1737` → IC=+0.175 (n=697)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1737 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4616` → IC=+0.163 (n=840)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4616 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.9066` → IC=+0.158 (n=1679)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9066 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8243.4336` → IC=+0.155 (n=1154)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8243.4336 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.187 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0037 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.152 (n=1968)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.158 (n=667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 4.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.1823` → IC=+0.160 (n=866)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1823 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.139 (n=350)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.274` → IC=+0.141 (n=1948)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.274 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1137` → IC=+0.142 (n=1645)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1137 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.149 (n=926)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.5707` → IC=+0.138 (n=1948)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5707 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8229` → IC=+0.143 (n=1299)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8229 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=2608)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7614.1842` → IC=+0.149 (n=1758)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7614.1842 (IC base=+0.133)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.170 (n=280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.172 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0035 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.185 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.192 (n=212)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5413 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2289` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2289 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.256` → IC=+0.164 (n=400)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 8.256 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.2549` → IC=+0.159 (n=318)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2549 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.832` → IC=+0.192 (n=212)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.832 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.3101` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3101 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.213 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.3963` → IC=+0.192 (n=144)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.3963 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `12609.7541` → IC=+0.206 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12609.7541 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.204 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.143 (n=876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.165 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.1568` → IC=+0.160 (n=386)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1568 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.6152` → IC=+0.139 (n=397)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.6152 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.7085` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7085 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.2264` → IC=+0.132 (n=903)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2264 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.156 (n=855)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.176 (n=584)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8847 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.161 (n=414)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.5736` → IC=+0.140 (n=873)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5736 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.142 (n=582)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `11358.9394` → IC=+0.147 (n=876)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 11358.9394 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `712.0` → IC=+0.137 (n=830)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 712.0 (IC base=+0.131)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.180 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4174` → IC=+0.173 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4174 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.9934` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9934 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.404` → IC=+0.217 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.404 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.166 (n=621)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.197 (n=282)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `2463.7708` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2463.7708 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.154 (n=761)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0087 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.153 (n=762)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0045 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.5025` → IC=+0.154 (n=761)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.5025 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.157 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 4.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.186` → IC=+0.157 (n=761)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.186 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.958` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.958 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.4193` → IC=+0.154 (n=724)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4193 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.684` → IC=+0.155 (n=760)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.684 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1122` → IC=+0.149 (n=670)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1122 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.6457` → IC=+0.149 (n=761)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6457 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.1148` → IC=+0.146 (n=701)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1148 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1755` → IC=+0.158 (n=226)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1755 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.173 (n=249)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=725)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `8065.8728` → IC=+0.149 (n=761)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 8065.8728 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.163 (n=550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0071 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.511` → IC=+0.181 (n=625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.511 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.157 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 10.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.161 (n=624)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.1001 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.154` → IC=+0.171 (n=284)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.154 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.3875` → IC=+0.149 (n=644)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.3875 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.985` → IC=+0.162 (n=140)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 8.985 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.261` → IC=+0.149 (n=565)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.261 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6472` → IC=+0.178 (n=209)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6472 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.7274` → IC=+0.155 (n=558)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7274 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.180 (n=267)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.168 (n=540)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4499` → IC=+0.162 (n=613)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4499 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `8082.96` → IC=+0.171 (n=624)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8082.96 (IC base=+0.149)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=137)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=160)

- **PATRÓN** `ibs_20min` > `0.9848` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.9848 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.125` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 7.125 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.156` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.156 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.020)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.253 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=298)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=301)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.211 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.161 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.625` → IC=+0.210 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.625 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.178 (n=321)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.072` → IC=+0.226 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.072 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.0919` → IC=+0.130 (n=611)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0919 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` > `0.9761` → IC=+0.127 (n=277)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.9761 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.4945` → IC=+0.159 (n=503)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4945 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` > `1.4086` → IC=+0.140 (n=503)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4086 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=495)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2468.387` → IC=+0.153 (n=266)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2468.387 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.0631` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0631 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.6098 (IC base=-0.029)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5857` → IC=-0.181 (n=70)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5857
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=210)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.179 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.006 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.5857` → IC=+0.207 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5857 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.734` → IC=+0.132 (n=131)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.734 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `1.0527` → IC=+0.136 (n=185)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0527 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.154 (n=151)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.188 (n=152)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.0426` → IC=+0.200 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0426 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.7371` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7371 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.9523` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9523 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.0643` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0643 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.0748` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.0748 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `3269.2861` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3269.2861 (IC base=+0.045)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=92)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.222 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.177 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.6355` → IC=+0.238 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6355 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.1205` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1205 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.087` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.087 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.0679` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0679 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6313` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6313 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.7434` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7434 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.165 (n=162)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=221)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1101.9191` → IC=+0.195 (n=185)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1101.9191 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1088` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1088 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.073)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.167 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.006 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.191 (n=189)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6667 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.8747` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8747 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.345` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.345 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.7896` → IC=+0.120 (n=127)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 0.7896 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.0632` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0632 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.187 (n=81)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.1854` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1854 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `1.5314` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5314 (IC base=+0.088)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.143 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.006 (IC base=-0.077)

- **PATRÓN** `ibs_20min` < `0.1154` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1154 (IC base=-0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.966` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.966 (IC base=-0.077)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `11.0` → IC=-0.429 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=125)

- **FILTRO** `dist_vwap_pct` > `0.2226` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2226
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=148)

- **FILTRO** `volumen_regimen` < `0.7296` → IC=-0.339 (n=54)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=111)

- **FILTRO** `volumen_pendiente_norm` > `0.1823` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1823
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=70)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.346 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=99)

- **FILTRO** `dist_vwap_pct` > `0.3412` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3412
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=120)

- **FILTRO** `sigma_ewma_delta_pct` > `8.432` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.432
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=120)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=47)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.210 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `volumen_regimen` < `0.892` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.892
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=38)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=42)

- **FILTRO** `sigma_ewma_delta_pct` > `3.354` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=38)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=41)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8218` → IC=-0.450 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8218
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **FILTRO** `dist_vwap_pct` > `0.0599` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0599
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=34)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.309 (n=19)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2345` → IC=-0.136 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=212)

- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=295)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.135 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0056 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.123 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.6522 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.4532` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.4532 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.2345` → IC=+0.121 (n=212)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2345 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `3837.0322` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3837.0322 (IC base=+0.034)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=83)

- **FILTRO** `ibs_20min` < `0.5548` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5548
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=75)

- **FILTRO** `volumen_regimen` < `0.7777` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7777
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=75)

- **PATRÓN** `ibs_20min` > `0.6466` → IC=+0.123 (n=67)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.6466 (IC base=-0.025)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1435 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `2.9499` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.9499 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.152 (n=110)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.095)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.8361` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8361
  - _Potencial_: sin este filtro IC_bueno=+0.209 (n=53)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=77)

- **FILTRO** `ibs_20min` > `0.3236` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3236
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=77)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.167 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0042 (IC base=+0.080)

- **PATRÓN** `drift_60min` |x|≤ `0.2791` → IC=+0.129 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2791 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.080)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8361 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.0869` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.0869 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.1989` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1989 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `1558.1749` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1558.1749 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.55` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=56)

- **FILTRO** `volumen_regimen` < `1.0339` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0339
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=36)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0047 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.177 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0058 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.167 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 17.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.7619` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7619 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.7619 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.2073` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2073 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.03 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `529.3167` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 529.3167 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.041)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.158 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 16.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.133 (n=518)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.5 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2845.305` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2845.305 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2326.7299` → IC=+0.123 (n=592)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2326.7299 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.158 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 16.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.133 (n=518)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` > 0.5 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2845.305` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2845.305 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2326.7299` → IC=+0.123 (n=592)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2326.7299 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=73)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=126)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.185 (n=106)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=36)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=195)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=181)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=33)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1384)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=49)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=81)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `33209.41` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `liq_usd_total` < 33209.41
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `569.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 569.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_usd_total` > `61042.02` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `liq_usd_total` > 61042.02 (IC base=+0.029)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.495 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `15568.3857` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 15568.3857 (IC base=+0.029)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=622)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=420)

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
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=77)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=429)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=273)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=273)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=240)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=162)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=162)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=99)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=62)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=78)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=166)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=66)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=99)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6785)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.179 (n=2820)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=8639)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.173 (n=2909)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=8995)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.213 (n=483)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1466)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.170 (n=495)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1628)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.205 (n=480)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=1512)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.221 (n=496)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1607)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.169 (n=514)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1589)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.198 (n=465)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1458)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.193 (n=512)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1592)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=2484)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=2576)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=2582)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=314)

- **FILTRO** `ibs_20min` > `0.1427` → IC=-0.132 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1427
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=263)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=198)

- **FILTRO** `ibs_20min` < `0.1457` → IC=-0.227 (n=86)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1457
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=176)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.185 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=176)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=178)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=654)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.038)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=8231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=18421)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.281 (n=6335)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=20317)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.242 (n=6620)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=20032)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.160 (n=9048)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=17604)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.230 (n=7871)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=25627)

- **FILTRO** `ibs_7min` > `0.2963` → IC=-0.177 (n=8357)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=25141)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1027)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3286)

- **FILTRO** `ibs_7min` < `0.7077` → IC=-0.259 (n=1423)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7077
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2890)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.199 (n=980)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3333)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.150 (n=3910)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1908)

- **FILTRO** `drift_7min_pct` |x|> `0.1111` → IC=-0.124 (n=1975)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1111
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3843)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.204 (n=1452)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4366)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1088)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3560)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.259 (n=1105)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3543)

- **FILTRO** `ibs_7min` < `0.7547` → IC=-0.187 (n=1162)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7547
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3486)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.177 (n=1161)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3487)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.258 (n=1134)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3593)

- **FILTRO** `ibs_7min` > `0.2549` → IC=-0.170 (n=1181)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2549
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3546)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.183 (n=1176)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3551)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.170 (n=1154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=2880)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.315 (n=974)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3060)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.266 (n=1001)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3033)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.220 (n=926)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=3108)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.236 (n=1439)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=4695)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.156 (n=2081)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=4053)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.253 (n=1081)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3318)

- **FILTRO** `ibs_7min` < `0.7425` → IC=-0.189 (n=1098)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7425
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3301)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.185 (n=1085)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3314)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1115)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3385)

- **FILTRO** `ibs_7min` > `0.274` → IC=-0.174 (n=1124)

  - _Acción_: SKIP cuando `ibs_7min` > 0.274
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3376)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.181 (n=1099)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3401)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.259 (n=1160)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3600)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.231 (n=1173)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3587)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.173 (n=1557)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4784)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.279 (n=1118)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3380)

- **FILTRO** `ibs_7min` < `0.7196` → IC=-0.233 (n=1124)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7196
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=3374)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1090)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3408)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.205 (n=1418)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=4560)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=988)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=488)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=313)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=535)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.137 (n=659)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 453.526 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.128 (n=299)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3728.089 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.130 (n=549)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 60.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.160 (n=51)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `417.524` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 417.524 (IC base=+0.134)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.188 (n=91)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 70.0 (IC base=+0.104)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.399` → IC=+0.198 (n=117)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio` |x|> 0.399 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.217 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `7671.127` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 7671.127 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 37.0 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.167 (n=112)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.149 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 13.0 (IC base=+0.119)

- **PATRÓN** `total_vol_5m` < `356326.0` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 356326.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.240 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.119)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.322 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=151)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.179 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0039 (IC base=-0.120)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.357 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=48)

- **FILTRO** `T_h` > `54.3209` → IC=-0.357 (n=47)

  - _Acción_: SKIP cuando `T_h` > 54.3209
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=48)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.119)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.234 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **FILTRO** `T_h` > `71.1632` → IC=-0.200 (n=231)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=79)

- **FILTRO** `pct_vs_K` |x|> `3.8394` → IC=-0.429 (n=82)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8394
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=169)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.194 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **FILTRO** `T_h` > `63.9918` → IC=-0.209 (n=84)

  - _Acción_: SKIP cuando `T_h` > 63.9918
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=68)

- **FILTRO** `pct_vs_K` |x|> `2.259` → IC=-0.433 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.259
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0054` → IC=-0.295 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=43)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.283 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=65)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=65)

- **FILTRO** `T_h` > `61.3303` → IC=-0.318 (n=64)

  - _Acción_: SKIP cuando `T_h` > 61.3303
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `135.927` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `T_h` > 135.927
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=53)

- **FILTRO** `pct_vs_K` |x|> `5.05` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.05
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=53)

- **FILTRO** `sigma_h` < `0.0129` → IC=-0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `T_h` > `84.9421` → IC=-0.361 (n=34)

  - _Acción_: SKIP cuando `T_h` > 84.9421
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.15` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.15 (IC base=+0.371)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.468 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.371)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.468 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.371)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.371)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.371)

- **PATRÓN** `edge` > `0.1035` → IC=+0.444 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1035 (IC base=+0.401)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.438 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.401)

- **PATRÓN** `T_h` > `1.0962` → IC=+0.417 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.0962 (IC base=+0.401)

- **PATRÓN** `dist_50` > `0.4085` → IC=+0.475 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4085 (IC base=+0.401)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.429 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.401)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.477)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.460 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.477)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.467 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.467)

- **PATRÓN** `T_h` > `0.958` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.958 (IC base=+0.467)

- **PATRÓN** `dist_50` > `0.4688` → IC=+0.481 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4688 (IC base=+0.467)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.456 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.467)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=140)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=244)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.016)

- **PATRÓN** `streak_estiramiento` < `0.5606` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `streak_estiramiento` < 0.5606 (IC base=+0.032)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=26)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_racha` < 991078.0 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=86)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=618)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=624)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=324)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `streak_len` < 4.0 (IC base=+0.013)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=491)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=988)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=587)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=609)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2466)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1271)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1279)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.192 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0041 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.221 (n=535)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0524` → IC=+0.189 (n=394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0524 (IC base=+0.181)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.182 (n=1181)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.236 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.188 (n=835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 11.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.181)

- **PATRÓN** `ibs_15` > `0.62` → IC=+0.256 (n=1180)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.62 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.4223` → IC=+0.174 (n=277)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.4223 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.5472` → IC=+0.175 (n=1221)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.5472 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.261 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `4692.4102` → IC=+0.183 (n=535)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4692.4102 (IC base=+0.181)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=399)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.214 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.197 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.005 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.278 (n=97)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.196)

- **PATRÓN** `drift_15min` |x|≤ `0.3775` → IC=+0.217 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3775 (IC base=+0.196)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1506` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1506 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.215 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.196)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.253 (n=290)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.3695` → IC=+0.253 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3695 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.0989` → IC=+0.200 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0989 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.68` → IC=+0.247 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.68 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15571.5606` → IC=+0.247 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15571.5606 (IC base=+0.196)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.180 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.154 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0057 (IC base=+0.140)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.177 (n=94)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.140)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2698` → IC=+0.167 (n=187)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2698 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.148 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_15` > `0.6853` → IC=+0.260 (n=252)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6853 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.0983` → IC=+0.165 (n=201)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.0983 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.996` → IC=+0.215 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.996 (IC base=+0.140)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

- **FILTRO** `ibs_15` > `0.1909` → IC=-0.224 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1909
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.209 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.171 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.188 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3347` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3347 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.177 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.241 (n=160)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.5902` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.5902 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=129)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3008.8466` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3008.8466 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.143)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5659` → IC=-0.136 (n=119)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5659
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=625)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=+0.006)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0158` → IC=+0.252 (n=220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0158 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.209 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0441` → IC=+0.202 (n=330)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0441 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0986` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0986 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.241 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.280 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.55 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1142` → IC=+0.204 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1142 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.3044` → IC=+0.190 (n=317)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.3044 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.55` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.55 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.191 (n=364)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2846.2656` → IC=+0.277 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2846.2656 (IC base=+0.190)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.168 (n=377)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.84€ cuando `ibs_15` < 0.1143 (IC base=+0.043)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.374 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.343 (n=290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.351 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2192` → IC=+0.374 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2192 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.352 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.376 (n=329)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4098` → IC=+0.371 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4098 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.085` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.085 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `3397.72` → IC=+0.352 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3397.72 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1228` → IC=+0.343 (n=81)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1228 (IC base=+0.338)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.335 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.359 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.338)

- **PATRÓN** `drift_60min` |x|≤ `0.1497` → IC=+0.348 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1497 (IC base=+0.338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.348 (n=123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.338)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.338)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.371 (n=184)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.338)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.344 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `9641.0136` → IC=+0.364 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9641.0136 (IC base=+0.338)

- **PATRÓN** `ballena_activa_n` < `463.0` → IC=+0.403 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 463.0 (IC base=+0.338)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.369 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.331 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.337 (n=145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.349 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.384 (n=145)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.1061` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1061 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.144` → IC=+0.355 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.144 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `3525.4286` → IC=+0.359 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3525.4286 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.331)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.207 (n=557)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1674)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.178 (n=715)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1516)

- **FILTRO** `libro_liquidez` < `3803.3718` → IC=-0.122 (n=1472)

  - _Acción_: SKIP cuando `libro_liquidez` < 3803.3718
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=759)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.256 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.058)

- **PATRÓN** `ibs_15` > `0.6189` → IC=+0.259 (n=553)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6189 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.186 (n=342)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1081 (IC base=-0.058)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1164` → IC=+0.236 (n=839)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1164 (IC base=-0.043)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1825` → IC=+0.240 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1825 (IC base=-0.043)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.279 (n=1258)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` > `0.6428` → IC=+0.259 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6428 (IC base=-0.043)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.208 (n=337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=1013)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.229 (n=445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=905)

- **FILTRO** `ibs_15` > `0.383` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.383
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=16)

- **FILTRO** `sigma_ewma_delta_pct` > `19.975` → IC=-0.241 (n=241)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.975
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1109)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.178 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0027 (IC base=+0.072)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.072)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.338 (n=115)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.0982` → IC=+0.261 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0982 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.3306` → IC=+0.265 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3306 (IC base=+0.072)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6537` → IC=-0.222 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6537
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=270)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=341)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.142 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0066 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.169 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.211 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.139)

- **PATRÓN** `drift_15min` |x|≤ `0.4631` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4631 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.240 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.257 (n=270)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.177 (n=193)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.902` → IC=+0.149 (n=289)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 18.902 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=341)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.246 (n=526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.3595` → IC=+0.231 (n=463)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3595 (IC base=+0.228)

- **PATRÓN** `drift_15min` |x|≤ `0.774` → IC=+0.238 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.774 (IC base=+0.228)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2` → IC=+0.258 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.240 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.228)

- **PATRÓN** `ibs_15` < `0.2757` → IC=+0.287 (n=463)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2757 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.3701` → IC=+0.258 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3701 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.004` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.004 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.153` → IC=+0.232 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.153 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `3576.5439` → IC=+0.229 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3576.5439 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.229 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.228)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.8773` → IC=-0.250 (n=134)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8773
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=403)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=204)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=333)

- **FILTRO** `sigma_ewma_delta_pct` > `18.154` → IC=-0.132 (n=278)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.154
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2227)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.155)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.155)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1181` → IC=+0.222 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1181 (IC base=-0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1964` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1964 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.251 (n=251)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.1738` → IC=+0.210 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1738 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.265 (n=334)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=336)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=496)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1292` → IC=+0.267 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1292 (IC base=-0.045)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1097` → IC=+0.343 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1097 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3457` → IC=+0.308 (n=363)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3457 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `1.0689` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0689 (IC base=-0.045)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.138 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0064 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.4393` → IC=+0.167 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4393 (IC base=+0.105)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.105)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.138 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0064 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.4393` → IC=+0.167 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4393 (IC base=+0.105)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.105)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.290 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.290 (n=250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0563` → IC=+0.317 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0563 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1415` → IC=+0.289 (n=368)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1415 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.218` → IC=+0.322 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.218 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.305 (n=572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8365` → IC=+0.325 (n=552)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8365 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.263` → IC=+0.325 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.263 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.325 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.289 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `12779.9707` → IC=+0.298 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12779.9707 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.288 (n=206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.289 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.319 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.277)

- **PATRÓN** `drift_15min` |x|≤ `0.3882` → IC=+0.281 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3882 (IC base=+0.277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2454` → IC=+0.281 (n=103)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2454 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3684` → IC=+0.294 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3684 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.333 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8242` → IC=+0.297 (n=309)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8242 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.337 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `15796.8084` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15796.8084 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.305 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.304 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.309 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.314 (n=111)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.340 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.342 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.341 (n=243)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` < `0.4406` → IC=+0.300 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4406 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.324 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.332` → IC=+0.298 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.332 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.298 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.085` → IC=-0.273 (n=64)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.085
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=196)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.244 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=172)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.161 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=322)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2171` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2171
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=66)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1851` → IC=-0.132 (n=74)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1851
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=75)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2312` → IC=-0.204 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2312
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2179` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2179
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2099` → IC=-0.389 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2099
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `73.926` → IC=+0.140 (n=231)

  - _Acción_: Kelly boost +0.70€ cuando `T_h` > 73.926 (IC base=+0.138)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.319 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.138)

- **PATRÓN** `T_h` > `145.8408` → IC=+0.407 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8408 (IC base=+0.350)

- **PATRÓN** `ratio` > `1.01` → IC=+0.386 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.350)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.522` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `T_h` > 144.522 (IC base=+0.096)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.096)

- **PATRÓN** `T_h` > `87.9969` → IC=+0.314 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9969 (IC base=+0.307)

- **PATRÓN** `ratio` > `1.0413` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0413 (IC base=+0.307)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9882` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9882 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.193)

- **PATRÓN** `T_h` > `93.2998` → IC=+0.350 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 93.2998 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.382 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.331)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.405)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.62 sube el IC de +0.181 a +0.256 en UPDOWN_GBM#15min (n=1180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.196 a +0.253 en UPDOWN_GBM#BTC#15min (n=290). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6853 sube el IC de +0.140 a +0.260 en UPDOWN_GBM#ETH#15min (n=252). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.143 a +0.241 en UPDOWN_GBM#SOL#15min (n=160). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.190 a +0.280 en UPDOWN_GBM#XRP#15min (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1143 sube el IC de +0.043 a +0.168 en UPDOWN_GBM#XRP#15min (n=377). Ya aplicado como kelly_boost=+0.84€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6189 sube el IC de -0.058 a +0.259 en UPDOWN_GBM_15M_TARDIO (n=553). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3605 sube el IC de -0.043 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1258). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.072 a +0.338 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=115). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.139 a +0.257 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=270). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2757 sube el IC de +0.228 a +0.287 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=463). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.155 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.044 a +0.251 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=251). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3457 sube el IC de -0.045 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=363). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8365 sube el IC de +0.287 a +0.325 en UPDOWN_GBM_IBS_ALTO (n=552). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8242 sube el IC de +0.277 a +0.297 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=309). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.297 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=243). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.336 a +0.376 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=329). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.338 a +0.371 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=184). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.331 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=145). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1173 | +0.085 | +147.09€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1173 | +0.085 | +147.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 848 | +0.091 | +117.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 848 | +0.091 | +117.96€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 242 | +0.045 | +4.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 242 | +0.045 | +4.70€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 57 | +0.178 | +25.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 57 | +0.178 | +25.94€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 21602 | -0.096 | -3131.93€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1280 | -0.050 | -192.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 20322 | -0.099 | -2939.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3334 | -0.100 | -570.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3334 | -0.100 | -570.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1280 | -0.050 | -192.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1280 | -0.050 | -192.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6197 | -0.042 | -606.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6197 | -0.042 | -606.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5724 | -0.097 | -476.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5724 | -0.097 | -476.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4693 | -0.174 | -1125.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4693 | -0.174 | -1125.42€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 13590 | -0.038 | +4181.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3616 | -0.005 | +1830.76€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 9974 | -0.050 | +2350.46€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 13590 | -0.038 | +4181.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3616 | -0.005 | +1830.76€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 9974 | -0.050 | +2350.46€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1203 | -0.097 | -157.67€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 104 | -0.038 | -9.03€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1099 | -0.102 | -148.64€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 684 | -0.082 | -78.07€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 80 | -0.024 | -3.81€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 604 | -0.089 | -74.25€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 340 | -0.137 | -66.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 316 | -0.141 | -61.22€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 118 | -0.042 | -13.02€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 118 | -0.042 | -13.02€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 78557 | +0.113 | -4023.99€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 12182 | +0.183 | -368.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 303 | -0.120 | -46.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 60729 | +0.100 | -3448.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5343 | +0.112 | -161.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 10115 | +0.097 | -927.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 41 | -0.151 | -1.09€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 10059 | +0.098 | -914.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 15893 | +0.132 | -317.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3761 | +0.202 | -114.06€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 10062 | +0.110 | -180.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2028 | +0.112 | -0.19€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 10153 | +0.088 | -987.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 47 | -0.051 | -1.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 10091 | +0.090 | -974.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 16802 | +0.124 | -312.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4705 | +0.173 | -68.98€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 10162 | +0.107 | -180.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1923 | +0.097 | -54.29€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 15463 | +0.115 | -899.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3587 | +0.186 | -193.04€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 206 | -0.082 | +7.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 10278 | +0.092 | -607.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1392 | +0.131 | -106.66€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 10131 | +0.103 | -580.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 41 | -0.012 | +10.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 10077 | +0.104 | -590.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 12418 | +0.190 | -843.35€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 12418 | +0.190 | -843.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3036 | +0.167 | -330.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3036 | +0.167 | -330.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 761 | +0.188 | +4.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 761 | +0.188 | +4.11€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2967 | +0.180 | -261.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2967 | +0.180 | -261.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2662 | +0.237 | -83.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2662 | +0.237 | -83.49€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2913 | +0.191 | -185.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2913 | +0.191 | -185.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 577 | +0.434 | -9.94€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 577 | +0.434 | -9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 220 | +0.437 | -2.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 220 | +0.437 | -2.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 218 | +0.441 | +0.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 218 | +0.441 | +0.45€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 131 | +0.410 | -7.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 131 | +0.410 | -7.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 42483 | +0.196 | -3473.59€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 42483 | +0.196 | -3473.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7396 | +0.172 | -917.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7396 | +0.172 | -917.58€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6750 | +0.224 | -242.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6750 | +0.224 | -242.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7352 | +0.171 | -910.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7352 | +0.171 | -910.37€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6847 | +0.217 | -287.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6847 | +0.217 | -287.62€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7010 | +0.204 | -458.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7010 | +0.204 | -458.44€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7128 | +0.191 | -657.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7128 | +0.191 | -657.45€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 15934 | +0.124 | +288.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 15934 | +0.124 | +288.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7902 | +0.128 | +190.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7902 | +0.128 | +190.36€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 8032 | +0.120 | +98.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 8032 | +0.120 | +98.29€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1289 | +0.286 | -28.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1289 | +0.286 | -28.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 573 | +0.267 | -30.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 573 | +0.267 | -30.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 615 | +0.294 | +1.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 615 | +0.294 | +1.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 101 | +0.335 | -0.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 101 | +0.335 | -0.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 565 | +0.433 | -5.49€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 565 | +0.433 | -5.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 265 | +0.433 | -2.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 265 | +0.433 | -2.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 261 | +0.435 | -2.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 261 | +0.435 | -2.21€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 910 | +0.072 | -40.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 321 | +0.057 | -27.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 589 | +0.080 | -13.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 711 | +0.081 | -16.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 122 | +0.081 | -3.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 589 | +0.080 | -13.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 144 | +0.007 | -28.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 144 | +0.007 | -28.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 28499 | +0.099 | -818.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2392 | +0.093 | +28.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 26107 | +0.100 | -847.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 16180 | +0.103 | -231.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2392 | +0.093 | +28.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 13788 | +0.105 | -260.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 5076 | +0.115 | +40.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 5076 | +0.115 | +40.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 7243 | +0.079 | -627.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 7243 | +0.079 | -627.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 739 | +0.239 | -93.11€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 739 | +0.239 | -93.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 739 | +0.239 | -93.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 739 | +0.239 | -93.11€ | 1 | 4 |
| ✅ GBM_LATE_15M | 20899 | +0.076 | +9412.72€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 20899 | +0.076 | +9412.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3434 | +0.193 | +2485.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3434 | +0.193 | +2485.80€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 3094 | +0.173 | +2069.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3094 | +0.173 | +2069.23€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 3584 | +0.196 | +2636.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3584 | +0.196 | +2636.85€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 3122 | +0.007 | +496.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3122 | +0.007 | +496.42€ | 1 | 13 |
| ✅ GBM_LATE_15M#SOL | 3053 | -0.039 | +636.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3053 | -0.039 | +636.30€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 4612 | -0.048 | +1088.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4612 | -0.048 | +1088.12€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 21991 | +0.079 | +10918.75€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 21991 | +0.079 | +10918.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4079 | +0.013 | +1987.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4079 | +0.013 | +1987.83€ | 1 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4637 | +0.007 | +879.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4637 | +0.007 | +879.49€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3115 | +0.258 | +3084.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3115 | +0.258 | +3084.71€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3492 | -0.010 | +486.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3492 | -0.010 | +486.58€ | 2 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3613 | +0.014 | +1265.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3613 | +0.014 | +1265.81€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3055 | +0.272 | +3214.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3055 | +0.272 | +3214.33€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 16960 | +0.168 | +12377.66€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 16960 | +0.168 | +12377.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2520 | +0.206 | +1989.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2520 | +0.206 | +1989.30€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2693 | +0.152 | +1922.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2693 | +0.152 | +1922.97€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2626 | +0.205 | +2057.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2626 | +0.205 | +2057.97€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2815 | +0.139 | +1897.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2815 | +0.139 | +1897.55€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3199 | +0.110 | +2064.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3199 | +0.110 | +2064.55€ | 1 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3107 | +0.203 | +2445.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3107 | +0.203 | +2445.32€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4329 | +0.126 | +1776.12€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4329 | +0.126 | +1776.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 175 | +0.116 | +70.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 175 | +0.116 | +70.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1193 | +0.120 | +502.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1193 | +0.120 | +502.70€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1172 | +0.151 | +541.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1172 | +0.151 | +541.19€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 918 | +0.088 | +260.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 918 | +0.088 | +260.39€ | 1 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 20963 | +0.172 | +15153.54€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 20963 | +0.172 | +15153.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3279 | +0.218 | +2732.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3279 | +0.218 | +2732.80€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3289 | +0.151 | +2159.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3289 | +0.151 | +2159.57€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3401 | +0.222 | +2884.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3401 | +0.222 | +2884.43€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3367 | +0.137 | +2176.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3367 | +0.137 | +2176.05€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3679 | +0.104 | +2136.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3679 | +0.104 | +2136.81€ | 1 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3948 | +0.202 | +3063.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3948 | +0.202 | +3063.89€ | 0 | 25 |
| ✅ GBM_LATE_5M | 6017 | +0.140 | +3248.69€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 6017 | +0.140 | +3248.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1590 | +0.138 | +962.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1590 | +0.138 | +962.02€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1846 | +0.147 | +1006.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1846 | +0.147 | +1006.83€ | 0 | 31 |
| ✅ GBM_LATE_5M#SOL | 325 | +0.023 | +34.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 325 | +0.023 | +34.18€ | 2 | 4 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1333 | +0.066 | +610.07€ | 2 | 15 |
| ✅ GBM_LATE_60M#60min | 1333 | +0.066 | +610.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 475 | +0.085 | +207.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 475 | +0.085 | +207.16€ | 1 | 15 |
| ✅ GBM_LATE_60M#ETH | 445 | +0.070 | +237.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 445 | +0.070 | +237.35€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 413 | +0.040 | +165.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 413 | +0.040 | +165.56€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 314 | -0.260 | -20.91€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 314 | -0.260 | -20.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 118 | -0.217 | -7.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 118 | -0.217 | -7.46€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 106 | -0.278 | -9.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 106 | -0.278 | -9.71€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 90 | -0.283 | -3.74€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 90 | -0.283 | -3.74€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 618 | +0.057 | +122.70€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 618 | +0.057 | +122.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 245 | +0.047 | +41.28€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 245 | +0.047 | +41.28€ | 3 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 181 | +0.035 | +3.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 181 | +0.035 | +3.29€ | 3 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 192 | +0.088 | +78.14€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 192 | +0.088 | +78.14€ | 2 | 15 |
| ✅ LATE_WINDOW_5MIN | 71 | +0.253 | +49.35€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 71 | +0.253 | +49.35€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 71 | +0.253 | +49.35€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 71 | +0.253 | +49.35€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1502 | +0.107 | +449.00€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1502 | +0.107 | +449.00€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1502 | +0.107 | +449.00€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1502 | +0.107 | +449.00€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M | 358 | -0.081 | -33.29€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 358 | -0.081 | -33.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 90 | -0.065 | -5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 90 | -0.065 | -5.65€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 120 | -0.016 | -3.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 120 | -0.016 | -3.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1582 | -0.003 | -4.72€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1582 | -0.003 | -4.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 170 | -0.012 | +5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 170 | -0.012 | +5.32€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 669 | +0.020 | +15.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 669 | +0.020 | +15.41€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 460 | -0.006 | -8.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 460 | -0.006 | -8.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 106 | -0.056 | -6.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 106 | -0.056 | -6.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 925 | -0.048 | -28.59€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 925 | -0.048 | -28.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 270 | -0.051 | -14.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 270 | -0.051 | -14.40€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 297 | -0.035 | -4.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 297 | -0.035 | -4.26€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 358 | -0.056 | -9.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 358 | -0.056 | -9.94€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 13649 | -0.011 | -190.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 13649 | -0.011 | -190.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2570 | -0.023 | -52.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2570 | -0.023 | -52.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2882 | -0.014 | -20.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2882 | -0.014 | -20.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3377 | -0.018 | -65.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3377 | -0.018 | -65.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 23363 | -0.010 | +1026.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 23363 | -0.010 | +1026.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4072 | +0.011 | +524.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4072 | +0.011 | +524.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3740 | -0.025 | -21.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3740 | -0.025 | -21.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4095 | +0.006 | +316.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4095 | +0.006 | +316.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3517 | -0.047 | -100.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3517 | -0.047 | -100.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3912 | -0.013 | +158.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3912 | -0.013 | +158.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4027 | +0.001 | +149.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4027 | +0.001 | +149.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5161 | -0.046 | -134.65€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5161 | -0.046 | -134.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1162 | -0.060 | -31.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1162 | -0.060 | -31.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 490 | -0.132 | -28.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 490 | -0.132 | -28.62€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1419 | -0.061 | -27.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1419 | -0.061 | -27.44€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3339 | +0.004 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3339 | +0.004 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 186 | +0.011 | -0.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 186 | +0.011 | -0.87€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1314 | +0.007 | +7.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1314 | +0.007 | +7.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 60150 | -0.073 | +1330.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 60150 | -0.073 | +1330.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 10131 | -0.080 | +622.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 10131 | -0.080 | +622.60€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 9375 | -0.090 | -378.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 9375 | -0.090 | -378.11€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 10168 | -0.070 | +541.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 10168 | -0.070 | +541.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8899 | -0.093 | -237.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8899 | -0.093 | -237.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 11101 | -0.049 | +320.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 11101 | -0.049 | +320.87€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 10476 | -0.063 | +460.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 10476 | -0.063 | +460.57€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6785 | -0.022 | -99.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6785 | -0.022 | -99.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1537 | -0.021 | -2.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1537 | -0.021 | -2.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1508 | -0.016 | -4.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1508 | -0.016 | -4.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1005 | -0.039 | -17.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1005 | -0.039 | -17.28€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1013 | +0.113 | +354.95€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 877 | +0.121 | +342.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 203 | +0.134 | +97.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 203 | +0.134 | +97.97€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 173 | +0.094 | +40.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 173 | +0.094 | +40.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 180 | +0.104 | +63.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 180 | +0.104 | +63.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 155 | +0.150 | +81.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 155 | +0.150 | +81.31€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 166 | +0.119 | +58.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 166 | +0.119 | +58.99€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 479 | -0.076 | -5.11€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 211 | -0.120 | -32.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 169 | -0.155 | -35.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 171 | -0.067 | +8.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 129 | -0.072 | +1.92€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 97 | +0.005 | +18.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 77 | -0.006 | +12.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 375 | -0.097 | -20.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 561 | -0.221 | -48.01€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 233 | -0.202 | -34.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 201 | -0.195 | -32.31€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 198 | -0.240 | -23.51€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 171 | -0.251 | -27.60€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 130 | -0.220 | +10.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 116 | -0.220 | +7.04€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 488 | -0.222 | -52.87€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 208 | +0.395 | +153.74€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 50 | +0.365 | +41.72€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 50 | +0.365 | +41.72€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 130 | +0.477 | +116.78€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 130 | +0.477 | +116.78€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#sniper | 208 | +0.395 | +153.74€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 422 | +0.026 | +8.99€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 422 | +0.026 | +8.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 193 | +0.023 | +0.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 193 | +0.023 | +0.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 47 | -0.031 | -4.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 47 | -0.031 | -4.66€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 156 | +0.032 | +8.49€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 156 | +0.032 | +8.49€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 2523 | -0.027 | -117.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2523 | -0.027 | -117.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 564 | -0.023 | -23.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 564 | -0.023 | -23.35€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 153 | -0.042 | -13.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 153 | -0.042 | -13.91€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1002 | -0.034 | -52.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1002 | -0.034 | -52.89€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 61 | -0.040 | -3.88€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 61 | -0.040 | -3.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 24 | +0.038 | +0.06€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 24 | +0.038 | +0.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6774 | +0.024 | +107.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6774 | +0.024 | +107.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2119 | +0.021 | +20.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2119 | +0.021 | +20.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1424 | +0.029 | +35.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1424 | +0.029 | +35.60€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1993 | +0.017 | +12.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1993 | +0.017 | +12.87€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1238 | +0.034 | +38.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1238 | +0.034 | +38.48€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6261 | +0.012 | -34.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6261 | +0.012 | -34.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2485 | +0.019 | -0.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2485 | +0.019 | -0.39€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2473 | +0.015 | -7.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2473 | +0.015 | -7.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1303 | -0.006 | -27.32€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1303 | -0.006 | -27.32€ | 2 | 0 |
| ✅ UPDOWN_GBM | 27627 | +0.030 | +1576.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 7452 | +0.059 | +1217.39€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1036 | +0.005 | +8.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 17345 | +0.023 | +344.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1684 | +0.003 | +4.96€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2457 | +0.072 | +253.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 329 | +0.138 | +117.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2109 | +0.062 | +136.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 5055 | +0.032 | +327.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 910 | +0.079 | +203.59€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 293 | +0.022 | +7.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3064 | +0.028 | +108.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 746 | +0.000 | +7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 42 | -0.114 | +0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3264 | +0.035 | +135.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 286 | +0.129 | +92.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2962 | +0.026 | +43.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 5781 | +0.017 | +229.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2021 | +0.047 | +224.00€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 280 | +0.007 | +7.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2849 | +0.003 | -1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 595 | +0.001 | -3.53€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 36 | -0.158 | +3.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6959 | +0.016 | +165.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1970 | +0.021 | +107.14€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 274 | -0.007 | -2.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4342 | +0.018 | +61.29€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 343 | +0.013 | +0.81€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 30 | -0.156 | -1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4109 | +0.041 | +467.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1936 | +0.077 | +472.71€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 154 | -0.006 | -2.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2019 | +0.009 | -2.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 108 | -0.145 | +3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 438 | +0.336 | +126.24€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 438 | +0.336 | +126.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 245 | +0.338 | +66.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 245 | +0.338 | +66.86€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 193 | +0.331 | +59.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 193 | +0.331 | +59.38€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 9615 | -0.046 | +1996.77€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 9615 | -0.046 | +1996.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 481 | -0.053 | +334.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 481 | -0.053 | +334.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1825 | -0.127 | +25.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1825 | -0.127 | +25.75€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 177 | +0.131 | +80.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 177 | +0.131 | +80.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1058 | +0.198 | +606.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1058 | +0.198 | +606.33€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3042 | -0.064 | +449.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3042 | -0.064 | +449.43€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3032 | -0.075 | +500.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3032 | -0.075 | +500.03€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 108 | +0.073 | +17.16€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 108 | +0.073 | +17.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 108 | +0.073 | +17.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 108 | +0.073 | +17.16€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 735 | +0.287 | +589.30€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 735 | +0.287 | +589.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 411 | +0.277 | +309.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 411 | +0.277 | +309.42€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 324 | +0.297 | +279.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 324 | +0.297 | +279.88€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 689 | -0.109 | -80.81€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 689 | -0.109 | -80.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 187 | -0.071 | -12.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 187 | -0.071 | -12.61€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1998 | +0.305 | +1042.24€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 668 | +0.251 | +109.91€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 723 | +0.294 | +310.36€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 607 | +0.375 | +621.96€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.019 n=387 — no justifica filtro, seguir monitorizando
  - _Datos_: n=387 IC=+0.019 PNL=+19.59€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 468 celda(s) pasan gate riguroso completo de 2070 evaluadas (n>=40) y 3049 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.021 < 0.08 — monitorear
  - _Datos_: n=1968 IC=+0.021 PNL=+108.16€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=723/15 IC=+0.294 PNL=+310.36€ | BTC: n=668/15 IC=+0.251 PNL=+109.91€ | SOL: n=607/15 IC=+0.375 PNL=+621.96€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: 40
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Solo 0 ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40.

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: 20
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: Solo 0 ops GBM con hora_utc en features. Esperar n≥20 para patrones.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.103 n=202/60 | contraria IC=+0.151 n=190 | gap=-0.048 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=251, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=594/40 IC=+0.000 PNL=-4.04€ | BTC#60min: n=745/40 IC=-0.001 PNL=+7.13€ | SOL#60min: n=343/40 IC=+0.013 PNL=+0.81€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=275898 | tras_1loss IC=+0.073 n=215417 | tras_2loss IC=+0.041 n=92006/40 | gap=+0.012 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.000 n=0 | contrario_BTC IC=+0.000 n=0/40 | gap=+0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=221 PNL=+148.90€
  - _Datos_: n=221 IC=+0.191 PNL=+148.90€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.08 con n=288 PNL=+191.68€
  - _Datos_: n=288 IC=+0.200 PNL=+191.68€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=33 PNL=+24.82€
  - _Datos_: n=33 IC=+0.243 PNL=+24.82€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.344 > 0.1 con n=1667 PNL=+1030.23€
  - _Datos_: n=1667 IC=+0.344 PNL=+1030.23€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=215 IC=+0.076 PNL=+28.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=215 IC=+0.076 PNL=+28.90€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=45 IC=+0.202 PNL=+32.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=45 IC=+0.202 PNL=+32.49€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=1229 IC=+0.006 PNL=-3.15€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1229 IC=+0.006 PNL=-3.15€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=453 IC=-0.008 PNL=+7.06€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=453 IC=-0.008 PNL=+7.06€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=387 IC=+0.019 PNL=+19.59€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=387 IC=+0.019 PNL=+19.59€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.1 con n=1570 PNL=+934.59€
  - _Datos_: n=1570 IC=+0.181 PNL=+934.59€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=907 IC=+0.080 PNL=+201.32€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=907 IC=+0.080 PNL=+201.32€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**⏳ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: 40
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=410 IC=+0.019 PNL=+34.16€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=410 IC=+0.019 PNL=+34.16€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=32 IC=+0.000 PNL=-0.67€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=32 IC=+0.000 PNL=-0.67€

**⏳ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: 40
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.253 n=71) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=71 IC=+0.253 PNL=+49.35€

**⏳ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: 40
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: 200
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: 100
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: 40
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.02 con n=577 PNL=+238.02€
  - _Datos_: n=577 IC=+0.130 PNL=+238.02€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=140 IC=-0.056 PNL=+31.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=140 IC=-0.056 PNL=+31.39€

**⏳ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=9227 IC=+0.051 PNL=+1077.30€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=9227 IC=+0.051 PNL=+1077.30€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.167 < -0.1 con n=172 PNL=+12.08€
  - _Datos_: n=172 IC=-0.167 PNL=+12.08€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1494 IC=+0.044 PNL=+161.64€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1494 IC=+0.044 PNL=+161.64€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=59 IC=-0.107 PNL=+6.34€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=59 IC=-0.107 PNL=+6.34€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.1 con n=293 PNL=+94.75€
  - _Datos_: n=293 IC=+0.141 PNL=+94.75€

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
  - _Estado_: n=14408 IC=-0.142 PNL=+730.36€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=14408 IC=-0.142 PNL=+730.36€

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
  - _Estado_: n=1596 IC=+0.136 PNL=+835.04€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1596 IC=+0.136 PNL=+835.04€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2849 IC=+0.016 PNL=+74.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2849 IC=+0.016 PNL=+74.66€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.081 > 0.08 con n=1670 PNL=+845.35€
  - _Datos_: n=1670 IC=+0.081 PNL=+845.35€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.242 < -0.1 con n=1444 PNL=-200.60€
  - _Datos_: n=1444 IC=-0.242 PNL=-200.60€

**⏳ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: 100
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: 40
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: 40
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 31/40 ops en el filtro definido (IC actual=-0.015 PNL=+4.04€)
  - _Datos_: n=31 IC=-0.015 PNL=+4.04€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=788) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=788 IC=+0.099 PNL=+206.98€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=397) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=397 IC=+0.412 PNL=+556.95€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=7392 IC=+0.172 PNL=-917.38€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=7392 IC=+0.172 PNL=-917.38€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.219 > 0.1 con n=112 PNL=+72.18€
  - _Datos_: n=112 IC=+0.219 PNL=+72.18€
