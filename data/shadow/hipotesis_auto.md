# Hipótesis automáticas — 2026-09-01 00:30 UTC
_Generado por shadow_postmortem.py sobre 231796 resoluciones (PNL=+18735.06€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `ballena_activa_n` > `121.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 121.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.256 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.168)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.180 (n=267)

  - _Acción_: Kelly boost +0.90€ cuando `n_ballena_banda` > 19.0 (IC base=+0.168)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.232 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.168)

- **PATRÓN** `banda_hit_calibrado` > `0.8193` → IC=+0.283 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8193 (IC base=+0.168)

- **PATRÓN** `banda_z` > `11.967` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.967 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.189 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=305)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `3000.2192` → IC=+0.221 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.2192 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 223.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.139 (n=206)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=-0.008)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `n_ballena_banda` < `34.0` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `n_ballena_banda` < 34.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=110)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.253 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.203)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.218 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 18.0 (IC base=+0.203)

- **PATRÓN** `n_total_lado` > `55.0` → IC=+0.243 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 55.0 (IC base=+0.203)

- **PATRÓN** `banda_hit_calibrado` > `0.8289` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8289 (IC base=+0.203)

- **PATRÓN** `banda_z` > `12.051` → IC=+0.279 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 12.051 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.212 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `4013.8598` → IC=+0.243 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4013.8598 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.282 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 234.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.030)

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

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

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
- **FILTRO** `restante_s_al_confirmar` < `145.55` → IC=-0.296 (n=3235)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.55
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=9706)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `147.84` → IC=-0.254 (n=420)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.84
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1262)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `102.87` → IC=-0.416 (n=416)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 102.87
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1249)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `157.96` → IC=-0.155 (n=871)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.96
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2616)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `139.1` → IC=-0.320 (n=732)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.1
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=2198)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `152.6` → IC=-0.376 (n=758)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.6
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=1542)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.193 (n=6829)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.7 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=1824)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2386.174` → IC=+0.178 (n=1748)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2386.174 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.147 (n=4234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 18.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=5483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.257 (n=4288)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3450)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `1917.6073` → IC=+0.182 (n=2921)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1917.6073 (IC base=+0.140)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.217 (n=768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.384 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `12921.3988` → IC=+0.225 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12921.3988 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.197 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.266 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=1029)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `12455.0907` → IC=+0.211 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12455.0907 (IC base=+0.190)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.125 (n=612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 18.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.133 (n=598)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.555 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=267)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `4815.2665` → IC=+0.151 (n=213)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4815.2665 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.197 (n=199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.175 (n=300)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.41 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5709.2026` → IC=+0.168 (n=209)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5709.2026 (IC base=+0.131)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=79)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.134 (n=1238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 15.0 (IC base=+0.129)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.309 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.287 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.277 (n=589)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.414 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `1951.5637` → IC=+0.281 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1951.5637 (IC base=+0.276)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.160 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.266 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=414)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2075.7066` → IC=+0.160 (n=304)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2075.7066 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.438 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` < `0.215` → IC=+0.349 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.215 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1957.8301` → IC=+0.227 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.8301 (IC base=+0.211)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.213 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=164)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.219 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=284)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.110)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.293 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=99)

- **FILTRO** `py_entrada` > `0.835` → IC=-0.364 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=5526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=4640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.203 (n=2633)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3780.1464` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3780.1464 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `18.0` → IC=+0.173 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 18.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=1441)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.166)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=82)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=83)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.330)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.330)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.175 (n=1340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.184 (n=505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=1428)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.181 (n=955)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.72 (IC base=+0.170)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=1260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.234 (n=1060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.312 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.233)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=1146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.196 (n=689)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.7 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.450 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.445)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.450 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.458 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `3363.9486` → IC=+0.456 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3363.9486 (IC base=+0.445)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.440 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `10601.0016` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10601.0016 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.448 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.443 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `2258.1962` → IC=+0.444 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2258.1962 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.434 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `1927.8949` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.8949 (IC base=+0.443)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.202 (n=5481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.191 (n=11431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.211 (n=14701)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=2933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.141 (n=2073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 12.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.171 (n=2092)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.72 (IC base=+0.140)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=2587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.266 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.231)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.169 (n=1948)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 12.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.204 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.168)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=1339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=1242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.223 (n=899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.242 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.189 (n=927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.191 (n=1919)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.221 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.205 (n=2176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.132)

- **PATRÓN** `restante_min` < `3.97` → IC=+0.141 (n=2001)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 3.97 (IC base=+0.132)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.155 (n=2132)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.93 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=2899)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.132)

- **PATRÓN** `lag_apertura_s` < `4.23` → IC=+0.156 (n=1998)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 4.23 (IC base=+0.132)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.209 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.135)

- **PATRÓN** `restante_min` < `3.93` → IC=+0.146 (n=993)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 3.93 (IC base=+0.135)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.150 (n=1374)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.161 (n=1436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.135)

- **PATRÓN** `lag_apertura_s` < `6.99` → IC=+0.152 (n=1311)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 6.99 (IC base=+0.135)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.129)

- **PATRÓN** `restante_min` < `4.02` → IC=+0.137 (n=1001)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 4.02 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.161 (n=1109)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.94 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=3152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.136 (n=1463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `3.39` → IC=+0.168 (n=1003)

  - _Acción_: Kelly boost +0.84€ cuando `lag_apertura_s` < 3.39 (IC base=+0.129)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.315 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.380 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.295 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `5557.2873` → IC=+0.316 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5557.2873 (IC base=+0.276)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.337 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.314 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.305)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.376 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.305)

- **PATRÓN** `libro_liquidez` > `2002.3189` → IC=+0.333 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2002.3189 (IC base=+0.305)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.343 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.344)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.357 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.344)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.368 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.344)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.424 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.418)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.424 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.418)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.418)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.419 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.418)

- **PATRÓN** `libro_liquidez` > `2076.1143` → IC=+0.429 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.1143 (IC base=+0.418)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.423 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.414 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.425 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.412)

- **PATRÓN** `libro_liquidez` > `5497.3627` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5497.3627 (IC base=+0.412)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.434 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.423 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.424 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `2076.021` → IC=+0.455 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.021 (IC base=+0.425)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.293 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.427 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.294 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2102.6762` → IC=+0.304 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2102.6762 (IC base=+0.279)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.293 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.427 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.294 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2102.6762` → IC=+0.304 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2102.6762 (IC base=+0.279)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.3481` → IC=+0.122 (n=3026)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.3481 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.171` → IC=+0.222 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.171 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.4826` → IC=+0.219 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4826 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.396` → IC=+0.152 (n=1167)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.396 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0803` → IC=+0.249 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0803 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.163 (n=1675)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.0803` → IC=+0.163 (n=710)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0803 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.459` → IC=+0.170 (n=1527)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.459 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.2073` → IC=+0.145 (n=1977)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.2073 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.3202` → IC=+0.137 (n=1022)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.3202 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.6773` → IC=+0.153 (n=445)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6773 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.3085` → IC=+0.269 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3085 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `2.9243` → IC=+0.227 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9243 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.224 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.032)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.148 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0052 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.172 (n=306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.007 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.187 (n=324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 8.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.302` → IC=+0.308 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.302 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2241` → IC=+0.201 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2241 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.886` → IC=+0.121 (n=386)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.886 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.4431` → IC=+0.135 (n=579)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4431 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=508)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.170 (n=325)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 60.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.260 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.261)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.276 (n=382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.1045` → IC=+0.327 (n=189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1045 (IC base=+0.261)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.277 (n=450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.0294` → IC=+0.322 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0294 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.991` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.991 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.057` → IC=+0.279 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.057 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.260 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.3026` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3026 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `1.5873` → IC=+0.284 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5873 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `1909.2548` → IC=+0.272 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.2548 (IC base=+0.261)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.263 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.261)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.249 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.216 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0932` → IC=+0.246 (n=175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0932 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.217 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.3908` → IC=+0.223 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3908 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.220 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.5162` → IC=+0.226 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5162 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.351` → IC=+0.232 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.351 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.6988` → IC=+0.215 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6988 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.249 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.223 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `2.109` → IC=+0.239 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.109 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `14039.8617` → IC=+0.226 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14039.8617 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.145 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0037 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.150 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.155 (n=195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.148 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.4745` → IC=+0.178 (n=513)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.4745 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.167 (n=487)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.993` → IC=+0.221 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.993 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6183` → IC=+0.190 (n=195)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6183 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.193 (n=203)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4183` → IC=+0.166 (n=477)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4183 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4857` → IC=+0.161 (n=426)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4857 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=755)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `14438.2519` → IC=+0.170 (n=265)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14438.2519 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.163 (n=173)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 234.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.214 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=225)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.071` → IC=+0.267 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.071 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.1342` → IC=+0.160 (n=516)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1342 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `3.3381` → IC=+0.156 (n=475)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 3.3381 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.7007` → IC=+0.172 (n=540)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.7007 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=612)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.250 (n=490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.4563` → IC=+0.246 (n=490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4563 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.265 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.5027` → IC=+0.272 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5027 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.288` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.288 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.385` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.385 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.6125` → IC=+0.233 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6125 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1859.1658` → IC=+0.241 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1859.1658 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.227 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.240)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.144 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=436)

- **FILTRO** `ibs_20min` < `0.2901` → IC=-0.142 (n=191)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2901
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=389)

- **FILTRO** `ibs_20min` > `0.8479` → IC=-0.182 (n=253)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8479
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=763)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=948)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1424 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` > `1.1445` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1445 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4376` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4376 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` > `1.9887` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9887 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=-0.048)

- **PATRÓN** `dist_vwap_pct` > `0.2734` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2734 (IC base=-0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=-0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.133 (n=156)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4704 (IC base=-0.047)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=104)

- **FILTRO** `sigma_ewma_delta_pct` > `8.292` → IC=-0.178 (n=178)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.292
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=1381)

- **FILTRO** `volumen_pendiente_norm` < `0.0837` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0837
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `volumen_spike_ratio` > `1.5398` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5398
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.160 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0066 (IC base=+0.026)

- **PATRÓN** `ibs_20min` > `0.2727` → IC=+0.123 (n=104)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.2727 (IC base=+0.026)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5143` → IC=-0.167 (n=298)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5143
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=579)

- **FILTRO** `ibs_20min` < `0.4138` → IC=-0.186 (n=438)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4138
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=439)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.198 (n=200)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=677)

- **FILTRO** `ibs_20min` > `0.7937` → IC=-0.176 (n=353)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7937
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1062)

- **FILTRO** `sigma_ewma_delta_pct` > `6.858` → IC=-0.149 (n=229)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.858
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1186)

- **PATRÓN** `dist_vwap_pct` > `0.488` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.488 (IC base=-0.107)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.0803` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0803 (IC base=-0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.4824` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4824 (IC base=-0.107)

- **PATRÓN** `dist_vwap_pct` < `0.2145` → IC=+0.209 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2145 (IC base=-0.055)

- **PATRÓN** `volumen_regimen` < `0.6756` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6756 (IC base=-0.055)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.253 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.0889` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0889 (IC base=-0.055)

- **PATRÓN** `volumen_spike_ratio` > `1.6954` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.6954 (IC base=-0.055)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=-0.055)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.138 (n=1734)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0076 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.2691` → IC=+0.123 (n=3824)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.2691 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `1.2207` → IC=+0.287 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2207 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `0.6785` → IC=+0.203 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6785 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1155` → IC=+0.200 (n=1695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1155 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2548` → IC=+0.204 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2548 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4951` → IC=+0.226 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4951 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.8921` → IC=+0.205 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8921 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.290 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0882` → IC=+0.203 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0882 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.768` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.768 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.226 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8585 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `1.2256` → IC=+0.234 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2256 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2611` → IC=+0.348 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2611 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.4527` → IC=+0.291 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4527 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.268 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.045)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2548` → IC=-0.156 (n=309)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2548
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=630)

- **FILTRO** `sigma_ewma_delta_pct` > `2.172` → IC=-0.165 (n=258)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.172
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=578)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.162 (n=235)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.7778 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.211` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.211 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.7645` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7645 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8771` → IC=-0.160 (n=333)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8771
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1001)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 288.0 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` > `0.6571` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6571 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1332 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5727 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` > `1.1074` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1074 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.0627` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0627 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.3623` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.3623 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.3512` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.3512 (IC base=-0.040)

- **PATRÓN** `ballena_activa_n` < `261.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 261.0 (IC base=-0.040)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.291 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.232 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.260 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.7122` → IC=+0.251 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7122 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.126` → IC=+0.279 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.126 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1444` → IC=+0.229 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1444 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `2.5365` → IC=+0.222 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5365 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `4.1476` → IC=+0.229 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.1476 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.257 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.327 (n=356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.3735` → IC=+0.313 (n=351)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3735 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.341 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` < `0.3226` → IC=+0.325 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3226 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.726` → IC=+0.313 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.726 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.3643` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3643 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `2.4365` → IC=+0.335 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4365 (IC base=+0.310)

- **PATRÓN** `libro_liquidez` > `1767.881` → IC=+0.342 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1767.881 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.310)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.145 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=453)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.167 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=407)

- **FILTRO** `dist_vwap_pct` < `0.3304` → IC=-0.207 (n=39)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3304
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=45)

- **FILTRO** `volumen_regimen` > `0.9565` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9565
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=64)

- **FILTRO** `ibs_20min` > `0.7397` → IC=-0.143 (n=382)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7397
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=742)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `volumen_pendiente_norm` < `0.1167` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1167
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=5)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1052)

- **PATRÓN** `dist_vwap_pct` > `0.3304` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3304 (IC base=-0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.0567` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0567 (IC base=-0.085)

- **PATRÓN** `volumen_spike_ratio` < `2.091` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.091 (IC base=-0.085)

- **PATRÓN** `volumen_spike_ratio` > `1.7258` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7258 (IC base=-0.085)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7647` → IC=-0.147 (n=550)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7647
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=284)

- **FILTRO** `ibs_20min` > `0.7683` → IC=-0.232 (n=244)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7683
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=733)

- **FILTRO** `dist_vwap_pct` > `0.1358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1358
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `volumen_regimen` > `1.3203` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3203
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

- **FILTRO** `volumen_pendiente_norm` < `0.1132` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1132
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `volumen_spike_ratio` > `1.4195` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4195
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `volumen_spike_ratio` < `2.3625` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.3625
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.296 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.5696` → IC=+0.309 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5696 (IC base=-0.012)

- **PATRÓN** `volumen_regimen` < `0.8618` → IC=+0.215 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8618 (IC base=-0.012)

- **PATRÓN** `volumen_regimen` > `1.0285` → IC=+0.279 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0285 (IC base=-0.012)

- **PATRÓN** `volumen_pendiente_norm` < `0.1176` → IC=+0.228 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1176 (IC base=-0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.231` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.231 (IC base=-0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4567` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4567 (IC base=-0.012)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.293 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=-0.012)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.025` → IC=+0.330 (n=221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.025 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.250 (n=318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.309 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.3483` → IC=+0.345 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3483 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.191` → IC=+0.285 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.191 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.8371` → IC=+0.277 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8371 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.276 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.5913` → IC=+0.246 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5913 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2469.502` → IC=+0.241 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2469.502 (IC base=+0.238)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.281 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.299 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.2938` → IC=+0.282 (n=465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2938 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.284 (n=661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` < `0.3654` → IC=+0.317 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3654 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.5433` → IC=+0.278 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5433 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` < `0.2079` → IC=+0.281 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2079 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.115` → IC=+0.318 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.115 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` < `0.6367` → IC=+0.287 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6367 (IC base=+0.276)

- **PATRÓN** `volumen_regimen` > `1.2602` → IC=+0.312 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2602 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.388 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` > `2.1862` → IC=+0.298 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1862 (IC base=+0.276)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.203 (n=1072)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3288` → IC=+0.168 (n=2828)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3288 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=3250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.284 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `1.1216` → IC=+0.243 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1216 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.462` → IC=+0.240 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.462 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.6257` → IC=+0.174 (n=2204)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6257 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1041` → IC=+0.184 (n=1181)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1041 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.3351` → IC=+0.166 (n=2598)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.3351 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.169 (n=3325)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.03 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3958.3691` → IC=+0.187 (n=1071)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3958.3691 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.182 (n=1871)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 94.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.194 (n=2001)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0061 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.179 (n=998)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0098 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0773` → IC=+0.213 (n=999)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0773 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.181 (n=1382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.413` → IC=+0.231 (n=2994)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.413 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.173 (n=2279)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.972` → IC=+0.218 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.972 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1618` → IC=+0.166 (n=2297)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1618 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2979` → IC=+0.261 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2979 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.7059` → IC=+0.207 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7059 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.179 (n=1722)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 98.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.170 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0053 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.191 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0071 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.272` → IC=+0.180 (n=529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.272 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.205 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.307 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.623` → IC=+0.284 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.623 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2241` → IC=+0.237 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2241 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.7275` → IC=+0.144 (n=447)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.7275 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.4557` → IC=+0.162 (n=447)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4557 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.269 (n=322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.2479` → IC=+0.289 (n=282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2479 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.268 (n=338)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.1641` → IC=+0.287 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1641 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.664` → IC=+0.261 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.664 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.0867` → IC=+0.237 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0867 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.3063` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3063 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` < `1.9514` → IC=+0.248 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9514 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `1.4233` → IC=+0.241 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4233 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1817.6848` → IC=+0.277 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1817.6848 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.238 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.246)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.240 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.4092` → IC=+0.192 (n=466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4092 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9857` → IC=+0.279 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9857 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.228 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.027` → IC=+0.244 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.027 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.566` → IC=+0.182 (n=444)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 7.566 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6383 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0613 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1606` → IC=+0.193 (n=138)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1606 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.1275` → IC=+0.202 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1275 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `13337.4554` → IC=+0.205 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13337.4554 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.168 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0059 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2258` → IC=+0.179 (n=496)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2258 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.176 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.4432` → IC=+0.194 (n=564)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.4432 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.5788` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5788 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.2004` → IC=+0.170 (n=562)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.2004 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.417` → IC=+0.228 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.417 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6864` → IC=+0.216 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6864 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1606` → IC=+0.219 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1606 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4807` → IC=+0.168 (n=456)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.4807 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.3935` → IC=+0.151 (n=456)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.3935 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `14215.1771` → IC=+0.167 (n=256)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 14215.1771 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 228.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.218 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.1601` → IC=+0.194 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1601 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.206 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.297` → IC=+0.276 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.297 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.2309` → IC=+0.161 (n=426)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.2309 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1342` → IC=+0.159 (n=177)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1342 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.9605` → IC=+0.184 (n=185)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.9605 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `3.4171` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 3.4171 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=464)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.228 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.247 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.2078` → IC=+0.272 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2078 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.264 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.3798` → IC=+0.270 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3798 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.563` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.563 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3671` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3671 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `3.94` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.94 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1860.9452` → IC=+0.250 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.9452 (IC base=+0.232)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.203 (n=412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3629` → IC=+0.186 (n=412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3629 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.4362` → IC=+0.215 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4362 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1444` → IC=+0.199 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1444 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.328` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.328 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.7028` → IC=+0.191 (n=418)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.7028 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6221` → IC=+0.212 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6221 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `12333.533` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12333.533 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.155 (n=357)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 173.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.203 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3745` → IC=+0.152 (n=553)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3745 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.5225` → IC=+0.183 (n=553)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5225 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.3378` → IC=+0.146 (n=597)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3378 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.378` → IC=+0.199 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.378 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1524` → IC=+0.145 (n=553)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1524 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.5986` → IC=+0.137 (n=552)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.5986 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.178 (n=175)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.9018` → IC=+0.152 (n=297)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.9018 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.577` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.577 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `9534.8435` → IC=+0.156 (n=251)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 9534.8435 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.168 (n=416)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0083 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5455` → IC=+0.190 (n=623)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5455 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.145` → IC=+0.260 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.145 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.122` → IC=+0.266 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.122 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.6244` → IC=+0.135 (n=623)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6244 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1649` → IC=+0.137 (n=617)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1649 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4403` → IC=+0.141 (n=196)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4403 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.7916` → IC=+0.124 (n=392)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.7916 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=486)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `3214.2982` → IC=+0.219 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3214.2982 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=236)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.191 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0107 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.135 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.413` → IC=+0.230 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.413 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.7428` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7428 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1784` → IC=+0.139 (n=475)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1784 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.843` → IC=+0.226 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.843 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.1342` → IC=+0.142 (n=535)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1342 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.834` → IC=+0.143 (n=357)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.834 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2651` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2651 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.0865` → IC=+0.192 (n=183)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.0865 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `2868.2407` → IC=+0.186 (n=243)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2868.2407 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0163` → IC=+0.220 (n=433)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0163 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1655` → IC=+0.208 (n=286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1655 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.185 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.895` → IC=+0.266 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.895 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.221 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.122` → IC=+0.243 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.122 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.8273` → IC=+0.220 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8273 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.5635` → IC=+0.204 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5635 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=779)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.260 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0881` → IC=+0.248 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0881 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.218 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.3942` → IC=+0.255 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3942 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.5141` → IC=+0.221 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5141 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.521` → IC=+0.272 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.521 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6915` → IC=+0.234 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6915 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.7468` → IC=+0.259 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7468 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2500.6634` → IC=+0.216 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2500.6634 (IC base=+0.215)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.182 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0097 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.161 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.6176` → IC=+0.184 (n=561)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6176 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.8774` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8774 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.673` → IC=+0.172 (n=303)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.673 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8863` → IC=+0.139 (n=339)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8863 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.701` → IC=+0.144 (n=453)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.701 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.3726` → IC=+0.135 (n=505)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.3726 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.9235` → IC=+0.141 (n=382)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.9235 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=466)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3064.7088` → IC=+0.148 (n=285)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3064.7088 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 12.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.31` → IC=+0.128 (n=423)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.31 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.165 (n=210)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 16.0 (IC base=+0.051)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=96)

- **FILTRO** `libro_liquidez` < `6959.6494` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 6959.6494
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=93)

- **FILTRO** `ibs_20min` > `0.676` → IC=-0.121 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` > 0.676
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=182)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.133 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 9.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.9306` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9306 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.7932` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.7932 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.247` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.247 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `12687.2059` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12687.2059 (IC base=+0.056)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.153 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0027 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.676` → IC=+0.125 (n=182)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.676 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.130 (n=117)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 278.0 (IC base=+0.042)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `ibs_20min` > `0.6298` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6298
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=91)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.282 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.322 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.2275` → IC=+0.293 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2275 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `0.8289` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8289 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` < `0.7834` → IC=+0.303 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7834 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` < `0.701` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.701 (IC base=+0.284)

- **PATRÓN** `volumen_regimen` > `1.2111` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2111 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.3845` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3845 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.7006` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7006 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2672.5659` → IC=+0.283 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2672.5659 (IC base=+0.284)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.258 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.016)

- **PATRÓN** `drift_60min` |x|≤ `0.1224` → IC=+0.167 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1224 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` < `0.8507` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8507 (IC base=+0.016)

- **PATRÓN** `libro_liquidez` > `9264.2772` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9264.2772 (IC base=+0.016)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=101)

- **FILTRO** `dist_vwap_pct` > `0.1911` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1911
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=107)

- **FILTRO** `volumen_regimen` > `1.2914` → IC=-0.227 (n=31)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2914
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=97)

- **FILTRO** `volumen_pendiente_norm` > `0.2325` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2325
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=90)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.123 (n=160)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.5714 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.5045` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5045 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.979` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.979 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.049)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.205 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2982` → IC=+0.172 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2982 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.56 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1962` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1962 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.275` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.275 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6571 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.2201` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.2201 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.9259` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.9259 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.196 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0135 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `1.0608` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0608 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.481` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 8.481 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `0.6173` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6173 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 18.0 (IC base=+0.102)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.201 (n=1714)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.169 (n=3829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `1.0494` → IC=+0.224 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0494 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.365` → IC=+0.230 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.365 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.8788` → IC=+0.152 (n=1762)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8788 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.0819` → IC=+0.159 (n=1198)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0819 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1032` → IC=+0.182 (n=1336)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1032 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `2.323` → IC=+0.163 (n=3044)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.323 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8784` → IC=+0.168 (n=2306)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.8784 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=2971)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3897.8392` → IC=+0.192 (n=1260)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3897.8392 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.212 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.207 (n=2360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.4717` → IC=+0.194 (n=3538)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4717 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=1597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5591` → IC=+0.238 (n=3537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5591 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.173 (n=2479)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.4351 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.572` → IC=+0.210 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.572 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.543` → IC=+0.189 (n=3466)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.543 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.6189` → IC=+0.181 (n=853)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6189 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.162 (n=852)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1929 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2395` → IC=+0.255 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2395 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.3386` → IC=+0.198 (n=1284)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.3386 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.175 (n=1636)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 54.0 (IC base=+0.186)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.191 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0052 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.210 (n=281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.205 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.334 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.663` → IC=+0.311 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.663 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.250 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.5851` → IC=+0.161 (n=237)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5851 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.8937` → IC=+0.176 (n=359)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8937 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.275 (n=446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.273 (n=399)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.1095` → IC=+0.303 (n=196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1095 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.293 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.513` → IC=+0.303 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.513 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.175` → IC=+0.287 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.175 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2963` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2963 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `1.4882` → IC=+0.285 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4882 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `1914.09` → IC=+0.275 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.09 (IC base=+0.270)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.262 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.270)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.201 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.171 (n=545)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0032 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.165 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.3307` → IC=+0.212 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3307 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.2359` → IC=+0.214 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2359 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.209 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.417` → IC=+0.168 (n=528)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 4.417 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.172 (n=610)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2653 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `1.0886` → IC=+0.181 (n=277)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0886 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.074` → IC=+0.186 (n=504)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.074 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1469` → IC=+0.177 (n=162)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1469 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.413` → IC=+0.192 (n=562)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.413 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.3839` → IC=+0.177 (n=561)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.3839 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `13044.1569` → IC=+0.197 (n=407)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 13044.1569 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.168 (n=576)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.006 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.169 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0049 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.196 (n=192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.167 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.172 (n=593)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 18.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.5897` → IC=+0.198 (n=575)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5897 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.3362` → IC=+0.177 (n=553)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.3362 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.6166` → IC=+0.253 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6166 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2129` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2129 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.4507` → IC=+0.186 (n=479)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.4507 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=745)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `287.0` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 287.0 (IC base=+0.164)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.258 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.250 (n=238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7031` → IC=+0.265 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7031 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.298` → IC=+0.335 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.298 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.222` → IC=+0.216 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.222 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.9243` → IC=+0.219 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9243 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `4.1833` → IC=+0.215 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.1833 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `1915.5084` → IC=+0.210 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.5084 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.286 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.237 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.267 (n=200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.5238` → IC=+0.288 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5238 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.578` → IC=+0.272 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.578 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3665` → IC=+0.271 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3665 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7297` → IC=+0.264 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7297 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.9367` → IC=+0.210 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9367 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1868.3264` → IC=+0.246 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1868.3264 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.202 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.235)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.151 (n=612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0087 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2337` → IC=+0.151 (n=408)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.2337 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.161 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.3306` → IC=+0.192 (n=611)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.3306 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.3783` → IC=+0.180 (n=264)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3783 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.376` → IC=+0.189 (n=284)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 4.376 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.9069` → IC=+0.171 (n=408)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.9069 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1004` → IC=+0.230 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1004 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.1967` → IC=+0.211 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1967 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4421.0538` → IC=+0.214 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4421.0538 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.159 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0072 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4486` → IC=+0.155 (n=526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4486 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1211` → IC=+0.231 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1211 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.219` → IC=+0.139 (n=239)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.219 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.3861` → IC=+0.139 (n=508)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3861 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.385` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.385 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.59` → IC=+0.137 (n=497)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.59 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.5848` → IC=+0.140 (n=176)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.5848 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6467` → IC=+0.150 (n=469)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6467 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.8437` → IC=+0.149 (n=311)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.8437 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.5341` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.5341 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `11748.9804` → IC=+0.201 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11748.9804 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `186.0` → IC=+0.154 (n=394)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 186.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.139 (n=444)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0082 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.131 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 12.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4773` → IC=+0.179 (n=664)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4773 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `1.1148` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1148 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.297` → IC=+0.203 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.297 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2971.9712` → IC=+0.250 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.9712 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.143 (n=393)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 57.0 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.182 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0057 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1299` → IC=+0.151 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1299 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.132 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.189 (n=631)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.5096` → IC=+0.123 (n=581)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.5096 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.7055` → IC=+0.145 (n=277)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7055 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.139 (n=192)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.130 (n=217)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2692.6188` → IC=+0.162 (n=285)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2692.6188 (IC base=+0.103)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0278` → IC=+0.237 (n=253)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0278 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.204 (n=758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.9437` → IC=+0.295 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9437 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `1.3532` → IC=+0.283 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3532 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.141` → IC=+0.249 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.141 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `0.6825` → IC=+0.211 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6825 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2405` → IC=+0.258 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2405 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `2.6398` → IC=+0.193 (n=709)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.6398 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.8291` → IC=+0.198 (n=472)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.8291 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.201 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.292 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.237 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.658` → IC=+0.221 (n=829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.658 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.218 (n=785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.222 (n=872)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.4944` → IC=+0.269 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4944 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.1792` → IC=+0.227 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1792 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.704` → IC=+0.296 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.704 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.245 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.316 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.8573` → IC=+0.215 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8573 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.190 (n=543)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 35.0 (IC base=+0.216)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=1455)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.130 (n=955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0102 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.4366` → IC=+0.137 (n=955)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4366 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.154 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.134 (n=370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 4.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.2674` → IC=+0.147 (n=1085)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.2674 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.3119` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 1.3119 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.266` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.266 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.63` → IC=+0.130 (n=1005)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.63 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.8718` → IC=+0.125 (n=513)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.8718 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.2476` → IC=+0.152 (n=202)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2476 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.449` → IC=+0.164 (n=358)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.449 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.6734` → IC=+0.146 (n=357)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.6734 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.182 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0036 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3655` → IC=+0.159 (n=971)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3655 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.174 (n=427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.2032` → IC=+0.164 (n=486)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.2032 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1908` → IC=+0.139 (n=469)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1908 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.150 (n=1101)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.142 (n=1074)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2227 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.1458` → IC=+0.139 (n=1103)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1458 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0681` → IC=+0.141 (n=528)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0681 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.494` → IC=+0.147 (n=1093)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.494 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.142 (n=1093)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=1455)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7341.4793` → IC=+0.142 (n=1103)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7341.4793 (IC base=+0.135)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.403` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.403
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=175)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.129 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 15.0 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.403` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.403 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.8077` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.8077 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.3696` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.3696 (IC base=+0.088)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.191 (n=260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0035 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.141 (n=588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.178 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.1762` → IC=+0.182 (n=259)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1762 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.6568` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6568 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.155 (n=584)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1909` → IC=+0.146 (n=588)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1909 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0649` → IC=+0.168 (n=278)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0649 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.5034` → IC=+0.138 (n=586)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5034 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.7958` → IC=+0.135 (n=390)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7958 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `11945.4632` → IC=+0.134 (n=525)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 11945.4632 (IC base=+0.129)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.209 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.190 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0104 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.5484` → IC=+0.164 (n=245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.5484 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.250 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.909` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.909 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.149` → IC=+0.174 (n=222)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 3.149 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.6474` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6474 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.4202` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4202 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `1778.451` → IC=+0.174 (n=219)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1778.451 (IC base=+0.159)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.150 (n=338)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0079 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.2708` → IC=+0.143 (n=256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.2708 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.176 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.131 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.8027` → IC=+0.176 (n=174)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.8027 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `1.0099` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 1.0099 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.2471` → IC=+0.135 (n=288)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2471 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.264` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.264 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.481` → IC=+0.133 (n=339)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.481 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.6457` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6457 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1811` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1811 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4166` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4166 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.8188` → IC=+0.131 (n=250)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8188 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7768.8878` → IC=+0.137 (n=384)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 7768.8878 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.205 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.177 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.162 (n=223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.2183` → IC=+0.140 (n=145)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.2183 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.1311` → IC=+0.149 (n=329)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.1311 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1463` → IC=+0.138 (n=150)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1463 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.3875` → IC=+0.145 (n=325)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3875 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.095` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.095 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.1943` → IC=+0.153 (n=329)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1943 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.7042` → IC=+0.135 (n=294)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.7042 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.1393` → IC=+0.149 (n=337)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1393 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4615` → IC=+0.156 (n=324)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4615 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.160 (n=324)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `7743.0752` → IC=+0.149 (n=329)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7743.0752 (IC base=+0.134)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=67)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=27)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.1303` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1303 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.7269` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.7269 (IC base=+0.016)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6842` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6842
  - _Potencial_: sin este filtro IC_bueno=+0.243 (n=177)

- **FILTRO** `sigma_h` > `0.011` → IC=-0.289 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=168)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.257 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=118)

- **FILTRO** `dist_vwap_pct` > `0.111` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.111
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=64)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.213 (n=179)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.243 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.902` → IC=+0.254 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.902 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `1.0552` → IC=+0.131 (n=155)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0552 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.1964` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1964 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` < `0.0651` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0651 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.3065` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3065 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4015` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4015 (IC base=+0.087)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=160)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2406.6759` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2406.6759 (IC base=+0.087)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7741` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7741
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=64)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.221 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.094)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.7741` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7741 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.251` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.251 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6992` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6992 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.094)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=47)

- **FILTRO** `ibs_20min` > `0.1674` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1674
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.191 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0058 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.469` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.469 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2791` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2791 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6214` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6214 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.0801` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0801 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2160.4489` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2160.4489 (IC base=+0.135)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.121 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=31)

- **FILTRO** `sigma_h` > `0.0119` → IC=-0.281 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0119
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=41)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.256 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

- **FILTRO** `volumen_regimen` > `0.8778` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8778
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.197 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=-0.006)

- **PATRÓN** `ibs_20min` > `0.7867` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.7867 (IC base=-0.006)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.804` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.804 (IC base=-0.006)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0047` → IC=-0.300 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.443 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=65)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.380 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=77)

- **FILTRO** `dist_vwap_pct` > `0.3683` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3683
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=81)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2614` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2614
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `sigma_h` < `0.0031` → IC=-0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0031
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.326 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `ibs_20min` > `0.8144` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8144
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `ibs_20min` < `0.5833` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.3782` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3782
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=150)

- **FILTRO** `ibs_20min` > `0.447` → IC=-0.202 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.447
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=138)

- **FILTRO** `dist_vwap_pct` > `0.213` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.213
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=148)

- **PATRÓN** `ibs_20min` > `0.5964` → IC=+0.138 (n=150)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.5964 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.447` → IC=+0.129 (n=138)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.447 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.659` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.659 (IC base=+0.046)

- **PATRÓN** `libro_liquidez` > `3314.3277` → IC=+0.128 (n=92)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3314.3277 (IC base=+0.046)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `sigma_h` < `0.0017` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=53)

- **FILTRO** `ibs_20min` < `0.557` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.557
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=47)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.176 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0035 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.251 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.5657` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5657 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.115)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=31)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.085)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6645` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6645 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.413` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 7.413 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8554 (IC base=+0.065)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `12.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **FILTRO** `sigma_ewma_delta_pct` > `1.488` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 1.488
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.129 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0069 (IC base=+0.093)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.143 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.121 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.791 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.093)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2492.097` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2492.097 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2478.0092` → IC=+0.132 (n=134)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2478.0092 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2492.097` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2492.097 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2478.0092` → IC=+0.132 (n=134)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2478.0092 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.189 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=47)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=103)

- **FILTRO** `libro_liquidez` < `2114.4748` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 2114.4748
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=90)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=138)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `libro_liquidez` < `11682.4811` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 11682.4811
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `libro_liquidez` < `13600.036` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 13600.036
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=817)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9444` → IC=-0.289 (n=36)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9444
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.134 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.035)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.035)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `31327.3` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `liq_usd_total` < 31327.3
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=71)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `libro_liquidez` < `15381.0964` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 15381.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `ballena_activa_n` > `630.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 630.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `liq_usd_total` > `138064.32` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `liq_usd_total` > 138064.32 (IC base=+0.005)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.005)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9045` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9045
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=54)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=250)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=340)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=62)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=27)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=83)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=32)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=33)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.6408` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.6408
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=642)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1771` → IC=-0.132 (n=112)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1771
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=220)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.45` → IC=-0.185 (n=1142)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=3620)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.206 (n=1143)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3792)

- **FILTRO** `ibs_20min` > `0.2708` → IC=-0.162 (n=1233)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2708
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3702)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.256 (n=170)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=519)

- **FILTRO** `ibs_20min` < `0.7215` → IC=-0.230 (n=172)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7215
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=517)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.218 (n=193)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=627)

- **FILTRO** `ballena_activa_n` > `62.0` → IC=-0.163 (n=203)

  - _Acción_: SKIP cuando `ballena_activa_n` > 62.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=617)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=785)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.191 (n=241)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=503)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.233 (n=193)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=626)

- **FILTRO** `ibs_20min` > `0.7391` → IC=-0.199 (n=204)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7391
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=615)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.175 (n=204)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=634)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.191 (n=202)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=628)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.162 (n=205)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=625)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.140 (n=223)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=585)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=193)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=616)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.163 (n=200)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=609)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.201 (n=192)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=585)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=762)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.241 (n=191)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=613)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.306 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=375)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=381)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.0752` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0752
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `drift_20min_pct` |x|> `0.1906` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1906
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

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
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.141 (n=2556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=9317)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=2888)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=8985)

- **FILTRO** `ibs_7min` < `0.7151` → IC=-0.242 (n=2967)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7151
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=8906)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.170 (n=4032)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7841)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.227 (n=3437)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=11367)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.170 (n=3695)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=11109)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.328 (n=410)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=1272)

- **FILTRO** `ibs_7min` < `0.9639` → IC=-0.198 (n=1110)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9639
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=572)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.243 (n=410)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=1272)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.235 (n=631)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1957)

- **FILTRO** `drift_7min_pct` |x|> `0.1176` → IC=-0.138 (n=879)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1176
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1709)

- **FILTRO** `ibs_7min` > `0.2973` → IC=-0.173 (n=879)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2973
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1709)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.150 (n=487)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1764)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.261 (n=521)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1730)

- **FILTRO** `ibs_7min` < `0.7775` → IC=-0.188 (n=562)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7775
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1689)

- **FILTRO** `ballena_activa_n` > `163.0` → IC=-0.192 (n=560)

  - _Acción_: SKIP cuando `ballena_activa_n` > 163.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1691)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.230 (n=538)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1742)

- **FILTRO** `ballena_activa_n` > `101.0` → IC=-0.183 (n=775)

  - _Acción_: SKIP cuando `ballena_activa_n` > 101.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1505)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.194 (n=432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=1333)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.311 (n=565)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1200)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.286 (n=441)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1324)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.236 (n=438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=1327)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.241 (n=593)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=2009)

- **FILTRO** `ibs_7min` > `0.8094` → IC=-0.173 (n=650)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8094
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1952)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.147 (n=607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=1418)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.254 (n=490)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1535)

- **FILTRO** `ibs_7min` < `0.7533` → IC=-0.191 (n=506)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7533
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=1519)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.183 (n=670)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=1355)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.235 (n=662)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1356)

- **FILTRO** `ibs_7min` > `0.2771` → IC=-0.185 (n=503)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2771
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=1515)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.192 (n=504)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=1514)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.237 (n=549)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1677)

- **FILTRO** `ibs_7min` < `0.7429` → IC=-0.206 (n=555)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1671)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.184 (n=552)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1674)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.192 (n=661)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=2088)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.299 (n=475)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1449)

- **FILTRO** `ibs_7min` < `0.7348` → IC=-0.245 (n=481)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7348
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1443)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.225 (n=471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=1453)

- **FILTRO** `libro_liquidez` < `2681.6088` → IC=-0.140 (n=1269)

  - _Acción_: SKIP cuando `libro_liquidez` < 2681.6088
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=655)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=525)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2042)

- **FILTRO** `ibs_7min` > `0.7982` → IC=-0.159 (n=641)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7982
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1926)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.139 (n=635)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1932)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=412)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3977` → IC=+0.133 (n=459)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3977 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `456.268` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 456.268 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=209)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3762.2112` → IC=+0.141 (n=129)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3762.2112 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.262 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.126)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3971` → IC=+0.136 (n=75)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3971 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2091.1708` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2091.1708 (IC base=+0.098)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4128` → IC=+0.186 (n=49)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.4128 (IC base=+0.090)

- **PATRÓN** `total_vol_5m` < `486.9033` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 486.9033 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `7829.679` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7829.679 (IC base=+0.090)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.196 (n=67)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 16.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.184 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 18.0 (IC base=+0.159)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 6300.756 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3738.4224` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3738.4224 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 73.0 (IC base=+0.159)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.395` → IC=+0.142 (n=79)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.395 (IC base=+0.107)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.135 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 18.0 (IC base=+0.107)

- **PATRÓN** `total_vol_5m` < `358653.4` → IC=+0.139 (n=70)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 358653.4 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 58.0 (IC base=+0.107)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9182` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9182
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=51)

- **FILTRO** `pct_vs_K` |x|> `3.8846` → IC=-0.423 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8846
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=99)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9866` → IC=-0.426 (n=25)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.300 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.138)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `4.9995` → IC=-0.321 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.9995
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=115)

- **FILTRO** `pct_vs_K` |x|> `4.3806` → IC=-0.476 (n=39)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.3806
  - _Potencial_: sin este filtro IC_bueno=-0.282 (n=76)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **PATRÓN** `T_h` < `119.1632` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `T_h` < 119.1632 (IC base=+0.008)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8662` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8662 (IC base=+0.008)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0057` → IC=-0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=31)

- **FILTRO** `sigma_h` > `0.0049` → IC=-0.380 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.308 (n=24)

### RESOLUTION_SNIPER
- **PATRÓN** `dist_50` > `0.47` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.373)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `5.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=54)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=106)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.042)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.437 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 44.0 (IC base=+0.042)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=72)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=108)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=114)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=118)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=135)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=211)

- **PATRÓN** `streak_estiramiento` < `0.2837` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2837 (IC base=+0.029)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=436)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=218)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=294)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=1412)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=800)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=808)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.158 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.122)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.143 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0062 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1878` → IC=+0.132 (n=414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.1878 (IC base=+0.122)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2109` → IC=+0.142 (n=188)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.2109 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.160 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_15` > `0.5321` → IC=+0.214 (n=414)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5321 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.175 (n=112)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.244 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=434)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `8560.6622` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8560.6622 (IC base=+0.122)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.2813` → IC=-0.167 (n=148)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2813
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=445)

- **FILTRO** `sigma_ewma_delta_pct` > `6.683` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.683
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=541)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0282` → IC=-0.204 (n=25)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0282
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=51)

- **FILTRO** `ibs_15` < `0.1315` → IC=-0.324 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1315
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.236` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 18.236 (IC base=+0.012)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.6681` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.6681
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=90)

- **FILTRO** `libro_liquidez` < `14061.5224` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 14061.5224
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.179 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0037 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.182 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0047 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.201 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.167)

- **PATRÓN** `drift_15min` |x|≤ `0.4558` → IC=+0.198 (n=84)

  - _Acción_: Kelly boost +0.99€ cuando `drift_15min` |x|≤ 0.4558 (IC base=+0.167)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2384` → IC=+0.182 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio_macro` |x|> 0.2384 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.195 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 4.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.172 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` > `0.881` → IC=+0.265 (n=83)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.881 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.3112` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3112 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.1171` → IC=+0.187 (n=81)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1171 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.227 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.167)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `libro_liquidez` < `13135.9064` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 13135.9064
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=96)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.984` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 17.984 (IC base=+0.000)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6314` → IC=-0.250 (n=38)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6314
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=80)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.125 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0044 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2671` → IC=+0.188 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.2671 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.220 (n=80)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.067)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=81)

- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=83)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `drift_15min` |x|> `0.5033` → IC=-0.152 (n=139)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5033
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=418)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6136` → IC=-0.147 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6136
  - _Potencial_: sin este filtro IC_bueno=+0.294 (n=32)

- **PATRÓN** `ibs_15` > `0.6136` → IC=+0.294 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6136 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.477` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.477 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `2964.2504` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2964.2504 (IC base=+0.076)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.023` → IC=-0.227 (n=31)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.023
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=63)

- **FILTRO** `drift_60min` |x|> `0.7244` → IC=-0.136 (n=31)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.7244
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=63)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=67)

- **FILTRO** `ibs_15` < `0.25` → IC=-0.300 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=71)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=49)

- **FILTRO** `sigma_ewma_delta_pct` < `6.107` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 6.107
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.015)

- **PATRÓN** `ibs_15` > `0.4634` → IC=+0.125 (n=38)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.62€ cuando `ibs_15` > 0.4634 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.3805` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.3805 (IC base=+0.015)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0597` → IC=+0.145 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio_macro` |x|> 0.0597 (IC base=+0.107)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.173 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.107)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.167 (n=109)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` > 0.4444 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.3338` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3338 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.845` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.845 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2479.6478` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2479.6478 (IC base=+0.107)

- **PATRÓN** `ibs_15` < `0.1429` → IC=+0.185 (n=128)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` < 0.1429 (IC base=+0.033)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.387 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.1141` → IC=+0.344 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1141 (IC base=+0.322)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.324 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.322)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.351 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.322)

- **PATRÓN** `ibs_15` > `0.9085` → IC=+0.377 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9085 (IC base=+0.322)

- **PATRÓN** `dist_vwap_pct` > `0.4531` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4531 (IC base=+0.322)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.649` → IC=+0.327 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.649 (IC base=+0.322)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.382` → IC=+0.321 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.382 (IC base=+0.322)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.324 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.322)

- **PATRÓN** `libro_liquidez` > `7959.8654` → IC=+0.357 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7959.8654 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `535.0` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 535.0 (IC base=+0.322)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1148` → IC=+0.338 (n=35)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1148 (IC base=+0.308)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.312 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.308)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.338 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.340 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.308)

- **PATRÓN** `drift_15min` |x|≤ `0.3756` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3756 (IC base=+0.308)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1063` → IC=+0.312 (n=94)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1063 (IC base=+0.308)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1131` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1131 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.341 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.308)

- **PATRÓN** `ibs_15` > `0.8418` → IC=+0.354 (n=94)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8418 (IC base=+0.308)

- **PATRÓN** `dist_vwap_pct` > `0.447` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.447 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.991` → IC=+0.317 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.991 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `11137.3038` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11137.3038 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `626.0` → IC=+0.414 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 626.0 (IC base=+0.308)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.333 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.361 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.368 (n=51)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.13` → IC=+0.365 (n=50)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.13 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2065` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2065 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.333 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.333)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.333 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.8893` → IC=+0.404 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8893 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.3445` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3445 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `20.548` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 20.548 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `174.0` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 174.0 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.201 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=898)

- **FILTRO** `ibs_15` < `0.5455` → IC=-0.211 (n=140)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5455
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.133 (n=311)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=886)

- **FILTRO** `sigma_ewma_delta_pct` > `17.952` → IC=-0.158 (n=422)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.952
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3232)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.347` → IC=+0.141 (n=157)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.347 (IC base=-0.071)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.194 (n=286)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.97€ cuando `ibs_15` > 0.5455 (IC base=-0.071)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0917` → IC=+0.234 (n=276)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0917 (IC base=-0.074)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1056` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1056 (IC base=-0.074)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.291 (n=309)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` > `0.76` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.76 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1698` → IC=+0.225 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1698 (IC base=-0.074)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.245 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=583)

- **FILTRO** `sigma_h` < `0.0036` → IC=-0.233 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=521)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.238 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=611)

- **FILTRO** `sigma_ewma_delta_pct` > `19.708` → IC=-0.250 (n=146)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.708
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=631)

- **FILTRO** `libro_liquidez` < `15759.0144` → IC=-0.220 (n=512)

  - _Acción_: SKIP cuando `libro_liquidez` < 15759.0144
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=265)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.308 (n=24)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.019)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4875` → IC=-0.324 (n=49)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4875
  - _Potencial_: sin este filtro IC_bueno=+0.185 (n=147)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=179)

- **PATRÓN** `drift_60min` |x|≤ `0.0637` → IC=+0.211 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0637 (IC base=+0.056)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3537` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3537 (IC base=+0.056)

- **PATRÓN** `ibs_15` > `0.4875` → IC=+0.185 (n=147)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` > 0.4875 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `10584.3604` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 10584.3604 (IC base=+0.056)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.256 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.227 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `0.4204` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4204 (IC base=+0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0822` → IC=+0.237 (n=158)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0822 (IC base=+0.222)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.304` → IC=+0.230 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.304 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.304 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.314 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_15` < `0.3453` → IC=+0.306 (n=158)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3453 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.7695` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7695 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.1516` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1516 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.486` → IC=+0.256 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.486 (IC base=+0.222)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.8104` → IC=-0.260 (n=73)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8104
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=221)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=109)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=185)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.125)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1261` → IC=+0.160 (n=48)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1261 (IC base=-0.055)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.182` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.182 (IC base=-0.055)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.203 (n=72)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.055)

- **PATRÓN** `dist_vwap_pct` < `0.2804` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2804 (IC base=-0.055)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0219` → IC=-0.268 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0219
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=215)

- **FILTRO** `drift_15min` |x|> `1.1512` → IC=-0.247 (n=81)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1512
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=244)

- **FILTRO** `sigma_ewma_delta_pct` > `15.703` → IC=-0.207 (n=39)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.703
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=286)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.293 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=298)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1618` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1618 (IC base=-0.070)

- **PATRÓN** `ibs_15` < `0.1429` → IC=+0.287 (n=45)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1429 (IC base=-0.070)

- **PATRÓN** `ibs_15` > `0.0937` → IC=+0.303 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.0937 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1865` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1865 (IC base=-0.070)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.070)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.298 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.293 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.330 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.135` → IC=+0.308 (n=196)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.135 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1186` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1186 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.316 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8348` → IC=+0.314 (n=294)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8348 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.3131` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3131 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.713` → IC=+0.291 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.713 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.290 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `13583.6664` → IC=+0.360 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13583.6664 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.072` → IC=+0.293 (n=56)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.072 (IC base=+0.281)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.289 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.293 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.305 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `0.6451` → IC=+0.285 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6451 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1374` → IC=+0.314 (n=111)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1374 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.338 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.968` → IC=+0.333 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.968 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.3306` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3306 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` < `0.1171` → IC=+0.281 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1171 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.879` → IC=+0.295 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.879 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `15220.5605` → IC=+0.362 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15220.5605 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.298 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0662` → IC=+0.328 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0662 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0545` → IC=+0.298 (n=127)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0545 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1069` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1069 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.320 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.846` → IC=+0.322 (n=127)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.846 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.0914` → IC=+0.326 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0914 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.003` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.003 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.173` → IC=+0.301 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.173 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.305 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.314 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 202.0 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0838` → IC=-0.279 (n=66)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0838
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=130)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=57)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1722` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1722
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=41)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1188` → IC=-0.132 (n=36)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1188
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=76)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.993` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.993 (IC base=+0.101)

- **PATRÓN** `ratio` < `0.9922` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.101)

- **PATRÓN** `T_h` > `146.0398` → IC=+0.423 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.341)

- **PATRÓN** `ratio` > `1.0094` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0094 (IC base=+0.341)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `63.9965` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `T_h` < 63.9965 (IC base=+0.090)

- **PATRÓN** `ratio` < `0.973` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.090)

- **PATRÓN** `T_h` < `135.9918` → IC=+0.304 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 135.9918 (IC base=+0.271)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.271)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `63.9712` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9712 (IC base=+0.142)

- **PATRÓN** `ratio` < `0.9726` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9726 (IC base=+0.142)

- **PATRÓN** `T_h` > `100.962` → IC=+0.321 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 100.962 (IC base=+0.310)

- **PATRÓN** `ratio` > `1.0398` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0398 (IC base=+0.310)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `127.3918` → IC=+0.430 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.3918 (IC base=+0.411)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0059 (IC=+0.184 n=17). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5321 sube el IC de +0.122 a +0.214 en UPDOWN_GBM#15min (n=414). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.881 sube el IC de +0.167 a +0.265 en UPDOWN_GBM#BTC#15min (n=83). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.067 a +0.220 en UPDOWN_GBM#ETH#15min (n=80). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6136 sube el IC de +0.076 a +0.294 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.107 a +0.167 en UPDOWN_GBM#XRP#15min (n=109). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1429 sube el IC de +0.033 a +0.185 en UPDOWN_GBM#XRP#15min (n=128). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5455 sube el IC de -0.071 a +0.194 en UPDOWN_GBM_15M_TARDIO (n=286). Ya aplicado como kelly_boost=+0.97€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.074 a +0.291 en UPDOWN_GBM_15M_TARDIO (n=309). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.019 a +0.308 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=24). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4875 sube el IC de +0.056 a +0.185 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=147). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3453 sube el IC de +0.222 a +0.306 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=158). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.125 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.055 a +0.203 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=72). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1429 sube el IC de -0.070 a +0.287 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=45). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.0937 sube el IC de -0.070 a +0.303 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8348 sube el IC de +0.286 a +0.314 en UPDOWN_GBM_IBS_ALTO (n=294). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.968 sube el IC de +0.281 a +0.333 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.846 sube el IC de +0.289 a +0.322 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=127). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.9085 sube el IC de +0.322 a +0.377 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8418 sube el IC de +0.308 a +0.354 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=94). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8893 sube el IC de +0.333 a +0.404 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=50). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.361 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.361 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN` — IC=+0.214 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC#5min` — IC=+0.214 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC` — IC=+0.214 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#5min` — IC=+0.214 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 687 | +0.092 | +35.74€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 687 | +0.092 | +35.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 435 | +0.116 | +26.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 435 | +0.116 | +26.13€ | 1 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 12941 | -0.106 | -2178.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 877 | -0.003 | -120.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 12064 | -0.114 | -2058.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1682 | -0.072 | -351.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1682 | -0.072 | -351.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 877 | -0.003 | -120.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 877 | -0.003 | -120.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1665 | -0.156 | -515.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1665 | -0.156 | -515.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 3487 | -0.062 | -310.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 3487 | -0.062 | -310.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2930 | -0.114 | -277.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2930 | -0.114 | -277.93€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2300 | -0.193 | -602.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2300 | -0.193 | -602.53€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 2532 | -0.057 | +1221.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 716 | -0.004 | +421.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 1816 | -0.078 | +799.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 2532 | -0.057 | +1221.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 716 | -0.004 | +421.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 1816 | -0.078 | +799.96€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 58 | -0.133 | -18.24€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 58 | -0.133 | -18.24€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 58 | -0.133 | -18.24€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 58 | -0.133 | -18.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 41350 | +0.114 | -2614.67€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 7177 | +0.188 | -216.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 130 | -0.099 | -53.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 30538 | +0.097 | -2293.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3505 | +0.118 | -50.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 5122 | +0.075 | -743.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 22 | -0.083 | +0.79€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 9 | -0.143 | -7.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 5091 | +0.077 | -736.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 8382 | +0.132 | -184.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2067 | +0.202 | -71.83€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 5074 | +0.107 | -144.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1199 | +0.128 | +54.55€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 5137 | +0.082 | -632.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 25 | +0.056 | +1.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#240min | 6 | -0.075 | -4.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 5106 | +0.082 | -630.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 9004 | +0.126 | -139.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2629 | +0.172 | -1.44€ | 1 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 5096 | +0.111 | -99.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1267 | +0.097 | -29.57€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 8587 | +0.129 | -560.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2416 | +0.198 | -146.59€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 58 | +0.017 | -9.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 5074 | +0.097 | -329.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1039 | +0.133 | -75.31€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 5118 | +0.104 | -354.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 18 | +0.000 | +0.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 5097 | +0.105 | -353.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 7122 | +0.177 | -545.92€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 7122 | +0.177 | -545.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1799 | +0.166 | -195.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1799 | +0.166 | -195.24€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 142 | -0.132 | -2.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 142 | -0.132 | -2.14€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1775 | +0.170 | -185.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1775 | +0.170 | -185.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1597 | +0.233 | -47.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1597 | +0.233 | -47.28€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1730 | +0.185 | -129.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1730 | +0.185 | -129.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 359 | +0.445 | +2.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 359 | +0.445 | +2.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 138 | +0.443 | +1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 138 | +0.443 | +1.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 131 | +0.432 | -1.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 131 | +0.432 | -1.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 86 | +0.443 | +1.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 86 | +0.443 | +1.93€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 21767 | +0.191 | -1953.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 21767 | +0.191 | -1953.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3904 | +0.140 | -650.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3904 | +0.140 | -650.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 3418 | +0.231 | -97.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 3418 | +0.231 | -97.51€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 3735 | +0.168 | -466.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 3735 | +0.168 | -466.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 3470 | +0.226 | -124.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 3470 | +0.226 | -124.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 3582 | +0.205 | -235.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 3582 | +0.205 | -235.57€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 3658 | +0.183 | -379.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 3658 | +0.183 | -379.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 7970 | +0.132 | +278.53€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 7970 | +0.132 | +278.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 3970 | +0.135 | +158.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 3970 | +0.135 | +158.88€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 4000 | +0.129 | +119.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 4000 | +0.129 | +119.65€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 883 | +0.298 | +1.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 883 | +0.298 | +1.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 382 | +0.276 | -13.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 382 | +0.276 | -13.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 413 | +0.305 | +12.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 413 | +0.305 | +12.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 88 | +0.344 | +2.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 88 | +0.344 | +2.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 375 | +0.418 | -13.75€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 375 | +0.418 | -13.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 169 | +0.412 | -8.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 169 | +0.412 | -8.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 172 | +0.425 | -4.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 172 | +0.425 | -4.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 34 | +0.361 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 34 | +0.361 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 363 | +0.111 | +5.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 112 | +0.114 | +0.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 251 | +0.109 | +5.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 16 | +0.133 | +2.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 16 | +0.133 | +2.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 293 | +0.120 | +12.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 42 | +0.182 | +6.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 251 | +0.109 | +5.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 54 | +0.036 | -8.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 54 | +0.036 | -8.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 10927 | +0.094 | -411.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1018 | +0.066 | -36.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 9909 | +0.097 | -374.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 6803 | +0.097 | -155.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1018 | +0.066 | -36.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 5785 | +0.103 | -118.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 1063 | +0.109 | +4.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 1063 | +0.109 | +4.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 3061 | +0.083 | -259.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 3061 | +0.083 | -259.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 523 | +0.279 | -39.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 523 | +0.279 | -39.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 523 | +0.279 | -39.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 523 | +0.279 | -39.91€ | 0 | 4 |
| ✅ GBM_LATE_15M | 10024 | +0.049 | +3583.17€ | 0 | 14 |
| ✅ GBM_LATE_15M#15min | 10024 | +0.049 | +3583.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1468 | +0.191 | +1031.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1468 | +0.191 | +1031.19€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 1473 | +0.177 | +926.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1473 | +0.177 | +926.42€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 1482 | +0.197 | +1075.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1482 | +0.197 | +1075.95€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 1596 | -0.048 | +48.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1596 | -0.048 | +48.05€ | 4 | 11 |
| ✅ GBM_LATE_15M#SOL | 1713 | -0.056 | +239.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1713 | -0.056 | +239.82€ | 4 | 2 |
| ✅ GBM_LATE_15M#XRP | 2292 | -0.075 | +261.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2292 | -0.075 | +261.75€ | 5 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 10827 | +0.050 | +4390.27€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 10827 | +0.050 | +4390.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1775 | -0.015 | +662.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1775 | -0.015 | +662.57€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2362 | -0.035 | +211.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2362 | -0.035 | +211.60€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1340 | +0.252 | +1288.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1340 | +0.252 | +1288.86€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1727 | -0.056 | -30.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1727 | -0.056 | -30.68€ | 10 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1811 | -0.029 | +457.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1811 | -0.029 | +457.73€ | 7 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1812 | +0.258 | +1800.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1812 | +0.258 | +1800.19€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 8275 | +0.171 | +5811.83€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 8275 | +0.171 | +5811.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1131 | +0.196 | +846.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1131 | +0.196 | +846.00€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1371 | +0.165 | +946.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1371 | +0.165 | +946.63€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1144 | +0.197 | +863.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1144 | +0.197 | +863.32€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1359 | +0.150 | +847.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1359 | +0.150 | +847.45€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1543 | +0.124 | +955.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1543 | +0.124 | +955.12€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1727 | +0.200 | +1353.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1727 | +0.200 | +1353.32€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1680 | +0.090 | +463.53€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1680 | +0.090 | +463.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 399 | +0.046 | +76.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 399 | +0.046 | +76.80€ | 3 | 9 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 246 | +0.153 | +122.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 246 | +0.153 | +122.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 289 | +0.173 | +112.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 289 | +0.173 | +112.89€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 339 | -0.010 | +10.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 339 | -0.010 | +10.53€ | 4 | 5 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 351 | +0.123 | +125.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 351 | +0.123 | +125.65€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO | 9754 | +0.173 | +6821.70€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 9754 | +0.173 | +6821.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1417 | +0.215 | +1157.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1417 | +0.215 | +1157.70€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1579 | +0.164 | +1064.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1579 | +0.164 | +1064.93€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1408 | +0.220 | +1177.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1408 | +0.220 | +1177.01€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1514 | +0.141 | +910.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1514 | +0.141 | +910.41€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1722 | +0.097 | +850.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1722 | +0.097 | +850.01€ | 0 | 16 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2114 | +0.206 | +1661.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2114 | +0.206 | +1661.64€ | 0 | 22 |
| ✅ GBM_LATE_5M | 2916 | +0.128 | +1320.17€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 2916 | +0.128 | +1320.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 119 | +0.211 | +88.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 119 | +0.211 | +88.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 985 | +0.121 | +458.26€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 985 | +0.121 | +458.26€ | 1 | 16 |
| ✅ GBM_LATE_5M#DOGE | 341 | +0.171 | +207.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 341 | +0.171 | +207.15€ | 0 | 12 |
| ✅ GBM_LATE_5M#ETH | 949 | +0.130 | +414.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 949 | +0.130 | +414.37€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 155 | +0.016 | +13.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 155 | +0.016 | +13.46€ | 2 | 3 |
| ✅ GBM_LATE_5M#XRP | 367 | +0.118 | +138.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 367 | +0.118 | +138.76€ | 0 | 0 |
| ✅ GBM_LATE_60M | 579 | -0.008 | +128.64€ | 4 | 11 |
| ✅ GBM_LATE_60M#60min | 579 | -0.008 | +128.64€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 199 | +0.027 | +21.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 199 | +0.027 | +21.69€ | 2 | 7 |
| ✅ GBM_LATE_60M#ETH | 213 | +0.030 | +80.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 213 | +0.030 | +80.22€ | 2 | 11 |
| ✅ GBM_LATE_60M#SOL | 167 | -0.098 | +26.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 167 | -0.098 | +26.74€ | 4 | 3 |
| 🚫 GBM_LATE_60M_FADE | 198 | -0.300 | -33.22€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 198 | -0.300 | -33.22€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 79 | -0.253 | -7.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 79 | -0.253 | -7.31€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 66 | -0.353 | -19.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 66 | -0.353 | -19.56€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 382 | +0.042 | +16.77€ | 3 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 382 | +0.042 | +16.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 163 | +0.039 | +21.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 163 | +0.039 | +21.02€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 95 | +0.077 | +2.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 95 | +0.077 | +2.03€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 124 | +0.016 | -6.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 124 | +0.016 | -6.29€ | 3 | 5 |
| ✅ LATE_WINDOW_5MIN | 33 | +0.214 | +11.72€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 33 | +0.214 | +11.72€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 33 | +0.214 | +11.72€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 33 | +0.214 | +11.72€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 380 | +0.100 | +93.91€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 380 | +0.100 | +93.91€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 380 | +0.100 | +93.91€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 380 | +0.100 | +93.91€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 278 | -0.093 | -32.27€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 278 | -0.093 | -32.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 67 | -0.094 | -8.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 67 | -0.094 | -8.12€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 60 | -0.048 | -4.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 60 | -0.048 | -4.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 74 | -0.013 | -2.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 74 | -0.013 | -2.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 48 | -0.180 | -9.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 48 | -0.180 | -9.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1012 | -0.013 | -16.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1012 | -0.013 | -16.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 62 | +0.000 | -1.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 62 | +0.000 | -1.97€ | 0 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 137 | -0.040 | -4.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 137 | -0.040 | -4.62€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 76 | -0.090 | -7.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 76 | -0.090 | -7.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 296 | +0.020 | +9.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 296 | +0.020 | +9.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 380 | +0.000 | -5.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 380 | +0.000 | -5.10€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 61 | -0.103 | -7.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 61 | -0.103 | -7.10€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 513 | -0.005 | +0.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 513 | -0.005 | +0.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 158 | -0.044 | -11.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 158 | -0.044 | -11.54€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 157 | +0.016 | +4.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 157 | +0.016 | +4.64€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 198 | +0.010 | +7.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 198 | +0.010 | +7.57€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 5698 | +0.001 | -69.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 5698 | +0.001 | -69.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 530 | -0.004 | +2.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 530 | -0.004 | +2.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 600 | +0.003 | -9.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 600 | +0.003 | -9.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1204 | +0.008 | -14.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1204 | +0.008 | -14.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1349 | +0.006 | +9.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1349 | +0.006 | +9.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 933 | -0.009 | -32.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 933 | -0.009 | -32.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1082 | -0.005 | -24.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1082 | -0.005 | -24.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 9697 | -0.038 | +214.32€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 9697 | -0.038 | +214.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1542 | -0.034 | +162.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1542 | -0.034 | +162.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1726 | -0.030 | -38.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1726 | -0.030 | -38.94€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1563 | -0.051 | +87.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1563 | -0.051 | +87.35€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1668 | -0.036 | -20.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1668 | -0.036 | -20.86€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1617 | -0.039 | +42.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1617 | -0.039 | +42.67€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1581 | -0.040 | -18.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1581 | -0.040 | -18.07€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 556 | -0.061 | -42.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 556 | -0.061 | -42.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 67 | -0.065 | -5.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 67 | -0.065 | -5.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3171 | +0.004 | -4.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3171 | +0.004 | -4.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1160 | +0.008 | +7.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1160 | +0.008 | +7.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 26677 | -0.080 | +402.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 26677 | -0.080 | +402.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 4270 | -0.093 | +361.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 4270 | -0.093 | +361.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 4531 | -0.075 | -73.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 4531 | -0.075 | -73.32€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 4367 | -0.086 | +76.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 4367 | -0.086 | +76.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 4043 | -0.100 | -213.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 4043 | -0.100 | -213.09€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 4975 | -0.055 | +84.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 4975 | -0.055 | +84.06€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 4491 | -0.076 | +166.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 4491 | -0.076 | +166.41€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1204 | +0.000 | -15.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1204 | +0.000 | -15.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1001 | -0.019 | -30.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1001 | -0.019 | -30.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 649 | +0.105 | +194.14€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 513 | +0.117 | +181.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 121 | +0.126 | +53.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 121 | +0.126 | +53.78€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 100 | +0.098 | +23.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 100 | +0.098 | +23.68€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 98 | +0.090 | +27.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 98 | +0.090 | +27.51€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 89 | +0.159 | +47.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 89 | +0.159 | +47.30€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 105 | +0.107 | +29.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 105 | +0.107 | +29.27€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 283 | -0.156 | -27.32€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 126 | -0.234 | -36.95€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 110 | -0.268 | -36.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 16 | +0.000 | -0.62€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 105 | -0.126 | -4.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 86 | -0.136 | -7.64€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 52 | -0.018 | +14.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 43 | -0.011 | +13.57€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 9 | -0.021 | +0.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 239 | -0.176 | -30.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 44 | -0.043 | +3.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 267 | -0.217 | -5.47€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 113 | -0.152 | -0.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 105 | -0.145 | -0.17€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 8 | -0.080 | -0.69€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 100 | -0.304 | -23.59€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 93 | -0.310 | -24.68€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 7 | -0.058 | +1.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 54 | -0.179 | +18.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 49 | -0.167 | +18.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 5 | -0.054 | +0.48€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 247 | -0.215 | -6.35€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 20 | -0.227 | +0.88€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 86 | +0.352 | +27.04€ | 0 | 1 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 22 | +0.333 | +4.02€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 22 | +0.333 | +4.02€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 47 | +0.480 | +25.97€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 47 | +0.480 | +25.97€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 86 | +0.352 | +27.04€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 199 | +0.042 | +5.02€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 199 | +0.042 | +5.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 87 | +0.039 | +0.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 87 | +0.039 | +0.20€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 14 | +0.044 | +1.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 14 | +0.044 | +1.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 20 | +0.136 | +3.26€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 20 | +0.136 | +3.26€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 78 | +0.013 | -0.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 78 | +0.013 | -0.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1537 | -0.024 | -70.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1537 | -0.024 | -70.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 561 | -0.010 | -14.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 561 | -0.010 | -14.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 539 | -0.023 | -22.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 539 | -0.023 | -22.96€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 135 | -0.040 | -12.98€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 135 | -0.040 | -12.98€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 302 | -0.043 | -20.84€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 302 | -0.043 | -20.84€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 42 | -0.023 | -1.73€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 42 | -0.023 | -1.73€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 26 | -0.107 | -3.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 26 | -0.107 | -3.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 16 | +0.089 | +1.64€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 16 | +0.089 | +1.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 3128 | +0.026 | +61.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 3128 | +0.026 | +61.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1028 | +0.020 | +8.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1028 | +0.020 | +8.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 604 | +0.041 | +25.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 604 | +0.041 | +25.71€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 942 | +0.021 | +7.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 942 | +0.021 | +7.10€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 554 | +0.029 | +20.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 554 | +0.029 | +20.22€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 3738 | +0.010 | -28.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3738 | +0.010 | -28.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1431 | +0.011 | -10.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1431 | +0.011 | -10.16€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1475 | +0.018 | +0.30€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1475 | +0.018 | +0.30€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 832 | -0.007 | -18.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 832 | -0.007 | -18.80€ | 2 | 0 |
| ✅ UPDOWN_GBM | 7688 | +0.002 | +139.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2737 | +0.034 | +228.99€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 310 | +0.010 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 4139 | -0.017 | -86.13€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 455 | -0.003 | -2.80€ | 3 | 1 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1640 | +0.014 | +76.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 285 | +0.085 | +55.70€ | 2 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 92 | +0.064 | +7.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1099 | -0.001 | +17.02€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 146 | -0.027 | -5.23€ | 1 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 844 | -0.008 | -4.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 123 | +0.100 | +28.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 712 | -0.028 | -33.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1784 | -0.007 | -20.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 819 | +0.008 | +3.95€ | 1 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 89 | +0.050 | +3.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 656 | -0.033 | -28.79€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 205 | +0.012 | +1.09€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 2099 | -0.005 | -16.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 687 | -0.006 | -5.34€ | 1 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 78 | -0.013 | -3.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1218 | -0.003 | -9.26€ | 4 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 104 | +0.000 | +1.34€ | 2 | 3 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1123 | +0.005 | +68.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 644 | +0.050 | +104.07€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 34 | -0.167 | -6.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 445 | -0.046 | -29.26€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 239 | +0.322 | +54.85€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 239 | +0.322 | +54.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 139 | +0.308 | +22.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 139 | +0.308 | +22.45€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 100 | +0.333 | +32.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 100 | +0.333 | +32.40€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 4851 | -0.074 | +914.55€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 4851 | -0.074 | +914.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 304 | -0.052 | +340.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 304 | -0.052 | +340.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 987 | -0.161 | -111.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 987 | -0.161 | -111.71€ | 5 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 78 | +0.062 | +12.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 78 | +0.062 | +12.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 406 | +0.142 | +190.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 406 | +0.142 | +190.64€ | 2 | 15 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1585 | -0.068 | +271.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1585 | -0.068 | +271.78€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1491 | -0.091 | +210.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1491 | -0.091 | +210.80€ | 4 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 37 | +0.038 | -0.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 37 | +0.038 | -0.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 37 | +0.038 | -0.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 37 | +0.038 | -0.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 391 | +0.286 | +307.97€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 391 | +0.286 | +307.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 222 | +0.281 | +169.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 222 | +0.281 | +169.63€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 169 | +0.289 | +138.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 169 | +0.289 | +138.34€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 621 | -0.094 | -68.56€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 621 | -0.094 | -68.56€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 309 | -0.079 | -35.49€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 309 | -0.079 | -35.49€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 150 | -0.033 | -5.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 150 | -0.033 | -5.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 51 | -0.141 | -6.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 51 | -0.141 | -6.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 48 | -0.180 | -7.92€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 48 | -0.180 | -7.92€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1265 | +0.291 | +550.23€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 395 | +0.215 | +17.03€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 411 | +0.270 | +116.36€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 459 | +0.372 | +416.83€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.087) — sin ventaja clara. oversold(IBS<0.3): IC=+0.015 n=2746 | neutral: IC=-0.002 n=2971 | overbought(IBS>0.7): IC=+0.085 n=3054
  - _Datos_: n=9130 IC=+0.035 PNL=+832.81€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 110s) 70 celda(s) GATE OK de 2320 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.006 < 0.08 — monitorear
  - _Datos_: n=687 IC=-0.006 PNL=-5.34€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=411/15 IC=+0.270 PNL=+116.36€ | BTC: n=395/15 IC=+0.215 PNL=+17.03€ | SOL: n=459/15 IC=+0.372 PNL=+416.83€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.072 n=129542 | tras_1loss IC=+0.044 n=101929 | tras_2loss IC=+0.007 n=46399/40 | gap=+0.065 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 20 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC
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
  - _Estado_: 7626 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.115 n=50/60 | contraria IC=+0.033 n=28 | gap=+0.082 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=125, boost estimado=+0.008. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 89 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=205/40 IC=+0.012 PNL=+1.09€ | BTC#60min: n=146/40 IC=-0.027 PNL=-5.23€ | SOL#60min: n=104/40 IC=+0.000 PNL=+1.34€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.012 n=783 | contrario_BTC IC=-0.028 n=616/40 | gap=-0.015 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=77 PNL=+50.02€
  - _Datos_: n=77 IC=+0.196 PNL=+50.02€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=97 PNL=+26.18€
  - _Datos_: n=97 IC=+0.136 PNL=+26.18€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 22/25 ops en el filtro definido (IC actual=+0.250 PNL=+16.04€)
  - _Datos_: n=22 IC=+0.250 PNL=+16.04€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=1075 PNL=+555.17€
  - _Datos_: n=1075 IC=+0.333 PNL=+555.17€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=67 IC=+0.036 PNL=+11.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=67 IC=+0.036 PNL=+11.39€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 24/30 ops en el filtro definido (IC actual=+0.192 PNL=+15.20€)
  - _Datos_: n=24 IC=+0.192 PNL=+15.20€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=7411 IC=-0.001 PNL=+86.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=7411 IC=-0.001 PNL=+86.33€

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
  - _Estado_: n=379 IC=+0.012 PNL=+3.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=379 IC=+0.012 PNL=+3.85€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=76 IC=-0.077 PNL=-6.65€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=76 IC=-0.077 PNL=-6.65€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.082 < -0.08 con n=132 PNL=-10.40€
  - _Datos_: n=132 IC=-0.082 PNL=-10.40€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.1 con n=551 PNL=+144.66€
  - _Datos_: n=551 IC=+0.122 PNL=+144.66€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=194 IC=+0.076 PNL=+41.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=194 IC=+0.076 PNL=+41.53€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=285 IC=+0.085 PNL=+55.70€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=285 IC=+0.085 PNL=+55.70€

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
  - _Estado_: n=1590 IC=+0.025 PNL=+97.07€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1590 IC=+0.025 PNL=+97.07€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 28/30 ops en el filtro definido (IC actual=-0.233 PNL=-6.05€)
  - _Datos_: n=28 IC=-0.233 PNL=-6.05€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=84 IC=-0.046 PNL=+6.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=84 IC=-0.046 PNL=+6.24€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=101 IC=+0.015 PNL=+6.49€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=101 IC=+0.015 PNL=+6.49€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 7/15 ops en el filtro definido (IC actual=+0.058 PNL=+1.59€)
  - _Datos_: n=7 IC=+0.058 PNL=+1.59€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2309 IC=-0.023 PNL=-61.98€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2309 IC=-0.023 PNL=-61.98€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.214 n=33) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=33 IC=+0.214 PNL=+11.72€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2015 IC=+0.012 PNL=+80.04€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2015 IC=+0.012 PNL=+80.04€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=517 IC=+0.026 PNL=+3.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=517 IC=+0.026 PNL=+3.99€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.08 con n=182 PNL=+48.68€
  - _Datos_: n=182 IC=+0.109 PNL=+48.68€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.08 con n=137 PNL=+3.26€
  - _Datos_: n=137 IC=+0.119 PNL=+3.26€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.138 > 0.08 con n=125 PNL=+43.67€
  - _Datos_: n=125 IC=+0.138 PNL=+43.67€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=26918 IC=+0.102 PNL=+8480.44€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=26918 IC=+0.102 PNL=+8480.44€

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
  - _Estado_: n=1037 IC=+0.024 PNL=+49.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1037 IC=+0.024 PNL=+49.08€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.02 con n=357 PNL=+117.03€
  - _Datos_: n=357 IC=+0.121 PNL=+117.03€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=96 IC=-0.092 PNL=+19.98€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=96 IC=-0.092 PNL=+19.98€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=665 PNL=+588.66€
  - _Datos_: n=665 IC=+0.445 PNL=+588.66€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1753 IC=+0.023 PNL=+103.65€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1753 IC=+0.023 PNL=+103.65€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=839 PNL=+315.27€
  - _Datos_: n=839 IC=+0.166 PNL=+315.27€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 39/40 ops en el filtro definido (IC actual=-0.232 PNL=-6.66€)
  - _Datos_: n=39 IC=-0.232 PNL=-6.66€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=501 IC=+0.033 PNL=+53.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=501 IC=+0.033 PNL=+53.99€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.1 con n=89 PNL=+11.61€
  - _Datos_: n=89 IC=+0.115 PNL=+11.61€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=6329 IC=-0.145 PNL=+231.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6329 IC=-0.145 PNL=+231.62€

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
  - _Estado_: n=777 IC=+0.144 PNL=+365.65€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=777 IC=+0.144 PNL=+365.65€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.08 con n=550 PNL=+146.40€
  - _Datos_: n=550 IC=+0.123 PNL=+146.40€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=778 IC=-0.004 PNL=-2.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=778 IC=-0.004 PNL=-2.05€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=771 PNL=+397.76€
  - _Datos_: n=771 IC=+0.083 PNL=+397.76€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.08 con n=166 PNL=+59.56€
  - _Datos_: n=166 IC=+0.167 PNL=+59.56€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.249 < -0.1 con n=694 PNL=-110.74€
  - _Datos_: n=694 IC=-0.249 PNL=-110.74€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1722 IC=+0.124 PNL=+901.32€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1722 IC=+0.124 PNL=+901.32€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=44 PNL=+11.29€
  - _Datos_: n=44 IC=+0.087 PNL=+11.29€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=811 IC=-0.026 PNL=+51.36€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=811 IC=-0.026 PNL=+51.36€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.178 > 0.08 con n=722 PNL=+436.89€
  - _Datos_: n=722 IC=+0.178 PNL=+436.89€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1206 IC=-0.067 PNL=+149.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1206 IC=-0.067 PNL=+149.32€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=284 PNL=-38.87€
  - _Datos_: n=284 IC=+0.115 PNL=-38.87€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.235 > 0.08 con n=1776 PNL=-169.74€
  - _Datos_: n=1776 IC=+0.235 PNL=-169.74€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 13/40 ops en el filtro definido (IC actual=-0.065 PNL=-0.09€)
  - _Datos_: n=13 IC=-0.065 PNL=-0.09€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=199) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=199 IC=+0.102 PNL=+45.10€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.08 con n=81 PNL=+50.44€
  - _Datos_: n=81 IC=+0.331 PNL=+50.44€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.427 n=260) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=260 IC=+0.427 PNL=+357.77€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=3904 IC=+0.140 PNL=-650.79€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3904 IC=+0.140 PNL=-650.79€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.1 con n=49 PNL=+29.61€
  - _Datos_: n=49 IC=+0.206 PNL=+29.61€
